---
title: "UC 5.1.8: Import danh sách Nhân viên"
type: "use-case"
uc_number: "5.1.8"
---

### UC 5.1.8: Import danh sách Nhân viên

  -----------------------------------------------------------------------------------------------------------
  **Mục tiêu:**               Cho phép người dùng Import File nhiều Hồ sơ nhân viên một lúc
  --------------------------- -------------------------------------------------------------------------------
  **Tài khoản:**              Tài khoản được phân quyền Import tại phân hệ con "Quản lý Hồ sơ Nhân viên"

  **Sự kiện kích hoạt:**      Người dùng nhấn nút "Import" tại màn hình danh sách "Quản lý Hồ sơ nhân viên"

  **Điều kiện tiên quyết:**   Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng

  **Kết quả bắt buộc:**       Hệ thống upload thành công những "Hồ sơ nhân viên" hợp lệ lên hệ thống
  -----------------------------------------------------------------------------------------------------------

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 5.1.8.1 | **Quy tắc Import danh sách Hồ sơ Nhân viên:** |
|  | - Người dùng nhấn nút "Import" tại màn hình danh sách "Hồ sơ Nhân viên" |
|  | - Hệ thống pop-up giao diện Import File |
|  | - Người dùng nhấn "Tải tệp mẫu tại đây" |
|  | - Tab 1 của File: Hiển thị những cột thông tin để nhập thông tin |
|  | - Tab 2 của File: Hiển thị danh sách của đã tạo của những cột thông tin tương ứng trên hệ thống |
|  | - Người dùng nhấn "Chọn tệp" |
|  | - Hệ thống hiển thị giao diện cho người dùng chọn tải file từ thiết bị đang sử dụng tương ứng |
|  | - Chỉ được upload lên file excel: nếu upload file khác: hệ thống báo lỗi |
|  | - Người dùng nhấn "Xác thực File" để gửi file lên hệ thống |
| QTNV 5.1.8.2 | **Quy tắc xác thực danh sách Import Hồ sơ nhân viên:** |
|  | - Nếu các cột thông tin File người dùng đã chính xác, hệ thống xác thực các thông tin: |
|  | - Những trường thông tin cần xác thực: |
|  | - Mã nhân viên: không được trùng với mã nhân viên khác |
|  | - Email: |
|  | - Đúng định dạng Email |
|  | - Không trùng với Email đã có |
|  | - Số điện thoại: đúng định dạng số điện thoại Việt Nam |
|  | - Số điện thoại ( liên hệ khẩn cấp): đúng định dạng số điện thoại Việt Nam |
|  | - Số CMND/CCCD: |
|  | - Không được trùng với nhân viên khác |
|  | - Là 9 hoặc 12 chữ số liền nhau (không có dấu cách) |
|  | - Nhân viên cần thuộc ít nhất 1 Khối hoặc 1 Phòng ban |
|  | - "Khối" được chọn cần thuộc "Chi nhánh" tương ứng |
|  | - "Phòng ban" được chọn cần thuộc "Chi nhánh" tương ứng (hay "Khối" nếu có) |
|  | - Số tài khoản, Mã số thuế: chỉ được điền chữ số từ 0 đến 9 |
|  | - Những trường thông tin cần xác thực đúng thông tin đã tạo trên hệ thống: Chi nhánh, Khối, Phòng ban, Loại HĐ, Chức vụ, Giới tính, Trạng thái |
|  | - Những trường thông tin Bắt buộc điền thông tin: Mã nhân viên, Họ tên, Số điện thoại, Giới tính, Ngày sinh, Chi nhánh, Loại hợp đồng, Chức vụ, Ngày bắt đầu, Trạng thái |
|  | - Hệ thống hiển thị màn hình kết quả xác thực thông tin hồ sơ |
|  | - Người dùng chọn danh sách những hồ sơ hợp lệ để Import |

#### Mô tả màn hình Import File

![](media/image129.png)

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**   **Kiểu dữ liệu**   **Mô tả**                                           **Logic nghiệp vụ**                                                   **Bắt buộc**
  --------------- ------------------ --------------------------------------------------- --------------------------------------------------------------------- --------------
  Tại đây         Nút                Nhấn để tải về file mẫu Import hồ sơ                Tải về File mẫu có Tab điền thông tin và Tab hiển thị thông tin mẫu   

  Chọn tệp        Nút                Nhấn để chọn Upload File từ thiết bị đang sử dụng   Xác thực File đúng định dạng Excel                                    

  Xác thực File   Nút                Nhấn để hệ thống xác thực File danh sách            Xác thực File excel đúng với file mẫu                                 
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Mô tả màn hình File Import mẫu (Tab 1: tab điền thông tin Hồ sơ nhân viên)

