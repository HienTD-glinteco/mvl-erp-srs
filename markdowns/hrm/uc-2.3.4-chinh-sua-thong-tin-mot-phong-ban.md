---
title: "UC 2.3.4: Chỉnh sửa thông tin một Phòng ban"
type: "use-case"
uc_number: "2.3.4"
---

### UC 2.3.4: Chỉnh sửa thông tin một Phòng ban

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa thông tin Phòng ban đã có |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền chỉnh sửa trong phân hệ "Quản lý Phòng ban" |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Chỉnh sửa" tại màn hình "Quản lý Phòng ban" hoặc màn Xem chi tiết thông tin 1 Phòng ban |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống cập nhật thông tin đã chỉnh sửa của Phòng ban tương ứng. |
|  | Thông tin "Phòng ban" ở những thông tin liên quan cũng được cập nhật |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 2.3.4 | **Quy tắc Chỉnh sửa thông tin Phòng ban:** |
|  | - Người dùng nhấn "Chỉnh sửa" với một Phòng ban đã tạo -\> hệ thống hiển thị màn "Chỉnh sửa thông tin Phòng ban" với những thông tin của Phòng ban tương ứng |
|  | - Người dùng chỉnh sửa thông tin Phòng ban và nút "Cập nhật" để xác thực: |
|  | - Những trường thông tin cần xác thực: |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Chỉnh sửa thành công |
|  | - Quay về màn hình danh sách Phòng ban với thông tin Phòng ban mới được cập nhật |
|  | - Sau khi đổi **thông tin**, tất cả thông tin liên quan tới Phòng ban (Hồ sơ nhân viên, báo cáo, màn hình hiển thị...) sẽ **tự động cập nhật theo thông tin mới** |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ: Hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image12.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Những trường thông tin hiển thị như của màn hình "Tạo mới một Phòng ban": |  |  |  |  |
| \- Điền sẵn những thông tin theo lần thay đổi cuối cùng của Phòng ban tương ứng |  |  |  |  |
| \- Tất cả thông tin đều được chỉnh sửa |  |  |  |  |
| Lưu | Nút | Nhấn nút để hệ thống xác thực thông tin | Xác thực thông tin đúng định dạng + bắt buộc |  |
| Hủy | Nút | Nhấn nút để dừng luồng Chỉnh sửa thông tin | Khi nhấn, hệ thống sẽ quay về [[màn hiển thị danh sách Phòng ban]{.underline}](#uc-2.3.1-xem-danh-sách-tìm-kiếm-phòng-ban) |  |
