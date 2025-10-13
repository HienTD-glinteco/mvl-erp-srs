---
title: "UC4.4.6: Xoá đề nghị tuyển dụng"
type: "use-case"
uc_number: "4.4.6"
---

### UC4.4.6: Xoá đề nghị tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xóa một đề nghị tuyển dụng đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xóa trong Màn hình Quản lý đề nghị tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống xoá toàn bộ thông tin và các lần thay đổi của dòng dữ liệu thực hiện thao tác. |
|  | Danh sách hiển thị lại, không còn bản ghi vừa bị xoá. |
|  | Hệ thống ghi nhận lịch sử thao tác xoá. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.4.6 | **Deleting Rules**\[2\] **:** |
|  | ❖ Hệ thống chỉ hiển thị nút xoá đối với các đề nghị đang ở trạng thái Lưu nháp |
|  | ❖ Hệ thống hiển thị thông báo '*Bạn có chắc chắn muốn xóa dữ liệu không?'* |
|  | ❖ Người dùng thực hiện nhấn nút Xác nhận của thông báo, hệ thống sẽ xoá toàn bộ thông tin theo ID. |
|  | ❖ Người dùng thực hiện nhấn nút Huỷ của thông báo, hệ thống sẽ không xoá dữ liệu và thoát ra màn hình ***Quản lý chi phí tuyển dụng*** |

1.  Phân hệ con "Quản lý Mô tả công việc (JD)"
    ------------------------------------------

    1.  ### UC4.5.1: Xem danh sách mô tả công việc

| **Mục tiêu:** | Cho phép người dùng xem danh sách các mô tả công việc trên hệ thống |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Quản lý mô tả công việc (JD)* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã hiển thị các mô tả tuyển dụng theo tiêu chí mà người dùng chọn (nếu có). |
|  | Hệ thống lưu log thông tin hành động của từng người dùng. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.5.1 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị Màn hình Xem danh sách các mô tả công việc |
|  | ❖ Hiển thị danh sách được sắp xếp theo thời gian tạo gần nhất |
|  | ❖ Chỉ hiển thị lần tạo hay lần thay đổi mới nhất |
|  | ❖ Trang danh sách có 20 dòng/trang, có các thanh công cụ chuyển trang (Pagination) nếu dòng dữ liệu lớn hơn 20 |

#### Mô tả màn hình

![](media/image54.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Ràng buộc** |
| --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |
| 1\. | Mã JD | Ký tự (10) |  | Hiển thị theo CSDL |
| 2\. | Tiêu đề | Ký tự (50) |  | Hiển thị theo CSDL |
| 3\. | Vị trí tuyển dụng | Ký tự (50) |  | Hiển thị theo CSDL |
| 4\. | Ngày tạo | DD/MM/YYYY |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |
| 5\. | Tìm kiếm | Button |  | Cho phép tìm kiếm các trường thông tin |
| 6\. | Thêm mới | Button |  | Hiển thị màn hình Thêm mới thông tin |
| 7\. | Xem chi tiết | Button |  | Cho phép xem chi tiết thông tin của mô tả công việc tại dòng thực hiện thao tác |
| 8\. | Chỉnh sửa | Button |  | Cho phép chỉnh sửa thông tin của mô tả công việc tại dòng thực hiện thao tác |
| 9\. | Xoá | Button |  | Cho phép xoá thông tin của mô tả công việc tại dòng thực hiện thao tác |
| 10\. | Kết xuất | Button |  | Cho phép kết xuất thông tin của mô tả công việc tại dòng thực hiện thao tác |
