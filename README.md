# SRS Documentation System

Automated conversion system for Software Requirements Specifications (SRS) documents from DOCX to Markdown format.

## Overview

This repository provides an automated workflow to convert DOCX-based SRS documents into well-structured Markdown files, making them easily searchable and accessible for GitHub Copilot and other AI coding assistants.

## Directory Structure

```
srs/
├── original/                   # Source DOCX files
│   └── *.docx                 # SRS documents in DOCX format
├── markdowns/                  # Generated Markdown files
│   ├── manifest.json          # Tracking file for conversions
│   └── <module>/              # Organized by module (e.g., hrm, crm)
│       ├── uc-*.md           # Individual Use Case files
│       └── *.md              # Section files
├── scripts/
│   └── convert_srs.py         # Conversion script
└── .github/workflows/
    └── convert-srs.yml        # GitHub Actions workflow
```

## How It Works

### Automated Conversion Process

1. **Trigger**: When DOCX files are added or modified in `/original/`, the GitHub Action automatically runs
2. **Conversion**: Uses Pandoc to convert DOCX to Markdown format
3. **Splitting**: Intelligently splits content by:
   - **H1 headings** (`#`) - Major sections
   - **H2 headings** (`##`) - Subsections
   - **H3 headings** (`###`) starting with "UC" - Individual Use Cases
4. **Organization**: Files are organized as:
   - Module name extracted from filename (e.g., "SRS - HRM..." → `markdowns/hrm/`)
   - Individual UC and section files placed directly in module directory with descriptive names
5. **Tracking**: Maintains a manifest with SHA256 hashes to detect changes
6. **Cleanup**: Automatically removes old files when sources are updated or deleted

### File Naming Convention

- **Use Cases**: `uc-{number}-{description}.md`
  - Example: `uc-1.1.1-đăng-nhập-bằng-mật-khẩu.md`
- **Sections**: `{section-name}.md`
  - Example: `phân-hệ-quản-lý-chung-sơ-đồ-tổ-chức.md`
- **Introduction**: `introduction.md` (document header content)

### YAML Front Matter

Each generated file includes metadata in YAML front matter:

**Use Case files:**
```yaml
---
title: "UC1.1.1: Đăng nhập bằng mật khẩu"
type: "use-case"
uc_number: "1.1.1"
---
```

**Section files:**
```yaml
---
title: "Section Title"
type: "section"
---
```

## Usage

### Adding or Updating SRS Documents

1. Place your DOCX file in the `/original/` directory
2. Commit and push to the main branch
3. The GitHub Action will automatically:
   - Convert the DOCX to Markdown
   - Split it into organized files
   - Commit the generated files back to the repository

### Manual Conversion

To run the conversion script manually:

```bash
# Ensure Pandoc is installed
sudo apt-get install pandoc

# Run the conversion script
python3 scripts/convert_srs.py
```

### Using with GitHub Copilot

When working with Copilot coding agents, reference specific Use Cases or sections:

**Example prompts:**
- "Implement the login functionality based on `markdowns/hrm/.../uc-1.1.1-đăng-nhập-bằng-mật-khẩu.md`"
- "Review the requirements in `markdowns/hrm/.../uc-2.1.1-xem-danh-sách-tìm-kiếm-chi-nhánh.md`"
- "Reference all UC files in `markdowns/hrm/.../ ` for the employee management module"

The structured format allows Copilot to:
- Quickly locate relevant requirements
- Understand context through YAML metadata
- Reference specific use cases precisely

## Manifest File

The `markdowns/manifest.json` file tracks:
- SHA256 hash of each source DOCX file
- Module name and output directory
- List of generated files
- Processing timestamp

This enables incremental updates - only changed files are reconverted.

## Module Naming

The system extracts module names from filenames:
- `SRS - HRM (...)` → `hrm`
- `SRS - CRM (...)` → `crm`
- Pattern: Extracts text after "SRS -" and before any parentheses

## Workflow Configuration

The GitHub Action (`.github/workflows/convert-srs.yml`) triggers on:
- Push to main/master branch with changes to `original/*.docx`
- Manual workflow dispatch

**Features:**
- Runs on Ubuntu with Python 3.12
- Installs Pandoc automatically
- Commits changes with `[skip ci]` to prevent loops
- Uses GitHub Actions bot for commits

## Benefits

✅ **Automated**: No manual conversion needed  
✅ **Incremental**: Only reconverts changed files  
✅ **Organized**: Structured by module and use case  
✅ **Searchable**: Markdown format is text-searchable  
✅ **AI-Friendly**: Optimized for Copilot context retrieval  
✅ **Version Controlled**: All changes tracked in Git  
✅ **Clean**: Automatically removes outdated files  

## Requirements

- Python 3.12+
- Pandoc 2.0+
- GitHub Actions (for automation)

## Troubleshooting

**Issue: Files not converting**
- Verify the DOCX file is in `/original/`
- Check that the filename contains "SRS -" for module extraction
- Review GitHub Actions logs for errors

**Issue: Incorrect module name**
- Ensure filename follows pattern: `SRS - MODULE ...`
- Check `manifest.json` for the extracted module name

**Issue: Use Cases not splitting correctly**
- Verify H3 headings start with "UC" or "UC " followed by a number
- Check the DOCX document structure

## Contributing

When adding new DOCX files:
1. Follow naming convention: `SRS - MODULE_NAME - description.docx`
2. Use proper heading structure (H1, H2, H3)
3. Start Use Case headings with "UC{number}:"
4. Test locally before pushing

## License

This automation system is for internal use. SRS documents remain proprietary.
