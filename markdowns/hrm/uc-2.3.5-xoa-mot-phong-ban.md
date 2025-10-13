---
title: "UC 2.3.5: Xóa một Phòng ban"
type: "use-case"
uc_number: "2.3.5"
---

### UC 2.3.5: Xóa một Phòng ban

  **Mục tiêu:**               Cho phép người dùng Xóa thông tin Phòng ban đã có
  --------------------------- -----------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền Xóa trong phân hệ "Quản lý Phòng ban"
  **Sự kiện kích hoạt:**      Người dùng truy cập nhấn nút "Xóa" tại màn hình "Quản lý Phòng ban"
  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng
  **Kết quả bắt buộc:**       Hệ thống xóa Phòng ban tương ứng khỏi màn hình danh sách "Phòng ban"

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

![](media/image10.png)

  **Thông tin**                                   **Kiểu dữ liệu**   **Mô tả**                                  **Logic nghiệp vụ**                            **Bắt buộc**
  ----------------------------------------------- ------------------ ------------------------------------------ ---------------------------------------------- --------------
  Bạn có chắc muốn xoá \[Tên Phòng ban\] không?   Trường dữ liệu     Hiển thị tên của Phòng ban đang được xóa   N/A                                            
  Xác nhận                                        Nút                Nhấn để xác nhận xóa Phòng ban             Xác thực Phòng ban có xóa được hay không       
  Hủy                                             Nút                Nhấn để hủy luồng xóa Phòng ban            Nhấn để quay về màn hình danh sách Phòng ban   

1.  Phân hệ con "Quản lý chức vụ"
    -----------------------------

    1.  ### UC 2.4.1: Xem danh sách + tìm kiếm Chức vụ

| **Mục tiêu:** | Cho phép người dùng xem danh sách Chức vụ đã tạo |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền xem trong phân hệ "Quản lý Chức vụ" |
| **Sự kiện kích hoạt:** | Người dùng truy cập Màn hình của Phân hệ con "Quản lý Chức vụ" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị màn hình Danh sách "Chức vụ" với đầy đủ thông tin |
|  | Hệ thống hiển thị danh sách "Chức vụ" đúng với mỗi truy vấn tìm kiếm |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.2.1.1 | **Quy tắc Xem màn hình danh sách các Chức vụ:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách những Chức vụ đã tạo với đầy đủ thông tin tương ứng từng Chức vụ |
|  | - Mỗi khi truy cập màn hình , hệ thống tự động sắp xếp dữ liệu theo thứ tự mã Chức vụ từ cao xuống thấp |
| QTNV 2.2.1.2 | **Quy tắc Tìm kiếm Chức vụ:** |
|  | - Điền **"Mã, Tên Chức vụ"** muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Hệ thống hiển thị danh sách chi nhánh nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Mã, Tên Chức vụ". Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Nếu không tìm thấy kết quả Chức vụ nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image19.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Ô textbox tìm kiếm | Textbox | Tìm kiếm "Chức vụ" tương ứng | Điền "Mã, Tên Chức vụ" và nhấn Enter để tìm kiếm |  |
| Thêm mới | Nút | Nhấn để thêm "Chức vụ" mới | [[UC 2.4.2: Tạo mới một Chức vụ]{.underline}](#uc-2.4.2-tạo-mới-một-chức-vụ) |  |
| STT | Trường dữ liệu | Hiển thị "Số thứ tự" tương ứng | N/A | Có |
| Mã | Trường dữ liệu | Hiển thị "Mã Chức vụ" tương ứng | Khi nhấn vào tiêu đề cột, hệ thống sẽ đảo chiều sắp xếp giữa tăng dần và giảm dần | Có |
| Tên Chức vụ | Trường dữ liệu | Hiển thị "Tên Chức vụ" tương ứng | N/A | Có |
| Mô tả | Trường dữ liệu | Hiển thị "Mô tả" tương ứng | N/A | Có |
| Thao tác | Nút | Hiển thị 3 nút thao tác: | \- Nút "Xem chi tiết: [[UC 2.4.3: Xem chi tiết một Chức vụ]{.underline}](#uc-2.4.3-xem-chi-tiết-thông-tin-một-chức-vụ) |  |
|  |  | \- Xem chi tiết | \- Nút "Chỉnh sửa": [[UC 2.4.4: Chỉnh sửa một thông tin Chức vụ]{.underline}](#uc-2.4.4-chỉnh-sửa-thông-tin-một-chức-vụ) |  |
|  |  | \- Chỉnh sửa | \- Nút "Xóa": [[UC 2.4.5: Xóa một Chức vụ]{.underline}](#uc-2.4.5-xóa-một-chức-vụ) |  |
|  |  | \- Xóa |  |  |
