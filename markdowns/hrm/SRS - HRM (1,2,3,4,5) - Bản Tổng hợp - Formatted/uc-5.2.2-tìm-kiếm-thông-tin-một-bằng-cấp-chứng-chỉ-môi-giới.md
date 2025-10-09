---
title: "UC 5.2.2: Tìm kiếm thông tin một Bằng cấp/ Chứng chỉ môi giới"
type: "use-case"
uc_number: "5.2.2"
---

### UC 5.2.2: Tìm kiếm thông tin một Bằng cấp/ Chứng chỉ môi giới

  ------------------------------------------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng tìm kiếm Hồ sơ Bằng cấp/ Chứng chỉ môi giới
  --------------------------- --------------------------------------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem tại "Quản lý Bằng cấp/ Chứng chỉ môi giới"

  **Sự kiện kích hoạt:**      Người dùng tìm kiếm Bằng cấp/ Chứng chỉ môi giới theo text hoặc dùng Filter

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền xem tại "Quản lý Quản lý Bằng cấp/ Chứng chỉ môi giới"

  **Kết quả bắt buộc:**       Hệ thống hiển thị danh sách "Bằng cấp/ Chứng chỉ môi giới" đúng với mỗi truy vấn tìm kiếm
  ------------------------------------------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Mã QTNV**  | **Mô tả**                                                                                                                                                                                                                                      |
+==============+================================================================================================================================================================================================================================================+
| QTNV 5.2.2.1 | **Quy tắc Tìm kiếm Bằng cấp/ Chứng chỉ môi giới (bằng Text) :**                                                                                                                                                                                |
|              |                                                                                                                                                                                                                                                |
|              | -   Tìm kiếm theo Text: "Mã, Tên nhân viên"; "Mã, Tên chứng chỉ"                                                                                                                                                                               |
|              |                                                                                                                                                                                                                                                |
|              |     -   Điền "Tên nhân viên", "Tên chứng chỉ" muốn tìm kiếm vào textbox và nhấn Enter                                                                                                                                                          |
|              |                                                                                                                                                                                                                                                |
|              |     -   Nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Tên nhân viên" hoặc "Tên chứng chỉ", hiển thị danh sách những Bằng cấp/ Chứng chỉ tương ứng. Tìm kiếm không phân biệt chữ hoa chữ thường.   |
|              |                                                                                                                                                                                                                                                |
|              |     -   Nếu không tìm thấy kết quả Bằng cấp/ Chứng chỉ nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ                                                                                                                          |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| QTNV 5.2.2.2 | **Quy tắc Tìm kiếm Bằng cấp/ Chứng chỉ môi giới (bằng Filter):**                                                                                                                                                                               |
|              |                                                                                                                                                                                                                                                |
|              | -   Tìm kiếm bằng Filter: "Tên chứng chỉ"                                                                                                                                                                                                      |
|              |                                                                                                                                                                                                                                                |
|              |     -   Khi nhấn vào icon lọc sẽ hiển thị danh sách Checkbox: "Tất cả" và danh sách những "Chứng chỉ"                                                                                                                                          |
|              |                                                                                                                                                                                                                                                |
|              |         -   Hệ thống tìm kiếm Hồ sơ theo những thông tin được Tick                                                                                                                                                                             |
|              |                                                                                                                                                                                                                                                |
|              |         -   Nếu Check "Tất cả", Tick tất cả Checkbox bên dưới                                                                                                                                                                                  |
|              |                                                                                                                                                                                                                                                |
|              |         -   Nếu Uncheck "Tất cả", Uncheck tất cả Checkbox bên dưới                                                                                                                                                                             |
|              |                                                                                                                                                                                                                                                |
|              |     -   Hệ thống tìm kiếm mỗi khi một Checkbox được thay đổi                                                                                                                                                                                   |
|              |                                                                                                                                                                                                                                                |
|              |     -   Nếu không tìm thấy kết quả Bằng cấp/ Chứng chỉ nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ                                                                                                                          |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Mô tả màn hình

![](media/image16.png){width="6.53125in" height="2.513888888888889in"}

+------------------------+------------------+-------------------------------------+------------------------------------------------+--------------+
| **Thông tin**          | **Kiểu dữ liệu** | **Mô tả**                           | **Logic nghiệp vụ**                            | **Bắt buộc** |
+========================+==================+=====================================+================================================+==============+
| Lọc theo tên Chứng chỉ | Checkbox         | Hiển thị danh sách chứng chỉ để lọc | Danh sách các Checkbox:                        |              |
|                        |                  |                                     |                                                |              |
|                        |                  |                                     | > \- Tất cả                                    |              |
|                        |                  |                                     | >                                              |              |
|                        |                  |                                     | > \- Chứng chỉ ngoại ngữ                       |              |
|                        |                  |                                     | >                                              |              |
|                        |                  |                                     | > \- Chứng chỉ tin học                         |              |
|                        |                  |                                     | >                                              |              |
|                        |                  |                                     | > \- Bằng tốt nghiệp                           |              |
|                        |                  |                                     | >                                              |              |
|                        |                  |                                     | > \- Khác                                      |              |
|                        |                  |                                     | >                                              |              |
|                        |                  |                                     | > \- Chứng nhận hoàn thành khóa học môi giới   |              |
|                        |                  |                                     | >                                              |              |
|                        |                  |                                     | > \- Chứng chỉ hành nghề môi giới Bất động sản |              |
+------------------------+------------------+-------------------------------------+------------------------------------------------+--------------+
