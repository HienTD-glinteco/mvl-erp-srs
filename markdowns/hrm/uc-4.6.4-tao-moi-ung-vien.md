---
title: "UC4.6.4: Tạo mới ứng viên"
type: "use-case"
uc_number: "4.6.4"
---

### UC4.6.4: Tạo mới ứng viên

| **Mục tiêu:** | Cho phép người dùng thêm mới một ứng viên trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào button Thêm mới trong Màn hình Quản lý ứng viên. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã lưu trữ thông tin ứng viên mới vào cơ sở dữ liệu. |
|  | Ứng viên mới hiển thị trong danh sách. |
|  | Hệ thống lưu log theo hành động của người dùng. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.6.4.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Thêm ứng viên mới. |
| QTNV 4.6.4.2 | **Creating Rules:** |
|  | ❖ Người dùng click vào button Thêm mới. |
|  | ❖ Hệ thống hiển thị màn hình Thêm ứng viên mới. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống hiển thị đỏ trường thông tin. |
|  | ❖ Hệ thống không cho phép tạo mới nếu CCCD đã tồn tại tương ứng với một ứng viên trên hệ thống |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin thêm mới xuống CSDL nếu đủ điều kiện và tự sinh Mã. Thoát ra màn hình Quản lý |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Thêm mới |

#### Mô tả màn hình

![](media/image70.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã ứng viên | Ký tự (10) | Có |  | Không cho phép nhập. |
| 2\. | Tên ứng viên | Ký tự (100) | Có |  | Cho phép nhập. |
| 3\. | CCCD | Ký tự (12) | Có |  | Cho phép nhập. |
|  |  |  |  |  | Hệ thống kiểm tra nếu đã tồn tại ứng viên với CCCD tương ứng, hiển thị cảnh báo đỏ |
| 4\. | Vị trí ứng tuyển | Ký tự (100) | Có |  | Cho phép nhập. |
| 5\. | Email | Ký tự (100) | Có |  | Cho phép nhập một địa chỉ email. |
|  |  |  |  |  | Bắt buộc kí tự nhập phải bao gồm '@'. |
| 6\. | Số điện thoại | Ký tự (10) | Có |  | Cho phép nhập. |
| 7\. | Nguồn | Dropdown | Có |  | Cho phép chọn một trong danh sách nguồn |
| 8\. | Kênh | Dropdown | Có |  | Cho phép chọn một trong danh sách kênh |
| 9\. | Ngày nộp đơn | DD/MM/YYYY | Có | Ngày hiện tại | Cho phép nhập hoặc chọn trong lịch |
| 10\. | Trạng thái | Ký tự (100) | Có |  | Cho phép chọn một trong danh sách: |
|  |  |  |  |  | \- Đã liên hệ |
|  |  |  |  |  | \- Đã hẹn PV |
|  |  |  |  |  | \- Đã PV vòng 1 |
|  |  |  |  |  | \- Đã hẹn PV vòng 2 |
|  |  |  |  |  | \- Đã PV vòng 2 |
|  |  |  |  |  | \- Đã nhận việc |
|  |  |  |  |  | \- Loại |
| 11\. | Số năm kinh nghiệm | Ký tự (2) | Không |  | Cho phép nhập. |
| 12\. | Danh sách các vòng phỏng vấn | Table | Không |  | Cho phép tạo bảng danh sách các vòng phỏng vấn: |
|  |  |  |  |  | \- Vòng |
|  |  |  |  |  | \- Người phỏng vấn |
|  |  |  |  |  | \- Địa điểm |
|  |  |  |  |  | \- Thời gian (ngày - giờ) |
|  |  |  |  |  | \- Ghi chú |
|  |  |  |  |  | \- Thao tác (xoá) |
| 13\. | Danh sách lần liên hệ | Table | Không |  | Cho phép tạo bảng danh sách các lần liên hệ: |
|  |  |  |  |  | \- Người liên hệ |
|  |  |  |  |  | \- Ngày liên hệ |
|  |  |  |  |  | \- Phương thức |
|  |  |  |  |  | \- Ghi chú |
|  |  |  |  |  | \- Thao tác (xoá) |
| 14\. | Ghi chú | Ký tự (500) | Không |  | Cho phép nhập. |
| ***Nút chức năng*** |  |  |  |  |  |
| 15\. | Huỷ | Button |  |  | Không lưu thông tin ứng viên và quay lại màn hình Quản lý. |
| 16\. | Lưu | Button |  |  | Cho phép lưu thông tin ứng viên. |
| 17\. | Thêm lần phỏng vấn | Button |  |  | Cho phép thêm các dòng để bổ sung lần phỏng vấn. |
| 18\. | Thêm lần liên hệ | Button |  |  | Cho phép thêm các dòng để bổ sung lần liên hệ. |
| 19\. | Xoá dòng chi tiết | Button |  |  | Cho phép xoá các dòng chi tiết thuộc danh sách lần phỏng vấn, lần liên hệ. |
