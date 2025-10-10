---
title: "UC 4.2.4: Tạo mới nguồn tuyển dụng"
type: "use-case"
uc_number: "4.2.4"
---

### UC 4.2.4: Tạo mới nguồn tuyển dụng

| **Mục tiêu:** | Cho phép người dùng thêm mới một nguồn tuyển dụng mới trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào button Thêm mới trong Màn hình Quản lý nguồn tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã lưu trữ thông tin nguồn tuyển dụng mới vào cơ sở dữ liệu. |
|  | Nguồn tuyển dụng mới hiển thị trong danh sách nguồn tuyển dụng. |
|  | Hệ thống lưu log theo hành động của người dùng. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.2.4.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Thêm nguồn tuyển dụng mới. |
| QTNV 4.2.4.2 | **Creating Rules:** |
|  | ❖ Người dùng click vào button Thêm mới. |
|  | ❖ Hệ thống hiển thị màn hình Thêm nguồn tuyển dụng mới. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống hiển thị đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin thêm mới xuống CSDL nếu đủ điều kiện và tự sinh Mã nguồn. Thoát ra màn hình Quản lý |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Thêm mới |

#### Mô tả màn hình

![](media/image58.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã nguồn | Kí tự (50) | Có |  | Không cho phép nhập |
| 2\. | Tên nguồn | Kí tự (250) | Có |  | Cho phép chọn một trong danh sách: |
|  |  |  |  |  | \- Nguồn giới thiệu |
|  |  |  |  |  | -Nguồn phòng tuyển dụng |
|  |  |  |  |  | \- Nguồn quay lại |
| 3\. | Mô tả | Kí tự (500) | Có |  | Cho phép nhập |
| ***Nút chức năng*** |  |  |  |  |  |
| 4\. | Lưu | Button | Không |  | Cho phép lưu thông tin đã nhập |
| 5\. | Thoát | Button | Không |  | Không lưu thông tin và thoát ra khỏi màn hình thêm mới, quay lại màn hình Quản lý nguồn tuyển dụng |
