---
title: "UC 3.2.2: Chỉnh sửa Role của Nhân viên"
type: "use-case"
uc_number: "3.2.2"
---

### UC 3.2.2: Chỉnh sửa Role của Nhân viên

| **Mục tiêu:** | Cho phép người dùng chỉnh sửa Role của Nhân viên đã có |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền chỉnh sửa trong "Quản lý Nhân viên theo Role" |
| **Sự kiện kích hoạt:** | Người dùng truy cập nhấn nút "Chỉnh sửa" tại màn hình "Quản lý Nhân viên theo Role" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống cập nhật thông tin đã chỉnh sửa Vai trò của những nhân viên tương ứng |
|  | Cập nhật giao diện hiển thị của những Nhân viên được chỉnh sửa Role |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 3.2.4 | **Quy tắc Chỉnh sửa Role của nhân viên:** |
|  | - Người dùng nhấn "Thay đổi vai trò" -\> hệ thống hiển thị màn "Thay đổi vai trò" với những nhân viên đã chọn tương ứng |
|  | - Nếu chưa chọn nhân viên nào, báo lỗi tương ứng |
|  | - Nếu số lượng nhân viên được chọn lớn hơn 25, báo lỗi tương ứng |
|  | - Người dùng chọn "Vai trò" mới và nút "Cập nhật" |
|  | - Hệ thống báo Chỉnh sửa thành công |
|  | - Quay về màn hình danh sách nhân viên theo role với thông tin mới được cập nhật |
|  | - Với những tài khoản của nhân viên thay được đổi vai trò, đăng xuất tài khoản đó ở thiết bị đang sử dụng. |
|  | - Khi đăng nhập lại, giao diện hiển thị tương ứng với vai trò mới |

#### Mô tả màn hình

![](media/image26.png)

| **Thông tin** | **Kiểu dữ liệu** | **Mô tả** | **Logic nghiệp vụ** | **Bắt buộc** |
| --- | --- | --- | --- | --- |
| STT | Trường dữ liệu | Hiển thị "STT" tương ứng | N/A |  |
| Mã | Trường dữ liệu | Hiển thị "Mã nhân viên" tương ứng | N/A |  |
| Tên | Trường dữ liệu | Hiển thị "Tên nhân viên" tương ứng | N/A |  |
| Vai trò | Trường dữ liệu | Hiển thị "Vai trò" tương ứng | N/A |  |
| Chi nhánh | Trường dữ liệu | Hiển thị "Chi nhánh" tương ứng | N/A |  |
| Chức vụ | Trường dữ liệu | Hiển thị "Chức vụ" tương ứng | N/A |  |
| Vai trò mới | Dropdownlist | Hiển thị danh sách "Vai trò" đã tạo | \- Nhấn để hiển thị danh sách "Vai trò" đã tạo |  |
|  |  |  | \- Chọn "Vai trò" mới |  |
| Chỉnh sửa | Nút | Nhấn để thay đổi "Vai trò" của những nhân viên đã chọn | Báo lỗi nếu chưa chọn thông tin "Vai trò sau thay đổi" |  |
| Hủy | Nút | Nhấn để dừng luồng Chỉnh sửa thông tin | Khi nhấn, hệ thống sẽ quay về màn hiển thị danh sách Nhân viên theo Role |  |

1.  Phân hệ con "Quản lý quyền"
    ---------------------------

    1.  ### UC 3.3.1: Xem danh sách + Tìm kiếm Quyền

| **Mục tiêu:** | Cho phép người dùng xem danh sách các Quyền của hệ thống |
| --- | --- |
| **Tài khoản:** | Tài khoản được phân quyền xem trong phân hệ "Quản lý Quyền" |
| **Sự kiện kích hoạt:** | Người dùng truy cập Màn hình của Phân hệ con "Quản lý Quyền" |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống với tài khoản được phân quyền tương ứng |
| **Kết quả bắt buộc:** | Hệ thống hiển thị màn hình Danh sách "Quyền" với đầy đủ thông tin |
|  | Hệ thống hiển thị danh sách "Quyền" đúng với mỗi truy vấn tìm kiếm |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 3.3.1.1 | **Quy tắc Xem màn hình danh sách các Quyền:** |
|  | - Hệ thống hiển thị Màn hình Xem danh sách những Quyền của hệ thống |
| QTNV 3.3.1.2 | **Quy tắc Tìm kiếm Quyền:** |
|  | - Điền **"Tên Quyền"** muốn tìm kiếm vào textbox và nhấn Enter |
|  | - Hệ thống hiển thị danh sách Quyền nếu cụm từ khóa nhập vào là một chuỗi liên tục và chính xác (không bỏ chữ giữa) nằm trong "Tên Quyền, Tên phân hệ". Tìm kiếm không phân biệt chữ hoa chữ thường. |
|  | - Ví dụ: Tên Quyền: **\"Xem danh sách hồ sơ nhân viên\"** |
|  | - **\"Hồ sơ\"** → tìm được |
|  | - **\"Xem viên\"** → không tìm được |
|  | - Nếu không tìm thấy kết quả Quyền nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |
| QTNV 3.3.1.3 | **Quy tắc Tìm kiếm Quyền (Bằng Filter):** |
|  | - Tìm kiếm bằng Filter "Phân hệ", "Phân hệ con" |
|  | - Hiển thị danh sách Hồ sơ nhân viên đúng với các điều kiện được chọn trong bộ lọc. |
|  | - Mỗi trường hiển thị dưới dạng dropdownlist, trong đó danh sách giá trị bao gồm: |
|  | - Tất cả |
|  | - Danh sách các Phân hệ/Phân hệ con tương ứng hiện có (trong hệ thống). |
|  | - Quy tắc chọn: |
|  | - **Phân hệ:** hiển thị tất cả phân hệ trong hệ thống |
|  | - **Chỉ được chọn Phân hệ con khi đã chọn Phân hệ**, danh sách hiển thị chỉ gồm các Phân hệ con thuộc Phân hệ đó. |
|  | - Người dùng chỉ được chọn 1 giá trị hoặc \"Tất cả\" cho mỗi dropdownlist. |
|  | - Nếu không tìm thấy kết quả Nhân viên nào, hiển thị màn hình thông báo không tìm thấy kết quả hợp lệ |

