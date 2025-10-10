---
title: "UC 5.3.2: Tìm kiếm thông tin Quan hệ nhân thân của nhân viên"
type: "use-case"
uc_number: "5.3.2"
---

### UC 5.3.2: Tìm kiếm thông tin Quan hệ nhân thân của nhân viên

  ------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng tìm kiếm "Quan hệ nhân thân" của nhân viên
  --------------------------- --------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem tại "Quản lý Quan hệ nhân thân"

  **Sự kiện kích hoạt:**      Người dùng tìm kiếm Quan hệ nhân thân theo text

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị danh sách "Quan hệ nhân thân" đúng với mỗi truy vấn tìm kiếm
  ------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.3.2 | **Quy tắc Tìm kiếm Quan hệ nhân thân (bằng Text) :** |
|  | - Tìm kiếm theo Text: **"Mã nhân viên", "Tên nhân viên", "Tên người thân", "Mối quan hệ"** |
|  | - Điền từ khóa muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong **"Mã nhân viên", "Tên nhân viên", "Tên người thân"** hoặc **"Mối quan hệ"**, hiển thị danh sách những Quan hệ nhân thân tương ứng. Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Nếu không tìm thấy kết quả Quan hệ nhân thân nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image99.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Tìm kiếm | Textbox | Nhập từ khóa cần tìm kiếm | Tìm kiếm theo **"Mã nhân viên", "Tên nhân viên", "Tên người thân", "Mối quan hệ"** |  |
