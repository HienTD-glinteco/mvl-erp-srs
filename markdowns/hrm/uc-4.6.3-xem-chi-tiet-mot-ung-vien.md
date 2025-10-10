---
title: "UC4.6.3: Xem chi tiết một ứng viên"
type: "use-case"
uc_number: "4.6.3"
---

### UC4.6.3: Xem chi tiết một ứng viên

| **Mục tiêu:** | Cho phép người dùng xem chi tiết thông tin một ứng viên trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xem chi tiết trong Màn hình Quản lý ứng viên. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin chi tiết của ứng viên được hiển thị đầy đủ, đúng với dữ liệu trong hệ thống theo lần thay đổi mới nhất |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.6.3 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị màn hình chi tiết: |
|  | o Hiển thị tương ứng với dòng NSD thực hiện thao tác. |

#### Mô tả màn hình

![](media/image103.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã ứng viên | Ký tự (10) |  |  | Hiển thị theo CSDL |
| 2\. | Tên ứng viên | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 3\. | CCCD | Ký tự (12) |  |  | Hiển thị theo CSDL |
| 4\. | Vị trí ứng tuyển | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 5\. | Email | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 6\. | Số điện thoại | Ký tự (10) |  |  | Hiển thị theo CSDL |
| 7\. | Nguồn | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 8\. | Kênh | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 9\. | Ngày nộp đơn | DD/MM/YYYY |  |  | Hiển thị theo CSDL |
| 10\. | Trạng thái | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 11\. | Số năm kinh nghiệm | Ký tự (2) |  |  | Hiển thị theo CSDL |
| 12\. | Danh sách các vòng phỏng vấn | Table |  |  | Hiển thị theo CSDL |
| 13\. | Danh sách lần liên hệ | Table |  |  | Hiển thị theo CSDL |
| 14\. | Ghi chú | Ký tự (500) |  |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 15\. | Quay lại | Button |  |  | Cho phép quay lại màn hình quản lý |
| 16\. | Chỉnh sửa | Button |  |  | Cho phép chỉnh sửa thông tin |
