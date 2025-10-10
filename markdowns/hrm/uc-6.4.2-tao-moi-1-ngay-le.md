---
title: "UC 6.4.2: Tạo mới 1 Ngày lễ"
type: "use-case"
uc_number: "6.4.2"
---

### UC 6.4.2: Tạo mới 1 Ngày lễ

| **Mục tiêu:** | Cho phép người dùng tạo Ngày lễ mới |
| **Tài khoản:** | Tài khoản được phân quyền tạo mới Ngày lễ trong phân hệ "Quản lý Ngày lễ " |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Thêm mới" tại màn hình "Quản lý Ngày lễ" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị "Ngày lễ" tạo mới ở màn hình danh sách |
|  | Ở màn hình "Bảng chấm công", hiển thị Ngày lễ tương ứng |

#### Luồng nghiệp vụ

![](media/image67.png)

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 6.4.2 | **Quy tắc Tạo mới Ngày lễ:** |
|  | - Người dùng nhấn nút "Thêm mới" -\> hệ thống hiển thị màn hình "Tạo Ngày lễ mới" |
|  | - Người dùng điền thông tin Ngày lễ và nhấn "Tạo mới" để xác thực thông tin: |
|  | - Những trường thông tin cần xác thực: |
|  | - Ngày bắt đầu ≤ Ngày kết thúc |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Tạo mới thành công |
|  | - Hiển thị trong Bảng chấm công: từ "Ngày bắt đầu" đến "Ngày kết thúc" là ngày lễ ( Ngoại trừ Chủ nhật) |
|  | - Quay về màn hình danh sách Ngày lễ mới tạo được hiển thị đầu tiên |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ: Hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Tên ngày lễ | Textbox | Nhập "Tên ngày lễ" tương ứng | N/A | Có |
| Ngày bắt đầu | Date picker | Chọn "Ngày bắt đầu" tương ứng | \- Xác thực: Ngày bắt đầu ≤ Ngày kết thúc | Có |
|  |  |  | \- Nhấn sẽ hiển thị màn chọn Ngày/Tháng/Năm![](media/image46.png) |  |
| Ngày kết thúc | Date picker | Chọn "Ngày kết thúc" tương ứng | \- Xác thực: Ngày bắt đầu ≤ Ngày kết thúc | Có |
|  |  |  | \- Nhấn sẽ hiển thị màn chọn Ngày/Tháng/Năm |  |
| Ghi chú | Textbox | Nhập "Ghi chú" tương ứng | N/A | Không |
| Tạo mới | Nút | Nhấn nút để hệ thống xác thực thông tin | Xác thực những trường thông tin đúng định dạng và bắt buộc điền |  |
| --- | --- | --- | --- | --- |
