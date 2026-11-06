
# Lab 02 – Discussion Answers

## Câu 1. Vì sao phải đồng bộ master trước khi tạo Pull Request?

Nhánh master có thể đã được cập nhật bởi các lập trình viên khác trong thời gian phát triển tính năng. Nếu không đồng bộ, nhánh feature có thể dựa trên phiên bản mã nguồn cũ, gây xung đột hoặc lỗi tích hợp khi merge.

Đồng bộ với master trước khi tạo Pull Request giúp phát hiện xung đột sớm, kiểm tra tính tương thích giữa các chức năng và giảm rủi ro khi tích hợp mã nguồn.

Trong Lab 02, nhánh `feature/search-by-title` được tạo từ master cũ. Sau khi PR #3 được merge, Dev 2 sử dụng `git fetch origin` và `git merge origin/master` để cập nhật các thay đổi từ tính năng `cart-print`. Sau khi đồng bộ, cả chương trình chính và chức năng tìm kiếm đều hoạt động đúng.

## Câu 2. Khi nào không được rebase?

Không nên rebase các commit đã được chia sẻ và đang được những người khác sử dụng, đặc biệt trên các nhánh dùng chung như master hoặc các nhánh release.

Nguyên nhân là rebase có thể tạo ra các commit với SHA mới, làm thay đổi lịch sử Git. Việc này có thể khiến các nhánh của thành viên khác bị lệch lịch sử và gây khó khăn khi đồng bộ.

Rebase phù hợp hơn với các nhánh cá nhân, chưa được chia sẻ hoặc khi nhóm đã thống nhất cho phép viết lại lịch sử.

Trong Lab 02, kiểu Rebase and merge được sử dụng thông qua Pull Request để đưa thay đổi vào master theo quy trình kiểm soát, thay vì tự ý rebase và force-push nhánh master.

## Câu 3. Nhánh feature/* khác topic/* như thế nào?

`feature/*` thường được sử dụng để phát triển chức năng mới của sản phẩm. Ví dụ:
- `feature/cart-print`: Bổ sung chức năng hiển thị giỏ hàng.
- `feature/search-by-title`: Bổ sung chức năng tìm DVD theo tiêu đề.

`topic/*` thường được sử dụng cho một công việc có phạm vi cụ thể, chẳng hạn cập nhật tài liệu, cấu hình hoặc thực hiện chỉnh sửa không trực tiếp bổ sung chức năng nghiệp vụ. Ví dụ:
- `topic/pr-template`: Tạo Pull Request template.
- `topic/use-case-diagram`: Bổ sung tài liệu Use Case.

Cả hai đều là quy ước đặt tên nhánh, không phải hai loại nhánh có cơ chế hoạt động khác nhau trong Git. Chúng giúp nhóm nhận biết mục đích công việc và quản lý Pull Request rõ ràng hơn.
