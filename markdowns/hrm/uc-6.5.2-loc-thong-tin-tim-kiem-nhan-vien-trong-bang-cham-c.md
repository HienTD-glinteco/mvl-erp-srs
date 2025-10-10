---
title: "UC 6.5.2: Lọc thông tin, tìm kiếm nhân viên trong Bảng chấm công"
type: "use-case"
uc_number: "6.5.2"
---

### UC 6.5.2: Lọc thông tin, tìm kiếm nhân viên trong Bảng chấm công

  -----------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem Bảng chấm công lọc tìm kiếm nhân viên tương ứng
  --------------------------- -------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem cho phân hệ con "Bảng chấm công"

  **Sự kiện kích hoạt:**      Người dùng tìm kiếm Nhân viên theo text hoặc dùng Filter

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản có phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị danh sách "Nhân viên" đúng với mỗi truy vấn tìm kiếm
  -----------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 6.5.2.1 | **Quy tắc Tìm kiếm Nhân viên ở Bảng chấm công (bằng Text) :** |
|  | - Tìm kiếm theo Text: "Mã nhân viên", Tên nhân viên" |
|  | - Điền "Mã nhân viên", "Tên nhân viên" muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Mã nhân viên" hoặc "Tên nhân viên", hiển thị danh sách những Nhân viên đó. Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Nếu không tìm thấy kết quả Nhân viên nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |
| QTNV 5.1.3.2 | **Quy tắc Tìm kiếm Nhân viên ở Bảng chấm công (bằng Filter):** |
|  | - Tìm kiếm bằng Filter: "Chi nhánh", "Khối", "Phòng ban", "Chức vụ" |
|  | - Hiển thị danh sách Nhân viên đúng với các điều kiện được chọn trong bộ lọc. |
|  | - Danh sách giá trị dropdown của "Chi nhánh/Khối/Phòng ban/Chức vụ" gồm những giá trị: |
|  | - Tất cả |
|  | - Với **"Chi nhánh/Khối/Phòng ban/Chức vụ"**: Thêm danh sách tương ứng hiện có (đã được tạo trong hệ thống). |
|  | - Quy tắc chọn: |
|  | - **Chi nhánh, Chức vụ** hiển thị tất cả thông tin trong hệ thống, không phụ thuộc các bộ lọc khác. |
|  | - **Chỉ được chọn Khối khi đã chọn Chi nhánh**, danh sách hiển thị chỉ gồm các Khối thuộc Chi nhánh đó. |
|  | - **Chỉ được chọn Phòng ban khi đã chọn Khối**, danh sách hiển thị chỉ gồm các Phòng ban thuộc Khối đó |
|  | - Người dùng chỉ được chọn 1 giá trị hoặc \"Tất cả\" cho mỗi dropdownlist. |
|  | - Nếu không tìm thấy kết quả Nhân viên nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image71.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Lọc theo Chi nhánh\ | Dropdownlist | Hiển thị danh sách tương ứng để lọc tìm Hồ sơ nhân viên | Danh sách các giá trị:\ |  |
| Lọc theo Khối\ |  |  | - Tất cả\ |  |
| Lọc theo Phòng ban |  |  | - Danh mục Chi nhánh/Khối/Phòng/Chức vụ tương ứng |  |
| Lọc theo Chức vụ |  |  |  |  |
