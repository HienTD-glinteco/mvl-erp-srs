---
title: "UC4.7.8: Gửi mail cho ứng viên"
type: "use-case"
uc_number: "4.7.8"
---

### UC4.7.8: Gửi mail cho ứng viên

| **Mục tiêu:** | Cho phép người dùng gửi mail cho các ứng viên được tạo theo lịch phỏng vấn. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng tích chọn các ứng viên và ấn (click) vào icon Gửi mail trong Màn hình Quản lý lịch phỏng vấn. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
|  | Ứng viên đã có thông tin email hợp lệ trong hệ thống. |
|  | Nội dung email được chọn từ mẫu (template) có sẵn. |
| **Kết quả bắt buộc:** | Email được gửi thành công đến ứng viên. |
|  | Lịch sử gửi mail được lưu trong hệ thống (thời gian gửi). Hiển thị trên màn hình xem chi tiết / chỉnh sửa lịch phỏng vấn. |

####  Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.7.8 | **Sending Mail Rules:** |
|  | ❖ Hệ thống cho phép HR tích chọn ứng viên hoặc danh sách ứng viên cần gửi email. |
|  | ❖ Hệ thống mặc định nội dung mail là tiếng Việt. |
|  | ❖ Hệ thống phải kiểm tra định dạng email hợp lệ trước khi gửi. |
|  | ❖ Người dùng chọn loại mẫu mail muốn gửi, có thể thay đổi nội dung và danh sách ứng viên đã chọn. |
|  | ❖ Nội dung email hỗ trợ Unicode (đa ngôn ngữ, có dấu). |
|  | ❖ Hệ thống đảm bảo bảo mật thông tin người nhận (không hiển thị email của ứng viên khác khi gửi nhiều người). |
|  | ❖ Nội dung mail dựa theo template mẫu: |
|  | ❖ Hệ thống ghi nhận những lần gửi thành công vả hiển thị lần gửi thành công gần nhất. |

#### Mô tả màn hình

![](media/image52.png)
