---
title: "UC4.7.4: Tạo mới lịch phỏng vấn"
type: "use-case"
uc_number: "4.7.4"
---

### UC4.7.4: Tạo mới lịch phỏng vấn

| **Mục tiêu:** | Cho phép người dùng thêm mới lịch phỏng vấn trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào button Thêm mới trong Màn hình Quản lý lịch phỏng vấn. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Lịch phỏng vấn mới được lưu thành công vào hệ thống. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.7.4.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Thêm lịch phỏng vấn mới. |
| QTNV 4.7.4.2 | **Creating Rules:** |
|  | ❖ Người dùng click vào button Thêm mới. |
|  | ❖ Hệ thống hiển thị màn hình Thêm lịch phỏng vấn mới. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống hiển thị đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin thêm mới xuống CSDL nếu đủ điều kiện và tự sinh Mã. Thoát ra màn hình Xem chi tiết. |
|  | ❖ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Thêm mới |

#### Mô tả màn hình

![](media/image1.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin hiển thị*** |  |  |  |  |  |
| 1\. | Lịch phỏng vấn | Ký tự (100) | Có |  | Cho phép nhập. |
| 2\. | Đề nghị tuyển dụng | Ký tự (100) | Có |  | Cho phép tìm kiếm và chọn một trong danh sách đề nghị tuyển dụng. |
| 3\. | Vị trí phỏng vấn | Ký tự (50) | Có |  | Hiển thị theo đề nghị tuyển dụng: Vị trí tuyển dụng. Không cho phép nhập |
| 4\. | Loại phỏng vấn | Radio button | Có |  | Cho phép chọn một trong hai: |
|  |  |  |  |  | \- Trực tuyến |
|  |  |  |  |  | \- Trực tiếp |
| 5\. | Địa điểm | Ký tự (200) | Có |  | Cho phép nhập. |
| 6\. | Thời gian từ | DD/MM/YYYY | Có | Ngày hiện tại | Cho phép nhập hoặc chọn trong lịch. |
| 7\. | Thời gian đến | DD/MM/YYYY | Không |  | Cho phép nhập hoặc chọn trong lịch. |
| 8\. | Ghi chú | Ký tự (500) | Không |  | Cho phép nhập. |
| ***Nút chức năng*** |  |  |  |  |  |
| 9\. | Huỷ | Button |  |  | Cho phép quay lại màn hình Quản lý |
| 10\. | Lưu | Button |  |  | Cho phép chỉnh sửa các thông tin lịch |
