---
title: "UC4.6.1: Xem danh sách ứng viên"
type: "use-case"
uc_number: "4.6.1"
---

### UC4.6.1: Xem danh sách ứng viên

| **Mục tiêu:** | Cho phép người dùng xem danh sách các mô tả công việc trên hệ thống |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Quản lý ứng viên* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã hiển thị danh sách ứng viên theo tiêu chí mà người dùng chọn (nếu có). |
|  | Hệ thống lưu log thông tin hành động của từng người dùng. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.6.1 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị Màn hình Xem danh sách các ứng viên |
|  | ❖ Hiển thị danh sách được sắp xếp theo thời gian tạo gần nhất |
|  | ❖ Chỉ hiển thị lần tạo hay lần thay đổi mới nhất |
|  | ❖ Trang danh sách có 20 dòng/trang, có các thanh công cụ chuyển trang (Pagination) nếu dòng dữ liệu lớn hơn 20 |

#### Mô tả màn hình

![](media/image55.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Ràng buộc** |
| --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |
| 1\. | Mã ứng viên | Ký tự (10) |  | Hiển thị theo CSDL |
| 2\. | Tên ứng viên | Ký tự (100) |  | Hiển thị theo CSDL |
| 3\. | Số điện thoại | Ký tự (12) |  | Hiển thị theo CSDL |
| 4\. | Đề nghị | Ký tự (50) |  | Hiển thị theo CSDL |
| 5\. | Vị trí ứng tuyển | Ký tự (100) |  | Hiển thị theo CSDL |
| 6\. | Nguồn | Ký tự (100) |  | Hiển thị theo CSDL |
| 7\. | Kênh | Ký tự (100) |  | Hiển thị theo CSDL |
| 8\. | Trạng thái | Ký tự (100) |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |
| 9\. | Tìm kiếm | Button |  | Cho phép tra cứu theo các tham số mong muốn |
| 10\. | Thêm mới | Button |  | Cho phép thêm mới một ứng viên trên hệ thống |
| 11\. | Xem chi tiết | Button |  | Cho phép xem chi tiết ứng viên |
| 12\. | Chỉnh sửa | Button |  | Cho phép chỉnh sửa thông tin ứng viên |
| 13\. | Kết xuất | Button |  | Cho phép kết xuất danh sách ứng viên |
| 14\. | Kế xuất chi tiết | Button |  | Cho phép kết xuất thông tin của một ứng viên |
| 15\. | Xoá | Button |  | Cho phép xóa một ứng viên |
