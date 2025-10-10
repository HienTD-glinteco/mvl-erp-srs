---
title: "UC 4.4.5: Chỉnh sửa đề nghị tuyển dụng"
type: "use-case"
uc_number: "4.4.5"
---

### UC 4.4.5: Chỉnh sửa đề nghị tuyển dụng

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa một đề nghị tuyển dụng đã có trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Sửa trong Màn hình Quản lý đề nghị tuyển dụng |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin đề nghị tuyển dụng đã được cập nhật thành công trong hệ thống (nếu người dùng lưu thay đổi). |
|  | Lịch sử thay đổi (nếu có yêu cầu audit/log) được ghi nhận. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.4.5.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Chỉnh sửa đề nghị tuyển dụng. |
| QTNV 4.4.5.2 | **Editing Rules:** |
|  | ❖ Người dùng click vào icon Sửa ở dòng dữ liệu. |
|  | ❖ Hệ thống hiển thị màn hình Chỉnh sửa đề nghị tương ứng với dòng dữ liệu NSD thực hiện thao tác. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống, hiển thị màu đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin chỉnh sửa xuống CSDL nếu đủ điều kiện. Thoát ra màn hình Quản lý đề nghị. Hệ thống lưu thông tin vào CSDL giữ nguyên ID và các lần thay đổi. |
|  | Các thay đổi về dữ liệu có liên quan đến Kênh tuyển dụng sẽ được lưu lịch sử. |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Chỉnh sửa |

#### Mô tả màn hình

![](media/image49.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã đề nghị | Ký tự (10) | Có | ID | Không cho phép sửa |
| 2\. | Tên đề nghị | Ký tự (50) | Có |  | Cho phép sửa |
| 3\. | Vị trí tuyển dụng | Ký tự (100) | Có |  | Cho phép sửa |
| 4\. | Chi nhánh | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách |
| 5\. | Khối | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách |
| 6\. | Phòng ban | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách |
| 7\. | Trạng thái | Dropdown | Có |  | Cho phép chọn một trong các trạng thái: |
|  |  |  |  |  | \+ Lưu nháp |
|  |  |  |  |  | \+ Đang tuyển |
|  |  |  |  |  | \+ Đã đóng |
|  |  |  |  |  | \+ Tạm dừng |
|  |  |  |  |  | Không cho phép chọn trạng thái Lưu nháp nếu đề nghị đã được gắn với Chi phí tuyển dụng |
| 8\. | Người đề xuất | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách nhân sự |
| 9\. | Mức lương | Ký tự (20) | Có |  | Cho phép sửa |
| 10\. | Số lượng | Ký tự (5) | Có |  | Cho phép sửa |
| 11\. | Yêu cầu | Ký tự (500) | Không |  | Cho phép sửa |
| 12\. | Quyền lợi | Ký tự (500) | Không |  | Cho phép sửa |
| 13\. | Mô tả công việc | Ký tự (500) | Có |  | Cho phép sửa |
| ***Nút chức năng*** |  |  |  |  |  |
| 14\. | Lưu | Button |  |  | Cho phép lưu thông tin chỉnh sửa |
| 15\. | Huỷ | Button |  |  | Không lưu thông tin và quay lại màn hình quản lý đề nghị |
