---
title: "UC4.7.8: Xoá lịch phỏng vấn"
type: "use-case"
uc_number: "4.7.8"
---

### UC4.7.8: Xoá lịch phỏng vấn

| **Mục tiêu:** | Cho phép người dùng xoá lịch phỏng vấn đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xoá trong Màn hình Quản lý lịch phỏng vấn. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Nếu lịch đã được gửi đến ứng viên, không cho phép xoá lịch phỏng vấn. |
|  | Nếu lịch được tạo nhưng chưa gửi đến ứng viên, xoá toàn bộ lịch phỏng vấn theo ID tương ứng. |
|  | Hệ thống ghi lại log hành động. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.7.7 | **Deleting Rules:** |
|  | ❖ Hệ thống chỉ hiển thị nút xoá đối với các ứng viên đang ở trạng thái Loại. |
|  | ❖ Hệ thống hiển thị thông báo '*Bạn có chắc chắn muốn xoá dữ liệu không?'.* |
|  | ❖ Người dùng thực hiện nhấn nút Xác nhận của thông báo, hệ thống sẽ xoá toàn bộ thông tin theo ID. |
|  | ❖ Người dùng thực hiện nhấn nút Huỷ của thông báo, hệ thống sẽ không xoá dữ liệu và thoát ra màn hình ***Quản lý lịch phỏng vấn.*** |
