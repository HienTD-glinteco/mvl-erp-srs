---
title: "UC 5.5.3: Xem lịch sử công tác của một nhân viên: tất cả các sự kiện liên quan"
type: "use-case"
uc_number: "5.5.3"
---

### UC 5.5.3: Xem lịch sử công tác của một nhân viên: tất cả các sự kiện liên quan

| **Mục tiêu:** | Cho phép người dùng xem chi tiết Lịch sử công tác của Nhân viên |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền cho xem phân hệ con "Lịch sử công tác" |
| **Sự kiện kích hoạt:** | Người dùng nhấn vào thanh thông tin của một Nhân viên tại màn hình danh sách "Lịch sử công tác" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị "Lịch sử công tác" của nhân viên tương ứng |
|  | Hệ thống hiển thị "Lịch sử công tác" đúng với mỗi lần Filter thông tin |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 5.5.3 | **Quy tắc Xem màn hình Chi tiết Lịch sử công tác của Nhân viên:** |
|  | - Người dùng ở màn hình "Lịch sử công tác" -\> nhấn vào một thanh thông tin Nhân viên |
|  | - Hệ thống hiển thị màn hình xem thông tin Chi tiết Lịch sử công tác của Nhân viên tương ứng |
|  | - Có 3 trường hợp của Lịch sử công tác và đều bắt đầu từ việc đổi thông tin tương ứng ở [[phần Quản lý Hồ sơ nhân viên]{.underline}](#uc-5.1.6-chỉnh-sửa-thông-tin-của-một-hồ-sơ-nhân-viên) |
|  | - **Đổi Trạng thái:** cách hiển thị |
|  | - TH đổi thông tin trạng thái của hồ sơ: |
|  | - **Từ trạng thái: (Trạng thái cũ) -\> (Trạng thái mới)** |
|  | - Nếu đổi sang trạng thái **"Đã nghỉ việc"**, lưu thông tin: **Từ trạng thái: (Trạng thái cũ) -\> Đã nghỉ việc (Ngày nghỉ việc) + (Lý do nghỉ việc)** |
|  | - Trường hợp Hồ sơ tạo từ danh sách Ứng viên đỗ phỏng vấn, hiển thị : |
|  | - **Từ trạng thái: Qua phỏng vấn -\> Onboarding** |
|  | - Trường hợp [[hồ sơ nhân viên được tạo mới]{.underline}](#uc-5.1.4-tạo-mới-một-hồ-sơ-nhân-viên), hiển thị: |
|  | - **Tạo mới với trạng thái: (Trạng thái khi tạo mới)** |
|  | - **Trường hợp Nhân viên quay lại làm việc, hiển thị:** |
|  | - **Quay lại làm việc: (Ngày bắt đầu quay lại làm việc)** |
|  | - **Đổi Chức vụ:** cách hiển thị |
|  | - TH đổi thông tin Chức vụ của hồ sơ: |
|  | - **" Đổi chức vụ: (Chức vụ cũ) -\> (Chức vụ mới) "** |
|  | - Trường hợp [[hồ sơ nhân viên được tạo mới]{.underline}](#uc-5.1.4-tạo-mới-một-hồ-sơ-nhân-viên), hiển thị: |
|  | - **"Tạo mới với chức vụ: (Chức vụ khi tạo mới) "** |
|  | - **Điều chuyển tổ chức:** cách hiển thị |
|  | - TH đổi Chi nhánh/Khối/Phòng ban của hồ sơ: (chỉ hiển thị một trong 3 Chi nhánh/Khối/Phòng ban với mỗi Lịch sử công tác) |
|  | - **" Điều chuyển Chi nhánh/Khối/Phòng ban: ( tổ chức cũ) -\> (tổ chức mới) "** |
|  | - Trường hợp [[hồ sơ nhân viên được tạo mới]{.underline}](#uc-5.1.4-tạo-mới-một-hồ-sơ-nhân-viên), hiển thị: |
|  | - **"Tạo mới với Chi nhánh/Khối/Phòng ban: (Tên Chi nhánh/Khối/Phòng ban khi tạo mới) "** |

#### Mô tả màn hình

![](media/image107.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Mã NV | Trường dữ liệu | Hiển thị "Mã NV" tương ứng | Read-only | Có |
| Họ tên | Trường dữ liệu | Hiển thị "Họ tên" tương ứng | Read-only | Có |
| Trạng thái | Trường dữ liệu | Hiển thị "Trạng thái" tương ứng | Có 3 trạng thái + màu hiển thị:\ | Có |
|  |  |  | - "Đang làm việc": màu xanh lá\ |  |
|  |  |  | - "On-boarding": màu vàng\ |  |
|  |  |  | - "Đã nghỉ việc": màu đỏ |  |
| Chi nhánh/Khối/Phòng ban | Trường dữ liệu | Hiển thị "Chi nhánh/Khối/Phòng ban" tương ứng | Hiển thị lần lượt theo thứ tự Chi nhánh/Khối/Phòng ban | Có |
| Chức vụ | Trường dữ liệu | Hiển thị "Chức vụ" tương ứng | Read-only | Có |
| Ngày vào làm | Trường dữ liệu | Hiển thị "Ngày vào làm" tương ứng | Read-only | Có |
| Đổi trạng thái | Checkbox | Nhấn để lọc tìm kiếm Lịch sử công tác | Check/Uncheck để lọc/ không lọc những Lịch sử công tác của "Đổi trạng thái" | Có |
| Điều chuyển tổ chức | Checkbox | Nhấn để lọc tìm kiếm Lịch sử công tác | Check/Uncheck để lọc/ không lọc những Lịch sử công tác của "Điều chuyển tổ chức" | Có |
| Đổi chức vụ | Checkbox | Nhấn để lọc tìm kiếm Lịch sử công tác | Check/Uncheck để lọc/ không lọc những Lịch sử công tác của "Đổi chức vụ" | Có |
| Tiếp theo là **Từng ngày** có sự kiện trong Lịch sử công tác. Với từng **Ngày tương ứng** sẽ có hiển thị cụ thể thông tin từng Lịch sử công tác như sau: |  |  |  |  |
| Đổi trạng thái | Trường dữ liệu | Hiển thị thay đổi của Lịch sử công tác tương ứng | một Ngày có thể hiển thị nhiều thay đổi khác nhau của nhân viên | Có |
| Đổi chức vụ |  |  |  |  |
| Điều chuyển tổ chức |  |  |  |  |
| Chi tiết thông tin thay đổi | Trường dữ liệu | Hiển thị thông tin thay đổi chi tiết của Lịch sử công tác | Hiển thị đúng theo từng trường hợp của Lịch sử công tác | Có |
| Tạo bởi | Trường dữ liệu | Hiển thị người tác động sự kiện | Cách hiển thị: " Tạo bởi + ( Mã nhân viên + Tên nhân viên) " | Có |
