---
title: "UC 4.4.1: Xem danh sách đề nghị tuyển dụng"
type: "use-case"
uc_number: "4.4.1"
---

### UC 4.4.1: Xem danh sách đề nghị tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xem danh sách các đề nghị tuyển dụng trên hệ thống |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Quản lý đề nghị tuyển dụng* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã hiển thị danh sách đề nghị tuyển dụng theo tiêu chí mà người dùng chọn (nếu có). |
|  | Hệ thống lưu log thông tin hành động của từng người dùng. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV | **Screen Displaying Rules:** |
| 4.4.1 | ❖ Hệ thống hiển thị Màn hình Xem danh sách các đề nghị tuyển dụng. |
|  | ❖ Hiển thị danh sách được sắp xếp theo thời gian tạo gần nhất |
|  | ❖ Chỉ hiển thị đề nghị có lần tạo hoặc thay đổi mới nhất |
|  | ❖ Trang danh sách có 20 dòng/trang, có các thanh công cụ chuyển trang (Pagination) nếu dòng dữ liệu lớn hơn 20 |

#### Mô tả màn hình

![](media/image28.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin tìm kiếm*** |  |  |  |  |  |
| 1\. | Mã đề nghị | Ký tự (50) | Không |  | Cho phép nhập. |
| 2\. | Tên đề nghị | Ký tự (100) | Không |  | Cho phép nhập. |
| 3\. | Vị trí tuyển dụng | Ký tự (100) | Không |  | Cho phép nhập. |
| 4\. | Chi nhánh | Dropdown | Không |  | Cho phép nhập hoặc chọn một hoặc nhiều dữ liệu. Lấy dữ liệu ở Quản lý chung sơ đồ tổ chức. |
| 5\. | Khối | Dropdown | Không |  | Cho phép nhập hoặc chọn một hoặc nhiều dữ liệu. Lấy dữ liệu ở Quản lý chung sơ đồ tổ chức. |
| 6\. | Phòng ban | Dropdown | Không |  | Cho phép nhập hoặc chọn một hoặc nhiều dữ liệu. Lấy dữ liệu ở Quản lý chung sơ đồ tổ chức. |
| 7\. | Trạng thái | Dropdown | Không |  | Cho phép nhập. |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 8\. | Mã đề nghị | Ký tự |  |  | Hiển thị theo CSDL |
| 9\. | Tên đề nghị | Ký tự |  |  | Hiển thị theo CSDL |
| 10\. | Vị trí tuyển dụng | Ký tự |  |  | Hiển thị theo CSDL |
| 11\. | Chi nhánh | Ký tự |  |  | Hiển thị theo CSDL |
| 12\. | Khối | Ký tự |  |  | Hiển thị theo CSDL |
| 13\. | Phòng ban | Ký tự |  |  | Hiển thị theo CSDL |
| 14\. | Số lượng | Ký tự |  |  | Hiển thị theo CSDL |
| 15\. | Trạng thái | Ký tự |  |  | Hiển thị theo CSDL |
| 16\. | Người đề xuất | Ký tự |  |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 17\. | Tìm kiếm | Button |  |  | Cho phép tìm kiếm theo các tham số đã nhập |
| 18\. | Xem chi tiết | Button |  |  | Cho phép xem chi tiết của dòng dữ liệu đã chọn |
| 19\. | Tạo mới | Button |  |  | Hệ thống hiển thị màn hình Thêm đề nghị mới |
| 20\. | Chính sửa | Button |  |  | Hệ thống hiển thị màn hình Chỉnh sửa đề nghị |
| 21\. | Xoá | Button |  |  | Cho phép xoá dòng dữ liệu |
