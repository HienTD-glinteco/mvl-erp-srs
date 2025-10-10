---
title: "UC 6.4.4: Chỉnh sửa thông tin 1 Ngày lễ"
type: "use-case"
uc_number: "6.4.4"
---

### UC 6.4.4: Chỉnh sửa thông tin 1 Ngày lễ

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa thông tin của 1 Ngày lễ |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền chỉnh sửa tại "Quản lý Ngày lễ" |
| **Sự kiện kích hoạt:** | Người dùng nhấn nút "Chỉnh sửa" tại màn danh sách "Quản lý Ngày lễ" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống cập nhật thông tin đã chỉnh sửa của "Ngày lễ" tương ứng |
|  | Thông tin "Ngày lễ" ở những thông tin liên quan được cập nhật |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 6.4.4 | **Quy tắc Chỉnh sửa Ngày lễ:** |
|  | - Người dùng nhấn "Chỉnh sửa" tại màn danh sách "Quản lý Ngày lễ" |
|  | - Chỉnh sửa thông tin + nhấn nút "Cập nhật" -\> Hệ thống xác thực những trường thông tin: |
|  | - Những trường thông tin cần xác thực: |
|  | - Ngày bắt đầu ≤ Ngày kết thúc |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ": |
|  | - Hệ thống báo Chỉnh sửa thành công |
|  | - Cập nhật "Ngày lễ" mới tương ứng ở Bảng chấm công |
|  | - Quay về màn hình danh sách Ngày lễ với thông tin Ngày lễ mới đã được cập nhật |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| \- Điền sẵn những thông tin của Ngày lễ tương ứng |  |  |  |  |
| \- Tất cả những trường thông tin đều có thể chỉnh sửa |  |  |  |  |
| Cập nhật | Nút | Nhấn để hệ thống xác thực Ngày lễ | Xác thực những trường thông tin đúng định dạng + bắt buộc điền |  |
| Hủy | Nút | Nhấn để quay về màn hình danh sách | N/A |  |
