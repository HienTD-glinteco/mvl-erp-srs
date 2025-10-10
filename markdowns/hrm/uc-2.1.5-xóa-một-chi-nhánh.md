---
title: "UC 2.1.5: Xóa một Chi nhánh"
type: "use-case"
uc_number: "2.1.5"
---

### UC 2.1.5: Xóa một Chi nhánh

  -----------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng Xóa một Chi nhánh đã có
  --------------------------- -------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền Xóa một Chi nhánh trong phân hệ "Quản lý Chi nhánh"

  **Sự kiện kích hoạt:**      Người dùng truy cập nhấn nút "Xóa" tại màn hình "Quản lý chi nhánh"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Điều kiện bắt buộc:**     Hệ thống xóa một Chi nhánh tương ứng khỏi màn hình danh sách "Chi nhánh"
  -----------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Mã QTNV** | **Mô tả**                                                                                                                                                                                                                              |
+=============+========================================================================================================================================================================================================================================+
| QTNV 2.1.5  | **Quy tắc Xóa Chi nhánh:**                                                                                                                                                                                                             |
|             |                                                                                                                                                                                                                                        |
|             | -   Người dùng nhấn "Xóa" với một chi nhánh đã tạo → hệ thống hiển thị màn hình "Xác nhận xóa thông tin chi nhánh"                                                                                                                     |
|             |                                                                                                                                                                                                                                        |
|             | -   Người dùng nhấn:                                                                                                                                                                                                                   |
|             |                                                                                                                                                                                                                                        |
|             |     -   Xác nhận:                                                                                                                                                                                                                      |
|             |                                                                                                                                                                                                                                        |
|             |         -   Hệ thống xác thực:                                                                                                                                                                                                         |
|             |                                                                                                                                                                                                                                        |
|             |             -   Nếu **Chi nhánh đang được sử dụng trong thông tin khác (ví dụ: Phòng ban thuộc Chi nhánh):**                                                                                                                           |
|             |                                                                                                                                                                                                                                        |
|             |                 -   Hệ thống báo lỗi tương ứng                                                                                                                                                                                         |
|             |                                                                                                                                                                                                                                        |
|             |             -   Nếu **Chi nhánh không còn được sử dụng trong thông tin khác**:                                                                                                                                                         |
|             |                                                                                                                                                                                                                                        |
|             |                 -   Hệ thống xóa Chi nhánh tương ứng khỏi màn danh sách                                                                                                                                                                |
|             |                                                                                                                                                                                                                                        |
|             |                 -   Thông tin vẫn được lưu trong CSDL, người dùng không thể khôi phục lại từ giao diện người dùng                                                                                                                      |
|             |                                                                                                                                                                                                                                        |
|             |                 -   Hệ thống quay về [[màn hình danh sách Chi nhánh]{.underline}](https://docs.google.com/document/d/1WbOFAfkOKmfCFZk0mFynFMj86AlJkGqW3Vn86678u_8/edit#heading=h.fewviky16u7v) (cập nhật đã xóa Chi nhánh tương ứng)   |
|             |                                                                                                                                                                                                                                        |
|             |     -   Hủy:                                                                                                                                                                                                                           |
|             |                                                                                                                                                                                                                                        |
|             |         -   Hệ thống quay về [[màn hình danh sách Chi nhánh]{.underline}](https://docs.google.com/document/d/1WbOFAfkOKmfCFZk0mFynFMj86AlJkGqW3Vn86678u_8/edit#heading=h.fewviky16u7v)                                                 |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Mô tả màn hình

![](media/image80.png){width="6.53125in" height="4.041666666666667in"}

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**                                   **Kiểu dữ liệu**   **Mô tả**                                  **Logic nghiệp vụ**                            **Bắt buộc**
  ----------------------------------------------- ------------------ ------------------------------------------ ---------------------------------------------- --------------
  Bạn có chắc muốn xoá \[Tên chi nhánh\] không?   Trường dữ liệu     Hiển thị tên của Chi nhánh đang được xóa   Hiển thị tên của Chi nhánh được xóa            

  Xác nhận                                        Nút                Nhấn để xác nhận xóa Chi nhánh             Xác thực Chi nhánh có xóa được hay không       

  Hủy                                             Nút                Nhấn để hủy luồng xóa Chi nhánh            Nhấn để quay về màn hình danh sách Chi nhánh   
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
