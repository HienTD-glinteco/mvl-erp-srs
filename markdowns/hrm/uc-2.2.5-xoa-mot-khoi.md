---
title: "UC 2.2.5: Xóa một Khối"
type: "use-case"
uc_number: "2.2.5"
---

### UC 2.2.5: Xóa một Khối

  **Mục tiêu:**               Cho phép người dùng Xóa thông tin Khối đã có
  --------------------------- -----------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền Xóa Khối trong phân hệ "Quản lý Khối"
  **Sự kiện kích hoạt:**      Người dùng truy cập nhấn nút "Xóa" tại màn hình "Quản lý Khối"
  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng
  **Kết quả bắt buộc:**       Hệ thống xóa Khối tương ứng khỏi màn hình danh sách "Khối"

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

  **Thông tin**                              **Kiểu dữ liệu**   **Mô tả**                             **Logic nghiệp vụ**                                                                              **Bắt buộc**
  ------------------------------------------ ------------------ ------------------------------------- ------------------------------------------------------------------------------------------------ --------------
  Bạn có chắc muốn xoá \[Tên Khối\] không?   Trường dữ liệu     Hiển thị tên của Khối đang được xóa   N/A                                                                                              
  Xác nhận                                   Nút                Nhấn để xác nhận xóa Khối             Xác thực Khối có xóa được hay không                                                              
  Hủy                                        Nút                Nhấn để hủy luồng xóa Khối            Nhấn để quay về [[màn hình danh sách Khối]{.underline}](#uc-2.2.1-xem-danh-sách-tìm-kiếm-khối)   

1.  Phân hệ con "Quản lý Phòng ban"
    -------------------------------

    1.  ### UC 2.3.1: Xem danh sách + Tìm kiếm Phòng ban

| **Mục tiêu:** | Cho phép người dùng xem danh sách Phòng ban đã tạo |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền xem trong phân hệ "Quản lý Phòng ban" |
| **Sự kiện kích hoạt:** | Người dùng truy cập Màn hình của Phân hệ con "Quản lý Phòng ban" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị màn hình Danh sách "Phòng ban" với đầy đủ thông tin |
|  | Hệ thống hiển thị danh sách "Phòng ban" đúng với mỗi truy vấn tìm kiếm |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.3.1.1 | **Quy tắc Xem màn hình danh sách các Phòng ban:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách những Phòng ban đã tạo với đầy đủ thông tin tương ứng từng Phòng ban |
|  | - Mỗi khi truy cập màn hình, hệ thống tự động sắp xếp dữ liệu theo thứ tự mã Phòng ban từ cao xuống thấp |
| QTNV 2.3.1.2 | **Quy tắc Tìm kiếm Phòng ban:** |
|  | - Điền **"Mã, Tên Phòng ban"** muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Hệ thống hiển thị danh sách chi nhánh nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Mã, Tên Phòng ban". Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Nếu không tìm thấy kết quả Phòng ban nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image76.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Ô textbox tìm kiếm | Textbox | Tìm kiếm "Phòng ban" tương ứng | Điền **"Mã, Tên Phòng ban"** và nhấn Enter để tìm kiếm |  |
| Thêm mới | Nút | Nhấn để thêm "Phòng ban" mới | [[UC 2.2.3: Tạo mới một Phòng ban]{.underline}](#uc-2.3.2-tạo-mới-một-phòng-ban) |  |
| STT | Trường dữ liệu | Hiển thị "Số thứ tự" tương ứng | N/A | Có |
| Mã | Trường dữ liệu | Hiển thị "Mã Phòng" tương ứng | Khi nhấn vào tiêu đề cột, hệ thống sẽ đảo chiều sắp xếp giữa tăng dần và giảm dần | Có |
| Tên Phòng ban | Trường dữ liệu | Hiển thị "Tên Phòng ban" tương ứng | N/A | Có |
| Cấp | Trường dữ liệu | Hiển thị nếu Phòng ban được Check "Đầu mối" trong thông tin "Cấp" | \- Nếu là "Phòng ban" được check: hiển thị "Đầu mối" | Có |
|  |  |  | \- Nếu "Phòng ban" không được check, không hiển thị thông tin |  |
| Chi nhánh | Trường dữ liệu | Hiển thị "Chi nhánh" tương ứng | N/A | Có |
| Khối | Trường dữ liệu | Hiển thị "Khối" tương ứng | N/A | Có |
| Thao tác | Nút | Hiển thị 3 nút thao tác: | \- Nút "Xem chi tiết": [[UC 2.3.3: Xem chi tiết một Phòng ban]{.underline}](#uc-2.3.3-xem-chi-tiết-thông-tin-một-phòng-ban) |  |
|  |  | \- Xem chi tiết | \- Nút "Chỉnh sửa": [[UC 2.3.4: Chỉnh sửa thông tin một Phòng ban]{.underline}](#uc-2.3.4-chỉnh-sửa-thông-tin-một-phòng-ban) |  |
|  |  | \- Chỉnh sửa | \- Nút "Xóa": [[UC 2.3.5: Xóa một Phòng ban]{.underline}](#uc-2.3.5-xóa-một-phòng-ban) |  |
|  |  | \- Xóa |  |  |
