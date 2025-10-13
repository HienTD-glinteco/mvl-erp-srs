---
title: "UC 4.3.8: Xoá chi phí tuyển dụng"
type: "use-case"
uc_number: "4.3.8"
---

### UC 4.3.8: Xoá chi phí tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xóa chi phí tuyển dụng đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xóa trong Màn hình Quản lý chi phí tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống xoá toàn bộ thông tin và các lần thay đổi của dòng dữ liệu thực hiện thao tác. |
|  | Danh sách hiển thị lại, không còn bản ghi vừa bị xoá. |
|  | Hệ thống ghi nhận lịch sử thao tác xoá. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.3.8 | **Deleting Rules**\[1\] **:** |
|  | ❖ Hệ thống hiển thị thông báo '*Bạn có chắc chắn muốn xoá dữ liệu không?'* |
|  | ❖ Người dùng thực hiện nhấn nút Xác nhận của thông báo, hệ thống sẽ xoá toàn bộ thông tin theo ID. |
|  | ❖ Người dùng thực hiện nhấn nút Huỷ của thông báo, hệ thống sẽ không xoá dữ liệu và thoát ra màn hình ***Quản lý chi phí tuyển dụng*** |
