---
title: "UC 5.5.1: Xem danh sách các danh viên cùng Lịch sử công tác gần nhất"
type: "use-case"
uc_number: "5.5.1"
---

### UC 5.5.1: Xem danh sách các danh viên cùng Lịch sử công tác gần nhất

  --------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem danh sách Nhân viên cùng Lịch sử công tác
  --------------------------- ----------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền cho xem phân hệ con "Lịch sử công tác"

  **Sự kiện kích hoạt:**      Người dùng truy cập Màn hình của Phân hệ con "Lịch sử công tác"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình Danh sách "Nhân viên" và "Lịch sử công tác" tương ứng
  --------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

+-------------+-------------------------------------------------------------------------------------------------------------------+
| **Mã QTNV** | **Mô tả**                                                                                                         |
+=============+===================================================================================================================+
| QTNV 5.5.1  | **Quy tắc Xem màn hình danh sách Lịch sử công tác:**                                                              |
|             |                                                                                                                   |
|             | -   Hệ thống hiển thị Màn hình Xem danh sách Lịch sử công tác với từng nhân viên                                  |
|             |                                                                                                                   |
|             |     -   Mỗi khi truy cập màn hình , hệ thống tự động sắp xếp dữ liệu theo thứ tự mã Nhân viên từ cao xuống thấp   |
|             |                                                                                                                   |
|             |     -   Với cột "Lịch sử công tác"                                                                                |
|             |                                                                                                                   |
|             |         -   Hiển thị Lịch sử công tác gần nhất của nhân viên tương ứng                                            |
|             |                                                                                                                   |
|             |         -   Có 3 trường hợp "Lịch sử công tác"                                                                    |
|             |                                                                                                                   |
|             |             -   Đổi chức vụ                                                                                       |
|             |                                                                                                                   |
|             |             -   Đổi trạng thái                                                                                    |
|             |                                                                                                                   |
|             |             -   Điều chuyển tổ chức                                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------+

#### Mô tả màn hình

![](media/image126.png){width="6.53125in" height="3.013888888888889in"}

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**                                                                                                                                                                                    **Kiểu dữ liệu**   **Mô tả**                                            **Logic nghiệp vụ**                                                                                                                              **Bắt buộc**
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------ ---------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ --------------
  Ô Tìm kiếm                                                                                                                                                                                       Textbox            Nhập "Họ Tên" hoặc "Mã nhân viên" để tìm kiếm        [[UC 5.5.2: Tìm kiếm thông tin nhân viên để xem Lịch sử công tác]{.underline}](#uc-5.5.2-tìm-kiếm-thông-tin-nhân-viên-để-xem-lịch-sử-công-tác)   

  Mã nhân viên                                                                                                                                                                                     Trường dữ liệu     Hiển thị "Mã nhân viên" tương ứng                    Khi nhấn vào tiêu đề cột, hệ thống sẽ đảo chiều sắp xếp giữa tăng dần và giảm dần                                                                Có

  Họ tên                                                                                                                                                                                           Trường dữ liệu     Hiển thị "Họ tên" tương ứng                          N/A                                                                                                                                              Có

  Chi nhánh                                                                                                                                                                                        Trường dữ liệu     Hiển thị "Chi nhánh" tương ứng                       N/A                                                                                                                                              Có

  Khối                                                                                                                                                                                             Trường dữ liệu     Hiển thị "Khối" tương ứng                            N/A                                                                                                                                              Có

  Phòng ban                                                                                                                                                                                        Trường dữ liệu     Hiển thị "Phòng ban" tương ứng                       N/A                                                                                                                                              Có

  Chức vụ                                                                                                                                                                                          Trường dữ liệu     Hiển thị "Chức vụ" tương ứng                         N/A                                                                                                                                              Có

  Trạng thái                                                                                                                                                                                       Trường dữ liệu     Hiển thị trạng thái tương ứng của nhân viên          Có 3 trạng thái + màu hiển thị:\                                                                                                                 Có
                                                                                                                                                                                                                                                                           - "Đang làm việc": màu xanh lá\                                                                                                                  
                                                                                                                                                                                                                                                                           - "On-boarding": màu vàng\                                                                                                                       
                                                                                                                                                                                                                                                                           - "Đã nghỉ việc": màu đỏ                                                                                                                         

  Ngày vào làm                                                                                                                                                                                     Trường dữ liệu     Hiển thị "Ngày vào làm" tương ứng                    N/A                                                                                                                                              Có

  Lịch sử công tác                                                                                                                                                                                 Trường dữ liệu     Hiển thị "Lịch sử công tác" gần nhất của nhân viên   Cách hiển thị: (Tên lịch sử công tác) + (Ngày                                                                                                    Có

  Nhấn vào một hàng ngang thông tin nhân viên sẽ hiện lên [[màn hình lịch sử công tác của nhân viên]{.underline}](#uc-5.5.3-xem-lịch-sử-công-tác-của-một-nhân-viên-tất-cả-các-sự-kiện-liên-quan)                                                                                                                                                                                                                            
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
