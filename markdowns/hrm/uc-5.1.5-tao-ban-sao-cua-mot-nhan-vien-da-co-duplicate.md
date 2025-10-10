---
title: "UC 5.1.5: Tạo bản sao của một nhân viên đã có (duplicate)"
type: "use-case"
uc_number: "5.1.5"
---

### UC 5.1.5: Tạo bản sao của một nhân viên đã có (duplicate)

  -----------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng tạo một bản sao với một Hồ sơ Nhân viên đã có
  --------------------------- -------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền tạo bản sao tại "Quản lý Hồ sơ Nhân viên"

  **Sự kiện kích hoạt:**      Người dùng nhấn nút "Tạo bản sao nhân viên" tại màn hình "Chỉnh sửa nhân viên"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn Tạo mới một Hồ sơ nhân viên với những thông tin được điền sẵn
  -----------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.1.5 | **Quy tắc Tạo bản sao Hồ sơ Nhân viên:** |
|  | - Người dùng vào màn hình "Chỉnh sửa Hồ sơ nhân viên" -\> nhấn nút "Tạo bản sao nhân viên" |
|  | - Hệ thống hiển thị [[màn hình "Tạo mới một Hồ sơ nhân viên"]{.underline}](#uc-5.1.4-tạo-mới-một-hồ-sơ-nhân-viên) với những trường thông tin sau được được điền sẵn (giống như thông tin của Hồ sơ nhân viên được tạo bản sao) |
|  | - Chi nhánh |
|  | - Khối |
|  | - Phòng ban |
|  | - Loại hợp đồng |
|  | - Chức vụ |
|  | - Trạng thái |
|  | - Ngày bắt đầu |
|  | - Ngày nghỉ việc |

#### Mô tả màn hình

![](media/image52.png)

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**           **Kiểu dữ liệu**   **Mô tả**                       **Logic nghiệp vụ**                                                                                                                                                     **Bắt buộc**
  ----------------------- ------------------ ------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------
  Tạo bản sao nhân viên   Nút                Nhấn để tạo bản sao nhân viên   Nhấn: hệ thống hiển thị [[Màn hình Tạo mới Hồ sơ nhân viên]{.underline}](#uc-5.1.4-tạo-mới-một-hồ-sơ-nhân-viên) với những thông tin được điền sẵn giống nhân viên gốc   

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
