---
title: "UC 4.1.3: Xem Chi tiết kênh tuyển dụng"
type: "use-case"
uc_number: "4.1.3"
---

### UC 4.1.3: Xem Chi tiết kênh tuyển dụng 

| **Mục tiêu:** | Cho phép người dùng xem chi tiết một quyết định trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xem chi tiết trong Màn hình Quản lý kênh tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin chi tiết của kênh tuyển dụng được hiển thị đầy đủ, đúng với dữ liệu trong hệ thống theo lần thay đổi mới nhất |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.1.3 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị màn hình chi tiết kênh tuyển dụng: |
|  | o Hiển thị tương ứng với dòng NSD thực hiện thao tác. |

#### Mô tả màn hình

![](media/image39.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã kênh | Kí tự (50) |  |  | Hiển thị theo CSDL |
| 2\. | Tên kênh | Kí tự (100) |  |  | Hiển thị theo CSDL |
| 3\. | Thuộc | Checkbox |  |  | Hiển thị theo CSDL |
| 4\. | Mô tả | Kí tự (500) |  |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 5\. | Thoát | Button | Không |  | Thoát ra khỏi màn hình Quản lý kênh tuyển dụng |
