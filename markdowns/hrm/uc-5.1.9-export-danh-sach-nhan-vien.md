---
title: "UC 5.1.9: Export danh sách Nhân viên"
type: "use-case"
uc_number: "5.1.9"
---

### UC 5.1.9: Export danh sách Nhân viên

  -----------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng Export File Hồ sơ Nhân viên
  --------------------------- -------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền Export phân hệ con "Quản lý Hồ sơ Nhân viên"

  **Sự kiện kích hoạt:**      Người dùng nhấn nút Export tại màn hình danh sách Hồ sơ Nhân viên

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản có phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống tải về thiết bị người dùng danh sách "Hồ sơ nhân viên" đang được lọc
  -----------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 5.1.9 | **Quy tắc Export danh sách Nhân viên:** |
|  | - Người dùng Lọc màn hình danh sách hồ sơ nhân viên để hiển thị danh sách Hồ sơ muốn Export + Nhấn nút Export |
|  | - Hệ thống tải về thiết bị người dùng File Danh sách hồ sơ nhân viên với những thông tin đang được lọc, tìm kiếm tại thời điểm tải về |

#### Mô tả màn hình

![](media/image127.png)

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**   **Kiểu dữ liệu**   **Mô tả**                                  **Logic nghiệp vụ**                                                                                   **Bắt buộc**
  --------------- ------------------ ------------------------------------------ ----------------------------------------------------------------------------------------------------- --------------
  Export          Nút                Nhấn để tải về Danh sách Hồ sơ nhân viên   Danh sách hồ sơ tải về là danh sách với những thông tin đang lọc trên màn hình tại thời điểm tải về   

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
