---
title: "UC 2.3.2: Tạo mới một Phòng ban"
type: "use-case"
uc_number: "2.3.2"
---

### UC 2.3.2: Tạo mới một Phòng ban

| **Mục tiêu:** | Cho phép người dùng tạo Phòng ban mới |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền tạo mới trong phân hệ "Quản lý Phòng ban" |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Thêm mới" tại màn hình "Quản lý Phòng ban" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị Phòng ban mới tạo ở màn danh sách "Phòng ban" |
|  | Phòng ban được tạo mới có thể: Xem chi tiết, Sửa, Xóa ( với TK được phân quyền tương ứng) |

#### Luồng nghiệp vụ

![](media/image69.png)

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.3.2 | **Quy tắc Tạo mới Phòng ban:** |
|  | - Người dùng nhấn nút "Thêm mới" -\> hệ thống hiển thị màn hình "Tạo Phòng ban mới" |
|  | - Người dùng điền thông tin Phòng ban và nhấn "Tạo mới" để xác thực thông tin: |
|  | - Những trường thông tin cần xác thực: |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Tạo mới thành công |
|  | - Mã phòng ban: hệ thống tự động sinh mã. Mã phòng ban có dạng: PBxxx |
|  | <!-- --> |
|  | ``` |
|  | - Với "PB" là cố định |
|  | - Với "xxx" có số thứ tự tăng dần 1 đơn vị bắt đầu từ 001 |
|  | - Quay về màn hình danh sách Phòng ban với Phòng ban mới đã được tạo |
|  | <!-- --> |
|  | ``` |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ: Hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image73.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Tên phòng ban | Textbox | Nhập "Tên phòng ban" | N/A | Có |
| Chi nhánh | Dropdown | Chọn "Chi nhánh" tương ứng | Nhấn vào sẽ hiển thị danh sách "Chi nhánh" đã tạo | Có |
|  | list |  |  |  |
| Khối | Dropdownlist | Chọn "Khối\ | \- Bị Disable đến khi thông tin "Chi nhánh" được chọn | Có |
|  |  | Tương ứng |  |  |
|  |  |  | \- Nhấn vào sẽ hiển thị danh sách "Khối" tương ứng với Chi nhánh đã chọn |  |
| Chức năng phòng ban | Dropdownlist | Chọn "Chức năng phòng ban" tương ứng | \- Bị Disable đến khi thông tin "Khối" được chọn | Có |
|  |  |  | \- Nếu "Khối" có loại "Khối kinh doanh", autofill "Chức năng" là "Kinh doanh" |  |
|  |  |  | \- Nếu "Khối" có loại "Khối hỗ trợ", dropdownlist danh sách "Chức năng" là: |  |
|  |  |  | - Hành chính Nhân sự |  |
|  |  |  | - Tuyển dụng - Đào tạo |  |
|  |  |  | - Marketing |  |
|  |  |  | - Thư ký Kinh doanh |  |
|  |  |  | - Kế toán |  |
|  |  |  | - Sàn liên kết |  |
|  |  |  | - Xúc tiến Dự án |  |
|  |  |  | - Phát triển Dự án |  |
| Đầu mối | Checkbox | Check với Phòng ban đầu mối trong Chức năng phòng ban tương ứng | Xác thực: Với mỗi "Chức năng phòng ban", giới hạn chỉ có 1 Phòng ban được Check "Đầu mối" | Không |
| Phòng ban quản lý | Dropdownlist | Chọn "Phòng ban quản lý" tương ứng | \- Bị Disable đến khi thông tin "Chức năng phòng ban" được chọn | Không |
|  |  |  | \- Hiển thị danh sách phòng ban cùng thông tin "Chi nhánh/Khối/Chức năng phòng ban" đã chọn |  |
| Mô tả | Textbox | Điền "Mô tả" tương ứng | N/A | Không |
| Tạo mới | Nút | Nhấn nút để hệ thống xác thực thông tin | Xác thực những trường thông tin đúng định dạng và bắt buộc điền |  |
| Hủy | Nút | Nhấn nút để dừng luồng tạo mới. | Khi nhấn, hệ thống sẽ quay về [[màn hình hiển thị danh sách Phòng ban]{.underline}](#uc-2.3.1-xem-danh-sách-tìm-kiếm-phòng-ban) |  |
