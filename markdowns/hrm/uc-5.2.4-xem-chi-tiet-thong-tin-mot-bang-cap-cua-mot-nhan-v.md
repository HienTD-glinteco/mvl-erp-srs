---
title: "UC 5.2.4: Xem chi tiết thông tin một Bằng cấp của một nhân viên"
type: "use-case"
uc_number: "5.2.4"
---

### UC 5.2.4: Xem chi tiết thông tin một Bằng cấp của một nhân viên

  --------------------------------------------------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem chi tiết Bằng cấp/Chứng chỉ của Nhân viên
  --------------------------- ----------------------------------------------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền cho xem phân hệ con "Quản lý Bằng cấp/Chứng chỉ môi giới"

  **Sự kiện kích hoạt:**      Người dùng nhấn nút "Xem chi tiết" của một Bằng cấp/Chứng chỉ tại màn hình danh sách "Quản lý Bằng cấp/Chứng chỉ môi giới"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình "Chi tiết" thông tin của Bằng cấp/Chứng chỉ môi giới
  --------------------------------------------------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.2.4 | **Quy tắc Xem màn hình Chi tiết Bằng cấp/Chứng chỉ của Nhân viên:** |
|  | - Người dùng ở màn hình "Quản lý Bằng cấp/Chứng chỉ môi giới" -\> nhấn nút "Xem chi tiết" của Bằng cấp/Chứng chỉ tương ứng |
|  | - Hệ thống hiển thị màn hình xem thông tin Chi tiết theo lần thay đổi cuối cùng của Bằng cấp/Chứng chỉ tương ứng |

#### Mô tả màn hình

![](media/image31.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Tên chứng chỉ | Trường dữ liệu | Hiển thị đầy đủ trường thông tin như của màn [[Tạo mới một Bằng cấp/Chứng chỉ môi giới]{.underline}](#uc-5.2.3-tạo-mới-bằng-cấpchứng-chỉ-môi-giới) | \- Hiển thị dạng: Read-only |  |
|  |  |  | \- Hiển thị thông tin của Bằng cấp/Chứng chỉ của nhân viên tương ứng |  |
| Mã chứng chỉ | Trường dữ liệu |  |  |  |
| Tên nhân viên | Trường dữ liệu |  |  |  |
| Mã nhân viên | Trường dữ liệu |  |  |  |
| Tổ chức cấp | Trường dữ liệu |  |  |  |
| Ngày cấp | Trường dữ liệu |  |  |  |
| Ngày hết hạn | Trường dữ liệu |  |  |  |
| Tải lên File chứng chỉ | Trường dữ liệu |  |  |  |
| Ghi chú | Trường dữ liệu |  |  |  |
