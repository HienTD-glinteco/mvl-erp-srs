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

1.  Phân hệ con "Quản lý nguồn tuyển dụng"
    --------------------------------------

    1.  ### UC 4.2.1: Xem danh sách nguồn tuyển dụng

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
