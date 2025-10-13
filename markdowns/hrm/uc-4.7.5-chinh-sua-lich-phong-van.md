---
title: "UC4.7.5: Chỉnh sửa lịch phỏng vấn"
type: "use-case"
uc_number: "4.7.5"
---

### UC4.7.5: Chỉnh sửa lịch phỏng vấn

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa lịch phỏng vấn đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng (nhân viên phụ trách ứng viên). |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Sửa trong Màn hình Quản lý ứng viên hoặc khi xem chi tiết. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Lịch phỏng vấn được cập nhật thành công trong hệ thống. |
|  | Lịch sử chỉnh sửa (nếu có) được ghi nhận để phục vụ audit/log. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.7.5.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Chỉnh sửa thông tin lịch phỏng vấn. |
| QTNV 4.7.5.2 | **Editing Rules:** |
|  | ❖ Người dùng click vào icon Sửa ở dòng dữ liệu. |
|  | ❖ Hệ thống hiển thị màn hình Chỉnh sửa tương ứng với dòng dữ liệu NSD thực hiện thao tác. |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống, hiển thị màu đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin chỉnh sửa xuống CSDL nếu đủ điều kiện. Thoát ra màn hình Quản lý ứng viên. Hệ thống lưu thông tin vào CSDL giữ nguyên ID. Các thay đổi về dữ liệu có liên quan đến ứng viên này sẽ được lưu lịch sử. |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Chỉnh sửa |

#### Mô tả màn hình

![](media/image51.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin hiển thị*** |  |  |  |  |  |
| 1\. | Lịch phỏng vấn | Ký tự (100) | Có |  | Cho phép sửa. |
| 2\. | Đề nghị tuyển dụng | Ký tự (100) | Có |  | Cho phép tìm kiếm và chọn một trong danh sách đề nghị tuyển dụng. |
| 3\. | Vị trí phỏng vấn | Ký tự (50) | Có |  | Hiển thị theo đề nghị tuyển dụng. Không cho phép nhập |
| 4\. | Loại phỏng vấn | Radio button | Có |  | Cho phép chọn một trong hai: |
|  |  |  |  |  | - Trực tuyến |
|  |  |  |  |  | - Trực tiếp |
| 5\. | Địa điểm | Ký tự (200) | Có |  | Cho phép sửa. |
| 6\. | Thời gian từ | DD/MM/YYYY | Có | Ngày hiện tại | Cho phép sửa hoặc chọn trong lịch. |
| 7\. | Thời gian đến | DD/MM/YYYY | Không |  | Cho phép sửa hoặc chọn trong lịch. |
| 8\. | Ghi chú | Ký tự (500) | Không |  | Cho phép sửa. |
| ***Nút chức năng*** |  |  |  |  |  |
| 9\. | Huỷ | Button |  |  | Cho phép quay lại màn hình Quản lý |
| 10\. | Lưu | Button |  |  | Cho phép chỉnh sửa các thông tin lịch |
| 11\. | Thêm mới danh sách ứng viên | Button |  |  | Hiển thị transfer list để chọn thông tin các ứng viên |
| 12\. | Xóa (thao tác ở danh sách ứng viên) | Button |  |  | Cho phép xóa một ứng viên trong danh sách |
| 13\. | Thêm mới danh sách người phỏng vấn | Button |  |  | Hiển thị transfer list để chọn thông tin các nhân viên |
| 14\. | Xóa (thao tác ở danh sách người phỏng vấn) | Button |  |  | Cho phép xóa một ứng viên trong danh sách |
