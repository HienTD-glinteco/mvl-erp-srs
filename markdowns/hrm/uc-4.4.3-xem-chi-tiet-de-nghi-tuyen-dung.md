---
title: "UC 4.4.3: Xem chi tiết đề nghị tuyển dụng"
type: "use-case"
uc_number: "4.4.3"
---

### UC 4.4.3: Xem chi tiết đề nghị tuyển dụng 

| **Mục tiêu:** | Cho phép người dùng xem chi tiết thông tin một đề nghị tuyển dụng trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xem chi tiết trong Màn hình Quản lý đề nghị tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin chi tiết của đề nghị tuyển dụng được hiển thị đầy đủ, đúng với dữ liệu trong hệ thống theo lần thay đổi mới nhất |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV | **Screen Displaying Rules:** |
| 4.4.3 | ❖ Hệ thống hiển thị màn hình chi tiết đề nghị tuyển dụng: |
|  | o Hiển thị tương ứng với dòng NSD thực hiện thao tác. |

####  Mô tả màn hình

![](media/image33.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã đề nghị | Ký tự (10) |  |  | Hiển thị theo CSDL |
| 2\. | Tên đề nghị | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 3\. | Vị trí tuyển dụng | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 4\. | Chi nhánh | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 5\. | Khối | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 6\. | Phòng ban | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 7\. | Trạng thái | Ký tự (50) |  |  | Hiển thị theo CSDL |
| 8\. | Người đề xuất | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 9\. | Mức lương | Ký tự (20) |  |  | Hiển thị theo CSDL |
| 10\. | Số lượng | Ký tự (5) |  |  | Hiển thị theo CSDL |
| 11\. | Yêu cầu | Ký tự (500) |  |  | Hiển thị theo CSDL |
| 12\. | Quyền lợi | Ký tự (500) |  |  | Hiển thị theo CSDL |
| 13\. | Mô tả công việc | Ký tự (500) |  |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 22\. | Quay lại | Button |  |  | Cho phép quay lại màn hình quản lý |
| 23\. | Chỉnh sửa | Button |  |  | Cho phép NSD chỉnh sửa thông tin của đề nghị |
