# Quick Start Guide

Quick reference for using the SRS DOCX to Markdown automation system.

## For Team Members

### Adding a New SRS Document

1. **Save your DOCX file** following this naming pattern:
   ```
   SRS - MODULE_NAME - description.docx
   ```
   Example: `SRS - CRM - Customer Management.docx`

2. **Copy to the repository**:
   ```bash
   cp "path/to/your/SRS - MODULE.docx" original/
   ```

3. **Commit and push**:
   ```bash
   git add original/
   git commit -m "docs: Add MODULE SRS document"
   git push
   ```

4. **Wait for automation** (usually < 1 minute):
   - GitHub Action will automatically run
   - Markdown files will be generated
   - Changes will be committed automatically

5. **Pull the results**:
   ```bash
   git pull
   ```

Your Markdown files will be in: `markdowns/<module>/<source-stem>/`

### Updating an Existing SRS Document

1. **Replace the DOCX file** in `original/` with the same filename
2. **Commit and push**
3. **System will automatically**:
   - Detect the change (via hash)
   - Remove old generated files
   - Generate new files
   - Commit the updates

### Using with GitHub Copilot

Reference specific Use Cases or sections in your prompts:

**Find UC files:**
```bash
# List all UC files for a module
ls markdowns/hrm/*/uc-*.md

# Find a specific UC
find markdowns -name "uc-1.1.1-*.md"
```

**Example Copilot prompts:**
```
"Implement login based on markdowns/hrm/.../uc-1.1.1-đăng-nhập-bằng-mật-khẩu.md"

"Review employee management requirements in markdowns/hrm/.../uc-5.1.*.md"

"Generate test cases for UC 2.1.1 in markdowns/hrm/.../uc-2.1.1-*.md"
```

## For Developers

### Running Conversion Manually

```bash
# Ensure Pandoc is installed
sudo apt-get install pandoc

# Run the script
python3 scripts/convert_srs.py
```

### Understanding the Output

Each generated file has:

1. **YAML front matter** (metadata):
   ```yaml
   ---
   title: "UC1.1.1: Đăng nhập bằng mật khẩu"
   type: "use-case"
   uc_number: "1.1.1"
   ---
   ```

2. **Markdown content** (the actual requirements)

### File Organization

```
markdowns/
├── manifest.json          # Tracks conversions
└── <module>/              # Module name (e.g., hrm)
    └── <source-stem>/     # DOCX filename without extension
        ├── uc-*.md        # Use Case files
        └── *.md           # Section files
```

### Troubleshooting

**Problem:** Files not generating  
**Solution:** Check filename has "SRS - MODULE" pattern

**Problem:** Wrong module name  
**Solution:** Rename DOCX to follow "SRS - MODULE ..." pattern

**Problem:** Script fails  
**Solution:** Ensure Pandoc is installed: `pandoc --version`

## Important Notes

⚠️ **DO NOT** manually edit files in `markdowns/` - they will be overwritten  
⚠️ Always edit the source DOCX files in `original/`  
⚠️ Use proper heading structure (H1, H2, H3) in your DOCX  
⚠️ Use Cases must start with "UC" in the heading (e.g., "UC1.1.1:")  

## Quick Command Reference

```bash
# Check what will be converted
ls original/*.docx

# See generated files
tree markdowns/

# Find specific UC
find markdowns -name "uc-1.1.1-*.md"

# View manifest
cat markdowns/manifest.json | jq .

# Force reconversion (delete manifest entry)
# Then run: python3 scripts/convert_srs.py

# Check GitHub Action status
# Go to: https://github.com/MaiVietLand/srs/actions
```

## Need Help?

- See [README.md](README.md) for detailed documentation
- See [IMPLEMENTATION_NOTES.md](IMPLEMENTATION_NOTES.md) for technical details
- Check GitHub Actions logs for conversion errors

## Example Workflow

```bash
# 1. Add new SRS document
cp ~/Documents/"SRS - CRM.docx" original/

# 2. Commit
git add original/
git commit -m "docs: Add CRM SRS"
git push

# 3. Wait ~30 seconds

# 4. Pull results
git pull

# 5. Use in Copilot
# "Reference markdowns/crm/.../uc-*.md files"
```

That's it! 🎉
