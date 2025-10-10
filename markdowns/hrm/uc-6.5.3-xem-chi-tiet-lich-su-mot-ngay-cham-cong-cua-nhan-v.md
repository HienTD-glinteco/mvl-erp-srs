---
title: "UC 6.5.3: Xem chi tiết Lịch sử một ngày chấm công của Nhân viên"
type: "use-case"
uc_number: "6.5.3"
---

### UC 6.5.3: Xem chi tiết Lịch sử một ngày chấm công của Nhân viên

  --------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng Xem chi tiết một Ngày chấm công của Nhân viên
  --------------------------- ----------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền Xem chi tiết tại danh sách "Bảng chấm công"

  **Sự kiện kích hoạt:**      Người dùng nhấn vào ô của Ngày chấm công của nhân viên tại màn "Bảng chấm công"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống hiển thị màn hình "Chi tiết" thông tin của Ngày chấm công của nhân viên
  --------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 6.5.3 | **Quy tắc Xem chi tiết một ngày chấm công của nhân viên:** |
|  | - Người dùng ở màn hình "Bảng chấm công" -\> nhấn vào ô của Ngày chấm công của nhân viên tương ứng |
|  | - Hệ thống hiển thị màn hình xem thông tin chi tiết của Ngày chấm công tương ứng |

#### Mô tả màn hình

![](media/image45.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Logic nghiệp vụ** |
| 1 | Tên nhân viên | Trường dữ liệu |  | Hiển thị "Tên" của nhân viên tương ứng |
| 2 | Ngày chấm công | Trường dữ liệu |  | \- Hiển thị "Ngày chấm công" tương ứng |
|  |  |  |  | \- Hiển thị dạng: "Phút/Giờ" |
| 3 | Trạng thái chấm công | Trường dữ liệu |  | \- Hiển thị "Trạng thái chấm công" của ngày tương ứng |
|  |  |  |  | \- Hiển thị theo "Quy tắc nghiệp vụ" của Trạng thái chấm công |
| 4 | Đề xuất được duyệt | Trường dữ liệu |  | Hiển thị những đề xuất đã được phòng nhân sự duyệt cho ngày |
| 5 | Giờ bắt đầu | Trường dữ liệu |  | \- Hiển thị "Giờ chấm công" đầu tiên trong ngày |
|  |  |  |  | \- Hiển thị dạng: "Phút/Giờ" |
| 6 | Giờ kết thúc | Trường dữ liệu |  | \- Hiển thị "Giờ chấm công" cuối cùng trong ngày |
|  |  |  |  | \- Hiển thị dạng: "Phút/Giờ" |
| 7 | Thời gian làm việc | Trường dữ liệu |  | \- Công thức là |
| --- | --- | --- | --- | --- |
|  |  |  |  | \- Hiển thị số giờ: 2 số sau dấu thập phân |
| 8 | Ngày công | Trường dữ liệu |  | \- Tính bằng: (Thời gian làm việc) / 8 |
|  |  |  |  | \- Nếu "Ngày công" khác 1: |
|  |  |  |  | \+ Hiển thị dạng số thập phân (2 chữ số sau dấu phẩy) |
| Hiển thị danh sách những lần chấm công trong ngày của nhân viên |  |  |  |  |
| 9 | Giờ chấm công | Trường dữ liệu |  | Hiển thị "Giờ" của lần chấm công tương ứng |
| 10 | Phương thức chấm công | Trường dữ liệu |  | \- Hiển thị "Phương thức" của lần chấm công tương ứng |
|  |  |  |  | \- Danh sách phương thức: |
|  |  |  |  | \+ Vân tay |
|  |  |  |  | \+ Wi-fi |
|  |  |  |  | \+ GPS |
|  |  |  |  | \+ Hình ảnh |
| Khi nhấn vào những lần chấm công, hiển thị Vị trí GPS hoặc Hình ảnh Check-in của lần |  |  |  |  |
| 11 | Vị trí GPS Check-in | Map |  | Hiển thị vị trí GPS của lần chấm công tương ứng |
| 12 | Hình ảnh Check-in | Hình ảnh |  | Hiển thị Hình ảnh upload của lần chấm công tương ứng |
| Hiển thị Lịch sử chỉnh sửa thông tin của Ngày chấm công tương ứng |  |  |  |  |
| 13 | Nội dung thay đổi | Trường dữ liệu |  | \- Có những trường hợp thay đổi nội dung là: |
|  |  |  |  | \+ Đề xuất được duyệt |
|  |  |  |  | \+ Giờ bắt đầu |
|  |  |  |  | \+ Giờ kết thúc |
| 14 | Giá trị ban đầu | Trường dữ liệu |  | \- Với "Đề xuất được duyệt", có 2 trường hợp: |
|  |  |  |  | \+ Được duyệt |
|  |  |  |  | \+ Không được duyệt |
|  |  |  |  | \- Với "Giờ bắt đầu/Giờ kết thúc", hiển thị |
|  |  |  |  | \+ Thời gian trước khi |
| 15 | Giá trị mới | Trường dữ liệu |  |  |
| 16 | Người chỉnh sửa | Trường dữ liệu |  |  |
| 17 | Thời gian chỉnh sửa | Trường dữ liệu |  |  |
| 18 | Chỉnh sửa | Nút |  |  |

#### 
