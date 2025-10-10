---
title: "UC4.4.6: Xoá đề nghị tuyển dụng"
type: "use-case"
uc_number: "4.4.6"
---

### UC4.4.6: Xoá đề nghị tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xoá một đề nghị tuyển dụng đã có trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xoá trong Màn hình Quản lý đề nghị tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống xoá toàn bộ thông tin và các lần thay đổi của dòng dữ liệu thực hiện thao tác. |
|  | Danh sách hiển thị lại, không còn bản ghi vừa bị xoá. |
|  | Hệ thống ghi nhận lịch sử thao tác xoá. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.4.6 | **Deleting Rules**\[2\] **:** |
|  | ❖ Hệ thống chỉ hiển thị nút xoá đối với các đề nghị đang ở trạng thái Lưu nháp |
|  | ❖ Hệ thống hiển thị thông báo '*Bạn có chắc chắn muốn xoá dữ liệu không?'* |
|  | ❖ Người dùng thực hiện nhấn nút Xác nhận của thông báo, hệ thống sẽ xoá toàn bộ thông tin theo ID. |
|  | ❖ Người dùng thực hiện nhấn nút Huỷ của thông báo, hệ thống sẽ không xoá dữ liệu và thoát ra màn hình ***Quản lý chi phí tuyển dụng*** |
