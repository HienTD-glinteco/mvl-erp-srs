---
title: "UC 4.2.3: Xem chi tiết nguồn tuyển dụng"
type: "use-case"
uc_number: "4.2.3"
---

### UC 4.2.3: Xem chi tiết nguồn tuyển dụng 

| **Mục tiêu:** | Cho phép người dùng xem chi tiết thông tin một nguồn tuyển dụng trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xem chi tiết trong Màn hình Quản lý nguồn tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin chi tiết của nguồn tuyển dụng được hiển thị đầy đủ, đúng với dữ liệu trong hệ thống theo lần thay đổi mới nhất |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.2.3 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị màn hình chi tiết nguồn tuyển dụng: |
|  | o Hiển thị tương ứng với dòng NSD thực hiện thao tác. |

####  Mô tả màn hình

![](media/image42.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã nguồn | Kí tự (50) | Có |  | Hiển thị thông tin theo CSDL |
| 2\. | Tên nguồn | Kí tự (250) | Có |  | Hiển thị thông tin theo CSDL |
| 3\. | Mô tả | Kí tự (500) | Có |  | Hiển thị thông tin theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 4\. | Thoát | Button | Không |  | Thoát ra màn hình Quản lý thư viện điện tử |
