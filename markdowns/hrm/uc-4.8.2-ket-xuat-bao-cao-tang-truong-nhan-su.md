---
title: "UC4.8.2: Kết xuất báo cáo Tăng trưởng nhân sự"
type: "use-case"
uc_number: "4.8.2"
---

### UC4.8.2: Kết xuất báo cáo Tăng trưởng nhân sự

| **Mục tiêu:** | Cho phép người dùng kết xuất báo cáo dạng bảng hoặc chi tiết báo cáo ở dạng excel Tăng trưởng nhân sự theo tuần trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Kết xuất trong Màn hình Báo cáo tăng giảm nhân sự (theo tuần). |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | File được kết xuất thành công với định dạng được chọn |
|  | - Báo cáo chi tiết (Excel/PDF) |
|  | - Báo cáo dạng bảng (ảnh) |
|  | Nếu có bộ lọc kết xuất theo bộ lọc cuối cùng được áp dụng. |
|  | Người dùng có thể tải về file hoặc lưu trữ nội bộ hệ thống. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.8.2 | **Exporting File Rules:** |
|  | ❖ Cho phép người dùng chọn kết xuất theo dạng bảng (file ảnh) hoặc chi tiết báo cáo (file excel/Pdf) |
|  | ❖ Hệ thống thực hiện kết xuất báo cáo. Nếu có bộ lọc, kết xuất theo bộ lọc cuối cùng được áp dụng. |
|  | ❖ Đối với báo cáo chi tiết, kết xuất thông tin chi tiết đến phòng (kể cả có áp dụng bộ lọc) |
|  | ❖ File kết xuất có định dạng Excel hoặc PDF. |
