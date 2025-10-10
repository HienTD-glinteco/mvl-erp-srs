#!/usr/bin/env python3
"""
SRS DOCX to Markdown Converter

This script converts DOCX files from the /original/ directory into well-structured
Markdown files organized by module and use case.

Features:
- Converts DOCX to Markdown using Pandoc
- Splits output by H1/H2 headings
- Creates individual UC (Use Case) files
- Maintains manifest with source file hashes
- Cleans up old files when sources change or are removed
"""

import os
import sys
import json
import hashlib
import subprocess
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from datetime import datetime
from unidecode import unidecode


class SRSConverter:
    """Handles conversion of SRS DOCX files to Markdown"""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.original_dir = repo_root / "original"
        self.markdowns_dir = repo_root / "markdowns"
        self.manifest_file = self.markdowns_dir / "manifest.json"
        self.manifest: Dict = {}
        
    def load_manifest(self):
        """Load existing manifest or create new one"""
        if self.manifest_file.exists():
            with open(self.manifest_file, 'r', encoding='utf-8') as f:
                self.manifest = json.load(f)
        else:
            self.manifest = {
                "version": "1.0",
                "last_updated": None,
                "files": {}
            }
    
    def save_manifest(self):
        """Save manifest to disk"""
        self.manifest["last_updated"] = datetime.now().isoformat()
        self.markdowns_dir.mkdir(parents=True, exist_ok=True)
        with open(self.manifest_file, 'w', encoding='utf-8') as f:
            json.dump(self.manifest, f, indent=2, ensure_ascii=False)
    
    def calculate_hash(self, filepath: Path) -> str:
        """Calculate SHA256 hash of a file"""
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    def extract_module_name(self, filename: str) -> str:
        """
        Extract module name from filename.
        Example: "SRS - HRM (1,2,3,4,5) - Bản Tổng hợp - Formatted.docx" -> "hrm"
        """
        # Look for pattern "SRS - MODULE" or just take the first significant word
        match = re.search(r'SRS\s*-\s*([A-Za-z]+)', filename)
        if match:
            return match.group(1).lower()
        
        # Fallback: take first word that's not "SRS"
        words = re.findall(r'[A-Za-z]+', filename)
        for word in words:
            if word.upper() != 'SRS':
                return word.lower()
        
        return "unknown"
    
    def convert_docx_to_markdown(self, docx_path: Path) -> str:
        """Convert DOCX file to Markdown using Pandoc"""
        try:
            result = subprocess.run(
                ['pandoc', str(docx_path), '-t', 'markdown', '--wrap=none'],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error converting {docx_path}: {e}", file=sys.stderr)
            print(f"Pandoc stderr: {e.stderr}", file=sys.stderr)
            raise
    
    def post_process_markdown(self, content: str) -> str:
        """Post-process markdown to clean up tables and images"""
        lines = content.split('\n')
        processed_lines = []
        in_grid_table = False
        grid_table_buffer = []
        
        for i, line in enumerate(lines):
            # Remove Pandoc image attributes like {width="..."}
            if '![' in line and '{' in line:
                line = re.sub(r'\{[^}]*\}', '', line)
            
            # Detect grid table borders (+---+)
            if re.match(r'^\+[-+=]+\+', line):
                if not in_grid_table:
                    # Start of a new grid table
                    in_grid_table = True
                    grid_table_buffer = []
                # Skip the border line
                continue
            
            # Process table rows in grid tables
            if in_grid_table:
                if line.strip().startswith('|'):
                    # This is a table row, store it
                    grid_table_buffer.append(line)
                else:
                    # End of grid table - process and output the buffer
                    if grid_table_buffer:
                        processed_table = self._convert_grid_table_to_gfm(grid_table_buffer)
                        processed_lines.extend(processed_table)
                        grid_table_buffer = []
                    in_grid_table = False
                    processed_lines.append(line)
                continue
            
            # Regular line (not in grid table)
            processed_lines.append(line)
        
        # Handle any remaining grid table at the end of file
        if in_grid_table and grid_table_buffer:
            processed_table = self._convert_grid_table_to_gfm(grid_table_buffer)
            processed_lines.extend(processed_table)
        
        return '\n'.join(processed_lines)
    
    def _convert_grid_table_to_gfm(self, table_lines: List[str]) -> List[str]:
        """Convert grid table lines to GFM pipe table format"""
        gfm_lines = []
        header_detected = False
        
        for line in table_lines:
            # Extract cells from the line
            cells = line.split('|')[1:-1]  # Remove first and last empty elements
            
            # Clean each cell
            cleaned_cells = []
            for cell in cells:
                # Remove blockquote markers (>) and excessive whitespace
                cell = cell.strip()
                cell = re.sub(r'^>\s*', '', cell)
                cell = re.sub(r'\s+', ' ', cell)
                cleaned_cells.append(cell)
            
            # Check if this is a header separator row (contains =)
            if any('=' in cell for cell in cells):
                # This marks the end of header - output a GFM separator
                if not header_detected:
                    gfm_lines.append('| ' + ' | '.join(['---'] * len(cleaned_cells)) + ' |')
                    header_detected = True
                continue
            
            # Skip empty rows
            if all(not cell.strip() for cell in cleaned_cells):
                continue
            
            # Output the row
            gfm_lines.append('| ' + ' | '.join(cleaned_cells) + ' |')
        
        return gfm_lines
    
    def slugify(self, text: str) -> str:
        """Convert text to ASCII-only URL-friendly slug"""
        # Convert to ASCII (remove accents)
        text = unidecode(text)
        # Remove special characters and convert to lowercase
        text = text.lower()
        # Replace spaces and special chars with hyphens
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text.strip('-')
    
    def split_markdown_by_sections(self, content: str) -> List[Tuple[str, str, str]]:
        """
        Split markdown content by H1 and H2 headings, creating individual files.
        Returns list of (filename, title, content) tuples.
        
        For headings (H2, H3, H4) that start with "UC", creates separate files.
        """
        sections = []
        lines = content.split('\n')
        
        current_h1 = None
        current_h2 = None
        current_section_content = []
        current_uc_content = []
        current_uc_header = None
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check for H1
            if line.startswith('# ') and not line.startswith('## '):
                # Save previous content
                if current_uc_header:
                    sections.append(self._create_uc_section(current_uc_header, current_uc_content))
                    current_uc_content = []
                    current_uc_header = None
                elif current_section_content:
                    sections.append(self._create_regular_section(
                        current_h1, current_h2, current_section_content
                    ))
                    current_section_content = []
                
                current_h1 = line[2:].strip()
                current_h2 = None
                current_section_content = [line]
            
            # Check for H2 (could be UC or regular section)
            elif line.startswith('## ') and not line.startswith('### '):
                heading_text = line[3:].strip()
                
                # Check if it's a Use Case
                if re.match(r'^UC\s*[\d.]+', heading_text, re.IGNORECASE):
                    # Save previous content
                    if current_uc_header:
                        sections.append(self._create_uc_section(current_uc_header, current_uc_content))
                    elif current_section_content:
                        sections.append(self._create_regular_section(
                            current_h1, current_h2, current_section_content
                        ))
                        current_section_content = []
                    
                    # Start new UC
                    current_uc_header = heading_text
                    current_uc_content = [line]
                else:
                    # Regular H2 section
                    if current_uc_header:
                        sections.append(self._create_uc_section(current_uc_header, current_uc_content))
                        current_uc_content = []
                        current_uc_header = None
                    elif current_section_content:
                        sections.append(self._create_regular_section(
                            current_h1, current_h2, current_section_content
                        ))
                        current_section_content = []
                    
                    current_h2 = heading_text
                    current_section_content = [line]
            
            # Check for H3 (potential Use Case)
            elif line.startswith('### ') and not line.startswith('#### '):
                heading_text = line[4:].strip()
                
                # Check if it's a Use Case (starts with UC or UC followed by number)
                if re.match(r'^UC\s*[\d.]+', heading_text, re.IGNORECASE):
                    # Save previous UC if any
                    if current_uc_header:
                        sections.append(self._create_uc_section(current_uc_header, current_uc_content))
                    
                    # Start new UC
                    current_uc_header = heading_text
                    current_uc_content = [line]
                else:
                    # Not a UC, treat as regular content
                    if current_uc_header:
                        current_uc_content.append(line)
                    else:
                        current_section_content.append(line)
            
            # Check for H4 (potential Use Case)
            elif line.startswith('#### '):
                heading_text = line[5:].strip()
                
                # Check if it's a Use Case
                if re.match(r'^UC\s*[\d.]+', heading_text, re.IGNORECASE):
                    # Save previous UC if any
                    if current_uc_header:
                        sections.append(self._create_uc_section(current_uc_header, current_uc_content))
                    
                    # Start new UC
                    current_uc_header = heading_text
                    current_uc_content = [line]
                else:
                    # Not a UC, treat as regular content
                    if current_uc_header:
                        current_uc_content.append(line)
                    else:
                        current_section_content.append(line)
            else:
                # Regular content line
                if current_uc_header:
                    current_uc_content.append(line)
                else:
                    current_section_content.append(line)
            
            i += 1
        
        # Save final section
        if current_uc_header:
            sections.append(self._create_uc_section(current_uc_header, current_uc_content))
        elif current_section_content:
            sections.append(self._create_regular_section(
                current_h1, current_h2, current_section_content
            ))
        
        return sections
    
    def extract_all_uc_numbers(self, content: str) -> Set[str]:
        """Extract all UC numbers from markdown content"""
        uc_numbers = set()
        lines = content.split('\n')
        
        for line in lines:
            # Match headings with UC numbers (any level)
            if line.startswith('#'):
                # Extract heading text
                heading_text = re.sub(r'^#+\s*', '', line).strip()
                # Check for UC pattern
                match = re.match(r'^UC\s*([\d.]+)', heading_text, re.IGNORECASE)
                if match:
                    uc_num = match.group(1)
                    # Normalize trailing dots
                    uc_num = uc_num.rstrip('.')
                    if uc_num and not uc_num.endswith('.'):
                        uc_numbers.add(uc_num)
        
        return uc_numbers
    
    def _create_uc_section(self, uc_header: str, content: List[str]) -> Tuple[str, str, str]:
        """Create a section tuple for a Use Case"""
        # Extract UC number (e.g., "UC1.1.1" or "UC 2.1.1")
        match = re.match(r'^UC\s*([\d.]+)', uc_header, re.IGNORECASE)
        uc_num = match.group(1) if match else "unknown"
        
        # Normalize UC number (remove trailing dots)
        uc_num = uc_num.rstrip('.')
        
        # Create filename: uc-1.1.1-description.md
        desc = re.sub(r'^UC\s*[\d.]+:?\s*', '', uc_header, flags=re.IGNORECASE)
        desc_slug = self.slugify(desc)[:50]  # Limit length
        filename = f"uc-{uc_num}-{desc_slug}.md"
        
        # Add YAML front matter
        front_matter = f"""---
title: "{uc_header}"
type: "use-case"
uc_number: "{uc_num}"
---

"""
        full_content = front_matter + '\n'.join(content)
        
        return (filename, uc_header, full_content)
    
    def _create_regular_section(self, h1: Optional[str], h2: Optional[str], 
                                content: List[str]) -> Tuple[str, str, str]:
        """Create a section tuple for non-UC content"""
        if h2:
            title = f"{h1} - {h2}" if h1 else h2
            slug = self.slugify(h2)[:50]
        elif h1:
            title = h1
            slug = self.slugify(h1)[:50]
        else:
            title = "Introduction"
            slug = "introduction"
        
        filename = f"{slug}.md"
        
        # Add YAML front matter
        front_matter = f"""---
title: "{title}"
type: "section"
---

"""
        full_content = front_matter + '\n'.join(content)
        
        return (filename, title, full_content)
    
    def process_docx_file(self, docx_path: Path):
        """Process a single DOCX file"""
        print(f"Processing: {docx_path.name}")
        
        # Calculate hash
        file_hash = self.calculate_hash(docx_path)
        
        # Check if file has changed
        file_key = docx_path.name
        if file_key in self.manifest["files"]:
            old_hash = self.manifest["files"][file_key].get("hash")
            if old_hash == file_hash:
                print(f"  Skipping (unchanged): {docx_path.name}")
                return
            
            # File changed, clean up old files
            print(f"  File changed, cleaning up old generated files...")
            self.cleanup_old_files(file_key)
        
        # Extract module name and create output directory
        module_name = self.extract_module_name(docx_path.name)
        output_dir = self.markdowns_dir / module_name
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Convert DOCX to Markdown
        print(f"  Converting to Markdown...")
        markdown_content = self.convert_docx_to_markdown(docx_path)
        
        # Post-process markdown (clean tables, images, etc.)
        print(f"  Post-processing markdown...")
        markdown_content = self.post_process_markdown(markdown_content)
        
        # Extract all UC numbers for diagnostics
        all_uc_numbers = self.extract_all_uc_numbers(markdown_content)
        print(f"  Found {len(all_uc_numbers)} UC sections in source")
        
        # Split into sections
        print(f"  Splitting into sections...")
        sections = self.split_markdown_by_sections(markdown_content)
        
        # Track extracted UC numbers
        extracted_uc_numbers = set()
        for filename, title, content in sections:
            if filename.startswith('uc-'):
                match = re.match(r'^uc-([\d.]+)-', filename)
                if match:
                    extracted_uc_numbers.add(match.group(1))
        
        # Report missing UCs
        missing_ucs = all_uc_numbers - extracted_uc_numbers
        if missing_ucs:
            print(f"  ⚠️  WARNING: {len(missing_ucs)} UC section(s) not extracted:")
            for uc_num in sorted(missing_ucs, key=lambda x: [int(n) if n.isdigit() else n for n in re.split(r'\.', x)]):
                print(f"      - UC {uc_num}")
        
        # Write section files
        generated_files = []
        for filename, title, content in sections:
            output_path = output_dir / filename
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            generated_files.append(str(output_path.relative_to(self.repo_root)))
            print(f"    Created: {output_path.relative_to(self.repo_root)}")
        
        # Update manifest
        self.manifest["files"][file_key] = {
            "hash": file_hash,
            "module": module_name,
            "output_dir": str(output_dir.relative_to(self.repo_root)),
            "generated_files": generated_files,
            "processed_at": datetime.now().isoformat()
        }
        
        print(f"  Generated {len(generated_files)} files ({len(extracted_uc_numbers)} UC files)")
    
    def cleanup_old_files(self, file_key: str):
        """Remove old generated files for a source file"""
        if file_key not in self.manifest["files"]:
            return
        
        old_files = self.manifest["files"][file_key].get("generated_files", [])
        for rel_path in old_files:
            file_path = self.repo_root / rel_path
            if file_path.exists():
                file_path.unlink()
                print(f"    Removed: {rel_path}")
        
        # Also try to remove the output directory if empty
        output_dir = self.manifest["files"][file_key].get("output_dir")
        if output_dir:
            dir_path = self.repo_root / output_dir
            if dir_path.exists() and not any(dir_path.iterdir()):
                dir_path.rmdir()
                print(f"    Removed empty directory: {output_dir}")
    
    def cleanup_removed_sources(self):
        """Remove generated files for DOCX files that no longer exist"""
        existing_files = {f.name for f in self.original_dir.glob("*.docx")}
        
        for file_key in list(self.manifest["files"].keys()):
            if file_key not in existing_files:
                print(f"Source file removed: {file_key}")
                self.cleanup_old_files(file_key)
                del self.manifest["files"][file_key]
    
    def run(self):
        """Main conversion process"""
        print("=" * 70)
        print("SRS DOCX to Markdown Converter")
        print("=" * 70)
        
        # Load existing manifest
        self.load_manifest()
        
        # Find all DOCX files
        docx_files = list(self.original_dir.glob("*.docx"))
        
        if not docx_files:
            print("No DOCX files found in /original/")
            return
        
        print(f"Found {len(docx_files)} DOCX file(s)\n")
        
        # Process each file
        for docx_file in docx_files:
            self.process_docx_file(docx_file)
            print()
        
        # Clean up files from removed sources
        self.cleanup_removed_sources()
        
        # Save manifest
        self.save_manifest()
        print("Manifest updated")
        print("=" * 70)
        print("Conversion complete!")


def main():
    """Main entry point"""
    # Determine repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    converter = SRSConverter(repo_root)
    converter.run()


if __name__ == "__main__":
    main()
