---
title: "UC 5.1.7: Xóa một Nhân viên đã có"
type: "use-case"
uc_number: "5.1.7"
---

### UC 5.1.7: Xóa một Nhân viên đã có

| **Mục tiêu:** | Cho phép người dùng xóa đi một Hồ sơ Nhân viên đã có |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền Xóa tại phân hệ con "Quản lý Hồ sơ Nhân viên" |
| **Sự kiện kích hoạt:** | Người dùng nhấn nút "Xóa" tại màn hình danh sách "Quản lý Hồ sơ nhân viên" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống xóa "Hồ sơ nhân viên" tương ứng khỏi màn hình danh sách "Hồ sơ nhân viên", "Nhân viên theo Role" và "Bảng chấm công" |
|  | Khóa tài khoản của "Hồ sơ nhân viên" tương ứng |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 5.1.7 | **Quy tắc Xóa Hồ sơ Nhân viên:** |
|  | - Người dùng nhấn nút "Xóa" Hồ sơ nhân viên tại màn hình danh sách của phân hệ con "Quản lý Hồ sơ Nhân viên" → Hệ thống hiển thị màn hình Xác nhận Xóa Hồ sơ nhân viên |
|  | - Người dùng nhấn |
|  | - "Xác nhận" |
|  | - **Nếu Nhân viên đang được sử dụng trong thông tin khác (ví dụ: Người phụ thuộc đang gắn với Nhân viên):** |
|  | - Hệ thống báo lỗi tương ứng |
|  | - Nếu **"Nhân viên" không còn được sử dụng trong thông tin khác**: |
|  | - Thông báo Xóa hồ sơ nhân viên thành công |
|  | - Xóa thông tin nhân viên ở [[màn hình "Quản lý Nhân viên theo Role"]{.underline}](#phân-hệ-con-quản-lý-nhân-viên-theo-role) |
|  | - Xóa thông tin nhân viên ở màn hình Quản lý Bảng chấm công |
|  | - Khóa tài khoản của "Hồ sơ nhân viên" được xóa |
|  | - Thông tin vẫn được lưu trong CSDL, người dùng không thể khôi phục lại từ giao diện người dùng |
|  | - Quay về [[màn hình hiển danh sách Hồ sơ Nhân viên]{.underline}](#uc-5.1.1-xem-danh-sách-hồ-sơ-nhân-viên) (đã xóa Hồ sơ Nhân viên tương ứng) |
|  | - "Hủy" |
|  | - Hệ thống Quay về [[màn hình hiển thị danh sách Hồ sơ Nhân viên]{.underline}](#uc-5.1.1-xem-danh-sách-hồ-sơ-nhân-viên) |

#### Mô tả màn hình

![](media/image26.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Xác nhận | Nút | Nhấn để xác nhận xóa hồ sơ nhân viên | \- Thông báo xóa thành công | Có |
|  |  |  | \- Về màn hình danh sách hồ sơ |  |
| Hủy | Nút | Nhấn để hủy luồng xóa hồ sơ | Nhấn để quay về màn hình danh sách hồ sơ nhân viên | Có |
