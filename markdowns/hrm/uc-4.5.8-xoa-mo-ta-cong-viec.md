---
title: "UC4.5.8: Xoá mô tả công việc"
type: "use-case"
uc_number: "4.5.8"
---

### UC4.5.8: Xoá mô tả công việc

| **Mục tiêu:** | Cho phép người dùng xoá một mô tả công việc đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xoá trong Màn hình Quản lý mô tả công việc. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống xoá toàn bộ thông tin và các lần thay đổi của dòng dữ liệu thực hiện thao tác. |
|  | Danh sách hiển thị lại, không còn bản ghi vừa bị xoá. |
|  | Hệ thống ghi nhận lịch sử thao tác xoá. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.5.8 | **Deleting Rules**\[3\] **:** |
|  | ❖ Hệ thống chỉ hiển thị nút xoá đối với các mô tả công việc chưa được gắn với đề nghị tuyển dụng. |
|  | ❖ Hệ thống hiển thị thông báo '*Bạn có chắc chắn muốn xoá dữ liệu không?'.* |
|  | ❖ Người dùng thực hiện nhấn nút Xác nhận của thông báo, hệ thống sẽ xoá toàn bộ thông tin theo ID. |
|  | ❖ Người dùng thực hiện nhấn nút Huỷ của thông báo, hệ thống sẽ không xoá dữ liệu và thoát ra màn hình ***Quản lý mô tả công việc.*** |
