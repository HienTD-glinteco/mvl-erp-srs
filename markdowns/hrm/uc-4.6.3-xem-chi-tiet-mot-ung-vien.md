---
title: "UC4.6.3: Xem chi tiết một ứng viên"
type: "use-case"
uc_number: "4.6.3"
---

### UC4.6.3: Xem chi tiết một ứng viên

| **Mục tiêu:** | Cho phép người dùng xem chi tiết thông tin một ứng viên trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xem chi tiết trong Màn hình Quản lý ứng viên. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin chi tiết của ứng viên được hiển thị đầy đủ, đúng với dữ liệu trong hệ thống theo lần thay đổi mới nhất |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.6.3 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị màn hình chi tiết: |
|  | o Hiển thị tương ứng với dòng NSD thực hiện thao tác. |

#### Mô tả màn hình

![](media/image38.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Ràng buộc** |
| --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |
| 1\. | Mã ứng viên | Ký tự (10) |  | Hiển thị theo CSDL |
| 2\. | Tên ứng viên | Ký tự (100) |  | Hiển thị theo CSDL |
| 3\. | CCCD | Ký tự (12) |  | Hiển thị theo CSDL |
| 4\. | Vị trí ứng tuyển | Ký tự (100) |  | Hiển thị theo CSDL |
| 5\. | Email | Ký tự (100) |  | Hiển thị theo CSDL |
| 6\. | Số điện thoại | Ký tự (10) |  | Hiển thị theo CSDL |
| 7\. | Nguồn | Ký tự (100) |  | Hiển thị theo CSDL |
| 8\. | Thông tin người giới thiệu | Dropdown |  | Cho phép nhập và chọn trong danh sách nhân viên. Chỉ được chọn một. |
|  |  |  |  | Các thông tin hiển thị: Mã nhân viên - Họ tên - Phòng ban. |
| 9\. | Kênh | Ký tự (100) |  | Hiển thị theo CSDL |
| 10\. | Ngày nộp đơn | DD/MM/YYYY |  | Hiển thị theo CSDL |
| 11\. | Đề nghị | Ký tự (50) |  | Hiển thị theo CSDL. Hiển thị tên đề nghị. |
| 12\. | Trạng thái | Ký tự (100) |  | Hiển thị theo CSDL |
| 13\. | Số năm kinh nghiệm | Ký tự (2) |  | Hiển thị theo CSDL |
| 14\. | Danh sách các vòng phỏng vấn | Table |  | Hiển thị theo CSDL. Dựa vào thông tin lịch phỏng vấn. |
| 15\. | Danh sách lần liên hệ | Table |  | Cho phép thêm mới hoặc xoá các lần liên hệ. Danh sach gồm các trường thông tin: |
|  |  |  |  | - Người liên hệ |
|  |  |  |  | - Ngày liên hệ |
|  |  |  |  | - Phương thức |
|  |  |  |  | - Ghi chú |
| 16\. | Ghi chú | Ký tự (500) |  | Hiển thị theo CSDL |
| 17\. | Thời gian nhận việc | DD/MM/YYYY |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |
| 18\. | Quay lại | Button |  | Cho phép quay lại màn hình quản lý |
| 19\. | Chỉnh sửa | Button |  | Cho phép chỉnh sửa thông tin |
| 20\. | Thêm mới | Button |  | Cho phép thêm mới các lần liên hệ vào danh sách chi tiết |
| 21\. | Xoá | Button |  | Ở các lần thao tác. Cho phép xoá từng lần liên hệ. |
