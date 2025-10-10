---
title: "UC1.1.7: Xem chi tiết thao tác người dùng"
type: "use-case"
uc_number: "1.1.7"
---

### UC1.1.7: Xem chi tiết thao tác người dùng

| **Mục tiêu:** | Cho phép người dùng xem chi tiết toàn bộ các thao tác của người dùng trên hệ thống, nhằm mục đích kiểm tra, giám sát và phục vụ truy vết khi cần. |
| --- | --- |
| **Tác nhân:** | Tài khoản được phân quyền. |
| **Sự kiện kích hoạt:** | Người dùng click vào xem chi tiết ở chức năng "Lịch sử thao tác người dùng". |
| **Điều kiện tiên quyết:** | Người dùng đã đăng nhập hợp lệ.\ |
|  | Hệ thống có cơ chế logging (ghi log) hoạt động ổn định. |
| **Kết quả bắt buộc:** | Dữ liệu nhạy cảm luôn bị mask, raw payload chỉ xem khi role được phép. |
|  | Hiển thị chi tiết các thông tin lưu trữ của dòng dữ liệu thực hiện thao tác. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 1.1.7 | **User Action Tracking Rules:** |
|  | - Dữ liệu nhạy cảm (mật khẩu, token) không lưu ở trường hiển thị; chỉ lưu trạng thái đã thay đổi hoặc dữ liệu được mask. |
|  | - Giao diện danh sách hiển thị các bản ghi log theo thứ tự thời gian giảm dần. |
|  | - Đối với các hành động Cập nhật (sửa): hiển thị dạng table các trường dữ liệu thay đổi với nội dung trước khi sửa và sau khi sửa. |
|  | - Đối với các hành động khác: hiển thị dạng textbox. |

#### Mô tả màn hình

![](media/image114.png)

*Màn hình xem chi tiết thao tác (Loại hành động: cập nhật thông tin)*

![](media/image116.png)

*Màn hình xem chi tiết thao tác (Loại hành động khác)*

Thông tin hiển thị:

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 1. | Mã nhân viên | Ký tự (10) |  |  | Hiển thị theo CSDL |
| 2. | Họ và tên | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 3. | Hành động | Ký tự (200) |  |  | Hiển thị theo CSDL |
| 4. | Đối tượng tác động | Ký tự (200) |  |  | Hiển thị theo CSDL |
| 5. | Thời gian | DD/MM/YYYY - hh:mm:ss |  |  | Hiển thị theo CSDL |
| 6. | URL | Ký tự (1000) |  |  | Hiển thị theo CSDL. |
|  |  |  |  |  | Cho phép người dùng click vào hiển thị đối tượng. Đối với các hành động là đăng nhập, đăng xuất, xóa không cho phép click |
| 7. | Nội dung thay đổi | Ký tự (1000) |  |  | Hiển thị theo CSDL. |
|  |  |  |  |  | Hiển thị theo từng loại hành động. |
| 8. | IP | Ký tự (40) |  |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 9\. | Quay lại | Button |  |  | Cho phép quay lại màn hình danh sách |
