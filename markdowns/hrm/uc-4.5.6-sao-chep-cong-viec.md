---
title: "UC4.5.6: Sao chép công việc"
type: "use-case"
uc_number: "4.5.6"
---

### UC4.5.6: Sao chép công việc

| **Mục tiêu:** | Cho phép người dùng sao chép một mô tả công việc có sẵn. Tạo thành mô tả công việc theo ID mới trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào button Sao chép trong Màn hình Xem chi tiết mô tả công việc. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống sao chép mô tả công việc thành một mã JD mới, cho phép người dùng điều chỉnh các trường thông tin. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.5.6 | **Creating Rules:** |
|  | ❖ Người dùng click vào button Sao chép. |
|  | ❖ Hệ thống hiển thị màn hình Sao chép công việc. |
|  | ❖ Người dùng sửa các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống hiển thị đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin thêm mới xuống CSDL nếu đủ điều kiện và tự sinh Mã. Thoát ra màn hình Quản lý |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Sao chép |

#### Mô tả màn hình

![](media/image75.png)

*Màn hình nút Tạo bản sao*

![](media/image57.png)

*Màn hình Bản sao chép*

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Tiêu đề | Ký tự (50) | Có |  | Cho phép sửa |
| 2\. | Chi nhánh | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách Chi nhánh. |
|  |  |  |  |  | Nếu đã chọn Khối và Phòng ban trước thì khi nhập lại Chi nhánh sẽ reset lại Khối và Phòng ban. |
| 3\. | Khối | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách Khối. |
|  |  |  |  |  | Nếu đã chọn Chi nhánh trước thì chỉ hiển thị danh sách Khối thuộc Chi nhánh đó. |
| 4\. | Phòng ban | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách Chi nhánh. |
|  |  |  |  |  | Nếu đã chọn Khối trước thì chỉ hiển thị danh sách Phòng ban thuộc Khối đó. |
| 5\. | Vị trí tuyển dụng | Ký tự (50) | Có |  | Cho phép nhập |
| 6\. | Tóm tắt công việc | Ký tự (500) |  |  | Cho phép nhập |
| 7\. | Yêu cầu | Ký tự (500) |  |  | Cho phép nhập |
| 8\. | Tiêu chí ưu tiên | Ký tự (500) |  |  | Cho phép nhập |
| 9\. | Quyền lợi | Ký tự (500) |  |  | Cho phép nhập |
| 10\. | Mức lương đề xuất | Ký tự (50) | Có |  | Cho phép nhập |
| 11\. | File JD nội dung | Tệp | Có |  | Cho phép upload hoặc download file (word và pdf) |
| 12\. | Ghi chú | Ký tự (500) | Không |  | Cho phép nhập |
| 13\. | Ngày tạo | DD/MM/ | Có | Ngày hiện tại | Hiển thị ngày tạo mới sau khi sao chép. |
|  |  | YYYY |  |  | Không cho phép nhập. |
| ***Nút chức năng*** |  |  |  |  |  |
| 14\. | Huỷ | Button |  |  | Cho phép thoát khỏi màn hình. Quay lại màn hình quản lý |
| 15\. | Lưu | Button |  |  | Cho phép lưu thông tin |
