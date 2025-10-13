# Fix for Missing First UC Files

## Problem
The generated markdown files were missing the first UC files in each module:
- UC 1.1.1
- UC 2.1.1
- UC 2.2.1
- UC 2.3.1
- UC 2.4.1
- ... and 11 more (16 total)

## Root Cause
The original conversion created an incomplete manifest with only 80 UC files instead of the expected 96 files. The issue was that when the conversion script detected that the source DOCX file hash was unchanged, it would skip regeneration entirely, even though files were missing.

## Solution
Modified `scripts/convert_srs.py` to add validation when a file is marked as "unchanged":

1. **File Existence Check**: Verify all files listed in the manifest actually exist on disk
2. **UC Count Validation**: Compare the number of UC files in the manifest against the number of UCs found in the source document
3. **Auto-Regeneration**: If either check fails, force a regeneration to restore or create missing files

## Implementation Details

The fix adds logic in the `process_docx_file` method around line 496:

```python
if old_hash == file_hash:
    # Quick validation: check if generated files actually exist
    old_files = self.manifest["files"][file_key].get("generated_files", [])
    missing_files = []
    for rel_path in old_files:
        file_path = self.repo_root / rel_path
        if not file_path.exists():
            missing_files.append(rel_path)
    
    if missing_files:
        # Regenerate to restore missing files
        ...
    else:
        # Also verify UC count matches the source
        markdown_content = self.convert_docx_to_markdown(docx_path)
        markdown_content = self.post_process_markdown(markdown_content)
        all_uc_numbers = self.extract_all_uc_numbers(markdown_content)
        
        uc_files_in_manifest = [f for f in old_files if '/uc-' in f]
        
        if len(uc_files_in_manifest) < len(all_uc_numbers):
            # Regenerate to create missing UC files
            ...
```

## Results
- ✓ All 96 UC files now generated correctly (was 80)
- ✓ All 16 first UC files now present (was 0)
- ✓ Existing unchanged files are preserved
- ✓ Missing files are automatically detected and regenerated
- ✓ Script correctly skips processing when everything is up to date

## Files Modified
- `scripts/convert_srs.py`: Added validation logic to detect missing UC files

## Files Added
- 16 missing first UC files in `markdowns/hrm/`:
  - uc-1.1.1-dang-nhap-bang-mat-khau.md
  - uc-2.1.1-xem-danh-sach-tim-kiem-chi-nhanh.md
  - uc-2.2.1-xem-danh-sach-tim-kiem-khoi.md
  - uc-2.3.1-xem-danh-sach-tim-kiem-phong-ban.md
  - uc-2.4.1-xem-danh-sach-tim-kiem-chuc-vu.md
  - uc-3.1.1-xem-danh-sach-tim-kiem-vai-tro-role.md
  - uc-3.2.1-xem-danh-sach-tim-kiem-nhan-vien-theo-role.md
  - uc-3.3.1-xem-danh-sach-tim-kiem-quyen.md
  - uc-4.1.1-xem-danh-sach-kenh-tuyen-dung.md
  - uc-4.2.1-xem-danh-sach-nguon-tuyen-dung.md
  - uc-4.3.1-xem-danh-sach-chi-phi-tuyen-dung.md
  - uc-4.4.1-xem-danh-sach-de-nghi-tuyen-dung.md
  - uc-4.5.1-xem-danh-sach-mo-ta-cong-viec.md
  - uc-4.6.1-xem-danh-sach-ung-vien.md
  - uc-4.7.1-xem-danh-sach-lich-phong-van.md
  - uc-4.8.1-xem-bao-cao-tang-truong-nhan-su-theo-tuan.md
