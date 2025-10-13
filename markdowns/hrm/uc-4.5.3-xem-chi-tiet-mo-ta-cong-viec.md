---
title: "UC4.5.3: Xem chi tiết mô tả công việc"
type: "use-case"
uc_number: "4.5.3"
---

### UC4.5.3: Xem chi tiết mô tả công việc

| **Mục tiêu:** | Cho phép người dùng xem chi tiết thông tin một mô tả công việc trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xem chi tiết trong Màn hình Quản lý mô tả công việc. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin chi tiết mô tả công việc được hiển thị đầy đủ, đúng với dữ liệu trong hệ thống theo lần thay đổi mới nhất |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.5.3 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị màn hình chi tiết mô tả công việc: |
|  | o Hiển thị tương ứng với dòng NSD thực hiện thao tác. |

#### Mô tả màn hình

![](media/image49.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Ràng buộc** |
| --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |
| 1\. | Mã JD | Ký tự (10) |  | Hiển thị theo CSDL |
| 2\. | Tiêu đề | Ký tự (50) |  | Hiển thị theo CSDL |
| 3\. | Vị trí tuyển dụng | Ký tự (50) |  | Hiển thị theo CSDL |
| 4\. | Tóm tắt công việc | Ký tự (500) |  | Hiển thị theo CSDL |
| 5\. | Yêu cầu | Ký tự (500) |  | Hiển thị theo CSDL |
| 6\. | Tiêu chí ưu tiên | Ký tự (500) |  | Hiển thị theo CSDL |
| 7\. | Quyền lợi | Ký tự (500) |  | Hiển thị theo CSDL |
| 8\. | Mức lương đề xuất | Ký tự (50) |  | Hiển thị theo CSDL |
| 9\. | File JD nội dung | Tệp |  | Hiển thị theo CSDL |
| 10\. | Ghi chú | Ký tự (500) |  | Hiển thị theo CSDL |
| 11\. | Ngày tạo | DD/MM/YYYY |  | Hiển thị theo CSDL |
| 12\. | Ngày cập nhật cuối cùng | DD/MM/YYYY |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |
| 13\. | Quay lại | Button |  | Cho phép thoát khỏi màn hình xem chi tiết. Quay lại màn hình quản lý |
| 14\. | Chỉnh sửa | Button |  | Cho phép chỉnh sửa thông tin mô tả công việc |
| 15\. | Sao chép | Button |  | Cho phép sao chép công việc |
