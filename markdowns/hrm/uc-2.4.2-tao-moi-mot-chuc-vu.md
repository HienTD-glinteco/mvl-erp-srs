---
title: "UC 2.4.2: Tạo mới một Chức vụ"
type: "use-case"
uc_number: "2.4.2"
---

### UC 2.4.2: Tạo mới một Chức vụ

| **Mục tiêu:** | Cho phép người dùng tạo một Chức vụ mới |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền tạo mới Chức vụ trong phân hệ "Quản lý Chức vụ" |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Thêm mới" tại màn hình "Quản lý Chức vụ" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị Chức vụ mới tạo ở màn danh sách "Chức vụ" |
|  | Chức vụ được tạo mới có thể: Xem chi tiết, Sửa, Xóa ( với TK được phân quyền tương ứng) |

#### Luồng nghiệp vụ

**\
**![](media/image12.png)

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.4.2 | **Quy tắc Tạo mới Chức vụ:** |
|  | - Người dùng nhấn nút "Thêm mới" -\> hệ thống hiển thị màn hình "Tạo Chức vụ mới" |
|  | - Người dùng điền thông tin Chức vụ và nhấn "Tạo mới" để xác thực thông tin: |
|  | - Những trường thông tin cần xác thực: |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Tạo mới thành công |
|  | - Mã chức vụ mới được hệ thống tự động sinh. Mã chức vụ có dạng: CVxxx |
|  | <!-- --> |
|  | ``` |
|  | - Với "CV" là cố định |
|  | - Với "xxx" có số thứ tự tăng dần 1 đơn vị bắt đầu từ 001 |
|  | - Quay về màn hình danh sách Chức vụ với Chức vụ mới đã được tạo |
|  | <!-- --> |
|  | ``` |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ: Hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image11.png)

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**   **Kiểu dữ liệu**   **Mô tả**                                 **Logic nghiệp vụ**                                                                                                           **Bắt buộc**
  --------------- ------------------ ----------------------------------------- ----------------------------------------------------------------------------------------------------------------------------- --------------
  Tên chức vụ     Textbox            Nhập "Tên chức vụ" tương ứng              N/A                                                                                                                           Có

  Mô tả           Textbox            Điền "Mô tả" tương ứng                    N/A                                                                                                                           Không

  Tạo mới         Nút                Nhấn nút để hệ thống xác thực thông tin   Xác thực những trường thông tin đúng định dạng và bắt buộc điền                                                               

  Hủy             Nút                Nhấn nút để dừng luồng tạo mới.           Khi nhấn, hệ thống sẽ quay về [[màn hình hiển thị danh sách chức vụ]{.underline}](#uc-2.4.1-xem-danh-sách-tìm-kiếm-chức-vụ)   
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
