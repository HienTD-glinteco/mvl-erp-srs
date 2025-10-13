---
title: "UC4.8.1: Xem báo cáo Tăng trưởng nhân sự theo tuần"
type: "use-case"
uc_number: "4.8.1"
---

### UC4.8.1: Xem báo cáo Tăng trưởng nhân sự theo tuần

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
