---
title: "UC 4.1.6: Xóa kênh tuyển dụng"
type: "use-case"
uc_number: "4.1.6"
---

### UC 4.1.6: Xóa kênh tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xóa một kênh tuyển dụng đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xóa trong Màn hình Quản lý kênh tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống xoá toàn bộ thông tin và các lần thay đổi của dòng dữ liệu thực hiện thao tác. |
|  | Danh sách hiển thị lại, không còn bản ghi vừa bị xoá. |
|  | Hệ thống ghi nhận lịch sử thao tác xoá. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.1.6 | **Deleting Rules:** |
|  | ❖ Người dùng click vào icon Xóa ở dòng dữ liệu. |
|  | ❖ Hệ thống hiển thị thông báo: *'Bạn có chắc chắn muốn xóa không?'* |
|  | ❖ Người dùng thực hiện nhấn nút Xác nhận của thông báo, hệ thống kiểm tra nếu kênh tuyển dụng này chưa được gắn với dữ liệu thông tin ứng viên và chi phí tuyển dụng thì xoá toàn bộ thông tin danh mục tài liệu; nếu đã được gắn hệ thống hiển thị thông báo: '*Không thể xoá thông tin do kênh tuyển dụng đã được gắn với \[Thông tin ứng viên/Chi phí tuyển dụng\].*' |
|  | ❖ Người dùng thực hiện nhấn nút Huỷ của thông báo, hệ thống sẽ không xoá dữ liệu và thoát ra màn hình ***Quản lý kênh tuyển dụng*** |
