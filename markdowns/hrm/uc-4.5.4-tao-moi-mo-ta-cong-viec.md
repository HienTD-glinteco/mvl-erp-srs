---
title: "UC4.5.4: Tạo mới mô tả công việc"
type: "use-case"
uc_number: "4.5.4"
---

### UC4.5.4: Tạo mới mô tả công việc

| **Mục tiêu:** | Cho phép người dùng thêm mới một đề nghị tuyển dụng mới trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào button Thêm mới trong Màn hình Quản lý mô tả công việc. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã lưu trữ thông tin mô tả công việc mới vào cơ sở dữ liệu. |
|  | Mô tả công việc mới hiển thị trong danh sách. |
|  | Hệ thống lưu log theo hành động. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.5.4.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Thêm mô tả công việc mới. |
| QTNV 4.5.4.2 | **Creating Rules:** |
|  | ❖ Người dùng click vào button Thêm mới. |
|  | ❖ Hệ thống hiển thị màn hình Thêm mô tả công việc mới. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống hiển thị đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin thêm mới xuống CSDL nếu đủ điều kiện và tự sinh Mã. Thoát ra màn hình Quản lý |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Thêm mới |

#### Mô tả màn hình

![](media/image37.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã JD | Ký tự (10) | Có |  | Không cho phép nhập |
| 2\. | Tiêu đề | Ký tự (50) | Có |  | Cho phép nhập |
| 3\. | Chi nhánh | Dropdown | Có |  | Cho phép nhập hoặc chọn trong danh sách Chi nhánh |
| 4\. | Khối | Dropdown | Có |  | Cho phép nhập hoặc chọn trong danh sách Khối. |
|  |  |  |  |  | Nếu đã chọn Chi nhánh trước thì chỉ hiển thị danh sách Khối thuộc Chi nhánh đó. |
| 5\. | Phòng ban | Dropdown | Có |  | Cho phép nhập hoặc chọn trong danh sách Chi nhánh. |
|  |  |  |  |  | Nếu đã chọn Khối trước thì chỉ hiển thị danh sách Phòng ban thuộc Khối đó. |
| 6\. | Chức vụ | Ký tự (50) | Có |  | Cho phép nhập |
| 7\. | Tóm tắt công việc | Ký tự (500) | Có |  | Cho phép nhập |
| 8\. | Trách nhiệm chính | Ký tự (500) | Không |  | Cho phép nhập |
| 9\. | Yêu cầu | Ký tự (500) | Có |  | Cho phép nhập |
| 10\. | Tiêu chí ưu tiên | Ký tự (500) | Không |  | Cho phép nhập |
| 11\. | Mức lương đề xuất | Ký tự (50) | Có |  | Cho phép nhập |
| 12\. | File JD nội dung | Tệp | Có |  | Cho phép upload hoặc download file (word và pdf) |
| 13\. | Ghi chú | Ký tự (500) | Không |  | Cho phép nhập |
| 14\. | Ngày tạo | DD/MM/YYYY | Có | Ngày hiện tại khi nhập thông tin | Hiển thị ngày tạo. |
|  |  |  |  |  | Cho phép sửa. |
| ***Nút chức năng*** |  |  |  |  |  |
| 15\. | Huỷ | Button |  |  | Cho phép thoát khỏi màn hình thêm mới. Quay lại màn hình quản lý |
| 16\. | Lưu | Button |  |  | Cho phép lưu thông tin tạo mới |
