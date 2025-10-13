---
title: "UC4.6.4: Tạo mới ứng viên"
type: "use-case"
uc_number: "4.6.4"
---

### UC4.6.4: Tạo mới ứng viên

| **Mục tiêu:** | Cho phép người dùng thêm mới một ứng viên trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào button Thêm mới trong Màn hình Quản lý ứng viên. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã lưu trữ thông tin ứng viên mới vào cơ sở dữ liệu. |
|  | Ứng viên mới hiển thị trong danh sách. |
|  | Hệ thống lưu log theo hành động của người dùng. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.6.4.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Thêm ứng viên mới. |
| QTNV 4.6.4.2 | **Creating Rules:** |
|  | ❖ Người dùng click vào button Thêm mới. |
|  | ❖ Hệ thống hiển thị màn hình Thêm ứng viên mới. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống hiển thị đỏ trường thông tin. |
|  | ❖ Hệ thống không cho phép tạo mới nếu CCCD đã tồn tại tương ứng với một ứng viên trên hệ thống. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin thêm mới xuống CSDL nếu đủ điều kiện và tự sinh Mã. Thoát ra màn hình Xem chi tiết. |
|  | ❖ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Thêm mới. |

#### Mô tả màn hình

![](media/image23.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã ứng viên | Ký tự (10) | Có |  | Không cho phép nhập. |
| 2\. | Tên ứng viên | Ký tự (100) | Có |  | Cho phép nhập. |
| 3\. | CCCD | Ký tự (12) | Không |  | Cho phép nhập. |
| 4\. | Email | Ký tự (100) | Có |  | Cho phép nhập một địa chỉ email. |
|  |  |  |  |  | Bắt buộc kí tự nhập phải bao gồm '@'. |
| 5\. | Số điện thoại | Ký tự (10) | Có |  | Cho phép nhập. |
|  |  |  |  |  | Kiểm tra nếu đã tồn tại số điện thoại với ứng viên tương ứng, hiển thị cảnh báo và vẫn cho lưu: 'Ứng viên đã tồn tại, vui lòng kiểm tra lại' |
| 6\. | Đề nghị | Dropdown | Có |  | Cho phép chọn danh sách đề nghị tuyển dụng |
| 7\. | Vị trí ứng tuyển | Ký tự (100) | Có |  | Không cho phép nhập. Hiển thị theo thông tin đề nghị đã chọn: Vị trí tuyển dụng. |
| 8\. | Nguồn | Dropdown | Có |  | Cho phép chọn một trong danh sách nguồn |
| 9\. | Thông tin người giới thiệu | Dropdown | Không |  | Cho phép nhập hoặc chọn thông tin từ danh sách mã nhân viên - họ tên. Các thông tin hiển thị: Mã nhân viên - Họ tên - Phòng ban. |
| 10\. | Kênh | Dropdown | Có |  | Cho phép chọn một trong danh sách kênh |
| 11\. | Ngày nộp đơn | DD/MM/YYYY | Có | Ngày hiện tại | Cho phép nhập hoặc chọn trong lịch |
| 12\. | Trạng thái | Ký tự (100) | Có |  | Cho phép chọn một trong danh sách: |
|  |  |  |  |  | - Đã liên hệ |
|  |  |  |  |  | - Đã hẹn PV |
|  |  |  |  |  | - Đã PV vòng 1 |
|  |  |  |  |  | - Đã hẹn PV vòng 2 |
|  |  |  |  |  | - Đã PV vòng 2 |
|  |  |  |  |  | - Đã nhận việc |
|  |  |  |  |  | - Loại |
| 13\. | Số năm kinh nghiệm | Ký tự (3) | Không |  | Cho phép nhập. |
| 14\. | Ghi chú | Ký tự (500) | Không |  | Cho phép nhập. |
| ***Nút chức năng*** |  |  |  |  |  |
| 15\. | Huỷ | Button |  |  | Không lưu thông tin ứng viên và quay lại màn hình Quản lý. |
| 16\. | Lưu | Button |  |  | Cho phép lưu thông tin ứng viên. |
| 17\. | Xóa dòng chi tiết | Button |  |  | Cho phép xóa các dòng chi tiết thuộc danh sách lần phỏng vấn, lần liên hệ. |
