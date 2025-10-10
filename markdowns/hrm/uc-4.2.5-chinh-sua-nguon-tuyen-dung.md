---
title: "UC 4.2.5: Chỉnh sửa nguồn tuyển dụng"
type: "use-case"
uc_number: "4.2.5"
---

### UC 4.2.5: Chỉnh sửa nguồn tuyển dụng

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa một nguồn tuyển dụng đã có trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Sửa trong Màn hình Quản lý đề xuất |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Thông tin nguồn tuyển dụng đã được cập nhật thành công trong hệ thống (nếu người dùng lưu thay đổi). |
|  | Lịch sử thay đổi (nếu có yêu cầu audit/log) được ghi nhận. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.2.5.1 | **Displaying Rules:** |
|  | ❖ Hiển thị màn hình Chỉnh sửa nguồn tuyển dụng. |
| QTNV 4.2.5.1 | **Editing Rules:** |
|  | ❖ Người dùng nhập các thông tin trên màn hình. |
|  | ❖ Hệ thống kiểm tra từng trường thông tin nhập của người dùng theo quy tắc (chi tiết ở bảng dưới). Nếu không đúng yêu cầu của hệ thống, hiển thị màu đỏ trường thông tin. |
|  | ❖ Các trường hợp: |
|  | o Người dùng xác nhận hủy, đóng biểu mẫu. |
|  | o Người dùng xác nhận lưu: |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin thành công' và lưu thông tin chỉnh sửa xuống CSDL nếu đủ điều kiện. Thoát ra màn hình Xem chi tiết. Hệ thống lưu thông tin vào CSDL giữ nguyên ID. Các thay đổi về dữ liệu có liên quan đến nguồn tuyển dụng sẽ được lưu lịch sử. |
|  | ▪ Hệ thống hiển thị thông báo 'Lưu thông tin không thành công' và không lưu thông tin nếu không đủ điều kiện. Ở nguyên màn hình Chỉnh sửa |

#### Mô tả màn hình

![](media/image75.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1\. | Mã nguồn | Kí tự (50) | Có |  | Không cho phép sửa |
| 2\. | Tên nguồn | Kí tự (250) | Có |  | Cho phép chọn một trong danh sách: |
|  |  |  |  |  | \- Nguồn giới thiệu |
|  |  |  |  |  | \- Nguồn phòng tuyển dụng |
|  |  |  |  |  | \- Nguồn quay lại |
| 3\. | Mô tả | Kí tự (500) | Có |  | Cho phép sửa |
| ***Nút chức năng*** |  |  |  |  |  |
| 4\. | Lưu | Button | Không |  | Cho phép lưu thông tin đã nhập |
| 5\. | Thoát | Button | Không |  | Không lưu thông tin và thoát ra khỏi màn hình thêm mới, quay lại màn hình Quản lý nguồn tuyển dụng |
