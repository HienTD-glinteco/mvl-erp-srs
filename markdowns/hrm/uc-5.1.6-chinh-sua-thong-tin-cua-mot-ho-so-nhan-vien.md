---
title: "UC 5.1.6: Chỉnh sửa thông tin của một Hồ sơ nhân viên"
type: "use-case"
uc_number: "5.1.6"
---

### UC 5.1.6: Chỉnh sửa thông tin của một Hồ sơ nhân viên

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa thông tin của một Hồ sơ nhân viên |
| **Tài khoản:** | Tài khoản được phân quyền chỉnh sửa tại phân hệ con "Quản lý Hồ sơ Nhân viên" |
| **Sự kiện kích hoạt:** | Người dùng nhấn nút "Chỉnh sửa" tại màn danh sách "Quản lý Hồ sơ Nhân viên" hoặc màn "Xem chi tiết" một Hồ sơ nhân viên |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống cập nhật thông tin đã chỉnh sửa của "Hồ sơ nhân viên" tương ứng |
|  | Thông tin "Hồ sơ nhân viên" ở những thông tin liên quan cũng được cập nhật |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.1.6.1 | **Quy tắc Chỉnh sửa Hồ sơ Nhân viên:** |
|  | - Người dùng nhấn nút "Chỉnh sửa" tại màn danh sách "Quản lý Hồ sơ Nhân viên" |
|  | - Chỉnh sửa thông tin + nhấn nút "Cập nhật" -\> Hệ thống xác thực những trường thông tin của Hồ sơ nhân viên: |
|  | - Những trường thông tin cần xác thực: |
|  | - Email: |
|  | - Đúng định dạng Email |
|  | - Không trùng với Email đã có |
|  | - Số điện thoại: đúng định dạng số điện thoại Việt Nam |
|  | - Số điện thoại ( liên hệ khẩn cấp): đúng định dạng số điện thoại Việt Nam |
|  | - Số CMND/CCCD: |
|  | - Không được trùng với nhân viên khác |
|  | - Là 9 hoặc 12 chữ số liền nhau (không có dấu cách) |
|  | - Nhân viên cần thuộc ít nhất một Khối hoặc một Phòng ban |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ": |
|  | - Hệ thống báo Chỉnh sửa thành công |
|  | - Quay về màn hình danh sách Hồ sơ Nhân viên với thông tin Hồ sơ mới đã được cập nhật |
|  | - Nếu đổi sang trạng thái "Đã nghỉ việc", khóa tài khoản của Nhân viên tương ứng |
|  | - Thêm thông tin tương ứng ở "Lịch sử công tác" (nếu có) |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |
| QTNV 5.1.6.2 | **Quy tắc Quay lại làm việc với Nhân viên "Đã nghỉ việc":** |
|  | - Người dùng nhấn nút "Quay lại làm việc". Hệ thống hiển thị Pop-up "Xác nhận quay lại làm việc" |
|  | - Bắt buộc chọn thông tin "Ngày bắt đầu quay lại làm việc" |
|  | - Sau khi nhấn "Xác nhận", hệ thống: |
|  | - Thay đổi trạng thái nhân viên thành "Đang làm việc" |
|  | - Đổi trường "Ngày bắt đầu" hiện tại của nhân viên thành "Ngày bắt đầu quay lại làm việc" vừa chon |
|  | - Bỏ khóa tài khoản của Nhân viên tương ứng |
|  | - Quay về màn hình danh sách Hồ sơ Nhân viên với thông tin Hồ sơ mới đã được cập nhật |
|  | - Bỏ hiển thị 2 thông tin "Ngày nghỉ việc" và "Lý do nghỉ việc" khi "Xem chi tiết" hay "Chỉnh sửa" Hồ sơ này |
|  | - Thêm thông tin tương ứng ở "Lịch sử công tác" |

#### Mô tả màn hình

![](media/image50.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Những trường thông tin hiển thị như của màn hình "[[Xem chi tiết một Hồ sơ nhân viên]{.underline}](#uc-5.1.2-xem-chi-tiết-thông-tin-một-nhân-viên)": |  |  |  |  |
| \- Điền sẵn những thông tin của Hồ sơ Nhân viên tương ứng |  |  |  |  |
| \- "Mã nhân viên" hiển thị dạng **Read-only** |  |  |  |  |
| Tạo bản sao | Nút | Nhấn để tạo bản sao của hồ sơ đang xem | [[UC 5.1.5: Tạo bản sao Hồ sơ nhân viên]{.underline}](#uc-5.1.5-tạo-bản-sao-của-một-nhân-viên-đã-có-duplicate) |  |
|  |  |  | Chỉ hiển thị với nhân viên có trạng thái "Đang làm việc" và "On-boarding" |  |
| Quay lại làm việc | Nút | Nhấn để đổi trạng thái nhân viên từ "Đã nghỉ việc" thành "Đang làm việc" | \- Chỉ hiển thị với nhân viên có trạng thái "Đã nghỉ việc" |  |
| Cập nhật | Nút | Nhấn để cập nhật thông tin của hồ sơ | Xác thực những trường thông tin đúng định dạng + bắt buộc |  |
| Hủy | Nút | Nhấn để quay về màn danh sách hồ sơ | N/A |  |
