---
title: "UC4.8.3: Xem báo cáo Tăng trưởng nhân sự theo tháng"
type: "use-case"
uc_number: "4.8.3"
---

### UC4.8.3: Xem báo cáo Tăng trưởng nhân sự theo tháng

| **Mục tiêu:** | Cho phép người dùng xem báo cáo tăng giảm nhân sự trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/Báo cáo* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Báo cáo hiển thị đúng dữ liệu theo tháng đã chọn. |
|  | Người dùng có thể tra cứu và kết xuất (export) báo cáo ra PDF/Excel. |
|  | Hệ thống ghi log thao tác xem (người dùng, thời gian, hành động). |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.8.3 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị báo cáo tăng trưởng nhân sự theo tháng (tính từ ngày đầu tiên của tháng đến ngày cuối cùng) |
|  | ❖ Nếu không có dữ liệu trong tháng → Hệ thống hiển thị thông báo "Không có dữ liệu đã chọn". |
|  | ❖ Cho phép lọc theo tháng. |

#### Mô tả màn hình

![](media/image35.png)

*Màn hình báo cáo*

![](media/image44.png)

*Bộ lọc tra cứu*
