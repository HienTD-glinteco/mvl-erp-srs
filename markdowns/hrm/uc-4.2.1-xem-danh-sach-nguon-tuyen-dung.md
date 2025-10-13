---
title: "UC 4.2.1: Xem danh sách nguồn tuyển dụng"
type: "use-case"
uc_number: "4.2.1"
---

### UC 4.2.1: Xem danh sách nguồn tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xem danh sách các nguồn trên hệ thống |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Quản lý nguồn tuyển dụng* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã hiển thị danh sách nguồn tuyển dụng theo tiêu chí mà người dùng chọn (nếu có). |
|  | Hệ thống lưu log thông tin hành động của từng người dùng. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.2.1 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị Màn hình Xem danh sách nguồn tuyển dụng. |
|  | ❖ Hiển thị danh sách đề xuất được sắp xếp theo thời gian tạo gần nhất |
|  | ❖ Chỉ hiển thị lần tạo hay lần thay đổi mới nhất |

####  Mô tả màn hình

![](media/image47.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Tra cứu thông tin*** |  |  |  |  |  |
| 1. | Mã nguồn | Kí tự (50) | Không |  | Cho phép nhập. |
| 2. | Tên nguồn | Kí tự (100) | Không |  | Cho phép nhập. |
| 3. | Mô tả | Kí tự (500) | Không |  | Cho phép nhập. |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 4. | Mã nguồn | Kí tự (50) | Có |  | Hiển thị theo CSDL |
| 5. | Tên nguồn | Kí tự (250) | Có |  | Hiển thị theo CSDL |
| 6. | Mô tả | Kí tự (500) | Có |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 7. | Tìm kiếm | Button | Không |  | Cho phép tìm kiếm theo các tham số đã nhập |
| 8. | Thêm mới | Button | Không |  | Cho phép tạo mới tài liệu |
| 9. | Xem chi tiết (Thao tác) | Button | Không |  | Cho phép xem màn hình chi tiết thông tin tài liệu tương ứng |
| 10. | Sửa (Thao tác) | Button | Không |  | Cho phép chỉnh sửa thông tin về tài liệu tương ứng |
| 11. | Xoá (Thao tác) | Button | Không |  | Cho phép xoá tài liệu tương ứng |
