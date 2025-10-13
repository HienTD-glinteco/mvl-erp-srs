---
title: "UC 4.1.5: Chỉnh sửa kênh tuyển dụng"
type: "use-case"
uc_number: "4.1.5"
---

### UC 4.1.5: Chỉnh sửa kênh tuyển dụng

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa một kênh tuyển dụng đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Sửa trong Màn hình Quản lý kênh tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin kênh tuyển dụng đã được cập nhật thành công trong hệ thống (nếu người dùng lưu thay đổi). |
|  | Lịch sử thay đổi (nếu có yêu cầu audit/log) được ghi nhận. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.1.5.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Chỉnh sửa quyết định. |
| QTNV 4.1.5.1 | **Editing Rules:** |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống, hiển thị màu đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin chỉnh sửa xuống CSDL nếu đủ điều kiện. Thoát ra màn hình Quản lý kênh tuyển dụng. Hệ thống lưu thông tin vào CSDL giữ nguyên ID và lần thay đổi mới nhất. |
|  | Các thay đổi về dữ liệu có liên quan đến Kênh tuyển dụng sẽ được lưu lịch sử. |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Chỉnh sửa |

#### Mô tả màn hình

![](media/image41.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1. | Mã kênh | Kí tự (50) | Có |  | Không cho phép sửa |
| 2. | Tên kênh | Kí tự (250) | Có |  | Cho phép sửa |
| 3. | Thuộc | Radio button | Không |  | Cho phép chọn một: |
|  |  |  |  |  | \- Web việc làm |
|  |  |  |  |  | \- Marketing |
| 4. | Mô tả | Kí tự (500) | Có |  | Cho phép sửa |
| ***Nút chức năng*** |  |  |  |  |  |
| 5. | Lưu | Button | Có |  | Cho phép lưu thông tin đã nhập |
| 6. | Huỷ | Button | Có |  | Không lưu thông tin và thoát ra khỏi màn hình thêm mới, quay lại màn hình Quản lý kênh tuyển dụng |
