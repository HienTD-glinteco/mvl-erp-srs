# Implementation Notes: SRS DOCX to Markdown Automation

## Completed Implementation

This document describes the completed implementation of the automated SRS DOCX to Markdown conversion system.

## Components Delivered

### 1. Python Conversion Script (`scripts/convert_srs.py`)

**Features:**
- ✅ Converts DOCX files to Markdown using Pandoc
- ✅ Extracts module name from filename (e.g., "SRS - HRM..." → "hrm")
- ✅ Splits Markdown content by headings (H1, H2, H3)
- ✅ Creates individual files for Use Cases (H3 starting with "UC")
- ✅ Generates YAML front matter with metadata
- ✅ Maintains manifest with SHA256 hashes for change tracking
- ✅ Implements incremental conversion (only processes changed files)
- ✅ Automatically cleans up old files when sources are updated/removed
- ✅ Smart rename detection preserves unchanged UC files

**Key Functions:**
- `calculate_hash()`: SHA256 hash calculation for change detection
- `extract_module_name()`: Extracts module name from filename
- `convert_docx_to_markdown()`: Pandoc wrapper for DOCX conversion
- `split_markdown_by_sections()`: Intelligent content splitting
- `extract_uc_contents()`: Extracts UC content hashes for comparison
- `find_renamed_file()`: Detects renamed files by module and SRS prefix
- `process_docx_file()`: Main processing pipeline with rename detection
- `cleanup_old_files()`: Removes outdated generated files
- `cleanup_removed_sources()`: Handles deleted source files

### 2. GitHub Actions Workflow (`.github/workflows/convert-srs.yml`)

**Triggers:**
- Push to main/master branch with changes to `original/*.docx`
- Manual workflow dispatch

**Steps:**
1. Checkout repository with full history
2. Set up Python 3.12
3. Install Pandoc via apt
4. Run conversion script
5. Configure Git with bot credentials
6. Commit and push changes (with `[skip ci]` to prevent loops)

**Permissions:**
- `contents: write` for committing generated files

### 3. Documentation

**README.md:**
- Overview of the system
- Directory structure
- How it works (detailed process flow)
- Usage instructions (manual and automated)
- Examples for GitHub Copilot integration
- Module naming patterns
- Troubleshooting guide
- Contributing guidelines

**markdowns/README.md:**
- Explanation of generated files
- File types (UC files vs section files)
- YAML front matter structure
- How to use the files with Copilot
- Regeneration process

### 4. Supporting Files

**.gitignore:**
- Python cache files (`__pycache__/`, `*.pyc`)
- Virtual environments
- IDE files
- Temporary files
- Pandoc temporary files

## File Organization

```
original/
└── SRS - MODULE (...).docx          # Source DOCX files

markdowns/
├── manifest.json                     # Tracking file
└── <module>/                         # e.g., hrm, crm
    ├── introduction.md              # Document header
    ├── uc-{number}-{desc}.md        # Individual Use Cases
    └── {section-name}.md            # Other sections
```

## File Naming Conventions

### Use Case Files
- Pattern: `uc-{number}-{description}.md`
- Examples:
  - `uc-1.1.1-đăng-nhập-bằng-mật-khẩu.md`
  - `uc-2.1.1-xem-danh-sách-tìm-kiếm-chi-nhánh.md`

### Section Files
- Pattern: `{slugified-section-name}.md`
- Examples:
  - `introduction.md`
  - `phân-hệ-quản-lý-chung-sơ-đồ-tổ-chức.md`

## YAML Front Matter

### Use Case Files
```yaml
---
title: "UC1.1.1: Đăng nhập bằng mật khẩu"
type: "use-case"
uc_number: "1.1.1"
---
```

### Section Files
```yaml
---
title: "Section Title"
type: "section"
---
```

## Manifest Structure

```json
{
  "version": "1.0",
  "last_updated": "2025-10-09T03:31:41.303965",
  "files": {
    "SRS - HRM (...).docx": {
      "hash": "4fa9bc838b3774cb4d3374371e7d0c79ea3ea7b36d902fdda402df7a772fa944",
      "module": "hrm",
      "output_dir": "markdowns/hrm/SRS - HRM (...)",
      "generated_files": [
        "markdowns/hrm/.../introduction.md",
        "markdowns/hrm/.../uc-1.1.1-....md",
        ...
      ],
      "processed_at": "2025-10-09T03:31:41.303965"
    }
  }
}
```

## Test Results

### Initial Conversion
- Source: `SRS - HRM (1,2,3,4,5) - Bản Tổng hợp - Formatted.docx`
- Generated: **143 files**
  - 135 Use Case files
  - 8 section files
- Processing time: ~10 seconds
- Module extracted: `hrm`

### Idempotency Test
- Re-ran script immediately after initial conversion
- Result: ✅ "Skipping (unchanged)" - no reconversion
- Confirms hash-based change detection works correctly

