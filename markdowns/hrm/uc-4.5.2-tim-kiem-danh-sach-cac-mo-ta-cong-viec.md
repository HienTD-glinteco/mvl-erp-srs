---
title: "UC4.5.2: Tìm kiếm danh sách các mô tả công việc"
type: "use-case"
uc_number: "4.5.2"
---

### UC4.5.2: Tìm kiếm danh sách các mô tả công việc

| **Mục tiêu:** | Cho phép người dùng tra cứu thông tin về mô tả công việc trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Quản lý mô tả công việc (JD)* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống hiển thị danh sách kênh tuyển dụng đã được lọc theo từ khóa/tiêu chí tìm kiếm mà người dùng nhập. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.5.2 | **Searching Rules:** |
|  | ❖ Cho phép người dùng tìm kiếm bằng các từ khóa liên quan đến mô tả công việc. Người dùng click "Tìm kiếm": |
|  | ⮚ Kết quả tìm kiếm bao gồm: danh sách theo tham số đã nhập |
|  | ⮚ Hệ thống hiển thị màn hình Kết quả tìm kiếm. |
|  | ⮚ Kết quả trả về được sắp xếp theo thứ tự thời gian tạo giảm dần. Nếu cùng ngày tạo thì xét đến giờ tạo. |

####  Mô tả màn hình

![](media/image16.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã JD | Ký tự (10) |  |  | Cho phép nhập |
| 2\. | Tiêu đề | Ký tự (50) |  |  | Cho phép nhập |
| 6\. | Vị trí tuyển dụng | Ký tự (50) |  |  | Cho phép nhập |
| 7\. | Ngày tạo | DD/MM/YYYY |  | Ngày hiện tại | Cho phép chọn từ ngày đến ngày |
| ***Nút chức năng*** |  |  |  |  |  |
| 8\. | Áp dụng | Button |  |  | Cho phép áp dụng bộ lọc những tham số đã tra cứu |
