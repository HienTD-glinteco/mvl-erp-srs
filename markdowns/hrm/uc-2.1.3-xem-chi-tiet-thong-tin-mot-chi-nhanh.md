---
title: "UC 2.1.3: Xem chi tiết thông tin một Chi nhánh"
type: "use-case"
uc_number: "2.1.3"
---

### UC 2.1.3: Xem chi tiết thông tin một Chi nhánh

  **Mục tiêu:**               Cho phép người dùng xem thông tin chi tiết một Chi nhánh
  --------------------------- ---------------------------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem Chi nhánh trong phân hệ "Quản lý Chi nhánh"
  **Sự kiện kích hoạt:**      Người dùng nhấn nhấn nút "Xem chi tiết" Chi nhánh tương ứng trong màn danh sách của "Quản lý Chi nhánh"
  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng
  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình "Chi tiết" thông tin của Chi nhánh

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.1.3 | **Quy tắc Xem màn hình Chi tiết thông tin Chi nhánh:** |
|  | - Người dùng ở màn hình "Quản lý Chi nhánh" -\> nhấn nút "Xem chi tiết" của Chi nhánh tương ứng: |
|  | - Hệ thống hiển thị màn hình xem thông tin chi tiết theo lần thay đổi cuối cùng của Chi nhánh tương ứng |

#### Mô tả màn hình

![](media/image96.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Mã chi nhánh | Trường dữ liệu | \- Hiển thị thông tin chi tiết theo lần thay đổi cuối cùng của Chi nhánh tương ứng | Hiển thị dạng Read-only |  |
|  |  | \- Những trường thông tin giống [[màn tạo mới một Chi nhánh]{.underline}](#uc-2.1.2-tạo-mới-một-chi-nhánh) |  |  |
|  |  | - Thêm thông tin "Mã chi nhánh" |  |  |
| Tên chi nhánh | Trường dữ liệu |  |  |  |
| Địa chỉ đường phố | Trường dữ liệu |  |  |  |
| Phường/Xã | Trường dữ liệu |  |  |  |
| Tỉnh | Trường dữ liệu |  |  |  |
| Số điện thoại liên hệ | Trường dữ liệu |  |  |  |
| Email | Trường dữ liệu |  |  |  |
| Mô tả | Trường dữ liệu |  |  |  |
| Xóa | Nút | Nhấn để Xóa Chi nhánh tương ứng | UC 2.1.5: Xóa một Chi nhánh |  |
| Chỉnh sửa | Nút | Nhấn để chỉnh sửa thông tin Chi nhánh | UC 2.1.4: Chỉnh sửa thông tin 1 Chi nhánh |  |
