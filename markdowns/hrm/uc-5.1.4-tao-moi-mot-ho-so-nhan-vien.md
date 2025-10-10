---
title: "UC 5.1.4: Tạo mới một Hồ sơ Nhân viên"
type: "use-case"
uc_number: "5.1.4"
---

### UC 5.1.4: Tạo mới một Hồ sơ Nhân viên

| **Mục tiêu:** | Cho phép người dùng tạo mới một Hồ sơ Nhân viên |
| **Tài khoản:** | Tài khoản được phân quyền Tạo mới với phân hệ con "Quản lý Hồ sơ Nhân viên" |
| **Sự kiện kích hoạt:** | Người dùng nhấn nút "Thêm mới" tại màn "Quản lý Hồ sơ Nhân viên" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị Hồ sơ nhân viên mới tạo ở màn hình danh sách "Hồ sơ nhân viên" |
|  | Hồ sơ nhân viên được tạo mới có thể: Xem chi tiết, Sửa, Xóa ( với TK được phân quyền tương ứng) |
|  | Hồ sơ được tạo mới ở màn hình "Nhân viên theo Role" và "Bảng chấm công" |
|  | Hệ thống tạo tài khoản nhân viên mới với thông tin tương ứng |

####  Luồng nghiệp vụ

![](media/image66.png)

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 5.1.4 | **Quy tắc Tạo mới Hồ sơ Nhân viên:** |
|  | - Người dùng nhấn nút "Thêm mới" và điền thông tin tương ứng của nhân viên: |
|  | - Nhấn "Lưu" để hệ thống xác thực thông tin |
|  | - Những trường thông tin cần xác thực: |
|  | - Mã nhân viên: không được trùng với mã nhân viên đã có (cả những Nhân viên đã xóa) |
|  | - Email: |
|  | - Đúng định dạng Email |
|  | - Không trùng với Email đã có |
|  | - Số điện thoại: đúng định dạng số điện thoại Việt Nam |
|  | - Số điện thoại ( liên hệ khẩn cấp): đúng định dạng số điện thoại Việt Nam |
|  | - Số CMND/CCCD: |
|  | - Không được trùng với nhân viên khác |
|  | - Là 9 hoặc 12 chữ số liền nhau (không có dấu cách) |
|  | - Nhân viên cần thuộc ít nhất một Khối hoặc một Phòng ban |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Tạo mới thành công |
|  | - Tạo một Nhân viên mới ở màn hình Danh sách Nhân viên theo Role với Vai trò có mã Vai trò là "VT002" |
|  | - Tạo nhân viên tương ứng ở màn Bảng chấm công |
|  | - Tạo một tài khoản nhân viên mới với thông tin: |
|  | - Tài khoản: (hệ thống tự tạo dựa tên Họ tên của nhân viên" |
|  | - Tên + họ tên đệm + \@MVL |
|  | - Ví dụ: **Tên** "Phạm Thu Trang" sẽ có **Tài khoản**: "TRANGPT@MVL" |
|  | - Nếu đã có Tài khoản TRANGPT@MVL, hệ thống tạo Tài khoản có STT tăng dần: TRANGPT1@MVL, TRANGPT2@MVL,\.... |
|  | - Mật khẩu: |
|  | - Hệ thống tự sinh một mã gồm 8 ký tự ngẫu nhiên |
|  | - Hệ thống gửi mật khẩu vào mail của nhân viên |
| --- | --- |
|  | - Quay về màn hình danh sách Hồ sơ Nhân viên với Hồ sơ mới đã được tạo |
|  | - Thêm thông tin tương ứng ở "Lịch sử công tác" |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ: Hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình

![](media/image79.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| Mã nhân viên | Textbox | Nhập "Mã nhân viên" tương ứng | Xác thực: không được trùng với mã nhân viên khác | Có |
| Họ tên | Textbox | Nhập "Họ tên" tương ứng | N/A | Có |
| Email | Textbox | Nhập "Email" tương ứng | Xác thực: đúng định dạng Email | Có |
| Số điện thoại | Textbox | Nhập "Chức vụ" tương ứng | \- Chỉ được điền số và dấu "+"\ | Không |
|  |  |  | - Xác thực: 10 chữ số bắt đầu bằng 0 hoặc 9 chữ số nếu bắt đầu từ +84 |  |
| Giới tính | Checkbox | Chọn giới tính cho nhân viên | \- Có 2 giới tính: Nam, Nữ | Có |
|  |  |  | \- Chỉ được chọn 1 trong 2 Checkbox |  |
| Ngày sinh | Date picker | Chọn Ngày sinh nhân viên | \- Nhấn để chọn thông tin Ngày/Tháng/Năm | Có |
|  |  |  | \- Điền ngày được chọn vào ô thông tin![](media/image69.png) |  |
| Địa chỉ | Textbox | Nhập "Địa chỉ" tương ứng | N/A | Không |
| Chi nhánh | Dropdownlist | Chọn "Chi nhánh" tương ứng | \- Nhấn sẽ dropdown danh sách Chi nhánh đã tạo | Có |
|  |  |  | \- Nếu đổi "Chi nhánh" bỏ chọn thông tin ở "Khối" và "Phòng ban" (nếu đã chọn) |  |
| Khối | Dropdownlist | Chọn "Khối" tương ứng | \- Dropdown hiển thị danh sách Khối theo Chi nhánh đã chọn và bổ sung một tùy chọn rỗng để cho phép bỏ chọn | Không |
|  |  |  | \- Trường thông tin bị disable đến khi chọn "Chi nhánh" |  |
|  |  |  | \- Nếu đổi "Khối", bỏ chọn thông tin "Phòng ban" (nếu đã chọn) |  |
| Phòng ban | Dropdownlist | Chọn "Phòng ban" tương ứng | \- Nhấn sẽ dropdown danh sách Phòng ban tương ứng với "Chi nhánh" và "Khối" đã chọn | Không |
|  |  |  | \- Trường thông tin bị disable đến khi chọn "Chi nhánh" |  |
|  |  |  | \- Nếu chưa chọn "Khối", hiển thị danh sách những "Phòng ban" không thuộc Khối nào |  |
| Loại hợp đồng | Dropdownlist | Chọn "Loại hợp đồng" tương ứng | \- Nhấn sẽ dropdown danh sách Loại hợp đồng đã tạo | Có |
|  |  |  | \- Chọn một Loại hợp đồng tương ứng |  |
| Chức vụ | Dropdownlist | Chọn "Chức vụ" tương ứng | \- Nhấn sẽ dropdown danh sách Chức vụ đã tạo | Có |
|  |  |  | \- Chọn một Chức vụ tương ứng |  |
| Ngày bắt đầu | Date picker | Chọn "Ngày bắt đầu" tương ứng | \- Nhấn để chọn thông tin Ngày/Tháng/Năm | Có |
|  |  |  | \- Điền ngày được chọn vào ô thông tin |  |
|  |  |  | ![](media/image51.png) |  |
| Trạng thái | Dropdownlist | Chọn "Trạng thái" tương ứng | Nhấn vào dropdown ra 3 Trạng thái:\ | Có |
|  |  |  | - Đang làm việc\ |  |
|  |  |  | - On-boarding\ |  |
|  |  |  | - Đã nghỉ việc |  |
|  |  |  | Chọn một trạng thái tương ứng |  |
| Ngày nghỉ việc | Date picker | Chọn "Ngày nghỉ việc" tương ứng | Chỉ hiển thị khi "Trạng thái" là "Đã nghỉ việc" | Có |
| Lý do nghỉ việc | Dropdownlist | Chọn "Lý do nghỉ việc" tương ứng | \- Chỉ hiển thị khi "Trạng thái" là "Đã nghỉ việc" | Có |
|  |  |  | \- Danh sách lý do nghỉ việc là: |  |
|  |  |  | - Đổi định hướng CV |  |
|  |  |  | - TV k đạt |  |
|  |  |  | - Sa thải |  |
|  |  |  | - Bận việc cá nhân |  |
|  |  |  | - Bỏ việc |  |
|  |  |  | - Không phù hợp |  |
|  |  |  | - Không đảm bảo Sức khỏe |  |
| Phần "Thông tin liên hệ khẩn cấp" có 2 trường thông tin: |  |  |  |  |
| Họ tên | Textbox | Nhập Họ tên người liên hệ khẩn cấp | N/A | Không |
| Số điện thoại | Textbox | Nhập SĐT người liên hệ khẩn cấp | \- Chỉ được điền số và dấu "+"\ | Không |
|  |  |  | - Xác thực: 10 chữ số bắt đầu bằng 0 hoặc 9 chữ số nếu bắt đầu từ +84 |  |
| Phần "Thông tin bổ sung" có 4 trường thông tin sau: |  |  |  |  |
| Số CMND/CCCD | Textbox | Nhập số CMND/CCCD nhân viên | Chỉ cho phép nhập ký tự số (0--9), dạng chuỗi liên tục, không chứa dấu cách hoặc ký tự khác | Không |
| Ngân hàng nhận lương | Textbox | Nhập Ngân hàng của nhân viên | N/A | Không |
| Số tài khoản | Textbox | Nhập số tài khoản của nhân viên | Chỉ cho phép nhập ký tự số (0--9), dạng chuỗi liên tục, không chứa dấu cách hoặc ký tự khác | Không |
| Mã số thuế | Textbox | Nhập mã số thuế của nhân viên | Chỉ cho phép nhập ký tự số (0--9), dạng chuỗi liên tục, không chứa dấu cách hoặc ký tự khác | Không |
| Lưu | Nút | Nhấn để xác thực thông tin nhân viên | Xác thực những trường thông tin cần đúng định dạng và bắt buộc điền |  |
| Hủy | Nút | Nhấn để quay về màn hình danh sách hồ sơ | N/A |  |
