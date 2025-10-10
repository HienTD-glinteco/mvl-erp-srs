---
title: "UC 3.1.1:Xem danh sách + Tìm kiếm Vai trò (Role)"
type: "use-case"
uc_number: "3.1.1"
---

### UC 3.1.1:Xem danh sách + Tìm kiếm Vai trò (Role)

| **Mục tiêu:** | Cho phép người dùng xem danh sách Vai trò (Role) đã tạo |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền xem trong phân hệ "Quản lý Vai trò" |
| **Sự kiện kích hoạt:** | Người dùng truy cập Màn hình của Phân hệ con "Quản lý Vai trò" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị màn hình Danh sách "Vai trò" với đầy đủ thông tin |
|  | Hệ thống hiển thị danh sách "Vai trò" đúng với mỗi truy vấn tìm kiếm |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 3.1.1.1 | **Quy tắc Xem màn hình danh sách các Vai trò:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách những vai trò đã tạo với đầy đủ thông tin tương ứng từng Vai trò |
|  | - Mỗi khi truy cập màn hình , hệ thống tự động sắp xếp dữ liệu theo thứ tự mã Vai trò từ cao xuống thấp |
| QTNV 3.1.1.2 | **Quy tắc Tìm kiếm Vai trò (Role):** |
|  | - Điền **"Mã, Tên Vai trò"** muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Hệ thống hiển thị danh sách Vai trò (Role) nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Mã, Tên Vai trò". Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Ví dụ: Tên vai trò: **\"Quản trị viên\"** |
|  | - **\"Quản trị\"** → tìm được |
|  | - **\"Quản viên\"** → không tìm được |
|  | - Nếu không tìm thấy kết quả Vai trò (Role) nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image43.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| STT | Trường dữ liệu | Hiển thị "Số thứ tự" tương ứng | N/A | Có |
| Mã | Trường dữ liệu | Hiển thị "Mã vai trò" tương ứng | Khi nhấn vào tiêu đề cột, hệ thống sẽ đảo chiều sắp xếp giữa tăng dần và giảm dần | Có |
| Tên vai trò | Trường dữ liệu | Hiển thị "Tên vai trò" tương ứng | N/A | Có |
| Người tạo | Trường dữ liệu | Hiển thị "Nguồn tạo" tương ứng | Có 2 Nguồn tạo: | Có |
|  |  |  | - Hệ thống: mặc định 2 Vai trò có mã VT001, VT002 là do hệ thống tạo |  |
|  |  |  | - Người dùng: hiển thị với những Vai trò được tạo mới bằng tài khoản của hệ thống |  |
| Mô tả | Trường dữ liệu | Hiển thị "Mô tả" của chi nhánh tương ứng | N/A | Không |
| Thao tác | Nút | Hiển thị 3 nút thao tác: | \- Nút "Xem chi tiết": [[UC 3.1.3: Xem chi tiết Vai trò (Role)]{.underline}](#uc-3.1.3-xem-chi-tiết-vai-trò-role) |  |
|  |  | \- Xem chi tiết | \- Nút "Chỉnh sửa": [[UC 3.1.4: Chỉnh sửa thông tin Vai trò (Role)]{.underline}](#uc-3.1.4-chỉnh-sửa-thông-tin-vai-trò-role)\ |  |
|  |  |  | - Nút "Xóa: [[UC 3.1.5: Xóa thông tin một Vai trò (Role)]{.underline}](#uc-3.1.5-xóa-một-vai-trò-role) |  |
|  |  | \- Chỉnh sửa |  |  |
|  |  | \- Xóa |  |  |
| Ô textbox tìm kiếm | Textbox | Tìm kiếm "Vai trò (Role)" tương ứng | Nhập "Mã, Tên Vai trò" và nhấn Enter để tìm kiếm |  |
| Thêm mới | Nút | Hiển thị nút để người dùng thêm Vai trò mới | Nút "Thêm mới": nhấn sẽ hiển thị [[màn hình "Tạo Vai trò mới"]{.underline}](#uc-3.1.2-tạo-mới-vai-trò-role) |  |
