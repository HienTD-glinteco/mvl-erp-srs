---
title: "UC 2.1.2: Tạo mới một Chi nhánh"
type: "use-case"
uc_number: "2.1.2"
---

### UC 2.1.2: Tạo mới một Chi nhánh

| **Mục tiêu:** | Cho phép người dùng tạo một Chi nhánh mới |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền tạo mới Chi nhánh trong phân hệ "Quản lý Chi nhánh" |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Thêm mới" tại màn hình "Quản lý Chi nhánh" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị Chi nhánh mới tạo ở màn hình danh sách "Chi nhánh" |
|  | Chi nhánh tạo mới có thể: Xem chi tiết, Sửa, Xóa ( với TK có phân quyền tương ứng) |

#### Luồng nghiệp vụ

**\
**![](media/image117.png)

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.1.2 | **Quy tắc Tạo mới Chi nhánh:** |
|  | - Người dùng nhấn nút "Thêm mới" -\> hệ thống hiển thị màn hình "Tạo Chi nhánh mới" |
|  | - Người dùng điền thông tin Chi nhánh và nhấn "Tạo mới" để xác thực thông tin: |
|  | - Những trường thông tin cần xác thực: |
|  | - Số điện thoại liên hệ: nếu điền nhiều số điện thoại cần được phân tách bằng dấu "-" |
|  | - Email: cần đúng định dạng Email |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Tạo mới thành công |
|  | - Mã chi nhánh mới được hệ thống tự động sinh. Mã chi nhánh có dạng: CNxxx |
|  | <!-- --> |
|  | ``` |
|  | - Với "CN" là cố định |
|  | - Với "xxx" có số thứ tự tăng dần 1 đơn vị bắt đầu từ 001 |
|  | - Quay về màn hình danh sách Chi nhánh với Chi nhánh mới đã được tạo |
|  | <!-- --> |
|  | ``` |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ: Hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image118.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Tên chi nhánh | Textbox | Nhập "Tên chi nhánh" mới | N/A | Có |
| Địa chỉ đường phố | Textbox | Nhập "Địa chỉ đường" chi nhánh mới | N/A | Có |
| Phường/Xã | Textbox | Nhập "Xã" chi nhánh mới | N/A | Có |
| Tỉnh | Textbox | Nhập "Tỉnh" chi nhánh mới | N/A | Có |
| Số điện thoại liên hệ | Textbox | Nhập SĐT chi nhánh mới | Hỗ trợ nhập nhiều số, phân tách bằng dấu "-" | Không |
| Email | Textbox | Nhập Email chi nhánh mới | Xác thực: đúng định dạng Email chuẩn | Không |
| Mô tả | Textbox | Nhập "Mô tả" tương ứng | N/A | Không |
| Tạo mới | Nút | Nhấn nút để hệ thống xác thực thông tin | Xác thực những trường thông tin đúng định dạng và bắt buộc điền |  |
