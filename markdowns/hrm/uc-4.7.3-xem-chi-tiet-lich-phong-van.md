---
title: "UC4.7.3: Xem chi tiết lịch phỏng vấn"
type: "use-case"
uc_number: "4.7.3"
---

### UC4.7.3: Xem chi tiết lịch phỏng vấn

| **Mục tiêu:** | Cho phép người dùng xem chi tiết thông tin lịch phỏng vấn trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xem chi tiết trong Màn hình Quản lý lịch phỏng vấn. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Người dùng xem được chi tiết lịch phỏng vấn đúng với bản ghi đã chọn; hệ thống đảm bảo hiển thị phiên bản dữ liệu mới nhất. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.7.3 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị màn hình chi tiết: |
|  | o Hiển thị tương ứng với dòng NSD thực hiện thao tác. |

#### Mô tả màn hình

![](media/image73.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin hiển thị*** |  |  |  |  |  |
| 1\. | Lịch phỏng vấn | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 2\. | Đề nghị tuyển dụng | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 3\. | Vị trí phỏng vấn | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 4\. | Loại phỏng vấn | Radio button |  |  | Hiển thị theo CSDL |
| 5\. | Địa điểm | Ký tự (200) |  |  | Hiển thị theo CSDL |
| 6\. | Thời gian từ | DD/MM/YYYY |  |  | Hiển thị theo CSDL |
| 7\. | Thời gian đến | DD/MM/YYYY |  |  | Hiển thị theo CSDL |
| 8\. | Ghi chú | Ký tự (500) |  |  | Hiển thị theo CSDL |
| ***Thông tin chi tiết danh sách ứng viên*** |  |  |  |  |  |
| 9\. | Mã ứng viên | Ký tự (10) |  |  | Hiển thị theo CSDL |
| 10\. | Họ và tên | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 11\. | CCCD | Ký tự (12) |  |  | Hiển thị theo CSDL |
| 12\. | Số điện thoại | Ký tự (10) |  |  | Hiển thị theo CSDL |
| 13\. | Email | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 14\. | Thời gian phỏng vấn | HH:MM:SS - DD/MM/YYYY |  |  | Hiển thị theo CSDL |
| 15\. | Thời gian gửi mail lần cuối | HH:MM:SS - DD/MM/YYYY |  |  | Hiển thị theo CSDL. Hiển thị theo lần gửi mail cuối cùng. |
| ***Thông tin chi tiết danh sách người phỏng vấn*** |  |  |  |  |  |
| 16\. | Mã nhân viên | Ký tự (10) |  |  | Hiển thị theo CSDL |
| 17\. | Họ và tên | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 18\. | Chức vụ | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 19\. | Chi nhánh | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 20\. | Khối | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 21\. | Phòng ban | Ký tự (50) |  |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 22\. | Quay lại | Button |  |  | Cho phép quay lại màn hình Quản lý |
| 23\. | Chỉnh sửa | Button |  |  | Cho phép chỉnh sửa các thông tin lịch |
| 24\. | Gửi mail | Button |  |  | Cho phép gửi mail thông báo tới danh sách ứng viên được tích chọn |
