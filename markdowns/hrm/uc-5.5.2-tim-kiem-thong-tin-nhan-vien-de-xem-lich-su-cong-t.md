---
title: "UC 5.5.2: Tìm kiếm thông tin nhân viên để xem Lịch sử công tác"
type: "use-case"
uc_number: "5.5.2"
---

### UC 5.5.2: Tìm kiếm thông tin nhân viên để xem Lịch sử công tác

  ----------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng tìm kiếm Nhân viên để xem Lịch sử công tác
  --------------------------- ------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền cho xem tại "Lịch sử công tác"

  **Sự kiện kích hoạt:**      Người dùng tìm kiếm Nhân viên theo text hoặc dùng Filter

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản có phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị danh sách "Nhân viên" đúng với mỗi truy vấn tìm kiếm
  ----------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.5.2.1 | **Quy tắc Tìm kiếm Hồ sơ Nhân viên (bằng Text) :** |
|  | - Tìm kiếm theo Text: "Mã nhân viên", "Họ tên" |
|  | - Điền "Mã nhân viên", "Họ tên" muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Mã nhân viên" hoặc "Họ tên", hiển thị danh sách những Nhân viên đó. Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Nếu không tìm thấy kết quả Hồ sơ Nhân viên nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |
| QTNV 5.5.2.2 | **Quy tắc Tìm kiếm Nhân viên (bằng Filter):** |
|  | - Tìm kiếm bằng Filter: "Chi nhánh", "Khối", "Phòng ban", "Chức vụ", "Trạng thái" |
|  | - Hiển thị danh sách Hồ sơ nhân viên đúng với các điều kiện được chọn trong bộ lọc. |
|  | - Danh sách giá trị dropdown của "Chi nhánh/Khối/Phòng ban/Chức vụ/Trạng thái" gồm những giá trị: |
|  | - Tất cả |
|  | - Với **"Chi nhánh/Khối/Phòng ban/Chức vụ"**: Thêm danh sách tương ứng hiện có (đã được tạo trong hệ thống). |
|  | - Với **"Trạng thái"**: Thêm mặc định 3 giá trị: "Đang làm việc/On-boarding/Đã nghỉ việc" |
|  | - Quy tắc chọn: |
|  | - **Chi nhánh, Chức vụ** hiển thị tất cả thông tin trong hệ thống, không phụ thuộc các bộ lọc khác. |
|  | - **Chỉ được chọn Khối khi đã chọn Chi nhánh**, danh sách hiển thị chỉ gồm các Khối thuộc Chi nhánh đó. |
|  | - **Chỉ được chọn Phòng ban khi đã chọn Khối**, danh sách hiển thị chỉ gồm các Phòng ban thuộc Khối đó |
|  | - Người dùng chỉ được chọn 1 giá trị hoặc \"Tất cả\" cho mỗi dropdownlist. |
|  | - Nếu không tìm thấy kết quả Nhân viên nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image71.png)![](media/image60.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Lọc theo Chi nhánh\ | Dropdownlist | Hiển thị danh sách tương ứng để lọc tìm Hồ sơ nhân viên | Danh sách các giá trị:\ |  |
| Lọc theo Khối\ |  |  | - Tất cả\ |  |
| Lọc theo Phòng ban |  |  | - Danh sách Chi nhánh, Khối hoặc Phòng ban tương ứng |  |
| Lọc theo Chức vụ |  |  |  |  |
| Lọc theo trạng thái | Dropdownlist | Hiển thị danh sách trạng thái để lọc tìm | Danh sách các giá trị:\ |  |
|  |  |  | - Tất cả |  |
|  |  |  | \- Đang làm việc\ |  |
|  |  |  | - On-boarding\ |  |
|  |  |  | - Đã nghỉ việc |  |
