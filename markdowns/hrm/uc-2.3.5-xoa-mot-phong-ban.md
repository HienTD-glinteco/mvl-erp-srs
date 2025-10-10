---
title: "UC 2.3.5: Xóa một Phòng ban"
type: "use-case"
uc_number: "2.3.5"
---

### UC 2.3.5: Xóa một Phòng ban

  ---------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng Xóa thông tin Phòng ban đã có
  --------------------------- -----------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền Xóa trong phân hệ "Quản lý Phòng ban"

  **Sự kiện kích hoạt:**      Người dùng truy cập nhấn nút "Xóa" tại màn hình "Quản lý Phòng ban"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống xóa Phòng ban tương ứng khỏi màn hình danh sách "Phòng ban"
  ---------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.3.5 | **Quy tắc Xóa Phòng ban:** |
|  | - Người dùng nhấn "Xóa" với một Phòng ban đã tạo → hệ thống hiển thị màn hình "Xác nhận xóa thông tin Phòng ban" |
|  | - Người dùng nhấn: |
|  | - Xác nhận: |
|  | - **Nếu Phòng ban đang được sử dụng trong thông tin khác (ví dụ: Nhân viên đang gắn với Phòng ban):** |
|  | - Hệ thống báo lỗi tương ứng |
|  | - Nếu **Phòng ban không còn được sử dụng trong thông tin khác**: |
|  | - Hệ thống xóa Phòng ban tương ứng khỏi màn hình danh sách |
|  | - Thông tin vẫn được lưu trong CSDL, người dùng không thể khôi phục lại từ giao diện người dùng |
|  | - Hệ thống quay về [[màn hình danh sách Phòng ban]{.underline}](#uc-2.3.1-xem-danh-sách-tìm-kiếm-phòng-ban) (cập nhật đã xóa Phòng ban tương ứng) |
|  | - Hủy: |
|  | - Hệ thống quay về [[màn hình danh sách Phòng ban]{.underline}](#uc-2.3.1-xem-danh-sách-tìm-kiếm-phòng-ban) |

#### Mô tả màn hình

![](media/image14.png)

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**                                   **Kiểu dữ liệu**   **Mô tả**                                  **Logic nghiệp vụ**                            **Bắt buộc**
  ----------------------------------------------- ------------------ ------------------------------------------ ---------------------------------------------- --------------
  Bạn có chắc muốn xóa \[Tên Phòng ban\] không?   Trường dữ liệu     Hiển thị tên của Phòng ban đang được xóa   N/A                                            

  Xác nhận                                        Nút                Nhấn để xác nhận xóa Phòng ban             Xác thực Phòng ban có xóa được hay không       

  Hủy                                             Nút                Nhấn để hủy luồng xóa Phòng ban            Nhấn để quay về màn hình danh sách Phòng ban   
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
