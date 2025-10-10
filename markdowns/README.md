# Generated Markdown Files

This directory contains automatically generated Markdown files from DOCX SRS documents.

## ⚠️ Important Notes

- **DO NOT manually edit files in this directory** - they are automatically generated and will be overwritten
- All changes should be made to the source DOCX files in `/original/`
- The conversion script will automatically regenerate these files when sources change

## Directory Structure

```
markdowns/
├── manifest.json              # Tracking file (SHA256 hashes, generated files list)
└── <module>/                  # Module directory (e.g., hrm, crm, etc.)
    ├── introduction.md       # Document header content
    ├── uc-*.md              # Individual Use Case files
    └── *.md                 # Section files (for H1/H2 content)
```

## File Types

### Use Case Files (`uc-*.md`)

Individual files for each Use Case (UC), extracted from H3 headings starting with "UC".

**Naming pattern**: `uc-{number}-{description}.md`

**Example**: `uc-1.1.1-đăng-nhập-bằng-mật-khẩu.md`

**YAML Front Matter**:
```yaml
---
title: "UC1.1.1: Đăng nhập bằng mật khẩu"
type: "use-case"
uc_number: "1.1.1"
---
```

### Section Files

Files for major sections (H1) and subsections (H2).

**Example**: `phân-hệ-quản-lý-chung-sơ-đồ-tổ-chức.md`

**YAML Front Matter**:
```yaml
---
title: "Section Title"
type: "section"
---
```

## Manifest File

The `manifest.json` file tracks:
- Source file hashes (SHA256)
- Module names
- Output directories
- List of all generated files
- Processing timestamps

This enables incremental conversion - only files that have changed are reconverted.

## Using These Files

### With GitHub Copilot

Reference specific files in your prompts:

```
"Implement based on markdowns/hrm/uc-1.1.1-đăng-nhập-bằng-mật-khẩu.md"
"Review requirements in markdowns/hrm/uc-2.1.1-xem-danh-sách-tìm-kiếm-chi-nhánh.md"
```

### Searching

Use GitHub's search or `grep` to find specific Use Cases:

```bash
# Find a specific UC number
find markdowns -name "uc-1.1.1-*.md"

# Search content
grep -r "authentication" markdowns/
```

### Reading

Each file is self-contained with:
- YAML metadata for context
- Full Use Case or section content
- Original formatting preserved from DOCX

## Regeneration

Files are automatically regenerated when:
- Source DOCX files in `/original/` are modified
- Source DOCX files are added
- Source DOCX files are removed (old generated files are cleaned up)

To manually regenerate:
```bash
python3 scripts/convert_srs.py
```

## Questions?

See the main [README.md](../README.md) in the repository root for complete documentation.
