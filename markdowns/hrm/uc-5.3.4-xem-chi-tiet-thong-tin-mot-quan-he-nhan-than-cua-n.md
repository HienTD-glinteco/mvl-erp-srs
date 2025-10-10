---
title: "UC 5.3.4: Xem chi tiết thông tin một Quan hệ nhân thân của nhân viên"
type: "use-case"
uc_number: "5.3.4"
---

### UC 5.3.4: Xem chi tiết thông tin một Quan hệ nhân thân của nhân viên

  ---------------------------------------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem chi tiết Quan hệ Nhân thân của Nhân viên
  --------------------------- -----------------------------------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền cho xem phân hệ con "Quản lý Nhân thân"

  **Sự kiện kích hoạt:**      Người dùng nhấn nút "Xem chi tiết" của một Quan hệ nhân thân tại màn hình danh sách "Quản lý Quan hệ nhân thân"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình "Chi tiết" thông tin của Quan hệ nhân thân
  ---------------------------------------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 5.3.4 | **Quy tắc Xem màn hình Chi tiết Quan hệ Nhân thân của Nhân viên:** |
|  | - Người dùng ở màn hình "Quản lý Quan hệ nhân thân" -\> nhấn nút "Xem chi tiết" của Quan hệ nhân thân tương ứng |
|  | - Hệ thống hiển thị màn hình xem thông tin Chi tiết theo lần thay đổi cuối cùng của Quan hệ nhân thân tương ứng |

#### Mô tả màn hình

![](media/image83.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Mã nhân viên | Trường dữ liệu | Autofill những thông tin tương ứng của Quan hệ nhân thân của Nhân viên | \- Hiển thị dang: Read-only |  |
|  |  |  | \- Những trường thông tin giống của [[màn Tạo mới một Quan hệ Nhân thân]{.underline}](#uc-5.3.3-tạo-mới-một-quan-hệ-nhân-thân-của-nhân-viên) |  |
| Tên nhân viên | Trường dữ liệu |  |  |  |
| Tên người thân | Trường dữ liệu |  |  |  |
| Mối quan hệ | Trường dữ liệu |  |  |  |
| Ngày sinh | Trường dữ liệu |  |  |  |
| Số CMND/CCCD | Trường dữ liệu |  |  |  |
| Địa chỉ | Trường dữ liệu |  |  |  |
| Số điện thoại | Trường dữ liệu |  |  |  |
| File đính kèm | Trường dữ liệu |  |  |  |
| Ghi chú | Trường dữ liệu |  |  |  |
| Chỉnh sửa | Nút | Nhấn để chỉnh sửa thông tin tương ứng | UC 5.3.5: Chỉnh sửa thông tin của một Quan hệ nhân thân |  |
