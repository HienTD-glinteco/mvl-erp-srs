---
title: "UC 6.3.1: Xem danh sách Lịch làm việc"
type: "use-case"
uc_number: "6.3.1"
---

### UC 6.3.1: Xem danh sách Lịch làm việc

  ---------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng xem danh sách Lịch làm việc đã tạo
  --------------------------- -----------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền xem trong phân hệ "Quản lý Lịch làm việc"

  **Sự kiện kích hoạt:**      Người dùng truy cập Màn hình của Phân hệ con "Quản lý Lịch làm việc"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình "Lịch làm việc"
  ---------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 6.3.1 | **Quy tắc Xem màn hình danh sách Lịch làm việc:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách Lịch làm việc mặc định để tính ngày, giờ công |
|  | - Không được chỉnh sửa thông tin ở phần này |

#### Mô tả màn hình

![](media/image77.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Thứ | Trường thông tin | Hiển thị lần lượt thứ tự Ngày trong tuần | Danh sách "Thứ" hiển thị là: | Có |
|  |  |  | - Thứ 2 |  |
|  |  |  | - Thứ 3 |  |
|  |  |  | - Thứ 4 |  |
|  |  |  | - Thứ 5 |  |
|  |  |  | - Thứ 6 |  |
|  |  |  | - Thứ 7 |  |
|  |  |  | - Chủ nhật |  |
| Buổi sáng | Trường thông tin | Hiển thị "Giờ làm việc buổi sáng" của ngày tương ứng | \- Từ **"Thứ 2" đến "Thứ 7**" hiển thị là: **"08:00 - 12:00"** | Có |
|  |  |  | \- Với **"Chủ nhật"**: hiển thị trống |  |
| Nghỉ trưa | Trường thông tin | Hiển thị "Giờ nghỉ trưa" của ngày tương ứng | \- Từ **"Thứ 2" đến "Thứ 6**" hiển thị là: **"12:00 - 13:30"** | Có |
|  |  |  | \- Với **"Thứ 7, Chủ nhật"**: hiển thị trống |  |
| Buổi chiều | Trường thông tin | Hiển thị "Giờ làm việc buổi chiều" của ngày tương ứng | \- Từ **"Thứ 2" đến "Thứ 6**" hiển thị là: **"13:30 - 17:30"** | Có |
|  |  |  | \- Với **"Thứ 7, Chủ nhật"**: hiển thị trống |  |
| Ghi chú | Trường thông tin | Hiển thị "Ghi chú" của ngày tương ứng | \- Với **"Thứ 7"** hiển thị: **"Làm buổi sáng"** | Có |
|  |  |  | \- Với **"Chủ nhật"** hiển thị: **"Nghỉ"** |  |
