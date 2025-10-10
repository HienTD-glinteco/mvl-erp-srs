---
title: "UC 5.4.6: Xóa một Người phụ thuộc của Nhân viên"
type: "use-case"
uc_number: "5.4.6"
---

### UC 5.4.6: Xóa một Người phụ thuộc của Nhân viên

| **Mục tiêu:** | Cho phép người dùng xóa đi một Người phụ thuộc đã có |
| **Tài khoản:** | Tài khoản được phân quyền Xóa tại phân hệ con "Quản lý Người phụ thuộc" |
| **Sự kiện kích hoạt:** | Người dùng nhấn "Xóa" tại màn "Quản lý Người phụ thuộc" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống xóa thông tin tương ứng khỏi màn hình danh sách "Người phụ thuộc" |
|  | Ở màn hình "Chi tiết Hồ sơ nhân viên", xóa thông tin tương ứng |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.4.6 | **Quy tắc Xóa Người phụ thuộc:** |
|  | - Người dùng nhấn nút "Xóa" Người phụ thuộc tại màn hình danh sách của phân hệ con "Quản lý Người phụ thuộc" → Hệ thống hiển thị màn hình Xác nhận Xóa Người phụ thuộc |
|  | - Người dùng nhấn |
|  | - "Xác nhận" |
|  | - **Nếu "Người phụ thuộc" đang được sử dụng trong thông tin khác:** |
|  | - Hệ thống báo lỗi tương ứng |
|  | - Nếu **"Người phụ thuộc" không còn được sử dụng trong thông tin khác**: |
|  | - Thông báo Xóa Người phụ thuộc thành công |
|  | - Xóa thông tin ở màn "Chi tiết Hồ sơ nhân viên" |
|  | - Thông tin vẫn được lưu trong CSDL, người dùng không thể khôi phục lại từ giao diện người dùng |
|  | - Quay về [[màn hình hiển danh sách Người phụ thuộc]{.underline}](#uc-5.4.1-xem-danh-sách-người-phụ-thuộc-của-nhân-viên) (đã xóa Người phụ thuộc tương ứng) |
|  | - "Hủy" |
|  | - Hệ thống Quay về [[màn hình hiển thị danh sách Người phụ thuộc]{.underline}](#uc-5.4.1-xem-danh-sách-người-phụ-thuộc-của-nhân-viên) |

#### Mô tả màn hình

![](media/image26.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Xác nhận | Nút | Nhấn để xác nhận xóa Người phụ thuộc | \- Thông báo xóa thành công |  |
|  |  |  | \- Về màn hình danh sách Người phụ thuộc |  |
| Hủy | Nút | Nhấn để hủy luồng xóa | Nhấn để quay về màn hình danh sách Người phụ thuộc |  |
