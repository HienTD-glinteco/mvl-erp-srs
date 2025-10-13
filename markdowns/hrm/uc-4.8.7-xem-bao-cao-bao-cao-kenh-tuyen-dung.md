---
title: "UC4.8.7: Xem báo cáo Báo cáo kênh tuyển dụng"
type: "use-case"
uc_number: "4.8.7"
---

### UC4.8.7: Xem báo cáo Báo cáo kênh tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xem báo cáo kênh tuyển dụng trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Báo cáo/Báo cáo kênh tuyển dụng.* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Báo cáo hiển thị đúng dữ liệu. |
|  | Người dùng có thể tra cứu và kết xuất (export) báo cáo ra PDF/Excel. |
|  | Hệ thống ghi log thao tác xem (người dùng, thời gian, hành động). |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.8.7 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị báo cáo theo các kênh tuyển dụng theo từng phòng trong tháng. |
|  | ❖ Nếu không có dữ liệu trong tháng → Hệ thống hiển thị thông báo "Không có dữ liệu đã chọn". |
|  | ❖ Báo cáo chi tiết theo danh sách các phòng. Được gom và tính tổng theo Khối và Chi nhánh. |
|  | ❖ Báo cáo được sắp xếp theo các Khối kinh doanh trước rồi mới đến Khối hỗ trợ. |
|  | ❖ Đối với các phòng, khối, chi nhánh không phát sinh dữ liệu sẽ không được hiển thị. |
|  | ❖ Chỉ hiển thị các kênh tuyển dụng có phát sinh dữ liệu. |
|  | ❖ Dữ liệu được lấy dựa theo thông tin Ứng viên có trạng thái Đã nhận việc theo từng kênh tuyển dụng trong tháng. |
|  | ❖ Cho phép lọc theo thời gian từ ngày - tới ngày, chi nhánh, khối, phòng ban. |

#### Mô tả màn hình

![](media/image62.png)

*Màn hình báo cáo*

![](media/image60.png)

*Màn hình bộ lọc báo cáo*
