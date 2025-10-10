---
title: "UC 3.1.4: Chỉnh sửa thông tin Vai trò (Role)"
type: "use-case"
uc_number: "3.1.4"
---

### UC 3.1.4: Chỉnh sửa thông tin Vai trò (Role)

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa thông tin một Vai trò (Role) đã có |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền chỉnh sửa trong phân hệ "Quản lý Vai trò (Role)" |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Chỉnh sửa" tại màn hình "Quản lý Vai trò (Role)" hoặc màn Xem chi tiết thông tin một Vai trò |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống cập nhật thông tin đã chỉnh sửa của Vai trò tương ứng |
|  | Cập nhật giao diện hiển thị của những tài khoản thuộc Vai trò được chỉnh sửa |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 3.1.4 | **Quy tắc Chỉnh sửa thông tin Vai trò (Role):** |
|  | - Người dùng nhấn "Chỉnh sửa" với một Vai trò (Role) đã tạo -\> hệ thống hiển thị màn "Chỉnh sửa thông tin Vai trò" với những thông tin của Vai trò tương ứng |
|  | - Người dùng chỉnh sửa thông tin Vai trò (Role) và nút "Cập nhật" để xác thực thông tin |
|  | - Những trường thông tin cần xác thực: |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Chỉnh sửa thành công |
|  | - Quay về màn hình danh sách Vai trò với thông tin Vai trò mới được cập nhật |
|  | - Nếu đổi **"Tên Vai trò"** trong danh mục, tất cả thông tin liên quan (Nhân viên theo Role) sẽ **tự động cập nhật theo tên mới** |
|  | - **Nếu đổi các quyền trong "Vai trò"** |
|  | - Với những tài khoản thuộc vai trò bị thay đổi, đăng xuất tài khoản đó ở thiết bị đang sử dụng. |
|  | - Khi nhân viên đăng nhập lại, giao diện hiển thị tương ứng với vai trò mới |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ: Hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image5.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Những trường thông tin hiển thị như của màn hình "Tạo mới một Vai trò (Role)": |  |  |  |  |
| \- Điền sẵn những thông tin của Vai trò tương ứng |  |  |  |  |
| Lưu | Nút | Nhấn nút để hệ thống xác thực thông tin | Xác thực thông tin đúng định dạng + bắt buộc |  |
| Hủy | Nút | Nhấn nút để dừng luồng Chỉnh sửa thông tin | Khi nhấn, hệ thống sẽ quay về [[màn hiển thị danh sách Vai trò]{.underline}](#uc-3.1.1xem-danh-sách-tìm-kiếm-vai-trò-role) |  |
