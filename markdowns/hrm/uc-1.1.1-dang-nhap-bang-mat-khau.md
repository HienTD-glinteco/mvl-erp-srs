---
title: "UC1.1.1: Đăng nhập bằng mật khẩu"
type: "use-case"
uc_number: "1.1.1"
---

### UC1.1.1: Đăng nhập bằng mật khẩu

| **Mục tiêu:** | Cho phép người dùng truy cập hệ thống bằng thông tin tài khoản đã được cấp, đảm bảo bảo mật và xác thực quyền sử dụng (trên nền tảng web và app mobile). |
| --- | --- |
| **Tác nhân:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập màn hình đăng nhập và nhập thông tin (tên đăng nhập + mật khẩu), sau đó nhấn nút **Đăng nhập** |
| **Điều kiện tiên quyết:** | Người dùng có tài khoản hợp lệ. |
|  | Hệ thống sẵn sàng, có kết nối mạng |
| **Kết quả bắt buộc:** | \- Nếu đăng nhập thành công → chuyển đến Trang chủ / dashboard. |
|  | \- Nếu thất bại → hiển thị thông báo lỗi phù hợp. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 1.1.1 | **Sign-in Rules:** |
|  | - Người dùng nhập các trường thông tin: Tên đăng nhập và Mật khẩu |
|  | - Người dùng ấn nút **Đăng nhập** |
|  | - Hệ thống kiểm tra Tên đăng nhập + mật khẩu phải khớp với dữ liệu trong hệ thống. |
|  | - Trường hợp sai thông tin, truy cập hệ thống thất bại, hiển thị lỗi phù hợp. Cho phép NSD đăng nhập lại liên tục 5 lần. Nếu sai tài khoản sẽ bị khóa tạm thời. **Sau 5 phút sẽ tự động mở khóa.** |
|  | - Trường hợp đúng thông tin, hệ thống sẽ gửi email mã OTP xác thực đến người dùng. |
|  | - Người dùng nhập thông tin OTP trên hệ thống. |
|  | - Hệ thống truy cập thành công và chuyển đến Trang chủ/ Dashboard chung của người dùng. |
|  | - Hệ thống giới hạn mỗi tài khoản chỉ có một phiên đăng nhập duy nhất trên một trình duyệt. |

#### Mô tả màn hình

![](media/image95.png)

*Màn hình đăng nhập trên web*

Thông tin màn hình Đăng nhập

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1. | Tên đăng nhập | Ký tự (100) | Có |  | Cho phép nhập. |
| 2. | Mật khẩu | Ký tự (100) | Có |  | Cho phép nhập. |
|  |  |  |  |  | Trường Mật khẩu được hệ thống mã hóa ở dưới CSDL và hiển thị dạng masked trên màn hình. Người dùng có thể xem mật khẩu bằng cách nhấn vào biểu tượng \'Hiển thị\' |
| ***Nút chức năng*** |  |  |  |  |  |
| 3. | Đăng nhập | Button |  |  | Cho phép đăng nhập vào hệ thống |
| 4. | Quên mật khẩu | Button |  |  | Cho phép thay đổi mật khẩu |
| 5. | Xác thực | Button |  |  | Cho phép đăng nhập bằng khuôn mặt hoặc vân tay (đối với app mobile) |

![](media/image88.png)

*Màn hình nhập mã OTP*

Thông tin màn hình Xác thực bảo mật OTP

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1. | Mã OTP | Ký tự (6) | Có |  | Cho phép nhập. |
| ***Nút chức năng*** |  |  |  |  |  |
| 2. | Xác thực | Button |  |  | Hệ thống kiểm tra thông tin OTP và cho phép đăng nhập vào hệ thống |
| 3. | Huỷ | Button |  |  | Quay lại màn hình đăng nhập |
