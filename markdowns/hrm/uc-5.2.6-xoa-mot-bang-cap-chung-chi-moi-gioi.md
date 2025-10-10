---
title: "UC 5.2.6: Xóa một Bằng cấp/ Chứng chỉ môi giới"
type: "use-case"
uc_number: "5.2.6"
---

### UC 5.2.6: Xóa một Bằng cấp/ Chứng chỉ môi giới 

| **Mục tiêu:** | Cho phép người dùng xóa đi một Bằng cấp/Chứng chỉ môi giới đã có |
| **Tài khoản:** | Tài khoản được phân quyền Xóa tại phân hệ con "Quản lý Bằng cấp/Chứng chỉ môi giới" |
| **Sự kiện kích hoạt:** | Người dùng nhấn "Xóa" tại màn "Quản lý Bằng cấp/Chứng chỉ môi giới" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống xóa thông tin tương ứng khỏi màn hình danh sách "Bằng cấp/Chứng chỉ" |
|  | Ở màn hình "Chi tiết Hồ sơ nhân viên", xóa thông tin tương ứng |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.2.6 | **Quy tắc Xóa Bằng cấp/Chứng chỉ môi giới:** |
|  | - Người dùng nhấn nút "Xóa" Bằng cấp/Chứng chỉ môi giới tại màn hình danh sách của phân hệ con "Quản lý Bằng cấp/Chứng chỉ môi giới" → Hệ thống hiển thị màn hình Xác nhận Xóa Bằng cấp/Chứng chỉ môi giới |
|  | - Người dùng nhấn |
|  | - "Xác nhận" |
|  | - **Nếu "Bằng cấp/Chứng chỉ môi giới" đang được sử dụng trong thông tin khác:** |
|  | - Hệ thống báo lỗi tương ứng |
|  | - Nếu **"Bằng cấp/Chứng chỉ môi giới" không còn được sử dụng trong thông tin khác**: |
|  | - Thông báo Xóa Bằng cấp/Chứng chỉ môi giới thành công |
|  | - Xóa thông tin ở màn "Chi tiết Hồ sơ nhân viên" |
|  | - Thông tin vẫn được lưu trong CSDL, người dùng không thể khôi phục lại từ giao diện người dùng |
|  | - Quay về màn hình hiển [[danh sách Bằng cấp/Chứng chỉ môi giới]{.underline}](#uc-5.2.1-xem-danh-sách-bằng-cấp-chứng-chỉ-môi-giới) (đã xóa Bằng cấp/Chứng chỉ môi giới tương ứng) |
|  | - "Hủy" |
|  | - Hệ thống Quay về [[màn hình hiển thị danh sách Bằng cấp/Chứng chỉ môi giới]{.underline}](#uc-5.2.1-xem-danh-sách-bằng-cấp-chứng-chỉ-môi-giới) |

#### Mô tả màn hình

![](media/image26.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Xác nhận | Nút | Nhấn để xác nhận xóa Bằng cấp/Chứng chỉ | \- Thông báo xóa thành công | Có |
|  |  |  | \- Về màn hình danh sách Bằng cấp/Chứng chỉ môi giới |  |
| Hủy | Nút | Nhấn để hủy luồng xóa hồ sơ | Nhấn để quay về màn hình danh sách Bằng cấp/Chứng chỉ | Có |
