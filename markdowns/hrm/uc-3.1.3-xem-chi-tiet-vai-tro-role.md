---
title: "UC 3.1.3: Xem chi tiết Vai trò (Role)"
type: "use-case"
uc_number: "3.1.3"
---

### UC 3.1.3: Xem chi tiết Vai trò (Role)

  -----------------------------------------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem thông tin chi tiết một Vai trò (Role)
  --------------------------- -------------------------------------------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem chi tiết trong phân hệ "Quản lý Vai trò (Role)"

  **Sự kiện kích hoạt:**      Người dùng nhấn nhấn nút "Xem chi tiết" vai trò (Role) tương ứng trong màn danh sách của "Quản lý Vai trò (Role)"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình "Chi tiết" thông tin của Vai trò
  -----------------------------------------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 3.1.3 | **Quy tắc Xem màn hình Chi tiết thông tin Vai trò (Role):** |
|  | - Người dùng ở màn hình "Quản lý Vai trò (Role)" -\> nhấn nút "Xem chi tiết" của Vai trò (Role) tương ứng: |
|  | - Hệ thống hiển thị màn hình xem thông tin theo lần thay đổi gần nhất của Vai trò (Role) tương ứng |

#### Mô tả màn hình

![](media/image15.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Mã vai trò | Trường dữ liệu | \- Hiển thị thông tin chi tiết của Vai trò (Role) tương ứng | Hiển thị dạng Read-only |  |
|  |  | \- Những trường thông tin giống [[màn tạo mới một Vai trò (Role)]{.underline}](#uc-3.1.2-tạo-mới-vai-trò-role) |  |  |
|  |  | - Thêm "Mã vai trò" và "Người tạo" |  |  |
| Tên vai trò | Trường dữ liệu |  |  |  |
| Người tạo | Trường dữ liệu |  |  |  |
| Danh sách quyền của vai trò tương ứng | Trường dữ liệu |  |  |  |
| Mô tả | Trường dữ liệu |  |  |  |
| Xóa | Nút | Nhấn để Xóa Vai trò tương ứng | UC 3.1.5: Xóa một Vai trò |  |
| Chỉnh sửa | Nút | Nhấn để chỉnh sửa thông tin của Vai trò | UC 3.1.4: Chỉnh sửa thông tin một Vai trò (Role) |  |
