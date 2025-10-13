---
title: "UC4.5.5: Chỉnh sửa mô tả công việc"
type: "use-case"
uc_number: "4.5.5"
---

### UC4.5.5: Chỉnh sửa mô tả công việc

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa một công việc đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Sửa trong Màn hình Quản lý mô tả công việc (JD). |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin mô tả tuyển dụng đã được cập nhật thành công trong hệ thống (nếu người dùng lưu thay đổi). |
|  | Lịch sử thay đổi (nếu có yêu cầu audit/log) được ghi nhận. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.5.5.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Chỉnh sửa mô tả công việc. |
| QTNV 4.5.5.2 | **Editing Rules:** |
|  | ❖ Người dùng click vào icon Sửa ở dòng dữ liệu. |
|  | ❖ Hệ thống hiển thị màn hình Chỉnh sửa mô tả công việc tương ứng với dòng dữ liệu NSD thực hiện thao tác. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống, hiển thị màu đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin chỉnh sửa xuống CSDL nếu đủ điều kiện. Thoát ra màn hình Quản lý mô tả công việc. Hệ thống lưu thông tin vào CSDL giữ nguyên ID. Các thay đổi về dữ liệu có liên quan đến mô tả công việc sẽ được lưu lịch sử. |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Chỉnh sửa. |

#### Mô tả màn hình

![](media/image45.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã JD | Ký tự (10) | Có |  | Không cho phép sửa |
| 2\. | Tiêu đề | Ký tự (50) | Có |  | Cho phép sửa |
| 3\. | Vị trí tuyển dụng | Ký tự (50) | Có |  | Cho phép nhập |
| 4\. | Tóm tắt công việc | Ký tự (500) | Có |  | Cho phép nhập |
| 5\. | Yêu cầu | Ký tự (500) | Có |  | Cho phép nhập |
| 6\. | Tiêu chí ưu tiên | Ký tự (500) | Không |  | Cho phép nhập |
| 7\. | Quyền lợi | Ký tự (500) | Có |  | Cho phép nhập |
| 8\. | Mức lương đề xuất | Ký tự (50) | Có |  | Cho phép nhập |
| 9\. | File JD nội dung | Tệp | Có |  | Cho phép upload hoặc download file (word và pdf) |
| 10\. | Ghi chú | Ký tự (500) | Không |  | Cho phép nhập |
| 11\. | Ngày tạo | DD/MM/ | Có | Theo thông tin lúc tạo | Không cho phép nhập. |
|  |  | YYYY |  |  |  |
| ***Nút chức năng*** |  |  |  |  |  |
| 12\. | Huỷ | Button |  |  | Cho phép thoát khỏi màn hình thêm mới. Quay lại màn hình quản lý |
| 13\. | Lưu | Button |  |  | Cho phép lưu thông tin tạo mới |
