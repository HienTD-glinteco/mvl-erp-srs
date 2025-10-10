---
title: "UC 3.1.5: Xóa một Vai trò (Role)"
type: "use-case"
uc_number: "3.1.5"
---

### UC 3.1.5: Xóa một Vai trò (Role)

  ----------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng Xóa Vai trò (Role) đã có
  --------------------------- ------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền Xóa Vai trò (Role) trong phân hệ "Quản lý Vai trò"

  **Sự kiện kích hoạt:**      Người dùng truy cập nhấn nút "Xóa" tại màn hình "Quản lý Vai trò"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống xóa Vai trò tương ứng khỏi màn hình danh sách "Vai trò"
  ----------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 3.1.5 | **Quy tắc Xóa Vai trò:** |
|  | - Người dùng nhấn "Xóa" với một Vai trò đã tạo → hệ thống hiển thị màn hình "Xác nhận xóa thông tin chi nhánh" |
|  | - Người dùng nhấn: |
|  | - Xác nhận: |
|  | - Hệ thống xác thực: |
|  | - Nếu **Vai trò (Role) đang được sử dụng trong thông tin khác (ví dụ: Nhân viên thuộc Vai trò (Role) ):** |
|  | - Hệ thống báo lỗi tương ứng |
|  | - Nếu **Vai trò (Role) không còn được sử dụng trong thông tin khác**: |
|  | - Hệ thống xóa thông tin Vai trò (Role) tương ứng khỏi màn hình danh sách |
|  | - Thông tin vẫn được lưu trong CSDL, người dùng không thể khôi phục lại từ giao diện người dùng |
|  | - Hệ thống quay về [[màn hình danh sách Vai trò]{.underline}](#uc-3.1.1xem-danh-sách-tìm-kiếm-vai-trò-role) (cập nhật đã xóa Vai trò tương ứng) |
|  | - Hủy: |
|  | - Hệ thống quay về [[màn hình danh sách Vai trò (Role)]{.underline}](#uc-3.1.1xem-danh-sách-tìm-kiếm-vai-trò-role) |

#### Mô tả màn hình

![](media/image7.png)

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**                                 **Kiểu dữ liệu**   **Mô tả**                                **Logic nghiệp vụ**                          **Bắt buộc**
  --------------------------------------------- ------------------ ---------------------------------------- -------------------------------------------- --------------
  Bạn có chắc muốn xóa \[Tên Vai trò\] không?   Trường dữ liệu     Hiển thị tên của Vai trò đang được xóa   N/A                                          

  Xác nhận                                      Nút                Nhấn để xác nhận xóa Vai trò             Xác thực Vai trò có xóa được hay không       

  Hủy                                           Nút                Nhấn để hủy luồng xóa Vai trò            Nhấn để quay về màn hình danh sách Vai trò   Có
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
