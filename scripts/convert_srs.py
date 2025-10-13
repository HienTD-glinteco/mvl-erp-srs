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
        first_row = True
        
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
            
            # If this is the first row and we haven't seen a header separator yet,
            # assume it's a header and add a separator after it
            if first_row and not header_detected:
                # Check if the first row looks like a header (has bold text)
                if any('**' in cell for cell in cleaned_cells):
                    gfm_lines.append('| ' + ' | '.join(['---'] * len(cleaned_cells)) + ' |')
                    header_detected = True
                first_row = False
        
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
    
    def _clean_heading_text(self, text: str) -> str:
        """Remove invisible characters and clean heading text"""
        # Remove zero-width spaces and other invisible Unicode characters
        text = re.sub(r'[\u200B-\u200D\uFEFF]', '', text)
        return text.strip()
    
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
                heading_text = self._clean_heading_text(line[3:])
                
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
                heading_text = self._clean_heading_text(line[4:])
                
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
                heading_text = self._clean_heading_text(line[5:])
                
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
                heading_text = re.sub(r'^#+\s*', '', line)
                # Clean invisible characters
                heading_text = self._clean_heading_text(heading_text)
                # Check for UC pattern
                match = re.match(r'^UC\s*([\d.]+)', heading_text, re.IGNORECASE)
                if match:
                    uc_num = match.group(1)
                    # Normalize trailing dots
                    uc_num = uc_num.rstrip('.')
                    if uc_num and not uc_num.endswith('.'):
                        uc_numbers.add(uc_num)
        
        return uc_numbers
    
    def extract_uc_contents(self, content: str) -> Dict[str, str]:
        """
        Extract UC content mapped by UC number.
        Returns dict of {uc_number: content_hash}
        """
        uc_contents = {}
        lines = content.split('\n')
        
        current_uc_num = None
        current_uc_content = []
        
        for line in lines:
            # Check if this is a UC heading (any level)
            if line.startswith('#'):
                heading_text = re.sub(r'^#+\s*', '', line)
                heading_text = self._clean_heading_text(heading_text)
                match = re.match(r'^UC\s*([\d.]+)', heading_text, re.IGNORECASE)
                
                if match:
                    # Save previous UC if any
                    if current_uc_num:
                        content_str = '\n'.join(current_uc_content)
                        # Create a hash of the content for comparison
                        content_hash = hashlib.sha256(content_str.encode('utf-8')).hexdigest()
                        uc_contents[current_uc_num] = content_hash
                    
                    # Start new UC
                    current_uc_num = match.group(1).rstrip('.')
                    current_uc_content = [line]
                elif current_uc_num:
                    # We're in a UC but hit a non-UC heading - end current UC
                    content_str = '\n'.join(current_uc_content)
                    content_hash = hashlib.sha256(content_str.encode('utf-8')).hexdigest()
                    uc_contents[current_uc_num] = content_hash
                    current_uc_num = None
                    current_uc_content = []
            elif current_uc_num:
                # Regular line within a UC
                current_uc_content.append(line)
        
        # Save final UC if any
        if current_uc_num:
            content_str = '\n'.join(current_uc_content)
            content_hash = hashlib.sha256(content_str.encode('utf-8')).hexdigest()
            uc_contents[current_uc_num] = content_hash
        
        return uc_contents
    
    def find_renamed_file(self, new_filename: str, new_module: str) -> Optional[str]:
        """
        Find if there's an old file that might be a renamed version.
        Returns the old file_key if found, None otherwise.
        """
        # Extract base pattern from new filename (SRS - MODULE pattern)
        for old_file_key in self.manifest["files"].keys():
            # Check if old file has same module
            old_module = self.manifest["files"][old_file_key].get("module")
            if old_module != new_module:
                continue
            
            # Both files should follow SRS - MODULE pattern
            if re.match(r'SRS\s*-\s*' + re.escape(new_module), new_filename, re.IGNORECASE) and \
               re.match(r'SRS\s*-\s*' + re.escape(old_module), old_file_key, re.IGNORECASE):
                # Found a potential renamed file (same module, both follow SRS pattern)
                return old_file_key
        
        return None
    
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
        
        # Extract module name and create output directory
        module_name = self.extract_module_name(docx_path.name)
        output_dir = self.markdowns_dir / module_name
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Check if file has changed
        file_key = docx_path.name
        old_file_key = None
        old_uc_contents = {}
        
        if file_key in self.manifest["files"]:
            old_hash = self.manifest["files"][file_key].get("hash")
            if old_hash == file_hash:
                # Quick validation: check if generated files actually exist
                old_files = self.manifest["files"][file_key].get("generated_files", [])
                missing_files = []
                for rel_path in old_files:
                    file_path = self.repo_root / rel_path
                    if not file_path.exists():
                        missing_files.append(rel_path)
                
                if missing_files:
                    print(f"  ⚠️  File unchanged but {len(missing_files)} generated file(s) are missing")
                    print(f"  Regenerating to restore missing files...")
                    old_file_key = file_key
                else:
                    # Also verify UC count matches the source to catch incomplete generations
                    # Do a quick conversion to check UC count
                    markdown_content = self.convert_docx_to_markdown(docx_path)
                    markdown_content = self.post_process_markdown(markdown_content)
                    all_uc_numbers = self.extract_all_uc_numbers(markdown_content)
                    
                    # Count UC files in manifest
                    uc_files_in_manifest = [f for f in old_files if '/uc-' in f]
                    
                    if len(uc_files_in_manifest) < len(all_uc_numbers):
                        print(f"  ⚠️  File unchanged but UC count mismatch:")
                        print(f"      Manifest has {len(uc_files_in_manifest)} UC files, source has {len(all_uc_numbers)} UCs")
                        print(f"  Regenerating to create missing UC files...")
                        old_file_key = file_key
                    else:
                        print(f"  Skipping (unchanged): {docx_path.name}")
                        return
            else:
                # File changed, we'll need to compare UCs
                print(f"  File changed, will compare UC content...")
                old_file_key = file_key
        else:
            # Check if this might be a renamed file
            old_file_key = self.find_renamed_file(docx_path.name, module_name)
            if old_file_key:
                print(f"  Detected potential file rename from: {old_file_key}")
                print(f"  Will compare UC content to preserve unchanged UCs...")
        
        # If we have an old file (changed or renamed), extract its UC contents for comparison
        if old_file_key:
            old_files = self.manifest["files"][old_file_key].get("generated_files", [])
            for rel_path in old_files:
                if '/uc-' in rel_path:
                    file_path = self.repo_root / rel_path
                    if file_path.exists():
                        # Extract UC number from filename
                        filename = file_path.name
                        match = re.match(r'^uc-([\d.]+)-', filename)
                        if match:
                            uc_num = match.group(1)
                            # Read the file content (skip YAML front matter)
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                # Extract content after YAML front matter
                                parts = content.split('---', 2)
                                if len(parts) >= 3:
                                    uc_content = parts[2].strip()
                                    content_hash = hashlib.sha256(uc_content.encode('utf-8')).hexdigest()
                                    old_uc_contents[uc_num] = content_hash
        
        # Convert DOCX to Markdown
        print(f"  Converting to Markdown...")
        markdown_content = self.convert_docx_to_markdown(docx_path)
        
        # Post-process markdown (clean tables, images, etc.)
        print(f"  Post-processing markdown...")
        markdown_content = self.post_process_markdown(markdown_content)
        
        # Extract all UC numbers for diagnostics
        all_uc_numbers = self.extract_all_uc_numbers(markdown_content)
        print(f"  Found {len(all_uc_numbers)} UC sections in source")
        
        # Extract UC contents for comparison
        new_uc_contents = self.extract_uc_contents(markdown_content)
        
        # Split into sections
        print(f"  Splitting into sections...")
        sections = self.split_markdown_by_sections(markdown_content)
        
        # Track extracted UC numbers and their content
        extracted_uc_numbers = set()
        new_uc_files = {}  # Map UC number to (filename, content)
        
        for filename, title, content in sections:
            if filename.startswith('uc-'):
                match = re.match(r'^uc-([\d.]+)-', filename)
                if match:
                    uc_num = match.group(1)
                    extracted_uc_numbers.add(uc_num)
                    new_uc_files[uc_num] = (filename, content)
        
        # Report missing UCs
        missing_ucs = all_uc_numbers - extracted_uc_numbers
        if missing_ucs:
            print(f"  ⚠️  WARNING: {len(missing_ucs)} UC section(s) not extracted:")
            for uc_num in sorted(missing_ucs, key=lambda x: [int(n) if n.isdigit() else n for n in re.split(r'\.', x)]):
                print(f"      - UC {uc_num}")
        
        # Process UC files - preserve, update, or create new
        uc_preserved = 0
        uc_updated = 0
        uc_created = 0
        uc_removed = 0
        
        generated_files = []
        
        # Write or preserve UC files
        for uc_num, (filename, content) in new_uc_files.items():
            output_path = output_dir / filename
            
            # Check if we need to write the file
            should_write = True
            action = "Created"
            
            if output_path.exists() and uc_num in old_uc_contents:
                # File exists, check if content is the same
                with open(output_path, 'r', encoding='utf-8') as f:
                    existing_content = f.read()
                
                # Compare the full content including YAML
                existing_hash = hashlib.sha256(existing_content.encode('utf-8')).hexdigest()
                new_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
                
                if existing_hash == new_hash:
                    # Content identical, don't rewrite
                    should_write = False
                    uc_preserved += 1
                    action = "Preserved (unchanged)"
                else:
                    # Content changed
                    uc_updated += 1
                    action = "Updated (content changed)"
            elif uc_num in old_uc_contents:
                # UC existed before but file doesn't exist (shouldn't happen normally)
                uc_updated += 1
                action = "Created (restored)"
            else:
                # New UC
                uc_created += 1
                action = "Created"
            
            # Write the file if needed
            if should_write:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            print(f"    {action}: {output_path.relative_to(self.repo_root)}")
            generated_files.append(str(output_path.relative_to(self.repo_root)))
        
        # Write non-UC section files
        for filename, title, content in sections:
            if not filename.startswith('uc-'):
                output_path = output_dir / filename
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                generated_files.append(str(output_path.relative_to(self.repo_root)))
                print(f"    Created: {output_path.relative_to(self.repo_root)}")
        
        # Remove UC files that are no longer in the new file
        if old_file_key:
            old_files = self.manifest["files"][old_file_key].get("generated_files", [])
            for rel_path in old_files:
                if '/uc-' in rel_path:
                    file_path = self.repo_root / rel_path
                    filename = file_path.name
                    match = re.match(r'^uc-([\d.]+)-', filename)
                    if match:
                        uc_num = match.group(1)
                        # If this UC no longer exists in new file, remove it
                        if uc_num not in new_uc_files and file_path.exists():
                            file_path.unlink()
                            uc_removed += 1
                            print(f"    Removed (no longer exists): {rel_path}")
                elif file_path.exists():
                    # Remove non-UC files from old version
                    file_path.unlink()
                    print(f"    Removed: {rel_path}")
        
        # Update manifest
        self.manifest["files"][file_key] = {
            "hash": file_hash,
            "module": module_name,
            "output_dir": str(output_dir.relative_to(self.repo_root)),
            "generated_files": generated_files,
            "processed_at": datetime.now().isoformat()
        }
        
        # If this was a rename, remove the old manifest entry
        if old_file_key and old_file_key != file_key:
            del self.manifest["files"][old_file_key]
            print(f"  Removed old manifest entry for: {old_file_key}")
        
        # Print summary
        print(f"  Generated {len(generated_files)} files ({len(extracted_uc_numbers)} UC files)")
        if old_uc_contents:
            print(f"  UC Summary: {uc_preserved} preserved, {uc_updated} updated, {uc_created} created, {uc_removed} removed")
    
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
