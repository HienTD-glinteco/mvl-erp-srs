---
title: "UC 5.4.1: Xem danh sách Người phụ thuộc của nhân viên"
type: "use-case"
uc_number: "5.4.1"
---

### UC 5.4.1: Xem danh sách Người phụ thuộc của nhân viên

  ----------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem danh sách Người phụ thuộc của nhân viên
  --------------------------- ------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem trong "Quản lý Người phụ thuộc"

  **Sự kiện kích hoạt:**      Người dùng truy cập Màn hình của Phân hệ con "Quản lý Người phụ thuộc"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn Danh sách "Người phụ thuộc" với đầy đủ thông tin
  ----------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.4.1 | **Quy tắc Xem màn hình danh sách Người phụ thuộc:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách những Người phụ thuộc đã tạo với đầy đủ thông tin tương ứng từng Nhân viên |
|  | - Mỗi khi truy cập màn hình , hệ thống tự động sắp xếp dữ liệu theo thứ tự được tạo ra từ gần nhất đến xa nhất |

#### Mô tả màn hình

![](media/image98.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Ô Tìm kiếm | Textbox | Nhập từ khóa và nhấn Enter để tìm kiếm | UC 5.4.2: Tìm kiếm thông tin Người phụ thuộc của Nhân viên | Có |
| Mã nhân viên | Trường dữ liệu | Hiển thị "Mã nhân viên" tương ứng | N/A | Có |
| Tên nhân viên | Trường dữ liệu | Hiển thị "Tên nhân viên" tương ứng | N/A | Có |
| Tên người phụ thuộc | Trường dữ liệu | Hiển thị "Tên người phụ thuộc" tương ứng | N/A | Có |
| Mối quan hệ | Trường dữ liệu | Hiển thị "Mối quan hệ" tương ứng | N/A | Có |
| Ngày sinh | Trường dữ liệu | Hiển thị "Ngày sinh" tương ứng | N/A | Có |
| Số CMND/CCCD | Trường dữ liệu | Hiển thị "Số CMND/CCCD" tương ứng | N/A | Có |
| Thao tác | Nút | Hiển thị 3 nút thao tác: | \- Nút "Xem chi tiết: [[UC 5.4.4: Xem chi tiết thông tin một Người phụ thuộc]{.underline}](#uc-5.4.4-xem-chi-tiết-thông-tin-một-người-phụ-thuộc-của-nhân-viên) |  |
|  |  | \- Xem chi tiết | \- Nút "Chỉnh sửa": [[UC 5.4.5: Chỉnh sửa thông tin một Người phụ thuộc]{.underline}](#uc-5.4.5-chỉnh-sửa-thông-tin-của-một-người-phụ-thuộc-của-nhân-viên) |  |
|  |  | \- Chỉnh sửa | \- Nút "Xóa": [[UC 5.4.6: Xóa một Người phụ thuộc]{.underline}](#uc-5.4.6-xóa-một-người-phụ-thuộc-của-nhân-viên) |  |
|  |  | \- Xóa |  |  |
