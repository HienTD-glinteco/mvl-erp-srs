---
title: "UC 2.2.1: Xem danh sách + Tìm kiếm Khối"
type: "use-case"
uc_number: "2.2.1"
---

### UC 2.2.1: Xem danh sách + Tìm kiếm Khối

| **Mục tiêu:** | Cho phép người dùng xem danh sách Khối đã tạo |
| **Tài khoản:** | Tài khoản được phân quyền xem trong phân hệ "Quản lý Khối" |
| **Sự kiện kích hoạt:** | Người dùng truy cập Màn hình của Phân hệ con "Quản lý Khối" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị màn hình Danh sách "Khối" với đầy đủ thông tin |
|  | Hệ thống hiển thị danh sách "Khối" đúng với mỗi truy vấn tìm kiếm |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 2.2.1.1 | **Quy tắc Xem màn hình danh sách các Khối:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách những Khối đã tạo với đầy đủ thông tin tương ứng từng Khối |
|  | - Mỗi khi truy cập màn hình này, hệ thống tự động sắp xếp dữ liệu theo thứ tự mã Khối từ cao xuống thấp |
| QTNV 2.2.1.2 | **Quy tắc Tìm kiếm Khối:** |
|  | - Điền **"Mã, Tên Khối"** muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Hệ thống hiển thị danh sách chi nhánh nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Mã, Tên Khối". Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Nếu không tìm thấy kết quả Khối nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image82.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Ô textbox tìm kiếm | Textbox | Tìm kiếm "Khối" tương ứng | Điền "Mã, Tên Khối" và nhấn Enter để tìm kiếm |  |
| Tạo mới | Nút | Nhấn để thêm "Khối" mới | [[UC 2.2.2: Tạo mới một Khối]{.underline}](#uc-2.2.2-tạo-mới-một-khối) |  |
| STT | Trường dữ liệu | Hiển thị "Số thứ tự" tương ứng | N/A | Có |
| Mã | Trường dữ liệu | Hiển thị "Mã Khối" tương ứng | Khi nhấn vào tiêu đề cột, hệ thống sẽ đảo chiều sắp xếp giữa tăng dần và giảm dần | Có |
| Tên Khối | Trường dữ liệu | Hiển thị "Tên Khối" tương ứng | N/A | Có |
| Loại Khối | Trường dữ liệu | Hiển thị "Loại khối" tương ứng | Có 2 Loại Khối: | Có |
|  |  |  | \- Kinh doanh: hiển thị màu xanh dương |  |
|  |  |  | \- Hỗ trợ: hiển thị màu xanh lá cây |  |
| Chi nhánh | Trường dữ liệu | Hiển thị "Chi nhánh" tương ứng | N/A | Có |
| Thao tác | Nút | Hiển thị 3 nút thao tác: | \- Nút "Xem chi tiết": [[UC 2.2.3: Xem chi tiết thông tin một Khối]{.underline}](#uc-2.2.3-xem-chi-tiết-thông-tin-một-khối) |  |
|  |  | \- Xem chi tiết | \- Nút "Chỉnh sửa": [[UC 2.2.4: Chỉnh sửa thông tin một Khối]{.underline}](#uc-2.2.4-chỉnh-sửa-thông-tin-một-khối) |  |
|  |  | \- Chỉnh sửa | \- Nút "Xóa": [[UC 2.2.5: Xóa một Khối]{.underline}](#uc-2.2.5-xóa-một-khối) |  |
|  |  | \- Xóa |  |  |
