---
title: "UC 5.4.4: Xem chi tiết thông tin một Người phụ thuộc của nhân viên"
type: "use-case"
uc_number: "5.4.4"
---

### UC 5.4.4: Xem chi tiết thông tin một Người phụ thuộc của nhân viên

  -----------------------------------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem chi tiết Người phụ thuộc của Nhân viên
  --------------------------- -------------------------------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền cho xem phân hệ con "Quản lý Người phụ thuộc"

  **Sự kiện kích hoạt:**      Người dùng nhấn nút "Xem chi tiết" của một Người phụ thuộc tại màn hình danh sách "Quản lý Người phụ thuộc"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình "Chi tiết" thông tin của Người phụ thuộc
  -----------------------------------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.4.4 | **Quy tắc Xem màn hình Chi tiết Người phụ thuộc của Nhân viên:** |
|  | - Người dùng ở màn hình "Quản lý Người phụ thuộc" -\> nhấn nút "Xem chi tiết" của Người phụ thuộc tương ứng |
|  | - Hệ thống hiển thị màn hình xem thông tin Chi tiết theo lần thay đổi cuối cùng của Người phụ thuộc tương ứng |

#### Mô tả màn hình

![](media/image130.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Mã nhân viên | Trường dữ liệu | Autofill những thông tin tương ứng của Người phụ thuộc của Nhân viên | \- Hiển thị dạng: Read-only |  |
|  |  |  | \- Những trường thông tin giống của [[màn hình Tạo mới một Người phụ thuộc]{.underline}](#uc-5.4.3-tạo-mới-một-người-phụ-thuộc-của-nhân-viên) |  |
| Tên nhân viên | Trường dữ liệu |  |  |  |
| Tên người phụ thuộc | Trường dữ liệu |  |  |  |
| Mối quan hệ | Trường dữ liệu |  |  |  |
| Ngày sinh | Trường dữ liệu |  |  |  |
| Số CMND/CCCD | Trường dữ liệu |  |  |  |
| File đính kèm | Trường dữ liệu |  |  |  |
| Ghi chú | Trường dữ liệu |  |  |  |
| Chỉnh sửa | Nút | Nhấn để chỉnh sửa thông tin tương ứng | UC 5.4.5: Chỉnh sửa thông tin của một Người phụ thuộc |  |
