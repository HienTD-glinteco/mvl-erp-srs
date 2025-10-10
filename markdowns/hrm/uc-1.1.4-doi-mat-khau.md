---
title: "UC1.1.4: Đổi mật khẩu"
type: "use-case"
uc_number: "1.1.4"
---

### UC1.1.4: Đổi mật khẩu

| **Mục tiêu:** | Cho phép người dùng đổi mật khẩu tài khoản của họ. |
| --- | --- |
| **Tác nhân:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng chọn chức năng "Đổi mật khẩu" từ menu tài khoản/cài đặt. |
| **Điều kiện tiên quyết:** | Người dùng đã đăng nhập vào hệ thống. |
|  | Có mật khẩu cũ hợp lệ trong cơ sở dữ liệu. |
|  | Mật khẩu đã quá 3 tháng chưa thay đổi. |
| **Kết quả bắt buộc:** | Nếu thành công → Mật khẩu mới được cập nhật trong hệ thống. |
|  | Nếu thất bại → Hiển thị thông báo lỗi phù hợp (mật khẩu cũ sai, mật khẩu mới không hợp lệ, xác nhận mật khẩu không khớp...). |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 1.1.4 | **Change Password Rules:** |
|  | - Yêu cầu đổi mật khẩu định kỳ 3 tháng/ lần. |
|  | - Mật khẩu cũ phải chính xác. |
|  | - Mật khẩu mới phải lớn hơn 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt. |
|  | - Trường Mật khẩu được hệ thống mã hóa ở dưới CSDL và hiển thị dạng masked trên màn hình. Người dùng có thể xem mật khẩu bằng cách nhấn vào biểu tượng \'Hiển thị\' |
|  | - Không cho phép sử dụng lại mật khẩu cũ trong vòng 3 tháng trở lại. |
|  | - Người dùng phải nhập xác nhận mật khẩu mới khớp 100%. |
|  | - Sau khi đổi mật khẩu, tất cả các phiên đăng nhập trước đó sẽ bị đăng xuất. |

#### Mô tả màn hình

![](media/image109.png)

![](media/image106.png)

*Màn hình đổi mật khẩu*

Thông tin màn hình Đổi mật khẩu

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1. | Mật khẩu cũ | Ký tự (100) | Có |  | Cho phép nhập |
| 2. | Mật khẩu mới | Ký tự (100) | Có |  | Cho phép nhập |
| 3. | Nhập lại mật khẩu mới | Ký tự (100) | Có |  | Cho phép nhập |
| ***Nút chức năng*** |  |  |  |  |  |
| 4. | Đổi mật khẩu | Button |  |  | Cho phép lưu thông tin mật khẩu mới |
| 5. | Huỷ | Button |  |  | Thoát ra và quay lại màn hình Đăng nhập |

![](media/image112.png)

![](media/image108.png)
