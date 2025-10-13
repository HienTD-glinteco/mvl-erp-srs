---
title: "UC 4.4.4: Tạo mới đề nghị tuyển dụng"
type: "use-case"
uc_number: "4.4.4"
---

### UC 4.4.4: Tạo mới đề nghị tuyển dụng

| **Mục tiêu:** | Cho phép người dùng thêm mới một đề nghị tuyển dụng mới trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào button Thêm mới trong Màn hình Quản lý đề nghị tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã lưu trữ thông tin đề nghị tuyển dụng mới vào cơ sở dữ liệu. |
|  | Đề nghị tuyển dụng mới hiển thị trong danh sách. |
|  | Hệ thống lưu log theo hành động của người dùng. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.4.4.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Thêm đề nghị tuyển dụng mới. |
| QTNV 4.4.4.2 | **Creating Rules:** |
|  | ❖ Người dùng click vào button Thêm mới. |
|  | ❖ Hệ thống hiển thị màn hình Thêm đề nghị tuyển dụng mới. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống hiển thị đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin thêm mới xuống CSDL nếu đủ điều kiện và tự sinh Mã. Thoát ra màn hình Xem chi tiết. |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Thêm mới. |

#### Mô tả màn hình

![](media/image99.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Ràng buộc** |
| --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |
| 1\. | Tên đề nghị | Ký tự (50) | Có | Cho phép nhập |
| 2\. | Vị trí tuyển dụng | Ký tự (100) | Có | Không cho phép nhập. Lấy thông tin theo Mô tả công việc: Vị trí tuyển dụng |
| 3\. | Chi nhánh | Dropdown | Không | Cho phép chọn trong danh sách |
| 4\. | Khối | Dropdown | Không | Cho phép chọn trong danh sách. Hiển thị theo danh sách chi nhánh đã chọn trước đó. |
| 5\. | Phòng ban | Dropdown | Không | Cho phép chọn trong danh sách. Hiển thị theo danh sách khối đã chọn trước đó. |
| 6\. | Trạng thái | Dropdown | Có | Cho phép chọn một trong các trạng thái: |
|  |  |  |  | \+ Lưu nháp |
|  |  |  |  | \+ Đang tuyển |
|  |  |  |  | \+ Đã đóng |
|  |  |  |  | \+ Tạm dừng |
| 7\. | Người đề xuất | Dropdown | Có | Cho phép nhập hoặc chọn trong danh sách nhân sự |
| 8\. | Mức lương | Ký tự (50) | Có | Không cho phép nhập. Lấy thông tin theo Mô tả công việc. |
| 9\. | Số lượng tuyển dụng | Ký tự (5) | Có | Cho phép nhập |
| 10\. | Yêu cầu | Ký tự (500) | Có | Không cho phép nhập. Lấy thông tin theo Mô tả công việc: Yêu cầu |
| 11\. | Quyền lợi | Ký tự (500) | Có | Không cho phép nhập. Lấy thông tin theo Mô tả công việc: Quyền lợi |
| 12\. | Mô tả công việc | Dropdown | Có | Cho phép chọn từ danh sách công việc: Mã - tiêu đề |
| 13\. | Loại tuyển dụng | Dropdown | Có | Cho phép chọn: |
|  |  |  |  | - Tuyển mới |
|  |  |  |  | - Thay thế |
| ***Nút chức năng*** |  |  |  |  |
| 14\. | Lưu | Button |  | Cho phép lưu thông tin tạo mới |
| 15\. | Huỷ | Button |  | Không lưu thông tin tạo mới và quay lại màn hình quản lý đề nghị |
