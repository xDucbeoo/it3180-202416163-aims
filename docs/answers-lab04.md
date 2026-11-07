# Lab 04 – Discussion Answers

## Câu 1. Vì sao không merge nhánh `release/*` ngược vào `master`?

Trong quy trình Release Flow được sử dụng trong bài thực hành, `master` là nhánh phát triển chính, còn các nhánh `release/*` dùng để lưu và bảo trì những phiên bản đã phát hành.

Việc merge toàn bộ nhánh `release/*` ngược vào `master` có thể đưa theo các thay đổi chỉ dành riêng cho phiên bản cũ, chẳng hạn như số phiên bản, CHANGELOG hoặc các điều chỉnh phục vụ bảo trì. Điều này dễ gây xung đột và ảnh hưởng đến phiên bản đang phát triển.

Thay vào đó, khi có lỗi cần sửa trên nhiều phiên bản, chúng ta có thể sử dụng `git cherry-pick -x` để đưa đúng commit sửa lỗi sang các nhánh liên quan, đồng thời giữ được thông tin truy vết commit gốc.

**Ví dụ trong bài thực hành:**

Sau khi phát hành `v1.0.0`, chúng ta bổ sung `sort_by_title()` và `sort_by_cost()` trên `master`. Trong khi đó, `release/lab04` và tag `v1.0.0` vẫn giữ nguyên ở commit `3894539`.

Kết quả này cho thấy việc phát triển tính năng mới không làm thay đổi bản phát hành cũ.

## Câu 2. So sánh Release Flow với GitFlow

Release Flow trong bài thực hành và GitFlow đều sử dụng các nhánh Git để kiểm soát thay đổi và quản lý phiên bản phần mềm. Tuy nhiên, hai mô hình có những điểm khác biệt.

| Tiêu chí | Release Flow trong bài thực hành | GitFlow |
|---|---|---|
| Nhánh phát triển chính | `master` | `develop` |
| Nhánh phiên bản ổn định | `release/*` kết hợp với tag | `main`/`master` kết hợp với tag |
| Phát triển tính năng | Tạo `feature/*` từ `master` | Tạo `feature/*` từ `develop` |
| Nhánh release | Lưu và bảo trì phiên bản đã phát hành | Chuẩn bị và ổn định phiên bản trước phát hành |
| Lan truyền sửa lỗi | Có thể dùng `cherry-pick -x` để đưa commit sửa lỗi sang các dòng phiên bản | Thường merge hotfix vào các nhánh chính cần cập nhật |
| Mức độ phức tạp | Tương đối đơn giản, tập trung vào một nhánh phát triển chính | Phức tạp hơn, có quy trình riêng cho phát triển và phát hành |

**Nhận xét:**

Release Flow trong bài thực hành phù hợp để quản lý nhiều phiên bản phát hành song song mà không cần duy trì một nhánh `develop` riêng biệt.

GitFlow có cấu trúc phân nhánh rõ ràng, phù hợp với những dự án có chu kỳ phát hành được tổ chức chặt chẽ. Tuy nhiên, việc quản lý nhiều nhánh và đồng bộ thay đổi có thể phức tạp hơn.

Cả hai mô hình đều cần tuân thủ nguyên tắc kiểm soát thay đổi, kiểm thử và truy vết lịch sử phát triển.

## Câu 3. Vì sao phát hành phiên bản `1.0.0` mà không phải `0.4.0`?

Theo Semantic Versioning, phiên bản phần mềm được biểu diễn theo cấu trúc:

`MAJOR.MINOR.PATCH`

Trong đó:

- **MAJOR:** Tăng khi có thay đổi không tương thích với phiên bản trước.
- **MINOR:** Tăng khi bổ sung tính năng mới nhưng vẫn đảm bảo tương thích.
- **PATCH:** Tăng khi sửa lỗi mà không làm thay đổi tính tương thích của giao diện công khai.

Các phiên bản bắt đầu bằng `0.y.z` thường được sử dụng trong giai đoạn phát triển ban đầu, khi phần mềm chưa cam kết giao diện ổn định.

Trong bài thực hành, các phiên bản `v0.1.0`, `v0.2.0` và `v0.3.0` tương ứng với những mốc hoàn thành Lab 01, Lab 02 và Lab 03.

Sau khi hoàn thiện các chức năng cơ bản, sửa lỗi và kiểm thử thành công, nhóm lựa chọn `v1.0.0` để đánh dấu bản phát hành ổn định đầu tiên của AIMS-mini.

Việc sử dụng `1.0.0` thể hiện quyết định công bố một phiên bản ổn định, thay vì tiếp tục coi phần mềm đang ở giai đoạn phát triển ban đầu như `0.4.0`.

**Kết luận:** Việc chuyển từ `0.3.0` lên `1.0.0` không bắt buộc chỉ vì đã hoàn thành ba phiên bản trước đó. Đây là quyết định phát hành, phản ánh mức độ sẵn sàng và cam kết ổn định của phần mềm.

---

## Tổng kết Lab 04

Qua Lab 04, chúng ta đã thực hành:

- Quản lý phiên bản theo Semantic Versioning.
- Ghi nhận thay đổi bằng `CHANGELOG.md`.
- Tạo và bảo vệ các nhánh `release/*`.
- Tạo Annotated Tags cho các phiên bản.
- Xuất bản GitHub Release `v1.0.0`.
- Phát triển tính năng mới trên `master` mà không ảnh hưởng đến bản phát hành.
- So sánh lịch sử các nhánh bằng `git log A..B`.
- Tái tạo phiên bản cũ bằng Detached HEAD và Git Worktree.
- Kiểm toán cấu hình và đóng gói mã nguồn bằng `git archive`.