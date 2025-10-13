---
title: "UC4.8.11: Xem báo cáo Thống kê số lượng ứng viên trúng tuyển"
type: "use-case"
uc_number: "4.8.11"
---

### UC4.8.11: Xem báo cáo Thống kê số lượng ứng viên trúng tuyển

| **Mục tiêu:** | Cho phép người dùng xem báo cáo số lượng tuyển dụng trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Báo cáo/Báo cáo Thống kê số lượng ứng viên trúng tuyển.* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Báo cáo hiển thị đúng và đầy đủ dữ liệu theo các bộ lọc tìm kiếm. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.8.11 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị báo cáo theo mẫu báo cáo. |
|  | ❖ Báo cáo được hiển thị theo từng tuần (tính từ thứ 2 đến thứ 7) hoặc theo tháng (trong năm) |
|  | ❖ Cho phép lọc theo thời gian từ ngày - tới ngày, chi nhánh, khối, phòng ban |
|  | ❖ Nếu không có dữ liệu → Hệ thống hiển thị thông báo "Không có dữ liệu đã chọn". |

#### Mô tả màn hình

![](media/image9.png)

*Màn hình báo cáo (theo tháng)*

![](media/image33.png)

*Màn hình báo cáo (theo tuần)*
