---
title: "UC 5.4.5: Chỉnh sửa thông tin của một Người phụ thuộc của nhân viên"
type: "use-case"
uc_number: "5.4.5"
---

### UC 5.4.5: Chỉnh sửa thông tin của một Người phụ thuộc của nhân viên

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa thông tin của một Người phụ thuộc của nhân viên |
| **Tài khoản:** | Tài khoản được phân quyền chỉnh sửa tại "Quản lý Người phụ thuộc" |
| **Sự kiện kích hoạt:** | Người dùng nhấn nút "Chỉnh sửa" tại màn danh sách "Quản lý Người phụ thuộc" hoặc màn Xem chi tiết Người phụ thuộc |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống cập nhật thông tin đã chỉnh sửa của "Người phụ thuộc" tương ứng |
|  | Thông tin "Người phụ thuộc" ở những thông tin liên quan cũng được cập nhật |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.4.5 | **Quy tắc Chỉnh sửa Người phụ thuộc:** |
|  | - Người dùng nhấn "Chỉnh sửa" tại màn danh sách "Quản lý Người phụ thuộc" |
|  | - Chỉnh sửa thông tin + nhấn nút "Cập nhật" -\> Hệ thống xác thực những trường thông tin: |
|  | - Những trường thông tin cần xác thực: |
|  | - Số CMND/CCCD: Là 9 hoặc 12 chữ số liền nhau (không có dấu cách) |
|  | - File chứng chỉ: dung lượng ≤ 10 MB |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ": |
|  | - Hệ thống báo Chỉnh sửa thành công |
|  | - Quay về màn hình danh sách Người phụ thuộc với thông tin Người phụ thuộc mới đã được cập nhật |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image120.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Những trường thông tin hiển thị như của [[màn hình tạo mới một Người phụ thuộc]{.underline}](#uc-5.4.3-tạo-mới-một-người-phụ-thuộc-của-nhân-viên): |  |  |  |  |
| \- Điền sẵn những thông tin của Người phụ thuộc tương ứng |  |  |  |  |
| \- Tất cả những trường thông tin đều có thể chỉnh sửa |  |  |  |  |
| Cập nhật | Nút | Nhấn để hệ thống xác thực Người phụ thuộc | Xác thực những trường thông tin đúng định dạng + bắt buộc điền |  |
| Hủy | Nút | Nhấn để quy về màn hình danh sách hồ sơ | N/A |  |
