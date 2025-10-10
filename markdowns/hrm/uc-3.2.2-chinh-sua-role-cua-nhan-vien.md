---
title: "UC 3.2.2: Chỉnh sửa Role của Nhân viên"
type: "use-case"
uc_number: "3.2.2"
---

### UC 3.2.2: Chỉnh sửa Role của Nhân viên

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa Role của Nhân viên đã có |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền chỉnh sửa trong "Quản lý Nhân viên theo Role" |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Chỉnh sửa" tại màn hình "Quản lý Nhân viên theo Role" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống cập nhật thông tin đã chỉnh sửa Vai trò của những nhân viên tương ứng |
|  | Cập nhật giao diện hiển thị của những Nhân viên được chỉnh sửa Role |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 3.2.4 | **Quy tắc Chỉnh sửa Role của nhân viên:** |
|  | - Người dùng nhấn "Thay đổi vai trò" -\> hệ thống hiển thị màn "Thay đổi vai trò" với những nhân viên đã chọn tương ứng |
|  | - Nếu chưa chọn nhân viên nào, báo lỗi tương ứng |
|  | - Nếu số lượng nhân viên được chọn lớn hơn 25, báo lỗi tương ứng |
|  | - Người dùng chọn "Vai trò" mới và nút "Cập nhật" |
|  | - Hệ thống báo Chỉnh sửa thành công |
|  | - Quay về màn hình danh sách nhân viên theo role với thông tin mới được cập nhật |
|  | - Với những tài khoản của nhân viên thay được đổi vai trò, đăng xuất tài khoản đó ở thiết bị đang sử dụng. |
|  | - Khi đăng nhập lại, giao diện hiển thị tương ứng với vai trò mới |

#### Mô tả màn hình

![](media/image1.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| STT | Trường dữ liệu | Hiển thị "STT" tương ứng | N/A |  |
| Mã | Trường dữ liệu | Hiển thị "Mã nhân viên" tương ứng | N/A |  |
| Tên | Trường dữ liệu | Hiển thị "Tên nhân viên" tương ứng | N/A |  |
| Vai trò | Trường dữ liệu | Hiển thị "Vai trò" tương ứng | N/A |  |
| Chi nhánh | Trường dữ liệu | Hiển thị "Chi nhánh" tương ứng | N/A |  |
| Chức vụ | Trường dữ liệu | Hiển thị "Chức vụ" tương ứng | N/A |  |
| Vai trò mới | Dropdownlist | Hiển thị danh sách "Vai trò" đã tạo | \- Nhấn để hiển thị danh sách "Vai trò" đã tạo |  |
|  |  |  | \- Chọn "Vai trò" mới |  |
| Chỉnh sửa | Nút | Nhấn để thay đổi "Vai trò" của những nhân viên đã chọn | Báo lỗi nếu chưa chọn thông tin "Vai trò sau thay đổi" |  |
| Hủy | Nút | Nhấn để dừng luồng Chỉnh sửa thông tin | Khi nhấn, hệ thống sẽ quay về màn hiển thị danh sách Nhân viên theo Role |  |
