---
title: "UC1.1.5: Cảnh báo hệ thống"
type: "use-case"
uc_number: "1.1.5"
---

### UC1.1.5: Cảnh báo hệ thống

| **Mục tiêu:** | Đảm bảo hệ thống có khả năng phát hiện và thông báo kịp thời các tình huống hoặc sự kiện quan trọng để người dùng hoặc quản trị viên xử lý. |
| **Tác nhân:** | Người dùng: Nhận cảnh báo liên quan đến tài khoản. |
|  | Quản trị viên: Nhận cảnh báo về sự cố hệ thống, an ninh, dữ liệu. |
| **Sự kiện kích hoạt:** | Xảy ra sự kiện trên hệ thống. |
| **Điều kiện tiên quyết:** | Người dùng/Quản trị viên đã đăng ký thông tin liên hệ (email, số điện thoại, app notification). |
|  | Hệ thống có cơ chế giám sát sự kiện và dịch vụ gửi cảnh báo đang hoạt động. |
| **Kết quả bắt buộc:** | Cảnh báo được hiển thị trên hệ thống và gửi email/SMS đến đúng người nhận. |

#### Quy tắc nghiệp vụ

| **Mã QTNV** | **Mô tả** |
| QTNV 1.1.5 | **System Alert Rules:** |
|  | - Mỗi cảnh báo phải được lưu trữ trong log thông báo. |
|  | - Thông báo sắp xếp theo thời gian gần nhất từ trên xuống |
|  | - Có các trạng thái của thông báo: đã xem, chưa xem. |
|  | - Những thông báo đã được click sẽ mặc định trạng thái là đã xem. |
|  | - Có nút chức năng đánh dấu đã xem cho các thông báo có trạng thái chưa xem. |
|  | - Khi ấn (click) vào thông báo sẽ chuyển sang màn hình tương ứng với tác vụ thông báo. |
|  | - Người dùng có thể xem lịch sử cảnh báo/ thông báo trong 90 ngày gần nhất đối với những thông báo đã xem. |
|  | - Hệ thống hiển thị danh sách thông báo và hỗ trợ cuộn để xem các thông báo trước đó. |
|  | - Các trường hợp hiển thị cảnh báo |
|  | - Đăng nhập: |
|  | - Khi tài khoản đang đăng nhập trên nhiều thiết bị |
|  | - Mỗi lần đăng nhập sai mật khẩu. |
|  | - Đổi/ Đặt lại mật khẩu |
|  | - Khi đổi/đặt mật khẩu mới thành công. |
|  | - Quản lý hợp đồng: |
|  | - Hợp đồng sắp hết hạn |
|  | - Chấm công: |
|  | - Chưa thực hiện chấm công trong ngày |
|  | - Group chat: |
|  | - Thông báo tin nhắn trong các group chat được tham gia |
|  | - E - learning: |
|  | - Thông báo cáo khoá học cần tham gia và hạn hoàn thành (ngay sau khi nhân sự gán thông tin khoá học cho nhân viên) |
|  | - Thông báo các khóa học hạn hoàn thành khóa học theo Chương trình đào tạo (Thông báo được đẩy hàng ngày từ thời điểm nhắc) |
|  | - Đề xuất: |
|  | - Thông báo cần ký duyệt đề xuất (người phụ trách ký duyệt) |
|  | - Thông báo đề xuất đã được duyệt bởi nhân viên nào |
|  | - Tài liệu: |
|  | - Thông báo có tài liệu/văn bản mới được công bố (người có quyền được xem) |
|  | - Quản lý đặt phòng |
|  | - Đặt phòng thành công (sau khi nhân sự duyệt) |
|  | - Quản lý đặt xe |
|  | - Đặt xe thành công (sau khi nhân sự duyệt) |

#### Mô tả màn hình

![](media/image115.png)
