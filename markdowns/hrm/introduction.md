---
title: "Introduction"
type: "section"
---

 

**\[[MVL NextGen ERP (MVL-NE)]{.mark}\]**

**TÀI LIỆU PHÂN TÍCH YÊU CẦU**

Version: 0.2

**Lịch sử cập nhật tài liệu**

| Ngày | Phiên bản | Tác giả | Mô tả |
| 11/08/2025 | 0.1 | TrangPT, | First Creation |
|  |  | DuyLS |  |
| 02/10/2025 | 0.2 | TrangPT | - UC1.1.1: Bổ sung nghiệp vụ chỉ cho phép đăng nhập trên một thiết bị (app mobile); |
|  |  |  | - Bổ sung trường thông tin Người liên hệ ở thông tin của các ứng viên (các chức năng xem/sửa/tạo); |
|  |  |  | - Bổ sung thêm UC 4.8.11, UC 4.8.12 liên quan đến báo cáo thống kê số lượng ứng viên trúng tuyển; |
|  |  |  | - Cập nhật lại các màn hình thiết kế liên quan đến các chức năng: |
|  |  |  | - Quản lý đề nghị tuyển dụng: |
|  |  |  | - IV.4.1. UC 4.4.1: Xem danh sách đề nghị |
|  |  |  | - IV.4.2. UC 4.4.2: Tìm kiếm danh sách đề nghị tuyển dụng |
|  |  |  | - IV.4.3. UC 4.4.3: Xem chi tiết đề nghị tuyển dụng |
|  |  |  | - IV.4.4. UC 4.4.4: Tạo mới đề nghị tuyển dụng |
|  |  |  | - IV.4.5. UC 4.4.5: Chỉnh sửa đề nghị tuyển dụng |
|  |  |  | - Quản lý mô tả công việc: |
|  |  |  | - IV.5.1. UC4.5.1: Xem danh sách mô tả công việc |
|  |  |  | - IV.5.2. UC4.5.2: Tìm kiếm danh sách các mô tả công việc |
|  |  |  | - IV.5.3. UC4.5.3: Xem chi tiết mô tả công việc |
|  |  |  | - IV.5.4. UC4.5.4: Tạo mới mô tả công việc |
|  |  |  | - IV.5.5. UC4.5.5: Chỉnh sửa mô tả công việc |
|  |  |  | - IV.5.6. UC4.5.6: Sao chép công việc |
|  |  |  | - Quản lý ứng viên: |
|  |  |  | - IV.6.1. UC4.6.1: Xem danh sách ứng viên |
|  |  |  | - IV.6.2. UC4.6.2: Tìm kiếm ứng viên |
|  |  |  | - IV.6.3. UC4.6.3: Xem chi tiết một ứng viên |
|  |  |  | - IV.6.4. UC4.6.4: Tạo mới ứng viên |
|  |  |  | - IV.6.5. UC4.6.5: Chỉnh sửa ứng viên |
|  |  |  | - Quản lý lịch phỏng vấn: |
|  |  |  | - IV.7.3. UC4.7.3: Xem chi tiết lịch phỏng vấn |
|  |  |  | - IV.7.4. UC4.7.4: Tạo mới lịch phỏng vấn |
|  |  |  | - IV.7.5. UC4.7.5: Chỉnh sửa lịch phỏng vấn |

**Mục lục**

