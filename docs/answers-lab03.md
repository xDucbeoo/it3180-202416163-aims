
# Lab 03 – Discussion Answers

## Câu 1. Merge base là gì?

Merge base là commit tổ tiên chung tốt nhất (best common ancestor) của hai nhánh trong lịch sử Git.

Khi thực hiện merge, Git thường sử dụng ba phiên bản để xác định các thay đổi:
- Merge base: Phiên bản chung trước khi hai nhánh phát triển độc lập.
- HEAD: Phiên bản hiện tại của nhánh đang làm việc.
- Nhánh được merge: Phiên bản cần tích hợp vào nhánh hiện tại.

Git so sánh sự thay đổi của hai nhánh so với merge base. Nếu những thay đổi không xung đột, Git có thể tự động kết hợp. Nếu hai nhánh sửa cùng một dòng theo các cách khác nhau, Git có thể phát sinh merge conflict và yêu cầu lập trình viên giải quyết.

Trong Lab 03, hai nhánh `feature/vietnamese-messages` và `feature/show-added-title` đều bắt đầu từ commit `ca5c926`.

Dev 1 thay đổi thông báo sang tiếng Việt, còn Dev 2 bổ sung tên DVD vào cùng một dòng. Sau khi PR #10 được merge vào master, Dev 2 chạy `git merge origin/master` và gặp conflict trong `aims/cart.py`.

Xung đột được giải quyết bằng cách kết hợp hai thay đổi:

`print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")`

Sau đó, cả bốn Unit Test đều PASS.

## Câu 2. Vì sao master và release/* phải sử dụng revert thay vì reset?

Các nhánh `master` và `release/*` thường là nhánh dùng chung, chứa lịch sử tích hợp mã nguồn hoặc các phiên bản phát hành.

`git reset` di chuyển con trỏ nhánh về một commit khác. Nếu dùng reset để xóa các commit đã được push, sau đó force-push, lịch sử nhánh trên remote sẽ bị viết lại. Điều này có thể làm mất dấu vết thay đổi, gây sai lệch lịch sử giữa các thành viên và ảnh hưởng đến việc truy vết phiên bản.

Ngược lại, `git revert` tạo một commit mới để đảo ngược tác động của commit trước đó, không xóa commit cũ khỏi lịch sử.

Vì vậy, khi cần hoàn tác thay đổi đã được chia sẻ trên `master` hoặc `release/*`, nên sử dụng revert thông qua Pull Request để giữ lịch sử minh bạch và có thể kiểm tra.

Trong Lab 03, nhóm thực hành:
- `git reset --soft`, `--mixed` và `--hard` trên nhánh nháp `topic/undo-practice`.
- `git reflog` để tìm lại và khôi phục commit `12a7c05`.
- `git revert -m 1 6ad35d9` trên nhánh `bugfix/revert-show-added-title`.
- Tạo PR #12 và merge vào master để hoàn tác thay đổi của PR #11.

Sau khi revert, thông báo tiếng Việt vẫn được giữ lại nhưng không còn hiển thị tên DVD. Các commit cũ vẫn tồn tại trong lịch sử Git và cả bốn Unit Test đều PASS.

## Kết luận

Merge base giúp Git xác định điểm chung để kết hợp các nhánh và phát hiện xung đột. Reset phù hợp với việc điều chỉnh lịch sử cục bộ chưa chia sẻ, trong khi revert phù hợp để hoàn tác an toàn trên các nhánh dùng chung.

Lab 03 đã thực hành đầy đủ quy trình bugfix, giải quyết merge conflict và hoàn tác thay đổi có kiểm soát.
