---
title: "UC 4.2.6: Xoá nguồn tuyển dụng"
type: "use-case"
uc_number: "4.2.6"
---

### UC 4.2.6: Xoá nguồn tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xóa một nguồn tuyển dụng đã có trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xóa trong Màn hình Quản lý nguồn tuyển dụng. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống xoá toàn bộ thông tin và các lần thay đổi của dòng dữ liệu thực hiện thao tác. |
|  | Danh sách hiển thị lại, không còn bản ghi vừa bị xoá. |
|  | Hệ thống ghi nhận lịch sử thao tác xoá. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.2.6 | **Deleting Rules:** |
|  | ❖ Người dùng click vào icon Xóa ở dòng dữ liệu. |
|  | ❖ Hệ thống hiển thị thông báo: 'Bạn có chắc chắn muốn xóa không?' |
|  | ❖ Người dùng thực hiện nhấn nút Xác nhận của thông báo, hệ thống kiểm tra nếu kênh tuyển dụng này chưa được gắn với dữ liệu thông tin ứng viên và chi phí tuyển dụng thì xoá toàn bộ thông tin danh mục tài liệu; nếu đã được gắn hệ thống hiển thị thông báo: 'Không thể xoá thông tin do kênh tuyển dụng đã được gắn với \[Thông tin ứng viên/Chi phí tuyển dụng\].' |
|  | ❖ Người dùng thực hiện nhấn nút Huỷ của thông báo, hệ thống sẽ không xoá dữ liệu và thoát ra màn hình ***Quản lý nguồn tuyển dụng*** |

1.  Phân hệ con "Quản lý chi phí tuyển dụng"
    ----------------------------------------

    1.  ### UC 4.3.1: Xem danh sách chi phí tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xem danh sách các khoản cho chi phí tuyển dụng trên hệ thống |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Quản lý chi phí tuyển dụng* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã hiển thị danh sách kênh tuyển dụng theo tiêu chí mà người dùng chọn (nếu có). |
|  | Hệ thống lưu log thông tin hành động của từng người dùng. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.3.1 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị Màn hình Xem danh sách các chi phí tuyển dụng. |
|  | ❖ Hiển thị danh sách được sắp xếp theo thời gian tạo gần nhất |
|  | ❖ Chỉ hiển thị lần tạo hay lần thay đổi mới nhất |
|  | ❖ Trang danh sách có 20 dòng/trang, có các thanh công cụ chuyển trang (Pagination) nếu dòng dữ liệu lớn hơn 20 |

#### Mô tả màn hình

![](media/image58.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin tìm kiếm*** |  |  |  |  |  |
| 1\. | Thời gian | Date (mm/yyyy) | Không |  | Cho phép nhập |
| 2\. | Nguồn tuyển dụng | Dropdown | Không |  | Cho phép nhập hoặc chọn. |
|  |  |  |  |  | Có thể chọn một hoặc nhiều dữ liệu |
| 3\. | Kênh tuyển dụng | Dropdown | Không |  | Cho phép nhập hoặc chọn. |
|  |  |  |  |  | Có thể chọn một hoặc nhiều dữ liệu |
| ***Thông tin danh sách*** |  |  |  |  |  |
| 5\. | Thời gian | Ký tự (7) | Có |  | Hiển thị theo CSDL |
| 6\. | Nguồn tuyển dụng | Ký tự (250) | Có |  | Hiển thị theo CSDL |
| 7\. | Kênh tuyển dụng | Ký tự (250) | Có |  | Hiển thị theo CSDL |
| 8\. | Số ứng viên tham gia | Số (4) | Có |  | Hiển thị theo CSDL |
| 9\. | Tổng chi phí | Ký tự (20) | Có |  | Hiển thị theo CSDL |
| 10\. | Số ứng viên đã tuyển | Số (4) | Có |  | Hiển thị theo CSDL |
| 11\. | Chi phí tính trên mỗi ứng viên | Ký tự (20) | Có |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 12\. | Tìm kiếm | Button | Không |  | Cho phép hiển thị danh sách theo các tham số đã chọn |
| 13\. | Thêm mới | Button | Không |  | Hệ thống hiển thị màn hình thêm mới |
| 14\. | Sửa (thao tác) | Button | Không |  | Hệ thống hiển thị màn hình sửa theo dòng dữ liệu thực hiện thao tác |
| 15\. | Xoá (thao tác) | Button | Không |  | Cho phép xóa dòng dữ liệu thực hiện thao tác |
| 16\. | Xem chi tiết (thao tác) | Button | Không |  | Hệ thống hiển thị màn hình xem chi tiết theo dòng dữ liệu thực hiện thao tác |
| 17\. | Kết xuất (thao tác) | Button | Không |  | Cho phép kết xuất dòng dữ liệu thực hiện thao tác |