![](media/image124.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Hiển thị lần lượt những cột thông tin để nhập hồ sơ nhân viên. Thứ tự hiển thị lần lượt từ trái sang phải là: |  |  |  |  |
| - Mã NV, Họ tên, Email, SĐT, Giới tính, Ngày sinh, Địa chỉ, Chi nhánh, Khối, Phòng ban, Loại HĐ, Chức vụ, Ngày bắt đầu, Trạng thái, LH khẩn cấp, SĐT khẩn cấp, CMND/CCCD, Ngân hàng, Số TK, Mã số thuế |  |  |  |  |

#### Mô tả màn hình File Import mẫu (Tab 2: tab hiển thị thông tin mẫu của hệ thống)

![](media/image113.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Với những cột thông tin "Chi nhánh", "Khối", "Phòng ban", Loại HĐ", "Chức vụ": hiển thị danh sách đã tạo của cột thông tin đó trên hệ thống |  |  |  |  |
| Giới tính | Text | Hiển thị danh sách "Giới tính" | Có 2 giới tính mặc định: |  |
|  |  |  | - Nam |  |
|  |  |  | - Nữ |  |
| Trạng thái | Text | Hiển thị danh sách "Trạng thái" | Có 3 trạng thái mặc định: |  |
|  |  |  | - Đang làm việc |  |
|  |  |  | - On-boarding |  |
|  |  |  | - Đã nghỉ việc |  |

#### Mô tả màn hình Xác thực thông tin File Import (Hồ sơ hợp lệ)

![](media/image119.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| Hồ sơ không hợp lệ | Nút | Nhấn để sang màn danh sách hồ sơ không hợp lệ | N/A |  |
| Import | Nút | Nhấn để Import những hồ sơ hợp lệ | \- Nhấn nút: |  |
|  |  |  | \+ Hệ thống báo Import thành công |  |
|  |  |  | \+ Hiển thị màn danh sách Hồ sơ với những hồ sơ mới tạo |  |
| Những cột thông tin hiển thị lần lượt của những hồ sơ hợp lệ: |  |  |  |  |
| - Mã nhân viên |  |  |  |  |
| - Họ tên, |  |  |  |  |
| - Email, |  |  |  |  |
| - Số điện thoại |  |  |  |  |
| - Giới tính |  |  |  |  |
| - Ngày sinh |  |  |  |  |
| - Địa chỉ |  |  |  |  |
| - Chi nhánh |  |  |  |  |
| - Khối |  |  |  |  |
| - Phòng ban |  |  |  |  |
| - Loại hợp đồng |  |  |  |  |
| - Chức vụ |  |  |  |  |
| - Ngày bắt đầu |  |  |  |  |
| - Trạng thái |  |  |  |  |
| - Họ tên (liên hệ khẩn cấp) |  |  |  |  |
| - SĐT khẩn cấp |  |  |  |  |
| - Số CMND/CCCD |  |  |  |  |
| - Ngân hàng |  |  |  |  |
| - Số tài khoản |  |  |  |  |
| - Mã số thuế |  |  |  |  |

#### Mô tả màn hình Xác thực thông tin FIle Import (Hồ sơ không hợp lệ)

![](media/image110.png)

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Thông tin**                                                                                                                  **Kiểu dữ liệu**   **Mô tả**                                    **Logic nghiệp vụ**                                            **Bắt buộc**
  ------------------------------------------------------------------------------------------------------------------------------ ------------------ -------------------------------------------- -------------------------------------------------------------- --------------
  Hiển thị những cột thông tin tương ứng với từng Hồ sơ nhân viên lần lượt từ trái sang phải giống của màn hình "Hồ sơ hợp lệ"                                                                                                                                  

  Thông tin không hợp lệ                                                                                                         Text               Hiển thị danh sách lỗi của hồ sơ tương ứng   Hiển thị những lỗi xác thực hoặc lỗi thông tin bắt buộc điền   
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
