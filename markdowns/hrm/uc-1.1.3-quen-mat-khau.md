---
title: "UC1.1.3: Quên mật khẩu"
type: "use-case"
uc_number: "1.1.3"
---

### UC1.1.3: Quên mật khẩu

| **Mục tiêu:** | Cho phép người dùng đặt lại mật khẩu trong trường hợp quên mật khẩu, đảm bảo an toàn và bảo mật thông tin tài khoản. |
| --- | --- |
| **Tác nhân:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng tại màn hình đăng nhập chọn chức năng "Quên mật khẩu". |
| **Điều kiện tiên quyết:** | Người dùng đã có tài khoản hợp lệ và email được đăng ký trong hệ thống.\ |
|  | Hệ thống có kết nối dịch vụ gửi email. |
| **Kết quả bắt buộc:** | Nếu thành công → Mật khẩu được cập nhật, người dùng có thể đăng nhập bằng mật khẩu mới. |
|  | Nếu thất bại → Hiển thị thông báo lỗi phù hợp (OTP sai/hết hạn, email không tồn tại...). |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 1.1.3 | **Forgot Password Rules:** |
|  | - OTP có độ dài 6 ký tự số, hiệu lực trong 3 phút. |
|  | - Hệ thống không hiển thị lại nút Quên mật khẩu 3 phút (180 giây) kể từ thời điểm người dùng ấn nút Quên mật khẩu (5). |
|  | - Mật khẩu mới phải có tối thiểu 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt. |
|  | - Trường Mật khẩu được hệ thống mã hóa ở dưới CSDL và hiển thị dạng masked trên màn hình. Người dùng có thể xem mật khẩu bằng cách nhấn vào biểu tượng \'Hiển thị\'. |
|  | - Thông tin Mật khẩu mới và Xác thực lại mật khẩu phải khớp nhau. |
|  | - Sau khi đổi mật khẩu, tất cả phiên đăng nhập cũ sẽ bị đăng xuất. |
|  | - Hệ thống gửi email: tài khoản đã thay đổi mật khẩu. |

#### Luồng nghiệp vụ

![](media/image84.png)

#### Mô tả màn hình

![](media/image101.png)

Thông tin màn hình Đặt lại mật khẩu

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1. | Email | Ký tự (100) | Có |  | Cho phép nhập |
| ***Nút chức năng*** |  |  |  |  |  |
| 2. | Gửỉ mã xác nhận | Button |  |  | Cho phép lưu thông tin mật khẩu mới |
| 3. | Huỷ | Button |  |  | Thoát ra và quay lại màn hình Đăng nhập |

![](media/image82.png)

Thông tin màn hình Xác thực bảo mật OTP

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1. | Mã OTP | Ký tự (6) | Có |  | Cho phép nhập. |
| ***Nút chức năng*** |  |  |  |  |  |
| 2. | Xác thực | Button |  |  | Hệ thống kiểm tra thông tin OTP và cho phép đăng nhập vào hệ thống |
| 3. | Huỷ | Button |  |  | Quay lại màn hình đăng nhập |

![](media/image83.png)

Thông tin màn hình

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1. | Mật khẩu mới | Ký tự (50) | Có |  | Cho phép nhập. |
| 2. | Nhập mật khẩu mới | Ký tự (50) | Có |  | Cho phép nhập. |
| ***Nút chức năng*** |  |  |  |  |  |
| 3. | Lưu mật khẩu | Button |  |  | Cho phép lưu thông tin mật khẩu mớ. |
| 4. 3\. | Huỷ | Button |  |  | Quay lại màn hình đăng nhập. |

![](media/image93.png)

*Màn hình hoàn tất đổi mật khẩu*