[***I. Xác thực người dùng 1***](#xác-thực-người-dùng)

> [I.1.1. UC1.1.1: Đăng nhập bằng mật khẩu 1](#uc1.1.1-đăng-nhập-bằng-mật-khẩu)
>
> [I.1.2. UC1.1.2: Đăng nhập bằng sinh trắc học 4](#uc1.1.2-đăng-nhập-bằng-sinh-trắc-học)
>
> [I.1.3. UC1.1.3: Quên mật khẩu 5](#uc1.1.3-quên-mật-khẩu)
>
> [I.1.4. UC1.1.4: Đổi mật khẩu 10](#uc1.1.4-đổi-mật-khẩu)
>
> [I.1.5. UC1.1.5: Cảnh báo hệ thống 14](#uc1.1.5-cảnh-báo-hệ-thống)
>
> [I.1.6. UC1.1.6: Theo dõi thao tác người dùng 16](#uc1.1.6-theo-dõi-thao-tác-người-dùng)
>
> [I.1.7. UC1.1.7: Xem chi tiết thao tác người dùng 19](#uc1.1.7-xem-chi-tiết-thao-tác-người-dùng)

[***II. Phân hệ "Quản lý Chung sơ đồ tổ chức" 23***](#phân-hệ-quản-lý-chung-sơ-đồ-tổ-chức)

> [**II.1. Phân hệ con "Quản lý chi nhánh" 23**](#phân-hệ-con-quản-lý-chi-nhánh)
>
> [II.1.1. UC 2.1.1: Xem danh sách + tìm kiếm chi nhánh 23](#uc-2.1.1-xem-danh-sách-tìm-kiếm-chi-nhánh)
>
> [II.1.2. UC 2.1.2: Tạo mới một Chi nhánh 26](#uc-2.1.2-tạo-mới-một-chi-nhánh)
>
> [II.1.3. UC 2.1.3: Xem chi tiết thông tin một Chi nhánh 29](#uc-2.1.3-xem-chi-tiết-thông-tin-một-chi-nhánh)
>
> [II.1.4. UC 2.1.4: Chỉnh sửa thông tin một Chi nhánh 31](#uc-2.1.4-chỉnh-sửa-thông-tin-một-chi-nhánh)
>
> [II.1.5. UC 2.1.5: Xóa một Chi nhánh 33](#uc-2.1.5-xóa-một-chi-nhánh)
>
> [**II.2. Phân hệ con "Quản lý Khối" 36**](#phân-hệ-con-quản-lý-khối)
>
> [II.2.1. UC 2.2.1: Xem danh sách + Tìm kiếm Khối 36](#uc-2.2.1-xem-danh-sách-tìm-kiếm-khối)
>
> [II.2.2. UC 2.2.2: Tạo mới một Khối 38](#uc-2.2.2-tạo-mới-một-khối)
>
> [II.2.3. UC 2.2.3: Xem chi tiết thông tin một Khối 42](#uc-2.2.3-xem-chi-tiết-thông-tin-một-khối)
>
> [II.2.4. UC 2.2.4: Chỉnh sửa thông tin một Khối 44](#uc-2.2.4-chỉnh-sửa-thông-tin-một-khối)
>
> [II.2.5. UC 2.2.5: Xóa một Khối 46](#uc-2.2.5-xóa-một-khối)
>
> [**II.3. Phân hệ con "Quản lý Phòng ban" 48**](#phân-hệ-con-quản-lý-phòng-ban)
>
> [II.3.1. UC 2.3.1: Xem danh sách + Tìm kiếm Phòng ban 48](#uc-2.3.1-xem-danh-sách-tìm-kiếm-phòng-ban)
>
> [II.3.2. UC 2.3.2: Tạo mới một Phòng ban 51](#uc-2.3.2-tạo-mới-một-phòng-ban)
>
> [II.3.3. UC 2.3.3: Xem chi tiết thông tin một Phòng ban 55](#uc-2.3.3-xem-chi-tiết-thông-tin-một-phòng-ban)
>
> [II.3.4. UC 2.3.4: Chỉnh sửa thông tin một Phòng ban 57](#uc-2.3.4-chỉnh-sửa-thông-tin-một-phòng-ban)
>
> [II.3.5. UC 2.3.5: Xóa một Phòng ban 59](#uc-2.3.5-xóa-một-phòng-ban)
>
> [**II.4. Phân hệ con "Quản lý chức vụ" 61**](#phân-hệ-con-quản-lý-chức-vụ)
>
> [II.4.1. UC 2.4.1: Xem danh sách + tìm kiếm Chức vụ 61](#uc-2.4.1-xem-danh-sách-tìm-kiếm-chức-vụ)
>
> [II.4.2. UC 2.4.2: Tạo mới một Chức vụ 63](#uc-2.4.2-tạo-mới-một-chức-vụ)
>
> [II.4.3. UC 2.4.3: Xem chi tiết thông tin một Chức vụ 67](#uc-2.4.3-xem-chi-tiết-thông-tin-một-chức-vụ)
>
> [II.4.4. UC 2.4.4: Chỉnh sửa thông tin một Chức vụ 68](#uc-2.4.4-chỉnh-sửa-thông-tin-một-chức-vụ)
>
> [II.4.5. UC 2.4.5: Xóa một Chức vụ 70](#uc-2.4.5-xóa-một-chức-vụ)

[***III. Phân hệ "Quản lý phân quyền" 73***](#phân-hệ-quản-lý-phân-quyền)

> [**III.1. Phân hệ con "Quản lý vai trò (Role)" 73**](#phân-hệ-con-quản-lý-vai-trò-role)
>
> [III.1.1. UC 3.1.1:Xem danh sách + Tìm kiếm Vai trò (Role) 73](#uc-3.1.1xem-danh-sách-tìm-kiếm-vai-trò-role)
>
> [III.1.2. UC 3.1.2: Tạo mới Vai trò (Role) 75](#uc-3.1.2-tạo-mới-vai-trò-role)
>
> [III.1.3. UC 3.1.3: Xem chi tiết Vai trò (Role) 81](#uc-3.1.3-xem-chi-tiết-vai-trò-role)
>
> [III.1.4. UC 3.1.4: Chỉnh sửa thông tin Vai trò (Role) 83](#uc-3.1.4-chỉnh-sửa-thông-tin-vai-trò-role)
>
> [III.1.5. UC 3.1.5: Xóa một Vai trò (Role) 86](#uc-3.1.5-xóa-một-vai-trò-role)
>
> [**III.2. Phân hệ con "Quản lý nhân viên theo Role" 88**](#phân-hệ-con-quản-lý-nhân-viên-theo-role)
>
> [III.2.1. UC 3.2.1: Xem danh sách + Tìm kiếm Nhân viên theo Role 88](#uc-3.2.1-xem-danh-sách-tìm-kiếm-nhân-viên-theo-role)
>
> [III.2.2. UC 3.2.2: Chỉnh sửa Role của Nhân viên 95](#uc-3.2.2-chỉnh-sửa-role-của-nhân-viên)
>
> [**III.3. Phân hệ con "Quản lý quyền" 97**](#phân-hệ-con-quản-lý-quyền)
>
> [III.3.1. UC 3.3.1: Xem danh sách + Tìm kiếm Quyền 97](#uc-3.3.1-xem-danh-sách-tìm-kiếm-quyền)

[***IV. Phân hệ "Quản lý tuyển dụng" 102***](#phân-hệ-quản-lý-tuyển-dụng)

> [**IV.1. Phân hệ con "Quản lý kênh tuyển dụng" 102**](#phân-hệ-con-quản-lý-kênh-tuyển-dụng)
>
> [IV.1.1. ​UC 4.1.1: Xem danh sách kênh tuyển dụng 102](#uc-4.1.1-xem-danh-sách-kênh-tuyển-dụng)
>
> [IV.1.2. UC 4.1.2: Tìm kiếm kênh tuyển dụng 105](#uc-4.1.2-tìm-kiếm-kênh-tuyển-dụng)
>
> [IV.1.3. UC 4.1.3: Xem Chi tiết kênh tuyển dụng 106](#uc-4.1.3-xem-chi-tiết-kênh-tuyển-dụng)
>
> [IV.1.4. UC 4.1.4: Tạo mới kênh tuyển dụng 107](#uc-4.1.4-tạo-mới-kênh-tuyển-dụng)
>
> [IV.1.5. UC 4.1.5: Chỉnh sửa kênh tuyển dụng 110](#uc-4.1.5-chỉnh-sửa-kênh-tuyển-dụng)
>
> [IV.1.6. UC 4.1.6: Xóa kênh tuyển dụng 112](#uc-4.1.6-xóa-kênh-tuyển-dụng)
>
> [**IV.2. Phân hệ con "Quản lý nguồn tuyển dụng" 113**](#phân-hệ-con-quản-lý-nguồn-tuyển-dụng)
>
> [IV.2.1. UC 4.2.1: Xem danh sách nguồn tuyển dụng 113](#uc-4.2.1-xem-danh-sách-nguồn-tuyển-dụng)
>
> [IV.2.2. UC 4.2.2: Tìm kiếm nguồn tuyển dụng 116](#uc-4.2.2-tìm-kiếm-nguồn-tuyển-dụng)
>
> [IV.2.3. UC 4.2.3: Xem chi tiết nguồn tuyển dụng 117](#uc-4.2.3-xem-chi-tiết-nguồn-tuyển-dụng)
>
> [IV.2.4. UC 4.2.4: Tạo mới nguồn tuyển dụng 118](#uc-4.2.4-tạo-mới-nguồn-tuyển-dụng)
>
> [IV.2.5. UC 4.2.5: Chỉnh sửa nguồn tuyển dụng 121](#uc-4.2.5-chỉnh-sửa-nguồn-tuyển-dụng)
>
> [IV.2.6. UC 4.2.6: Xoá nguồn tuyển dụng 123](#uc-4.2.6-xoá-nguồn-tuyển-dụng)
>
> [**IV.3. Phân hệ con "Quản lý chi phí tuyển dụng" 124**](#phân-hệ-con-quản-lý-chi-phí-tuyển-dụng)
>
> [IV.3.1. UC 4.3.1: Xem danh sách chi phí tuyển dụng 124](#uc-4.3.1-xem-danh-sách-chi-phí-tuyển-dụng)
>
> [IV.3.2. UC 4.3.2: Tìm kiếm danh sách chi phí tuyển dụng 127](#uc-4.3.2-tìm-kiếm-danh-sách-chi-phí-tuyển-dụng)
>
> [IV.3.3. UC 4.3.4: Xem chi tiết chi phí tuyển dụng 129](#uc-4.3.4-xem-chi-tiết-chi-phí-tuyển-dụng)
>
> [IV.3.4. UC 4.3.5: Tạo mới Chi phí tuyển dụng 131](#uc-4.3.5-tạo-mới-chi-phí-tuyển-dụng)
>
> [IV.3.5. UC 4.3.6: Chỉnh sửa chi phí tuyển dụng 135](#uc-4.3.6-chỉnh-sửa-chi-phí-tuyển-dụng)
>
> [IV.3.6. UC 4.3.7: Kết xuất chi phí tuyển dụng 138](#uc-4.3.7-kết-xuất-chi-phí-tuyển-dụng)
>
> [IV.3.7. UC 4.3.8: Xoá chi phí tuyển dụng 139](#uc-4.3.8-xoá-chi-phí-tuyển-dụng)
>
> [**IV.4. Phân hệ con "Quản lý đề nghị tuyển dụng" 140**](#phân-hệ-con-quản-lý-đề-nghị-tuyển-dụng)
>
> [IV.4.1. UC 4.4.1: Xem danh sách đề nghị tuyển dụng 140](#uc-4.4.1-xem-danh-sách-đề-nghị-tuyển-dụng)
>
> [IV.4.2. UC 4.4.2: Tìm kiếm danh sách đề nghị tuyển dụng 144](#uc-4.4.2-tìm-kiếm-danh-sách-đề-nghị-tuyển-dụng)
>
> [IV.4.3. UC 4.4.3: Xem chi tiết đề nghị tuyển dụng 144](#uc-4.4.3-xem-chi-tiết-đề-nghị-tuyển-dụng)
>
> [IV.4.4. UC 4.4.4: Tạo mới đề nghị tuyển dụng 147](#uc-4.4.4-tạo-mới-đề-nghị-tuyển-dụng)
>
> [IV.4.5. UC 4.4.5: Chỉnh sửa đề nghị tuyển dụng 151](#uc-4.4.5-chỉnh-sửa-đề-nghị-tuyển-dụng)
>
> [IV.4.6. UC4.4.6: Xoá đề nghị tuyển dụng 156](#uc4.4.6-xoá-đề-nghị-tuyển-dụng)
>
> [**IV.5. Phân hệ con "Quản lý Mô tả công việc (JD)" 157**](#phân-hệ-con-quản-lý-mô-tả-công-việc-jd)
>
> [IV.5.1. UC4.5.1: Xem danh sách mô tả công việc 157](#uc4.5.1-xem-danh-sách-mô-tả-công-việc)
>
> [IV.5.2. UC4.5.2: Tìm kiếm danh sách các mô tả công việc 159](#uc4.5.2-tìm-kiếm-danh-sách-các-mô-tả-công-việc)
>
> [IV.5.3. UC4.5.3: Xem chi tiết mô tả công việc 161](#uc4.5.3-xem-chi-tiết-mô-tả-công-việc)
>
> [IV.5.4. UC4.5.4: Tạo mới mô tả công việc 164](#uc4.5.4-tạo-mới-mô-tả-công-việc)
>
> [IV.5.5. UC4.5.5: Chỉnh sửa mô tả công việc 168](#uc4.5.5-chỉnh-sửa-mô-tả-công-việc)
>
> [IV.5.6. UC4.5.6: Sao chép công việc 172](#uc4.5.6-sao-chép-công-việc)
>
> [IV.5.7. UC4.5.7: Kết xuất file JD 177](#uc4.5.7-kết-xuất-file-jd)
>
> [IV.5.8. UC4.5.8: Xoá mô tả công việc 177](#uc4.5.8-xoá-mô-tả-công-việc)
>
> [**IV.6. Phân hệ con "Quản lý ứng viên" 178**](#phân-hệ-con-quản-lý-ứng-viên)
>
> [IV.6.1. UC4.6.1: Xem danh sách ứng viên 178](#uc4.6.1-xem-danh-sách-ứng-viên)
>
> [IV.6.2. UC4.6.2: Tìm kiếm ứng viên 181](#uc4.6.2-tìm-kiếm-ứng-viên)
>
> [IV.6.3. UC4.6.3: Xem chi tiết một ứng viên 183](#uc4.6.3-xem-chi-tiết-một-ứng-viên)
>
> [IV.6.4. UC4.6.4: Tạo mới ứng viên 187](#uc4.6.4-tạo-mới-ứng-viên)
>
> [IV.6.5. UC4.6.5: Chỉnh sửa ứng viên 191](#uc4.6.5-chỉnh-sửa-ứng-viên)
>
> [IV.6.6. UC4.6.6: Kết xuất danh sách ứng viên 196](#uc4.6.6-kết-xuất-danh-sách-ứng-viên)
>
> [IV.6.7. UC4.6.7: Tải lên danh sách ứng viên 196](#uc4.6.7-tải-lên-danh-sách-ứng-viên)
>
> [IV.6.8. UC4.6.8: Xoá ứng viên 197](#uc4.6.8-xoá-ứng-viên)
>
> [IV.6.9. UC4.6.9: Chuyển thông tin ứng viên thành nhân viên 198](#uc4.6.9-chuyển-thông-tin-ứng-viên-thành-nhân-viên)
>
> [**IV.7. Phân hệ con "Quản lý lịch phỏng vấn" 199**](#phân-hệ-con-quản-lý-lịch-phỏng-vấn)
>
> [IV.7.1. UC4.7.1: Xem Danh sách lịch phỏng vấn 199](#uc4.7.1-xem-danh-sách-lịch-phỏng-vấn)
>
> [IV.7.2. UC4.7.2: Tìm kiếm lịch phỏng vấn 201](#uc4.7.2-tìm-kiếm-lịch-phỏng-vấn)
>
> [IV.7.3. UC4.7.3: Xem chi tiết lịch phỏng vấn 204](#uc4.7.3-xem-chi-tiết-lịch-phỏng-vấn)
>
> [IV.7.4. UC4.7.4: Tạo mới lịch phỏng vấn 209](#uc4.7.4-tạo-mới-lịch-phỏng-vấn)
>
> [IV.7.5. UC4.7.5: Chỉnh sửa lịch phỏng vấn 212](#uc4.7.5-chỉnh-sửa-lịch-phỏng-vấn)
>
> [IV.7.6. UC4.7.6: Kết xuất lịch phỏng vấn 216](#uc4.7.6-kết-xuất-lịch-phỏng-vấn)
>
> [IV.7.7. UC4.7.8: Xoá lịch phỏng vấn 217](#uc4.7.8-xoá-lịch-phỏng-vấn)
>
> [IV.7.8. UC4.7.8: Gửi mail cho ứng viên 218](#uc4.7.8-gửi-mail-cho-ứng-viên)
>
> [**IV.8. Phân hệ con "Quản lý báo cáo" 219**](#phân-hệ-con-quản-lý-báo-cáo)
>
> [IV.8.1. UC4.8.1: Xem báo cáo Tăng trưởng nhân sự theo tuần 219](#uc4.8.1-xem-báo-cáo-tăng-trưởng-nhân-sự-theo-tuần)
>
> [IV.8.2. UC4.8.2: Kết xuất báo cáo Tăng trưởng nhân sự 222](#uc4.8.2-kết-xuất-báo-cáo-tăng-trưởng-nhân-sự)
>
> [IV.8.3. UC4.8.3: Xem báo cáo Tăng trưởng nhân sự theo tháng 223](#uc4.8.3-xem-báo-cáo-tăng-trưởng-nhân-sự-theo-tháng)
>
> [IV.8.4. UC4.8.4: Kết xuất báo cáo Tăng trưởng nhân sự theo tháng 225](#uc4.8.4-kết-xuất-báo-cáo-tăng-trưởng-nhân-sự-theo-tháng)
>
> [IV.8.5. UC4.8.5: Xem báo cáo Báo cáo nguồn tuyển dụng 225](#uc4.8.5-xem-báo-cáo-báo-cáo-nguồn-tuyển-dụng)
>
> [IV.8.6. UC4.8.6: Kết xuất báo cáo nguồn tuyển dụng 228](#uc4.8.6-kết-xuất-báo-cáo-nguồn-tuyển-dụng)
>
> [IV.8.7. UC4.8.7: Xem báo cáo Báo cáo kênh tuyển dụng 228](#uc4.8.7-xem-báo-cáo-báo-cáo-kênh-tuyển-dụng)
>
> [IV.8.8. UC4.8.8: Kết xuất báo cáo kênh tuyển dụng 231](#uc4.8.8-kết-xuất-báo-cáo-kênh-tuyển-dụng)
>
> [IV.8.9. UC4.8.9: Xem báo cáo Báo cáo chi phí tuyển dụng 231](#uc4.8.9-xem-báo-cáo-báo-cáo-chi-phí-tuyển-dụng)
>
> [IV.8.10. UC4.8.10: Kết xuất báo cáo chi phí tuyển dụng 233](#uc4.8.10-kết-xuất-báo-cáo-chi-phí-tuyển-dụng)
>
> [IV.8.11. UC4.8.11: Xem báo cáo Thống kê số lượng ứng viên trúng tuyển 234](#uc4.8.11-xem-báo-cáo-thống-kê-số-lượng-ứng-viên-trúng-tuyển)
>
> [IV.8.12. UC4.8.12: Kết xuất báo cáo Thống kê số lượng ứng viên trúng tuyển 236](#uc4.8.12-kết-xuất-báo-cáo-thống-kê-số-lượng-ứng-viên-trúng-tuyển)
