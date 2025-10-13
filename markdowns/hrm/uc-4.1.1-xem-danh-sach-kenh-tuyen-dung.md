---
title: "UC 4.1.1: Xem danh sách kênh tuyển dụng"
type: "use-case"
uc_number: "4.1.1"
---

### ​UC 4.1.1: Xem danh sách kênh tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xem danh sách các kênh tuyển dụng trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/ Quản lý kênh tuyển dụng* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã hiển thị danh sách kênh tuyển dụng theo tiêu chí mà người dùng chọn (nếu có). |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.1.1 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị Màn hình Xem danh sách các kênh tuyển dụng. |
|  | ❖ Hiển thị danh sách được sắp xếp theo thời gian tạo gần nhất. |
|  | ❖ Chỉ hiển thị lần tạo hay lần thay đổi mới nhất. |

#### Mô tả màn hình

![](media/image34.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin tra cứu*** |  |  |  |  |  |
| 1\. | Mã kênh | Kí tự (50) | Không | Không | Cho phép nhập. |
| 2\. | Tên kênh | Kí tự (250) | Không | Không | Cho phép nhập |
| ***Thông tin dữ liệu*** |  |  |  |  |  |
| 3\. | Mã kênh | Kí tự (50) | Có |  | Hiển thị theo CSDL |
| 4\. | Tên kênh | Kí tự (250) | Có |  | Hiển thị theo CSDL |
| 5\. | Mô tả | Kí tự (500) | Có |  | Hiển thị theo CSDL. |
|  |  |  |  |  | Trên màn hình danh sách, chỉ hiển thị **50 ký tự đầu tiên**, phần dư sẽ được cắt bỏ và hiển thị dấu \"...\" (ellipsis). |
| ***Nút chức năng*** |  |  |  |  |  |
| 6\. | Tìm kiếm | Button | Không |  | Cho phép hiển thị danh sách theo các tham số đã chọn |
| 7\. | Thêm mới | Button | Không |  | Hệ thống hiển thị màn hình thêm mới |
| 8\. | Sửa (thao tác) | Button | Không |  | Hệ thống hiển thị màn hình sửa theo dòng dữ liệu thực hiện thao tác |
| 9\. | Xoá (thao tác) | Button | Không |  | Cho phép xóa dòng dữ liệu thực hiện thao tác |
| 10\. | Xem chi tiết (thao tác) | Button | Không |  | Cho phép xem dòng dữ liệu thực hiện thao tác |
