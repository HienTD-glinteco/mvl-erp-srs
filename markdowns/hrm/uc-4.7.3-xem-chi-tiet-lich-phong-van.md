---
title: "UC4.7.3: Xem chi tiết lịch phỏng vấn"
type: "use-case"
uc_number: "4.7.3"
---

### UC4.7.3: Xem chi tiết lịch phỏng vấn

| **Mục tiêu:** | Cho phép người dùng xem chi tiết thông tin lịch phỏng vấn trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng click vào icon Xem chi tiết trong Màn hình Quản lý lịch phỏng vấn. |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Người dùng xem được chi tiết lịch phỏng vấn đúng với bản ghi đã chọn; hệ thống đảm bảo hiển thị phiên bản dữ liệu mới nhất. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.7.3 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị màn hình chi tiết: |
|  | o Hiển thị tương ứng với dòng NSD thực hiện thao tác. |
|  | ❖ Cho phép thêm hoặc xoá từng ứng viên/ từng người phỏng vấn trong danh sách. |
|  | ❖ Khi thêm mới ứng viên hiển thị popup màn hình cho phép chọn mã ứng viên - họ tên và nhập thời gian phỏng vấn. Hiển thị cảnh báo nếu thời gian nhập không trong khoảng thời gian phỏng vấn (ở phần thông tin chung) |
|  | ❖ Khi thêm mới người phỏng vấn hiển thị popup màn hình cho phép chọn mã nhân viên - họ tên và nhập thời gian phỏng vấn. |

#### Mô tả màn hình

![](media/image15.png)

*Xem chi tiết lịch phỏng vấn*

![](media/image7.png)

*Màn hình thêm mới ứng viên*

![](media/image48.png)

*Màn hình thêm mới người phỏng vấn*

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Ràng buộc** |
| --- | --- | --- | --- | --- |
| ***Thông tin hiển thị*** |  |  |  |  |
| 1\. | Lịch phỏng vấn | Ký tự (100) |  | Hiển thị theo CSDL |
| 2\. | Đề nghị tuyển dụng | Ký tự (100) |  | Hiển thị theo CSDL |
| 3\. | Vị trí phỏng vấn | Ký tự (50) |  | Hiển thị theo CSDL |
| 4\. | Loại phỏng vấn | Radio button |  | Hiển thị theo CSDL |
| 5\. | Địa điểm | Ký tự (200) |  | Hiển thị theo CSDL |
| 6\. | Thời gian từ | DD/MM/YYYY |  | Hiển thị theo CSDL |
| 7\. | Thời gian đến | DD/MM/YYYY |  | Hiển thị theo CSDL |
| 8\. | Ghi chú | Ký tự (500) |  | Hiển thị theo CSDL |
| ***Thông tin chi tiết danh sách ứng viên*** |  |  |  |  |
| 9\. | Mã ứng viên | Dropdown |  | Cho phép thêm từ danh sách (màn hình popup) |
| 10\. | Họ và tên | Dropdown |  | Cho phép thêm từ danh sách (màn hình popup) |
| 11\. | CCCD | Ký tự (12) |  | Hiển thị tương ứng với ứng viên đã chọn. |
| 12\. | Số điện thoại | Ký tự (10) |  | Hiển thị tương ứng với ứng viên đã chọn. |
| 13\. | Email | Ký tự (100) |  | Hiển thị tương ứng với ứng viên đã chọn. |
| 14\. | Thời gian phỏng vấn | HH:MM:SS - DD/MM/YYYY |  | Cho phép nhập |
| 15\. | Thời gian gửi mail lần cuối | HH:MM:SS - DD/MM/YYYY |  | Hiển thị theo CSDL. Hiển thị theo lần gửi mail cuối cùng. |
| ***Thông tin chi tiết danh sách người phỏng vấn*** |  |  |  |  |
| 16\. | Mã nhân viên | Ký tự (10) |  | Cho phép chọn trong danh sách nhân viên. (màn hình popup) |
| 17\. | Họ và tên | Ký tự (100) |  | Cho phép chọn trong danh sách nhân viên. (màn hình popup) |
| 18\. | Chức vụ | Ký tự (50) |  | Hiển thị tương ứng theo mã nhân viên |
| 19\. | Chi nhánh | Ký tự (50) |  | Hiển thị tương ứng theo mã nhân viên |
| 20\. | Khối | Ký tự (50) |  | Hiển thị tương ứng theo mã nhân viên |
| 21\. | Phòng ban | Ký tự (50) |  | Hiển thị tương ứng theo mã nhân viên |
| ***Nút chức năng*** |  |  |  |  |
| 22\. | Quay lại | Button |  | Cho phép quay lại màn hình Quản lý |
| 23\. | Chỉnh sửa | Button |  | Cho phép chỉnh sửa các thông tin lịch |
| 24\. | Gửi mail | Button |  | Cho phép gửi mail thông báo tới danh sách ứng viên được tích chọn |
| 25\. | Xoá | Button |  | Cho phép xoá từng ứng viên, từng người phỏng vấn ở màn hình danh sách. |
