---
title: "UC 4.1.4: Tạo mới kênh tuyển dụng"
type: "use-case"
uc_number: "4.1.4"
---

### UC 4.1.4: Tạo mới kênh tuyển dụng 

| **Mục tiêu:** | Cho phép người dùng thêm mới một kênh tuyển dụng trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào button Thêm mới trong Màn hình Quản lý kênh tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã lưu trữ thông tin kênh tuyển dụng mới vào cơ sở dữ liệu. |
|  | Kênh tuyển dụng mới hiển thị trong danh sách kênh tuyển dụng. |
|  | Hệ thống lưu log theo hành động của người dùng. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.1.4.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Thêm kênh tuyển dụng mới. |
| QTNV 4.1.4.2 | **Creating Rules:** |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống hiển thị đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin thêm mới xuống CSDL nếu đủ điều kiện. Thoát ra màn hình Quản lý |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Thêm mới |

#### Mô tả màn hình

![](media/image48.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã kênh | Kí tự (50) | Có |  | Không cho phép nhập |
| 2\. | Tên kênh | Kí tự (250) | Có |  | Cho phép nhập |
| 3\. | Thuộc | Checkbox | Không |  | Cho phép chọn một: |
|  |  |  |  |  | \- Web việc làm |
|  |  |  |  |  | \- Marketing |
| 4\. | Mô tả | Kí tự (500) | Có |  | Cho phép nhập hoặc chọn trong lịch |
| ***Nút chức năng*** |  |  |  |  |  |
| 5\. | Lưu | Button | Có |  | Cho phép lưu thông tin đã nhập |
| 6\. | Huỷ | Button | Có |  | Không lưu thông tin và thoát ra khỏi màn hình thêm mới, quay lại màn hình Quản lý kênh tuyển dụng |
