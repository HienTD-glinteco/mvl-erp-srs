---
title: "UC4.5.1: Xem danh sách mô tả công việc"
type: "use-case"
uc_number: "4.5.1"
---

### UC4.5.1: Xem danh sách mô tả công việc

| **Mục tiêu:** | Cho phép người dùng xem danh sách các mô tả công việc trên hệ thống |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Quản lý mô tả công việc (JD)* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã hiển thị các mô tả tuyển dụng theo tiêu chí mà người dùng chọn (nếu có). |
|  | Hệ thống lưu log thông tin hành động của từng người dùng. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.5.1 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị Màn hình Xem danh sách các mô tả công việc |
|  | ❖ Hiển thị danh sách được sắp xếp theo thời gian tạo gần nhất |
|  | ❖ Chỉ hiển thị lần tạo hay lần thay đổi mới nhất |
|  | ❖ Cho phép kéo để mở rộng hoặc thu hẹp cột |
|  | ❖ Trang danh sách có 20 dòng/trang, có các thanh công cụ chuyển trang (Pagination) nếu dòng dữ liệu lớn hơn 20 |

#### Mô tả màn hình

![](media/image36.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã JD | Ký tự (10) |  |  | Hiển thị theo CSDL |
| 2\. | Tiêu đề | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 3\. | Chi nhánh | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 4\. | Khối | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 5\. | Phòng ban | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 6\. | Chức vụ | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 7\. | Ngày tạo | DD/MM/YYYY |  |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 8\. | Tìm kiếm | Button |  |  | Cho phép tìm kiếm các trường thông tin |
| 9\. | Thêm mới | Button |  |  | Hiển thị màn hình Thêm mới thông tin |
| 10\. | Xem chi tiết | Button |  |  | Cho phép xem chi tiết thông tin của mô tả công việc tại dòng thực hiện thao tác |
| 11\. | Chỉnh sửa | Button |  |  | Cho phép chỉnh sửa thông tin của mô tả công việc tại dòng thực hiện thao tác |
| 12\. | Xoá | Button |  |  | Cho phép xoá thông tin của mô tả công việc tại dòng thực hiện thao tác |
| 13\. | Kết xuất | Button |  |  | Cho phép kết xuất thông tin của mô tả công việc tại dòng thực hiện thao tác |
