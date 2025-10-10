---
title: "UC 5.2.1: Xem danh sách Bằng cấp/ Chứng chỉ môi giới"
type: "use-case"
uc_number: "5.2.1"
---

### UC 5.2.1: Xem danh sách Bằng cấp/ Chứng chỉ môi giới

  -----------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem danh sách Bằng cấp/ Chứng chỉ môi giới của nhân viên
  --------------------------- -------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem trong "Quản lý Bằng cấp/ Chứng chỉ môi giới"

  **Sự kiện kích hoạt:**      Người dùng truy cập Màn hình của Phân hệ con "Quản lý Bằng cấp/ Chứng chỉ môi giới"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn Danh sách "Bằng cấp/ Chứng chỉ môi giới" với đầy đủ thông tin
  -----------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 5.2.1 | **Quy tắc Xem màn hình danh sách Bằng cấp/ Chứng chỉ môi giới:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách những Bằng cấp/ Chứng chỉ môi giới đã tạo với đầy đủ thông tin tương ứng từng Nhân viên |
|  | - Mỗi khi truy cập màn hình , hệ thống tự động sắp xếp dữ liệu theo thứ tự mã Chứng chỉ từ cao xuống thấp |

#### Mô tả màn hình

![](media/image22.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Ô Tìm kiếm | Textbox | Nhập "Tên chứng chỉ" hoặc "Tên nhân viên" để tìm kiếm | [[UC 5.2.2: Tìm kiếm thông tin một Bằng cấp/ Chứng chỉ môi giới]{.underline}](#uc-5.2.2-tìm-kiếm-thông-tin-một-bằng-cấp-chứng-chỉ-môi-giới) |  |
| Mã chứng chỉ | Trường dữ liệu | Hiển thị Mã của chứng chỉ tương ứng | Khi nhấn vào tiêu đề cột, hệ thống sẽ đảo chiều sắp xếp giữa tăng dần và giảm dần | Có |
| Tên chứng chỉ | Trường dữ liệu | Hiển thị Tên chứng chỉ của nhân viên | N/A | Có |
| Tên nhân viên | Trường dữ liệu | Hiển thị Tên nhân viên | N/A | Có |
| Tổ chức cấp | Trường dữ liệu | Hiển thị Tổ chức cấp của chứng chỉ | N/A | Có |
| Ngày cấp | Trường dữ liệu | Hiển thị Ngày cấp của chứng chỉ | N/A | Có |
| Ngày hết hạn | Trường dữ liệu | Hiển thị Ngày hết hạn của chứng chỉ | N/A | Có |
| Trạng thái | Trường dữ liệu | Hiển thị Trạng thái của chứng chỉ | Có 2 trạng thái:\ | Có |
|  |  |  | - "**Còn hiệu lực"**: hiển thị khi **Ngày hiện tại ≤ Ngày hết hạn**. |  |
|  |  |  | **- "Hết hiệu lực"**: hiển thị khi **Ngày hiện tại \> Ngày hết hạn**. |  |
| Thao tác | Nút | Hiển thị 3 nút thao tác: | \- Nút "Xem chi tiết": [[UC 5.2.4:Xem chi tiết Bằng cấp/ Chứng chỉ]{.underline}](#uc-5.2.4-xem-chi-tiết-thông-tin-một-bằng-cấp-của-một-nhân-viên) |  |
|  |  | \- Xem chi tiết | \- Nút "Chỉnh sửa": [[UC 5.2.5: Chỉnh sửa thông tin một Bằng cấp/ Chứng chỉ]{.underline}](#uc-5.2.5-chỉnh-sửa-thông-tin-của-một-bằng-cấpchứng-chỉ-môi-giới) |  |
|  |  | \- Chỉnh sửa | \- Nút "Xóa": [[UC 5.2.6: Xóa một Bằng cấp/ Chứng chỉ]{.underline}](#uc-5.2.6-xóa-một-bằng-cấp-chứng-chỉ-môi-giới) |  |
|  |  | \- Xóa |  |  |