#### Mô tả màn hình

![](media/image17.png)

  **Thông tin**   **Kiểu dữ liệu**   **Mô tả**                        **Logic nghiệp vụ**                               **Bắt buộc**
  --------------- ------------------ -------------------------------- ------------------------------------------------- --------------
  Ô tìm kiếm      Textbox            Tìm kiếm "Quyền" tương ứng       Điền "Tên quyền" tương ứng và nhấn Enter để tìm   Có
  STT             Trường dữ liệu     Hiển thị "Số thứ tự" tương ứng   N/A                                               Có
  Tên quyền       Trường dữ liệu     Hiển thị "Tên quyền" tương ứng   N/A                                               Có
  Mô tả           Trường dữ liệu     Hiển thị "Mô tả" tương ứng       N/A                                               Có

#### Mô tả màn hình Filter danh sách Quyền

![](media/image36.png)

  **Thông tin**   **Kiểu dữ liệu**   **Mô tả**                                                        **Logic nghiệp vụ**                 **Bắt buộc**
  --------------- ------------------ ---------------------------------------------------------------- ----------------------------------- --------------
  Phân hệ         Dropdownlist       Nhấn để hiển thị danh sách Phân hệ                                                                   
  Phân hệ con     Dropdownlist       Nhấn để hiển thị danh sách phân hệ con ứng với Phân hệ đã chọn   Disable đến khi đã chọn "Phân hệ"   
  Xóa bộ lọc      Button             Nhấn để bỏ hết bộ lọc hiện có                                                                        
  Áp dụng         Button             Nhấn để áp dụng tìm kiếm bộ lọc hiện tại đang có                 N/A                                 

IV. Phân hệ "Quản lý tuyển dụng"
    ============================

    1.  Phân hệ con "Quản lý kênh tuyển dụng"
        -------------------------------------

        1.  ### ​UC 4.1.1: Xem danh sách kênh tuyển dụng

| **Mục tiêu:** | Cho phép người dùng xem danh sách các kênh tuyển dụng trên hệ thống. |
| --- | --- |
| **Tài khoản:** | Người sử dụng. |
| **Sự kiện kích hoạt:** | Người dùng truy cập chức năng *Quản lý tuyển dụng/ Quản lý kênh tuyển dụng* |
| **Điều kiện tiên quyết:** | Người dùng login vào hệ thống và được phân quyền. |
| **Kết quả bắt buộc:** | Hệ thống đã hiển thị danh sách kênh tuyển dụng theo tiêu chí mà người dùng chọn (nếu có). |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| --- | --- |
| QTNV 4.1.1 | **Screen Displaying Rules:** |
|  | ❖ Hệ thống hiển thị Màn hình Xem danh sách các kênh tuyển dụng. |
|  | ❖ Hiển thị danh sách được sắp xếp theo thời gian tạo gần nhất. |
|  | ❖ Chỉ hiển thị lần tạo hay lần thay đổi mới nhất. |

#### Mô tả màn hình

![](media/image34.png)

| **STT** | **Thông tin** | **Kiểu dữ liệu** | **Bắt buộc** | **Giá trị mặc định** | **Ràng buộc** |
| --- | --- | --- | --- | --- | --- |
| ***Thông tin tra cứu*** |  |  |  |  |  |
| 1\. | Mã kênh | Kí tự (50) | Không | Không | Cho phép nhập. |
| 2\. | Tên kênh | Kí tự (250) | Không | Không | Cho phép nhập |
| ***Thông tin dữ liệu*** |  |  |  |  |  |
| 3\. | Mã kênh | Kí tự (50) | Có |  | Hiển thị theo CSDL |
| 4\. | Tên kênh | Kí tự (250) | Có |  | Hiển thị theo CSDL |
| 5\. | Mô tả | Kí tự (500) | Có |  | Hiển thị theo CSDL. |
|  |  |  |  |  | Trên màn hình danh sách, chỉ hiển thị **50 ký tự đầu tiên**, phần dư sẽ được cắt bỏ và hiển thị dấu \"...\" (ellipsis). |
| ***Nút chức năng*** |  |  |  |  |  |
| 6\. | Tìm kiếm | Button | Không |  | Cho phép hiển thị danh sách theo các tham số đã chọn |
| 7\. | Thêm mới | Button | Không |  | Hệ thống hiển thị màn hình thêm mới |
| 8\. | Sửa (thao tác) | Button | Không |  | Hệ thống hiển thị màn hình sửa theo dòng dữ liệu thực hiện thao tác |
| 9\. | Xoá (thao tác) | Button | Không |  | Cho phép xóa dòng dữ liệu thực hiện thao tác |
| 10\. | Xem chi tiết (thao tác) | Button | Không |  | Cho phép xem dòng dữ liệu thực hiện thao tác |
