---
title: "UC4.6.8: Xoá ứng viên"
type: "use-case"
uc_number: "4.6.8"
---

### UC4.6.8: Xoá ứng viên

| **Mục tiêu:** | Cho phép người dùng xoá ứng viên đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xoá trong Màn hình Quản lý ứng viên. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Nếu ứng viên được xóa thành công → hồ sơ biến mất khỏi danh sách quản lý ứng viên. |
|  | Hệ thống ghi lại log hành động (mã ứng viên, tên ứng viên, CCCD, người xóa, thời gian). |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.6.8 | **Deleting Rules:** |
|  | ❖ Hệ thống chỉ hiển thị nút xoá đối với các ứng viên đang ở trạng thái Loại. |
|  | ❖ Hệ thống hiển thị thông báo '*Bạn có chắc chắn muốn xoá dữ liệu không?'.* |
|  | ❖ Người dùng thực hiện nhấn nút Xác nhận của thông báo, hệ thống sẽ xoá toàn bộ thông tin theo ID. |
|  | ❖ Người dùng thực hiện nhấn nút Huỷ của thông báo, hệ thống sẽ không xoá dữ liệu và thoát ra màn hình ***Quản lý ứng viên.*** |
