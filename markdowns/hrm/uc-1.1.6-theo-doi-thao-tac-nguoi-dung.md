---
title: "UC1.1.6: Theo dõi thao tác người dùng"
type: "use-case"
uc_number: "1.1.6"
---

### UC1.1.6: Theo dõi thao tác người dùng

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Ghi nhận và lưu trữ toàn bộ các thao tác của người dùng trên hệ thống, nhằm mục đích kiểm tra, giám sát và phục vụ truy vết khi cần.
  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------
  **Tác nhân:**               Người dùng: Thực hiện thao tác trên hệ thống.\
                              Người dùng được phân quyền: Xem hoặc truy vấn nhật ký thao tác.

  **Sự kiện kích hoạt:**      Người dùng chọn chức năng "Lịch sử thao tác người dùng".

  **Điều kiện tiên quyết:**   Người dùng đã đăng nhập hợp lệ.\
                              Hệ thống có cơ chế logging (ghi log) hoạt động ổn định.

  **Kết quả bắt buộc:**       Thao tác người dùng được lưu trữ vào nhật ký (log).\
                              Thông tin log có thể được tra cứu và truy xuất khi cần.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 1.1.6 | **User Action Tracking Rules:** |
|  | - Tất cả thao tác (login, logout, thêm/sửa/xóa dữ liệu, thay đổi mật khẩu, phân quyền) phải được ghi log. |
|  | - Các trường thông tin cần lưu: Mã nhân viên, Họ tên, Hành động, Đối tượng tác động, Thời gian, URL, Nội dung thay đổi, IP. |
|  | - Thông tin được hiển thị theo thao tác có thời gian gần nhất. |
|  | - Dữ liệu log không được chỉnh sửa thủ công, chỉ có thể tra cứu và xem. |
|  | - Thời gian lưu trữ log tối đa là 12 tháng. |
|  | - Chỉ người có quyền Admin mới được xem toàn bộ log. Các cấp trên được xem thông tin của họ và các nhân viên trực thuộc. (theo Chức vụ) |

#### Mô tả màn hình

![](media/image85.png)

![](media/image39.png)

*Màn hình bộ lọc (Thao tác người dùng)*

Thông tin chi tiết màn hình

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin tra cứu*** |  |  |  |  |  |
| 1. | Mã nhân viên | Dropdown | Không |  | Cho phép tìm kiếm và chọn một hoặc nhiều thuộc danh sách |
| 2. | Thời gian từ - đến | DD/MM/YYYY | Bắt buộc | Một tháng tính từ ngày hiện tại trở về trước | Cho phép nhập hoặc chọn trong danh mục. |
|  |  |  |  |  | Nếu không nhập thời gian từ, mặc định từ thời điểm ghi nhận log trên hệ thống. |
|  |  |  |  |  | Nếu không nhập thời gian đến, mặc định đến ngày hiện tại. |
| 3. | Loại hành động | Dropdown | Không |  | Cho phép tìm kiếm và chọn một hoặc nhiều thuộc danh sách |
| 4. | Loại đối tượng | Dropdown | Không |  | Cho phép tìm kiếm và chọn một hoặc nhiều thuộc danh sách |
| ***Thông tin chi tiết*** |  |  |  |  |  |
| 5. | Mã nhân viên | Ký tự (10) |  |  | Hiển thị theo CSDL |
| 6. | Họ và tên | Ký tự (100) |  |  | Hiển thị theo CSDL |
| 7. | Hành động | Ký tự (200) |  |  | Hiển thị theo CSDL |
| 8. | Loại đối tượng | Ký tự (200) |  |  | Hiển thị theo CSDL |
| 9. | Thời gian | DD/MM/YYYY - hh:mm:ss |  |  | Hiển thị theo CSDL |
| ***Nút chức năng*** |  |  |  |  |  |
| 10. | Tra cứu | Button |  |  | Cho phép lưu thông tin mật khẩu mới |
| 11. | Xem chi tiết | Button |  |  | Hệ thống cho phép xem chi tiết thao tác của người dùng |
