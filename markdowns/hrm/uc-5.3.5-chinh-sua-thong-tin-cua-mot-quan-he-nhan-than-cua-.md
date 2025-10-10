---
title: "UC 5.3.5: Chỉnh sửa thông tin của một Quan hệ nhân thân của nhân viên"
type: "use-case"
uc_number: "5.3.5"
---

### UC 5.3.5: Chỉnh sửa thông tin của một Quan hệ nhân thân của nhân viên

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa thông tin của một Quan hệ nhân thân của nhân viên |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền chỉnh sửa tại "Quản lý Quan hệ nhân thân" |
| **Sự kiện kích hoạt:** | Người dùng nhấn nút "Chỉnh sửa" tại màn danh sách "Quản lý Quan hệ nhân thân" hoặc màn Xem chi tiết Quan hệ nhân thân |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống cập nhật thông tin đã chỉnh sửa của "Quan hệ nhân thân" tương ứng |
|  | Thông tin "Quan hệ nhân thân" ở những thông tin liên quan cũng được cập nhật |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 5.3.5 | **Quy tắc Chỉnh sửa Quan hệ nhân thân:** |
|  | - Người dùng nhấn "Chỉnh sửa" tại màn danh sách "Quản lý Quan hệ nhân thân" |
|  | - Chỉnh sửa thông tin + nhấn nút "Cập nhật" -\> Hệ thống xác thực những trường thông tin: |
|  | - Những trường thông tin cần xác thực: |
|  | - Số điện thoại: đúng định dạng SĐT Việt Nam |
|  | - Số CMND/CCCD: Là 9 hoặc 12 chữ số liền nhau (không có dấu cách) |
|  | - File chứng chỉ: dung lượng ≤ 10 MB |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ": |
|  | - Hệ thống báo Chỉnh sửa thành công |
|  | - Quay về màn hình danh sách Quan hệ nhân thân với thông tin Quan hệ nhân thân mới đã được cập nhật |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image97.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Những trường thông tin hiển thị như của [[màn hình tạo mới một Quan hệ nhân thân]{.underline}](#uc-5.3.3-tạo-mới-một-quan-hệ-nhân-thân-của-nhân-viên): |  |  |  |  |
| \- Điền sẵn những thông tin của Quan hệ nhân thân tương ứng |  |  |  |  |
| \- Tất cả những trường thông tin đều có thể chỉnh sửa |  |  |  |  |
| Cập nhật | Nút | Nhấn để hệ thống xác thực Hồ sơ | Xác thực những trường thông tin cần xác thực + bắt buộc |  |
| Hủy | Nút | Nhấn để quy về màn hình danh sách hồ sơ | N/A |  |
