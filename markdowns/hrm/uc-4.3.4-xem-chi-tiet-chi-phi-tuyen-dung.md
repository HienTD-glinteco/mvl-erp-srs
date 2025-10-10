---
title: "UC 4.3.4: Xem chi tiết chi phí tuyển dụng"
type: "use-case"
uc_number: "4.3.4"
---

### UC 4.3.4: Xem chi tiết chi phí tuyển dụng 

| **Mục tiêu:** | Cho phép người dùng xem chi tiết thông tin chi phí tuyển dụng trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xem chi tiết trong Màn hình Quản lý chi phí tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin chi tiết của chi phí tuyển dụng được hiển thị đầy đủ, đúng với dữ liệu trong hệ thống theo lần thay đổi mới nhất |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.3.4 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị màn hình chi tiết chi phí tuyển dụng: |
|  | o Hiển thị tương ứng với dòng NSD thực hiện thao tác. |

#### Mô tả màn hình

![](media/image25.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Thời gian (tháng/năm) | Date (mm/yyyy) | Có |  | Hiển thị theo CSDL |
| 2\. | Nguồn tuyển dụng | Dropdown | Có |  | Hiển thị theo CSDL |
| 3\. | Kênh tuyển dụng | Dropdown | Có |  | Hiển thị theo CSDL |
| 4\. | Đề nghị tuyển dụng | Dropdown | Có |  | Hiển thị theo CSDL |
| 5\. | Số ứng viên tham gia | Số (4) | Không |  | Hiển thị theo CSDL |
| 6\. | Tổng chi phí | Ký tự (20) | Có |  | Hiển thị theo CSDL |
| 7\. | Số ứng viên đã trúng tuyển | Số (4) | Không |  | Hiển thị theo CSDL |
| 8\. | Chi phí tính trên mỗi ứng viên | Ký tự (20) | Có |  | Hiển thị theo CSDL |
| 9\. | Hoạt động (nội dung tuyển dụng) | Ký tự (1000) |  |  | Hiển thị theo CSDL |
| 10\. | Ghi chú | Ký tự (500) |  |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 11\. | Thoát | Button | Không |  | Thoát ra khỏi màn hình Quản lý chi phí tuyển dụng |
