# Lab 05 – Discussion Answers

## 1. Ưu và nhược điểm của upstream-first so với release-first

**Upstream-first** là sửa lỗi trên nhánh phát triển chính trước, sau đó lan truyền commit phù hợp sang các nhánh release.

- **Ưu điểm:** Nhánh chính sớm có bản sửa chuẩn; các nhánh release nhận cùng thay đổi qua commit có thể truy vết; giảm nguy cơ nhánh phát triển tiếp tục dựa trên lỗi đã biết.
- **Nhược điểm:** Việc sửa và kiểm thử trên nhánh chính có thể làm chậm bản vá khẩn cấp cho người dùng của một phiên bản ổn định. Cần cherry-pick chính xác và kiểm thử riêng trên từng release; khác biệt giữa các nhánh có thể gây xung đột.

**Release-first** là sửa và phát hành bản vá trên nhánh release bị ảnh hưởng trước, sau đó lan truyền sửa lỗi về nhánh chính và các release khác.

- **Ưu điểm:** Có thể ưu tiên khôi phục nhanh phiên bản đang được sử dụng mà không chờ chu kỳ phát triển của nhánh chính.
- **Nhược điểm:** Nếu quên hoặc trì hoãn lan truyền, lỗi có thể còn trên `master` hoặc các release khác. Khi lan truyền muộn, thay đổi có thể xung đột hoặc cần điều chỉnh thêm.

Hai cách đều cần ghi nhận quan hệ giữa các commit (ví dụ `git cherry-pick -x`) và kiểm thử từng nhánh. Chọn thứ tự dựa trên mức độ khẩn cấp của release và quy trình của dự án, không được bỏ qua bước lan truyền.

## 2. Kiểm toán để phát hiện sửa lỗi chưa được lan truyền

Dùng:

```bash
git cherry -v release/lab05 master
```

Lệnh so sánh các commit ở `master` với `release/lab05` theo nội dung patch. Dấu `+` cho biết commit từ `master` chưa có patch tương đương trên `release/lab05`; dấu `-` cho biết patch tương đương đã có, dù SHA khác do cherry-pick. Nếu bản sửa trên `master` hiện bằng dấu `+`, cần kiểm tra và lan truyền nó sang release.
