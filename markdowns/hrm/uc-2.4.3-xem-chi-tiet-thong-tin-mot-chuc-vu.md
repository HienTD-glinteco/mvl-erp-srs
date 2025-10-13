---
title: "UC 2.4.3: Xem chi tiết thông tin một Chức vụ"
type: "use-case"
uc_number: "2.4.3"
---

### UC 2.4.3: Xem chi tiết thông tin một Chức vụ

  ---------------------------------------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem thông tin chi tiết một Chức vụ
  --------------------------- -----------------------------------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem chức vụ trong phân hệ "Quản lý Chức vụ"

  **Sự kiện kích hoạt:**      Người dùng nhấn nút "Xem chi tiết" của Chức vụ tương ứng trong màn danh sách của "Quản lý Chức vụ"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình "Chi tiết" thông tin của Chức vụ với thông tin theo lần thay đổi cuối cùng tương ứng
  ---------------------------------------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.4.3 | **Quy tắc Xem màn hình Chi tiết thông tin Chức vụ:** |
|  | - Người dùng ở màn hình "Quản lý Chức vụ" -\> nhấn nút "Xem chi tiết" của Chức vụ tương ứng: |
|  | - Hệ thống hiển thị màn hình xem thông tin chi tiết theo lần thay đổi cuối cùng của Chức vụ tương ứng |

#### Mô tả màn hình

![](media/image40.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Mã chức vụ | Trường dữ liệu | \- Hiển thị thông tin chi tiết của Khối tương ứng | Hiển thị dạng Read-only |  |
|  |  | \- Những trường thông tin giống [[màn tạo mới một Chức vụ]{.underline}](#uc-2.4.2-tạo-mới-một-chức-vụ) |  |  |
|  |  | - Thêm thông tin "Mã chức vụ" |  |  |
| Tên chức vụ | Trường dữ liệu |  |  |  |
| Mô tả | Trường dữ liệu |  |  |  |
| Xóa | Nút | Nhấn để xóa Chức vụ tương ứng | UC 2.4.5: Xóa một Chức vụ |  |
| Chỉnh sửa | Nút | Nhấn để chỉnh sửa thông tin Chức vụ | UC 2.4.4: Chỉnh sửa thông tin một chức vụ |  |
