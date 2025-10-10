---
title: "UC 4.4.2: Tìm kiếm danh sách đề nghị tuyển dụng"
type: "use-case"
uc_number: "4.4.2"
---

### UC 4.4.2: Tìm kiếm danh sách đề nghị tuyển dụng

| **Mục tiêu:** | Cho phép người dùng tra cứu thông tin về đề nghị tuyển dụng trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Quản lý đề nghị tuyển dụng* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống hiển thị danh sách kênh tuyển dụng đã được lọc theo từ khóa/tiêu chí tìm kiếm mà người dùng nhập. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV | **Searching Rules:** |
| 4.4.2 | ❖ Cho phép người dùng tìm kiếm bằng các từ khóa liên quan đến đề nghị tuyển dụng. Người dùng click "Tìm kiếm": |
|  | ⮚ Kết quả tìm kiếm bao gồm: danh sách theo tham số đã nhập |
|  | ⮚ Hệ thống hiển thị màn hình Kết quả tìm kiếm. |
|  | ⮚ Kết quả trả về được sắp xếp theo thứ tự thời gian tạo giảm dần. Nếu cùng ngày tạo thì xét đến giờ tạo. |
