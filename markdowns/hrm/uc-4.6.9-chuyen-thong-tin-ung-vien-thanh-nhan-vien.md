---
title: "UC4.6.9: Chuyển thông tin ứng viên thành nhân viên"
type: "use-case"
uc_number: "4.6.9"
---

### UC4.6.9: Chuyển thông tin ứng viên thành nhân viên

| **Mục tiêu:** | Cho phép người dùng chuyển đổi hồ sơ của ứng viên đã được tuyển dụng thành hồ sơ nhân viên chính thức trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Chuyển hồ sơ thành nhân viên trong Màn hình Quản lý ứng viên hoặc khi Xem chi tiết thông tin ứng viên. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
|  | Ứng viên đang có trạng thái Đã nhận việc. |
| **Kết quả bắt buộc:** | Thông tin ứng viên được tạo mới thành hồ sơ nhân viên trong hệ thống HRM. |
|  | Không cho phép chuyển thông tin khi ứng viên có CCCD bị trùng với thông tin nhân viên. |
|  | Hệ thống ghi lại log hành động. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.6.9 | ❖ Chỉ cho phép chuyển thông tin ứng viên thành nhân viên khi trạng thái của ứng viên là Đã nhận việc. |
|  | ❖ Nếu CCCD của ứng viên đã tồn tại ở thông tin của nhân viên thì hệ thống hiển thị cảnh báo tương ứng và không cho chuyển thông tin sang ứng viên. |
|  | ❖ Đảm bảo tính toàn vẹn dữ liệu giữa các module. |
|  | ❖ Ghi log toàn bộ thao tác để phục vụ kiểm tra/audit. |

1.  Phân hệ con "Quản lý lịch phỏng vấn"
    ------------------------------------

    1.  ### UC4.7.1: Xem Danh sách lịch phỏng vấn

| **Mục tiêu:** | Cho phép người dùng xem danh sách lịch phỏng vấn trên hệ thống |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Quản lý lịch phỏng vấn* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Người dùng xem được màn hình danh sách lịch phỏng vấn. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.7.1 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị Màn hình Xem danh sách lịch phỏng vấn. |
|  | ❖ Hiển thị danh sách được sắp xếp theo thời gian tạo gần nhất. |
|  | ❖ Chỉ hiển thị lần tạo hay lần thay đổi mới nhất. |
|  | ❖ Trang danh sách có 20 dòng/trang, có các thanh công cụ chuyển trang (Pagination) nếu dòng dữ liệu lớn hơn 20. |

#### Mô tả màn hình

![](media/image59.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Ràng buộc** |
| --- | --- | --- | --- | --- |
| ***Thông tin tra cứu*** |  |  |  |  |
| 1\. | Lịch phỏng vấn | Ký tự (100) |  | Hiển thị theo CSDL |
| 2\. | Đề nghị tuyển dụng | Ký tự (100) |  | Hiển thị theo CSDL |
| 3\. | Vị trí phỏng vấn | Ký tự (50) |  | Hiển thị theo CSDL |
| 4\. | Số lượng ứng tuyển | Ký tự (4) |  | Hiển thị theo CSDL |
| 5\. | Thời gian từ | DD/MM/YYYY |  | Hiển thị theo CSDL |
| 6\. | Thời gian đến | DD/MM/YYYY |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |
| 7\. | Tìm kiếm | Button |  | Cho phép tra cứu theo các tham số mong muốn |
| 8\. | Thêm mới | Button |  | Cho phép thêm mới lịch phỏng vấn trên hệ thống |
| 9\. | Xem chi tiết | Button |  | Cho phép xem chi tiết lịch phỏng vấn |
| 10\. | Chỉnh sửa | Button |  | Cho phép chỉnh sửa thông tin lịch phỏng vấn |
| 11\. | Kết xuất | Button |  | Cho phép kết xuất lịch phỏng vấn |
| 12\. | Xoá | Button |  | Cho phép xóa lịch phỏng vấn |
