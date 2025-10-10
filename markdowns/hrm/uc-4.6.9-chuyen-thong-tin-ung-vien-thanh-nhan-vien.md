---
title: "UC4.6.9: Chuyển thông tin ứng viên thành nhân viên"
type: "use-case"
uc_number: "4.6.9"
---

### UC4.6.9: Chuyển thông tin ứng viên thành nhân viên

| **Mục tiêu:** | Cho phép người dùng chuyển đổi hồ sơ của ứng viên đã được tuyển dụng thành hồ sơ nhân viên chính thức trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Chuyển hồ sơ thành nhân viên trong Màn hình Quản lý ứng viên hoặc khi Xem chi tiết thông tin ứng viên. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
|  | Ứng viên đang có trạng thái Đã nhận việc. |
| **Kết quả bắt buộc:** | Thông tin ứng viên được tạo mới thành hồ sơ nhân viên trong hệ thống HRM. |
|  | Không cho phép chuyển thông tin khi ứng viên có CCCD bị trùng với thông tin nhân viên. |
|  | Hệ thống ghi lại log hành động. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.6.9 | ❖ Chỉ cho phép chuyển thông tin ứng viên thành nhân viên khi trạng thái của ứng viên là Đã nhận việc. |
|  | ❖ Nếu CCCD của ứng viên đã tồn tại ở thông tin của nhân viên thì hệ thống hiển thị cảnh báo tương ứng và không cho chuyển thông tin sang ứng viên. |
|  | ❖ Đảm bảo tính toàn vẹn dữ liệu giữa các module. |
|  | ❖ Ghi log toàn bộ thao tác để phục vụ kiểm tra/audit. |
