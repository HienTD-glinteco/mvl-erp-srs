---
title: "UC 2.1.1: Xem danh sách + tìm kiếm chi nhánh"
type: "use-case"
uc_number: "2.1.1"
---

### UC 2.1.1: Xem danh sách + tìm kiếm chi nhánh

| **Mục tiêu:** | Cho phép người dùng xem danh sách Chi nhánh đã tạo |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền xem trong phân hệ "Quản lý Chi nhánh" |
| **Sự kiện kích hoạt:** | Người dùng truy cập Màn hình của Phân hệ con "Quản lý Chi nhánh" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị màn hình Danh sách "Chi nhánh" với đầy đủ thông tin. |
|  | Hệ thống hiển thị danh sách "Chi nhánh" đúng với mỗi truy vấn tìm kiếm. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.1.1.1 | **Quy tắc Xem màn hình danh sách các Chi nhánh:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách những Chi nhánh đã tạo với đầy đủ thông tin tương ứng từng Chi nhánh |
|  | - Mỗi khi truy cập màn hình này, hệ thống tự động sắp xếp dữ liệu theo thứ tự mã Chi nhánh từ cao xuống thấp |
| QTNV 2.1.1.2 | **Quy tắc Tìm kiếm Chi nhánh:** |
|  | - Điền **"Mã, Tên Chi nhánh"** muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Hệ thống hiển thị danh sách chi nhánh nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Mã, Tên Chi nhánh". Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Ví dụ: Tên chi nhánh: **\"Chi nhánh Hà Nội - Trung Hòa\"** |
|  | - **\"Hà Nội\"** → tìm được |
|  | - **\"Hà Hòa\"** → không tìm được |
|  | - Nếu không tìm thấy kết quả Chi nhánh nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image89.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| STT | Trường dữ liệu | Hiển thị "Số thứ tự" tương ứng | N/A | Có |
| Mã | Trường dữ liệu | Hiển thị "Mã chi nhánh" tương ứng | Khi nhấn vào tiêu đề cột, hệ thống sẽ đảo chiều sắp xếp giữa tăng dần và giảm dần | Có |
| Tên chi nhánh | Trường dữ liệu | Hiển thị "Tên chi nhánh" tương ứng | N/A | Có |
| Địa chỉ | Trường dữ liệu | Hiển thị Địa chỉ của Chi nhánh tương ứng | \- Cách hiển thị là lần lượt từng thông tin sau của chi nhánh: "Địa chỉ đường phố", "Phường/Xã", "Tỉnh"\ | Có |
|  |  |  | - Hiển thị dấu "," cách nhau giữa những thông tin này |  |
| Số điện thoại | Trường dữ liệu | Hiển thị "Số điện thoại" tương ứng | Hiển thị tất cả những số điện thoại của Chi nhánh | Có |
| Email | Trường dữ liệu | Hiển thị "Email" của chi nhánh tương ứng | N/A | Có |
| Thao tác | Nút | Hiển thị 3 nút thao tác: | \- Nút "Xem chi tiết": [[UC 2.1.3: Xem chi tiết thông tin một Chi nhánh]{.underline}](#uc-2.1.3-xem-chi-tiết-thông-tin-một-chi-nhánh) |  |
|  |  | \- Xem chi tiết | \- Nút "Chỉnh sửa": [[UC 2.1.4: Chỉnh sửa thông tin một Chi nhánh]{.underline}](#uc-2.1.4-chỉnh-sửa-thông-tin-một-chi-nhánh)\ |  |
|  |  |  | - Nút "Xóa: [[UC 2.1.5: Xóa thông tin một Chi nhánh]{.underline}](#uc-2.1.5-xóa-một-chi-nhánh) |  |
|  |  | \- Chỉnh sửa |  |  |
|  |  | \- Xóa |  |  |
| Ô textbox tìm kiếm | Textbox | Tìm kiếm "Chi nhánh" tương ứng | Nhập "Mã, Tên chi nhánh" và nhấn Enter để tìm kiếm |  |
| Thêm mới | Nút | Hiển thị nút để người dùng thêm Chi nhánh mới | Nút "Thêm mới": nhấn sẽ hiển thị [[màn hình "Tạo Chi nhánh mới"]{.underline}](#uc-2.1.2-tạo-mới-một-chi-nhánh) |  |
