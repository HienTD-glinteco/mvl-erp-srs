---
title: "UC 2.2.2: Tạo mới một Khối"
type: "use-case"
uc_number: "2.2.2"
---

### UC 2.2.2: Tạo mới một Khối

| **Mục tiêu:** | Cho phép người dùng tạo Khối mới |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền tạo mới Khối trong phân hệ "Quản lý Khối" |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Thêm mới" tại màn hình "Quản lý Khối" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị Khối mới tạo ở màn hình danh sách "Khối" |
|  | Khối được tạo mới có thể: Xem chi tiết, Sửa, Xóa ( với TK được phân quyền tương ứng) |

#### Luồng nghiệp vụ

![](media/image81.png)

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.2.2 | **Quy tắc Tạo mới Khối:** |
|  | - Người dùng nhấn nút "Thêm mới" -\> hệ thống hiển thị màn hình "Tạo Khối mới" |
|  | - Người dùng điền thông tin Khối và nhấn "Tạo mới" để xác thực thông tin: |
|  | - Những trường thông tin cần xác thực: |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Tạo mới thành công |
|  | - Mã khối mới được hệ thống tự động sinh. Mã khối có dạng: KHxxx |
|  | <!-- --> |
|  | ``` |
|  | - Với "KH" là cố định |
|  | - Với "xxx" có số thứ tự tăng dần 1 đơn vị bắt đầu từ 001 |
|  | - Quay về màn hình danh sách Khối với Khối mới đã được tạo |
|  | <!-- --> |
|  | ``` |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ: Hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image84.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Tên khối | Textbox | Nhập "Tên khối" tương ứng | N/A | Có |
| Loại Khối | Checkbox | Chọn "Loại Khối" tương ứng | Có 2 loại khối: | Có |
|  |  |  | - Kinh doanh |  |
|  |  |  | - Hỗ trợ |  |
|  |  |  | Chỉ chọn 1 trong 2 "Loại khối" |  |
| Chi nhánh | Dropdownlist | Chọn "Chi nhánh" tương ứng | Nhấn vào sẽ hiển thị danh sách "Chi nhánh" đã tạo | Có |
| Mô tả | Textbox | Điền "Mô tả" tương ứng | N/A | Không |
| Tạo mới | Nút | Nhấn nút để hệ thống xác thực thông tin | Xác thực những trường thông tin đúng định dạng và bắt buộc điền |  |
| Hủy | Nút | Nhấn nút để dừng luồng tạo mới. | Khi nhấn, hệ thống sẽ quay về [[màn hình hiển thị danh sách Khối]{.underline}](#uc-2.2.1-xem-danh-sách-tìm-kiếm-khối) |  |
