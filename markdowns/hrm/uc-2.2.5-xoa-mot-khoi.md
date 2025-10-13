---
title: "UC 2.2.5: Xóa một Khối"
type: "use-case"
uc_number: "2.2.5"
---

### UC 2.2.5: Xóa một Khối

  ---------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng Xóa thông tin Khối đã có
  --------------------------- -----------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền Xóa Khối trong phân hệ "Quản lý Khối"

  **Sự kiện kích hoạt:**      Người dùng truy cập nhấn nút "Xóa" tại màn hình "Quản lý Khối"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống xóa Khối tương ứng khỏi màn hình danh sách "Khối"
  ---------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.2.5 | **Quy tắc Xóa Khối:** |
|  | - Người dùng nhấn "Xóa" với một Khối đã tạo → hệ thống hiển thị màn hình "Xác nhận xóa thông tin Khối" |
|  | - Người dùng nhấn: |
|  | - Xác nhận: |
|  | - Hệ thống xác thực: |
|  | - **Nếu Khối đang được sử dụng trong thông tin khác (ví dụ: Nhân viên đang gắn với Khối):** |
|  | - Hệ thống hiển thị thông báo lỗi tương ứng |
|  | - **Nếu Khối không còn được sử dụng trong thông tin khác**: |
|  | - Hệ thống xóa Khối tương ứng khỏi màn danh sách |
|  | - Thông tin vẫn được lưu trong CSDL, người dùng không thể khôi phục lại từ giao diện người dùng |
|  | - Hệ thống quay về [[màn hình danh sách Khối]{.underline}](#uc-2.2.1-xem-danh-sách-tìm-kiếm-khối) (danh sách đã cập nhật). |
|  | - Hủy: |
|  | - Hệ thống quay về [[màn hình danh sách Khối]{.underline}](#uc-2.2.1-xem-danh-sách-tìm-kiếm-khối) |

#### Mô tả màn hình

![](media/image81.png)

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**                              **Kiểu dữ liệu**   **Mô tả**                             **Logic nghiệp vụ**                                                                              **Bắt buộc**
  ------------------------------------------ ------------------ ------------------------------------- ------------------------------------------------------------------------------------------------ --------------
  Bạn có chắc muốn xoá \[Tên Khối\] không?   Trường dữ liệu     Hiển thị tên của Khối đang được xóa   N/A                                                                                              

  Xác nhận                                   Nút                Nhấn để xác nhận xóa Khối             Xác thực Khối có xóa được hay không                                                              

  Hủy                                        Nút                Nhấn để hủy luồng xóa Khối            Nhấn để quay về [[màn hình danh sách Khối]{.underline}](#uc-2.2.1-xem-danh-sách-tìm-kiếm-khối)   
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
