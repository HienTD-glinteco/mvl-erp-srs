---
title: "UC 6.4.5: Xóa thông tin 1 Ngày lễ"
type: "use-case"
uc_number: "6.4.5"
---

### UC 6.4.5: Xóa thông tin 1 Ngày lễ

| **Mục tiêu:** | Cho phép người dùng xóa đi 1 Ngày lễ đã có |
| **Tài khoản:** | Tài khoản được phân quyền Xóa tại phân hệ con "Quản lý Ngày lễ" |
| **Sự kiện kích hoạt:** | Người dùng nhấn "Xóa" tại màn "Quản lý Ngày lễ" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống xóa thông tin tương ứng khỏi màn hình danh sách "Ngày lễ" |
|  | Ở màn hình "Bảng chấm công", xóa Ngày lễ tương ứng |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV VT.4.5 | **Quy tắc Xóa Ngày lễ:** |
|  | - Người dùng nhấn nút "Xóa" tại màn hình danh sách của phân hệ con "Quản lý Ngày lễ" → Hệ thống hiển thị màn hình Xác nhận Xóa Ngày lễ |
|  | - Người dùng nhấn |
|  | - "Xác nhận" |
|  | - **Nếu "Ngày lễ" đang được sử dụng trong thông tin khác ( trừ "Bảng chấm công"):** |
|  | - Hệ thống báo lỗi tương ứng |
|  | - Nếu **"Ngày lễ" không còn được sử dụng trong thông tin khác ( trừ "Bảng chấm công"**: |
|  | - Thông báo Ngày lễ thành công |
|  | - Quay về màn hình hiển danh sách Ngày lễ (đã xóa Ngày lễ tương ứng) |
|  | - "Hủy" |
| --- | --- |

#### Mô tả màn hình

![](media/image26.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Xác nhận | Nút | Nhấn để xác nhận xóa Ngày lễ | \- Thông báo xóa thành công |  |
|  |  |  | \- Về màn hình danh sách Ngày lễ |  |
| Hủy | Nút | Nhấn để hủy luồng xóa | Nhấn để quay về màn hình danh sách Ngày lễ |  |
