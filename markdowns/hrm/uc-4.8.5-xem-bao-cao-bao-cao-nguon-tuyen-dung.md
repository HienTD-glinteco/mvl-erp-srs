---
title: "UC4.8.5: Xem báo cáo Báo cáo nguồn tuyển dụng"
type: "use-case"
uc_number: "4.8.5"
---

### UC4.8.5: Xem báo cáo Báo cáo nguồn tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xem báo cáo nguồn tuyển dụng trên hệ thống. |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Báo cáo/Báo cáo nguồn tuyển dụng.* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Báo cáo hiển thị đúng dữ liệu. |
|  | Người dùng có thể tra cứu và kết xuất (export) báo cáo ra PDF/Excel. |
|  | Hệ thống ghi log thao tác xem (người dùng, thời gian, hành động). |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 4.8.5 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị báo cáo theo các nguồn tuyển dụng theo từng phòng trong tháng. |
|  | ❖ Nếu không có dữ liệu trong tháng → Hệ thống hiển thị thông báo "Không có dữ liệu đã chọn". |
|  | ❖ Cho phép kéo thả các cột dữ liệu trong báo cáo. |
|  | ❖ Báo cáo chi tiết theo danh sách các phòng. Được gom và tính tổng theo Khối và Chi nhánh. |
|  | ❖ Báo cáo được sắp xếp theo các Khối kinh doanh trước rồi mới đến Khối hỗ trợ. |
|  | ❖ Đối với các phòng, khối, chi nhánh không phát sinh dữ liệu sẽ không được hiển thị. |
|  | ❖ Chỉ hiển thị các nguồn tuyển dụng có phát sinh dữ liệu. |
|  | ❖ Dữ liệu được lấy dựa theo thông tin Ứng viên có trạng thái Đã nhận việc theo từng nguồn tuyển dụng trong tháng. |
|  | ❖ Cho phép lọc theo tháng. |
| --- | --- |
