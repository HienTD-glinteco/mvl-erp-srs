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

1.  Phân hệ con "Quản lý báo cáo"
    -----------------------------

    1.  ### UC4.8.1: Xem báo cáo Tăng trưởng nhân sự theo tuần

| **Mục tiêu:** | Cho phép người dùng xem báo cáo tăng giảm nhân sự trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Báo cáo/Báo cáo tăng trưởng nhân sự* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Báo cáo hiển thị đúng dữ liệu theo tuần đã chọn. |
|  | Người dùng có thể tra cứu và kết xuất (export) báo cáo ra PDF/Excel. |
|  | Hệ thống ghi log thao tác xem (người dùng, thời gian, hành động). |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.8.1 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị báo cáo tăng trưởng nhân sự theo tuần dạng biểu đồ. Báo cáo tổng hợp dữ liệu từ Thứ 2 đến Thứ 7. |
|  | ❖ Nếu biểu đồ không có dữ liệu→ Hệ thống hiển thị thông báo "Không có dữ liệu đã chọn". Nếu cột không có dữ liệu hiển thị số lượng 0. |
|  | ❖ Cho phép lọc theo tuần. |

#### Mô tả màn hình

![](media/image70.png)

*Màn hình báo cáo*

![](media/image44.png)

*Bộ lọc tra cứu*