## Usage Examples for Copilot

### Example 1: Reference a specific Use Case
```
"Implement the login functionality according to the requirements in 
markdowns/hrm/.../uc-1.1.1-đăng-nhập-bằng-mật-khẩu.md"
```

### Example 2: Reference multiple related UCs
```
"Review the employee management requirements in 
markdowns/hrm/.../uc-5.1.* files"
```

### Example 3: Reference a section
```
"Understand the overall structure from 
markdowns/hrm/.../phân-hệ-quản-lý-chung-sơ-đồ-tổ-chức.md"
```

## Workflow Process

### Automated (Production)
1. Developer adds/updates DOCX file in `/original/`
2. Commits and pushes to main/master branch
3. GitHub Action triggers automatically
4. Conversion script runs
5. Generated files are committed and pushed
6. Team members pull latest changes

### Manual (Development/Testing)
```bash
# Install Pandoc (if not installed)
sudo apt-get install pandoc

# Run conversion script
python3 scripts/convert_srs.py

# Review changes
git status
git diff markdowns/

# Commit if satisfied
git add markdowns/
git commit -m "docs: Update SRS Markdown files"
git push
```

## Design Decisions

### 1. Why Pandoc?
- Industry-standard document converter
- Excellent DOCX support
- Maintains formatting through Markdown
- Command-line interface easy to automate

### 2. Why split by headings?
- Makes files more manageable (smaller, focused)
- Easier for Copilot to retrieve specific context
- Better version control (smaller diffs)
- Simpler to reference specific requirements

### 3. Why SHA256 hashing?
- Reliable change detection
- Fast comparison (no need to reconvert unchanged files)
- Prevents unnecessary Git churn
- Industry standard for file integrity

### 4. Why YAML front matter?
- Structured metadata
- Easy to parse by tools
- Common convention in static site generators
- Provides context without reading full file

### 5. Why [skip ci] in commits?
- Prevents infinite loop (action → commit → action → ...)
- Generated files don't need to trigger another conversion
- Reduces unnecessary GitHub Actions usage

## Edge Cases Handled

1. **File with spaces in name**: ✅ Handled correctly
2. **Unicode characters in filename**: ✅ Handled correctly
3. **Unchanged files**: ✅ Skipped (hash-based detection)
4. **Removed source files**: ✅ Old generated files cleaned up
5. **Multiple DOCX files**: ✅ Processed independently
6. **Empty or malformed DOCX**: ⚠️ Will fail with error (Pandoc error)

## Known Limitations

1. **Pandoc dependency**: Requires Pandoc to be installed
2. **DOCX format dependency**: Only supports DOCX, not DOC
3. **Heading structure dependency**: Relies on proper H1/H2/H3 usage
4. **Module name extraction**: Expects "SRS - MODULE" pattern

## Future Enhancements (Not Implemented)

These were not required but could be added:

1. **Validation**: Pre-flight checks for DOCX structure
2. **Error reporting**: Email/Slack notifications on failure
3. **Statistics**: Generate reports on UC counts, changes
4. **Cross-references**: Detect and link related UCs
5. **Change summaries**: Generate changelog for each conversion
6. **Multiple format support**: PDF, ODT, etc.
7. **Batch processing**: Process multiple files in parallel

## Maintenance

### Adding New Modules
Simply add DOCX files following the naming pattern:
```
SRS - MODULE_NAME - description.docx
```

### Updating Existing Documents
Replace the DOCX file in `/original/` with the same name. The system will:
1. Detect the change via hash comparison
2. Remove old generated files
3. Generate new files from updated source

### Removing Documents
Delete the DOCX file from `/original/`. On next run, the system will:
1. Detect missing source file
2. Remove all generated files
3. Remove entry from manifest

## Troubleshooting

### Issue: Script fails with "Pandoc not found"
**Solution:** Install Pandoc: `sudo apt-get install pandoc`

### Issue: Generated files are incorrect
**Solution:** Check DOCX heading structure (H1, H2, H3 for UCs)

### Issue: Module name is "unknown"
**Solution:** Ensure filename follows pattern "SRS - MODULE ..."

### Issue: Files not regenerating
**Solution:** Check if hash changed. Delete manifest entry to force regeneration.

## Success Criteria Met

✅ DOCX files automatically converted to Markdown  
✅ Split into individual UC and section files  
✅ Organized under `markdowns/<module>/`  
✅ Manifest tracks hashes and generated files  
✅ Only changed files are reconverted  
✅ Old files removed when sources change/are removed  
✅ GitHub Action automates the process  
✅ Comprehensive documentation provided  
✅ Copilot can reference files easily  

## Conclusion

The automated SRS DOCX to Markdown conversion system is fully implemented and tested. It meets all requirements specified in the issue and provides a robust, maintainable solution for converting and organizing SRS documentation.

The system is production-ready and can be used immediately by team members.
