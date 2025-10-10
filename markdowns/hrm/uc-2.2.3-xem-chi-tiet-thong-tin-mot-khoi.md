---
title: "UC 2.2.3: Xem chi tiết thông tin một Khối"
type: "use-case"
uc_number: "2.2.3"
---

### UC 2.2.3: Xem chi tiết thông tin một Khối

  ------------------------------------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem thông tin chi tiết một Khối
  --------------------------- --------------------------------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem Khối trong phân hệ "Quản lý Khối"

  **Sự kiện kích hoạt:**      Người dùng nhấn nút "Xem chi tiết" của Khối tương ứng trong màn danh sách của "Quản lý Khối"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình "Chi tiết" thông tin của Khối với thông tin theo lần thay đổi cuối cùng tương ứng
  ------------------------------------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.2.3 | **Quy tắc Xem màn hình Chi tiết thông tin Khối:** |
|  | - Người dùng ở màn hình "Quản lý Khối" -\> nhấn nút "Xem chi tiết" của Khối tương ứng: |
|  | - Hệ thống hiển thị màn hình xem thông tin chi tiết theo lần thay đổi cuối cùng của Khối tương ứng |

#### Mô tả màn hình

![](media/image91.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Mã khối | Trường dữ liệu | \- Hiển thị thông tin chi tiết của Khối tương ứng | Hiển thị dạng Read-only |  |
|  |  | \- Những trường thông tin giống của "[[màn tạo mới một Khối]{.underline}](#uc-2.2.2-tạo-mới-một-khối)" |  |  |
|  |  | - Thêm thông tin "Mã khối" |  |  |
| Tên khối | Trường dữ liệu |  |  |  |
| Loại Khối | Trường dữ liệu |  |  |  |
| Chi nhánh | Trường dữ liệu |  |  |  |
| Mô tả | Trường dữ liệu |  |  |  |
| Xóa | Nút | Nhấn để xóa Khối tương ứng | UC 2.2.5 Xóa một Khối |  |
| Chỉnh sửa | Nút | Nhấn để chỉnh sửa thông tin Khối | UC 2.2.4: Chỉnh sửa thông tin một Khối |  |
