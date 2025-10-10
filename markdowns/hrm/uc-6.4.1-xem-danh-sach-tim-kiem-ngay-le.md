---
title: "UC 6.4.1: Xem danh sách + tìm kiếm Ngày lễ"
type: "use-case"
uc_number: "6.4.1"
---

### UC 6.4.1: Xem danh sách + tìm kiếm Ngày lễ

| **Mục tiêu:** | Cho phép người dùng xem danh sách Ngày lễ và tìm kiếm Ngày lễ đã tạo |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền xem trong phân hệ "Quản lý Ngày lễ" |
| **Sự kiện kích hoạt:** | Người dùng truy cập Màn hình của Phân hệ con "Quản lý Ngày lễ" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị màn hình Danh sách "Ngày lễ" với đầy đủ thông tin |
|  | Hệ thống hiển thị danh sách "Ngày lễ" đúng với mỗi truy vấn tìm kiếm |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 6.4.1.1 | **Quy tắc Xem màn hình danh sách các Ngày lễ:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách những Ngày lễ đã tạo với đầy đủ thông tin tương ứng từng Ngày lễ |
| QTNV 6.4.1.2 | **Quy tắc Tìm kiếm Ngày lễ:** |
|  | 6. Điền **"Tên Ngày lễ"** muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Hệ thống hiển thị danh sách chi nhánh nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Tên Ngày lễ". Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Ví dụ: Tên Ngày lễ: **\"Tết Nguyên Đán\"** |
|  | - **"Tết Nguyên\"** → tìm được |
|  | - **\"Tết Đán\"** → không tìm được |
|  | - Nếu không tìm thấy kết quả Ngày lễ nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image89.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Tên ngày lễ | Trường dữ liệu | Hiển thị "Tên ngày lễ" tương ứng | N/A | Có |
| Ngày bắt đầu - Ngày kết thúc | Trường dữ liệu | Hiển thị "Ngày bắt đầu - Ngày kết thúc" tương ứng | N/A | Có |
| Ghi chú | Trường dữ liệu | Hiển thị "Ghi chú" tương ứng | N/A | Không |
| Thao tác | Nút | Hiển thị 3 nút thao tác: | \- Nút "Xem chi tiết": UC 6.4.3: Xem chi tiết thông tin một Ngày lễ | Có |
|  |  | \- Xem chi tiết | \- Nút "Chỉnh sửa": UC 6.4.4: Chỉnh sửa thông tin một Ngày lễ\ |  |
|  |  |  | - Nút "Xóa: UC 6.4.5: Xóa thông tin một Ngày lễ |  |
|  |  | \- Chỉnh sửa |  |  |
|  |  | \- Xóa |  |  |
| Ô textbox tìm kiếm | Textbox | Điền từ khóa để tìm kiếm "Ngày lễ" | Nhập "Tên Ngày lễ" và nhấn Enter để tìm kiếm |  |
| Thêm mới | Nút | Hiển thị nút để người dùng thêm Ngày lễ mới | Nút "Thêm mới": [[UC 6.4.2: Tạo mới một Ngày lễ]{.underline}](#uc-6.4.2-tạo-mới-1-ngày-lễ) |  |
