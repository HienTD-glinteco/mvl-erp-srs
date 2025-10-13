---
title: "UC4.8.12: Kết xuất báo cáo Thống kê số lượng ứng viên trúng tuyển"
type: "use-case"
uc_number: "4.8.12"
---

### UC4.8.12: Kết xuất báo cáo Thống kê số lượng ứng viên trúng tuyển

| **Mục tiêu:** | Cho phép người dùng kết xuất báo cáo trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Kết xuất trong Màn hình Báo cáo Thống kê số lượng ứng viên trúng tuyển. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Người dùng có thể tra cứu và kết xuất (export) báo cáo ra PDF/Excel. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.8.12 | **Exporting File Rules:** |
|  | ❖ Hệ thống thực hiện kết xuất báo cáo. Nếu có bộ lọc, kết xuất theo bộ lọc cuối cùng được áp dụng. |
|  | ❖ File kết xuất có định dạng Excel hoặc PDF. |
