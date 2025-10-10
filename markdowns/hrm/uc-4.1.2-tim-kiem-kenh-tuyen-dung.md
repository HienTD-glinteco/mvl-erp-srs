---
title: "UC 4.1.2: Tìm kiếm kênh tuyển dụng"
type: "use-case"
uc_number: "4.1.2"
---

### UC 4.1.2: Tìm kiếm kênh tuyển dụng

| **Mục tiêu:** | Cho phép người dùng tìm kiếm kênh tuyển dụng trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng bấm nút tìm kiếm trong Màn hình Quản lý kênh tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống hiển thị danh sách kênh tuyển dụng đã được lọc theo từ khóa/tiêu chí tìm kiếm mà người dùng nhập. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.1.2 | **Searching Rules:** |
|  | ❖ Cho phép người dùng tìm kiếm bằng các từ khóa liên quan đến kênh tuyển dụng. Người dùng click "Tìm kiếm": |
|  | ⮚ Kết quả tìm kiếm bao gồm: danh sách các quyết định theo tham số đã nhập. |
|  | ⮚ Hệ thống hiển thị màn hình Kết quả tìm kiếm có chứa toàn bộ kết quả tìm kiếm. |
|  | ⮚ Với từ khóa, điều kiện tìm kiếm: gần đúng. |
|  | ⮚ Kết quả trả về được sắp xếp theo thứ tự thời gian tạo giảm dần. Nếu cùng ngày tạo thì xét đến giờ tạo. |
