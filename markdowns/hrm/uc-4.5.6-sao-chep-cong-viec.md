---
title: "UC4.5.6: Sao chép công việc"
type: "use-case"
uc_number: "4.5.6"
---

### UC4.5.6: Sao chép công việc

| **Mục tiêu:** | Cho phép người dùng sao chép một mô tả công việc có sẵn. Tạo thành mô tả công việc theo ID mới trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào button Sao chép trong Màn hình Xem chi tiết mô tả công việc. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
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

![](media/image65.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã JD | Ký tự (10) | Có |  | Không cho phép nhập |
| 2\. | Tiêu đề | Ký tự (50) | Có |  | Cho phép sửa |
| 3\. | Chi nhánh | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách Chi nhánh. |
|  |  |  |  |  | Nếu đã chọn Khối và Phòng ban trước thì khi nhập lại Chi nhánh sẽ reset lại Khối và Phòng ban. |
| 4\. | Khối | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách Khối. |
|  |  |  |  |  | Nếu đã chọn Chi nhánh trước thì chỉ hiển thị danh sách Khối thuộc Chi nhánh đó. |
| 5\. | Phòng ban | Dropdown | Có |  | Cho phép sửa hoặc chọn trong danh sách Chi nhánh. |
|  |  |  |  |  | Nếu đã chọn Khối trước thì chỉ hiển thị danh sách Phòng ban thuộc Khối đó. |
| 6\. | Chức vụ | Ký tự (50) | Có |  | Cho phép nhập |
| 7\. | Tóm tắt công việc | Ký tự (500) | Có |  | Cho phép nhập |
| 8\. | Trách nhiệm chính | Ký tự (500) | Không |  | Cho phép nhập |
| 9\. | Yêu cầu | Ký tự (500) | Có |  | Cho phép nhập |
| 10\. | Tiêu chí ưu tiên | Ký tự (500) | Không |  | Cho phép nhập |
| 11\. | Mức lương đề xuất | Ký tự (50) | Có |  | Cho phép nhập |
| 12\. | File JD nội dung | Tệp | Có |  | Cho phép upload hoặc download file (word và pdf) |
| 13\. | Ghi chú | Ký tự (500) | Không |  | Cho phép nhập |
| 14\. | Ngày tạo | DD/MM/YYYY | Có | Ngày hiện tại khi nhập thông tin | Hiển thị ngày tạo mới sau khi sao chép. |
|  |  |  |  |  | Không cho phép nhập. |
| ***Nút chức năng*** |  |  |  |  |  |
| 15\. | Huỷ | Button |  |  | Cho phép thoát khỏi màn hình. Quay lại màn hình quản lý |
| 16\. | Lưu | Button |  |  | Cho phép lưu thông tin |
