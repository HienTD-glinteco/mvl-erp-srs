---
title: "UC 4.3.6: Chỉnh sửa chi phí tuyển dụng"
type: "use-case"
uc_number: "4.3.6"
---

### UC 4.3.6: Chỉnh sửa chi phí tuyển dụng

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa một chi phí tuyển dụng đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Sửa trong Màn hình Quản lý chi phí tuyển dụng |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin chi phí tuyển dụng đã được cập nhật thành công trong hệ thống (nếu người dùng lưu thay đổi). |
|  | Lịch sử thay đổi (nếu có yêu cầu audit/log) được ghi nhận. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.3.6.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Chỉnh sửa chi phí tuyển dụng. |
| QTNV 4.3.6.2 | **Editing Rules:** |
|  | ❖ Người dùng click vào icon Sửa ở dòng dữ liệu. |
|  | ❖ Hệ thống hiển thị màn hình Chỉnh sửa chi phí tương ứng với dòng dữ liệu NSD thực hiện thao tác. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống, hiển thị màu đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin chỉnh sửa xuống CSDL nếu đủ điều kiện. Thoát ra màn hình Quản lý chi phí. Hệ thống lưu thông tin vào CSDL giữ nguyên ID. Các thay đổi về dữ liệu có liên quan đến Chi phí tuyển dụng sẽ được lưu lịch sử. |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Chỉnh sửa |

#### Mô tả màn hình

![](media/image32.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Thời gian (tháng/năm) | Date (mm/yyyy) | Có | Hiện tại | Cho phép sửa. |
| 2\. | Nguồn tuyển dụng | Dropdown | Có |  | Cho phép nhập tìm kiếm và chọn trong danh sách. Chỉ chọn một. |
| 3\. | Kênh tuyển dụng | Dropdown | Có |  | Cho phép nhập tìm kiếm và chọn trong danh sách. Chỉ chọn một. |
| 4\. | Đề nghị tuyển dụng | Dropdown | Có |  | Cho phép nhập tìm kiếm và chọn trong danh sách. Chỉ chọn một. |
|  |  |  |  |  | Chỉ hiển thị những đề nghị đang ở trạng thái Đang tuyển, Đã đóng, Tạm dừng |
| 5\. | Số ứng viên tham gia | Số (4) | Không |  | Cho phép sửa. |
| 6\. | Tổng chi phí | Ký tự (20) | Có |  | Cho phép sửa. |
| 7\. | Số ứng viên đã trúng tuyển | Số (4) | Không |  | Cho phép sửa. |
| 8\. | Chi phí tính trên mỗi ứng viên | Ký tự (20) | Có |  | Không cho phép nhập. Hệ thống tính theo công thức: Tổng chi phí / Số ứng viên đã tuyển |
| 9\. | Hoạt động (nội dung tuyển dụng) | Ký tự (1000) |  |  | Cho phép sửa. |
| 10\. | Ghi chú | Ký tự (500) |  |  | Cho phép sửa. |
| ***Nút chức năng*** |  |  |  |  |  |
| 11\. | Lưu | Button | Không |  | Cho phép lưu thông tin đã nhập |
| 12\. | Huỷ | Button | Không |  | Không lưu thông tin và thoát ra khỏi màn hình thêm mới, quay lại màn hình Quản lý chi phí tuyển dụng |
