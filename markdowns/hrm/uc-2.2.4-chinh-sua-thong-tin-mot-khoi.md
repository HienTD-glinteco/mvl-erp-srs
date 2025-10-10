---
title: "UC 2.2.4: Chỉnh sửa thông tin một Khối"
type: "use-case"
uc_number: "2.2.4"
---

### UC 2.2.4: Chỉnh sửa thông tin một Khối

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa thông tin Khối đã có |
| **Tài khoản:** | Tài khoản được phân quyền chỉnh sửa trong phân hệ "Quản lý Khối" |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Chỉnh sửa" tại màn hình "Quản lý Khối" hoặc màn Xem chi tiết thông tin 1 Khối |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống cập nhật thông tin đã chỉnh sửa của Khối tương ứng. |
|  | Thông tin "Khối" ở những thông tin liên quan cũng được cập nhật |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 2.2.4 | **Quy tắc Chỉnh sửa thông tin Khối:** |
|  | - Người dùng nhấn "Chỉnh sửa" với một Khối đã tạo -\> hệ thống hiển thị màn "Chỉnh sửa thông tin Khối" với những thông tin theo lần thay đổi cuối cùng của Khối tương ứng |
|  | - Người dùng chỉnh sửa thông tin Khối và nút "Cập nhật" để xác thực thông tin |
|  | - Những trường thông tin cần xác thực: |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Chỉnh sửa thành công |
|  | - Quay về màn hình danh sách Khối với thông tin Khối mới được cập nhật |
|  | - Khi đổi **"Tên Khối" hay "Chi nhánh"** trong danh mục, tất cả thông tin liên quan (Hồ sơ nhân viên, báo cáo, màn hình hiển thị...) sẽ **tự động cập nhật theo thông tin mới** |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ: Hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image85.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Những trường thông tin hiển thị như của màn hình "Tạo mới một Khối": |  |  |  |  |
| \- Điền sẵn những thông tin theo lần thay đổi cuối cùng của Khối tương ứng |  |  |  |  |
| \- Tất cả thông tin đều được chỉnh sửa |  |  |  |  |
| Lưu | Nút | Nhấn nút để hệ thống xác thực thông tin | Xác thực thông tin đúng định dạng + bắt buộc |  |
| Hủy | Nút | Nhấn nút để dừng luồng Chỉnh sửa thông tin | Khi nhấn, hệ thống sẽ quay về [[màn hiển thị danh sách Khối]{.underline}](#uc-2.2.1-xem-danh-sách-tìm-kiếm-khối) |  |
