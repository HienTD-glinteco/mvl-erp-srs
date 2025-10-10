---
title: "UC 5.4.3: Tạo mới một Người phụ thuộc của nhân viên"
type: "use-case"
uc_number: "5.4.3"
---

### UC 5.4.3: Tạo mới một Người phụ thuộc của nhân viên

| **Mục tiêu:** | Cho phép người dùng tạo mới một Người phụ thuộc của Nhân viên |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền Tạo mới tại "Quản lý Người phụ thuộc" |
| **Sự kiện kích hoạt:** | Người dùng nhấn "Thêm mới" tại màn "Quản lý Người phụ thuộc" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị Người phụ thuộc tạo mới ở màn hình danh sách |
|  | Người phụ thuộc được tạo mới có thể: Xem chi tiết, Sửa, Xóa ( với TK được phân quyền tương ứng) |
|  | Ở màn hình "Chi tiết hồ sơ nhân viên", thêm thông tin mới tương ứng |

#### Luồng nghiệp vụ

![](media/image128.png)

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 5.4.3 | **Quy tắc Tạo mới Quan hệ Người phụ thuộc:** |
|  | - Người dùng nhấn nút "Thêm mới" và điền thông tin tương ứng của nhân viên: |
|  | - Nhấn "Lưu" để hệ thống xác thực thông tin |
|  | - Những trường thông tin cần xác thực: |
|  | - Số CMND/CCCD: Là 9 hoặc 12 chữ số liền nhau (không có dấu cách) |
|  | - File chứng chỉ: dung lượng ≤ 10 MB |
|  | - Những trường thông tin Bắt buộc điền thông tin |
|  | - Nếu thông tin "hợp lệ: |
|  | - Hệ thống báo Tạo mới thành công |
|  | - Hiển thị thêm thông tin tương ứng ở Tab "Người phụ thuộc" ở màn xem chi tiết "Hồ sơ nhân viên" |
|  | - Quay về màn hình danh sách Bằng cấp/ Chứng chỉ với Bằng cấp/ Chứng chỉ mới đã được tạo |
|  | - Nếu thông tin "không hợp lệ": |
|  | - Báo lỗi tương ứng với những ô thông tin không hợp lệ |
|  | - Những ô thông tin không hợp lệ hiển thị viền đỏ |
|  | - Khi người dùng nhấn vào trường thông tin không hợp lệ, hệ thống báo lỗi tương ứng với thông tin đó. |
|  | - Hệ thống dẫn màn hình đến ô thông tin không hợp lệ đầu tiên |

#### Mô tả màn hình 

![](media/image131.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Tên nhân viên | Trường dữ liệu + Nút | Chọn "Tên nhân viên" | \- Nhấn để hiển thị [[màn hình "Pop-up tìm kiếm nhân viên"]{.underline}](#sos-màn-hình-pop-up-tìm-kiếm-nhân-viên-nhapsing-sẽ-có-update) | Có |
|  |  |  | \- Fill thông tin nhân viên được chọn tương ứng |  |
| Mã nhân viên | Trường dữ liệu + Nút | Chọn "Mã nhân viên" | \- Nhấn để hiển thị [[màn hình "Pop-up tìm kiếm nhân viên"]{.underline}](#sos-màn-hình-pop-up-tìm-kiếm-nhân-viên-nhapsing-sẽ-có-update) | Có |
|  |  |  | \- Fill thông tin nhân viên được chọn tương ứng |  |
| Tên người phụ thuộc | Textbox | Điền "Tên người thân" | N/A | Có |
| Mối quan hệ | Dropdownlist | Chọn "Mối quan hệ" tương ứng | Nhấn sẽ dropdown danh sách mối quan hệ là: | Có |
|  |  |  | [Con, Vợ, Chồng, Khác, Anh, Ông, Cha, Mẹ, Bà, Chị, Em]{.mark} |  |
| Ngày sinh | Date picker | [Chọn "Ngày sinh" tương ứng]{.mark} | Nhấn hiển thị giao diện chọn Ngày sinh | Không |
|  |  |  | ![](media/image74.png) |  |
| Số CMND/CCCD | Textbox | Điền "Số CMND/CCCD" | Chỉ cho phép nhập ký tự số (0--9), dạng chuỗi liên tục, không chứa dấu cách hoặc ký tự khác | Không |
| File đính kèm | File Upload | Tải lên lên File Bằng cấp tương ứng | \- Nhấn để hiển thị giao diện chọn file từ thiết bị người dùng\ | Không |
|  |  |  | - Dung lượng File ≤ 10 MB |  |
|  |  |  | \- Khi File được upload thành công, hiển thị Tên File vừa upload |  |
|  |  |  | \- Nếu up file khi có một File up từ trước, thay thế file cũ |  |
| Ghi chú | Textbox | Điền "Ghi chú" tương ứng | N/A | Không |
| Tạo mới | Nút | Nhấn để xác thực các trường thông tin | Xác thực trường thông tin cần đúng định dạng và trường thông tin bắt buộc điền | Có |
| Hủy | Nút | Nhấn để về màn danh sách Bằng cấp/Chứng chỉ | N/A | Có |
