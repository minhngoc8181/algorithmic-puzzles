# Quy tắc dàn trang và kiểm tra bản in

Sách có một cột đọc chính, A4 hai mặt, lề trong 22 mm, lề ngoài 21 mm, trên 24 mm và dưới 23 mm. Mỗi bài là một khối gồm tiêu đề, đề và hình liên quan; giữ khối cùng trang. Chương mới mở ở trang mới. Khoảng trắng cuối chương được giữ có chủ đích; không kéo giãn chữ hoặc tranh để lấp trang.

Cân đối hai trang cuối chương khi dàn tự động đẩy một bài ngắn sang trang riêng. Các điểm ngắt đã xem trực tiếp nằm trong `pagination` của cấu hình ấn phẩm; cần review lại nếu nội dung hoặc hình thay đổi. Khoảng trắng ở hai trang cuối được phân bố lại, không thu nhỏ chữ.

## Vị trí và kích thước hình

Không có một quy tắc bắt buộc mọi hình phải ở trước hoặc sau chữ. Ở tuyển tập này, dải kiến, hàng slime và cảnh ếch giúp nhận diện tình huống trước khi đọc nên đặt sau tiêu đề, trước đề. Tranh gọn đặt bên phải đoạn văn liên quan để mắt bắt đầu đọc ở lề trái. Kích thước thay đổi theo nội dung tranh, lượng chữ, khả năng đếm/nhận diện chi tiết và độ phân giải thực tế.

- `banner-before`: hình ngang mở đầu, canh giữa, chiều rộng riêng từng bài; không phóng hết trang chỉ vì ảnh có khung ngang.
- `text-only`: đề và bảng/chuỗi dùng toàn chiều ngang; không có tranh hoặc khoảng trống giữ chỗ cho tranh đã bỏ.
- `data-inline`: hình có nhãn mang đầy đủ dữ kiện, đặt ngay tại vị trí bảng trong đề; không in thêm bảng hoặc hình lặp lại.
- `side-right`: đề ngắn hoặc phần giới thiệu trước bảng, căn đỉnh chữ và hình. Hình chỉ chiếm diện tích cần thiết.
- `wrap-right`: văn xuôi dài chảy cạnh hình rồi trở về toàn chiều ngang dưới hình, tạo phần chữ hình chữ L. Dùng cho 11 bài đủ chữ; không dùng cho bảng hoặc danh sách. Kết thúc phần wrap trong cùng khối bài.
- Bảng dữ liệu trở lại toàn chiều ngang trang. Giữ thứ tự giới thiệu → bảng → yêu cầu, không để bảng mắc trong cột hẹp.
- Hình dữ kiện vẽ bằng TeX giữ cỡ nhãn thật. Hình 15-puzzle chỉ giữ bảng ban đầu; bỏ lưới ghi chú rỗng bên cạnh để không chiếm cột chữ hoặc tràn lề.
- Khoảng cách chữ–hình 5 mm; khoảng cách giữa các bài 6 mm. Không buộc mọi ảnh cao 48 mm. Crop khoảng trắng thừa khi cần, không cắt mất đối tượng hoặc dữ kiện.
- Hình được chữ bao quanh có thêm 2 mm khoảng cách trên/dưới, để chữ chuyển về chiều ngang đầy đủ không chạm mép tranh.

[`wrapfig`](https://mirrors.ctan.org/macros/latex/contrib/wrapfig/wrapfig-doc.pdf) cho phép chữ bao quanh hình trong minipage, nhưng yêu cầu kết thúc wrap trước khi đóng nhóm và tránh danh sách/ngắt trang. Renderer dùng vị trí cố định trong khối bài; không dùng float tự trôi sang bài khác.

## Chữ và caption

Thân bài Charis SIL 11 pt; tiêu đề Inter; nhãn/bảng 10 pt, caption 9,5 pt. Các cỡ tương ứng trong glyph PDF xấp xỉ 10,909 / 9,963 / 9,465 PDF pt do quy đổi TeX point. Chỉ số toán học và số trang nhỏ hơn có chủ đích.

Caption nằm ngoài bitmap, ngắn, trung tính và canh giữa theo **chiều rộng hình**, kể cả trong cột bên phải. Không cần caption chỉ để lặp tên bài. Caption cần thiết giải thích mã màu hoặc xác định hình là trích đoạn. Không dùng caption để gợi phương pháp giải. Không thu cả sơ đồ có chữ để ép vào chỗ trống.

## PNG nguồn và JPG dùng in

PNG gốc nằm trong `assets/masters/`, giữ nguyên byte. JPG trong `assets/figures/` là bản nhẹ dùng in.

Độ phân giải hữu ích phụ thuộc kích thước sử dụng: `ppi = số pixel ngang còn lại sau crop / (chiều rộng in mm / 25,4)`. Không chỉ đọc trường DPI trong metadata. JPG 1.200 px đạt 300 ppi khi in rộng tối đa 101,6 mm; JPG 1.000 px đạt ở 84,7 mm. Đoàn người đội mũ dùng PNG nguồn vì JPG thiếu pixel ở kích thước đã chọn. Hàng tiền đã thay bằng vector; những tranh còn lại ưu tiên JPG. Không tạo thêm pixel bằng upscale.

Mức 300 ppi cho tranh màu liên tục tham khảo [hướng dẫn artwork của Cambridge University Press](https://www.cambridge.org/core/services/authors/journals-artwork-guide). Tranh có đường nét hoặc chữ rất nhỏ cần nguồn tốt hơn; sơ đồ/nhãn ở sách này ưu tiên TeX vector. Đây là kiểm tra pixel và khả năng đọc ở kích thước đã chọn, chưa phải một bản in thử trên giấy. Hình bìa rộng 1.774 px ở 160 mm, xấp xỉ 282 ppi; đây là ngoại lệ, cần nguồn lớn hơn nếu in bìa chất lượng cao.

`tools/artwork.py` đọc header PNG/JPEG bằng thư viện chuẩn Python và chặn build khi raster đề bài dưới 300 ppi, đường dẫn sai, crop không hợp lệ hoặc bảng bị đặt vào chế độ wrap. Cấu hình chi tiết ở [edition.json](edition.json); không cần Pillow để build.

Kiểm chất lượng raster và quyết định có dùng raster là hai bước riêng: tranh đạt ppi vẫn có thể bị bỏ nếu không giúp đọc đề. Lý do bỏ hoặc thay từng hình ghi trong `layout.puzzle_layouts.<ID>.reason` của [edition.json](edition.json).

## Review nội dung hình

Tranh có số lượng cụ thể phải được đếm đối chiếu với dữ kiện. Raster sai số lượng không được dùng; thay bằng hình TeX vẽ đúng dữ kiện, giữ nguyên PNG/JPG nguồn. Tranh biểu trưng (ví dụ kiến có tên) không quyết định vị trí hay số lượng; bảng mới là dữ kiện.

## Kiểm tra mỗi lần dựng

1. Validate nguồn, crop và ppi; render từ ngân hàng hiện hành.
2. XeLaTeX hai lượt cho mỗi PDF. Build không công bố bản mới nếu có Overfull box, thiếu glyph hoặc cảnh báo wrapfig; xem `.log` và `.fls` trong thư mục logs.
3. Kiểm đủ tiêu đề theo selection, dữ kiện, font, biên trang và vị trí raster; bản giảng viên không có tranh đề, bìa, mục lục hay ID nội bộ.
4. Xem toàn bộ trang ở kích thước đọc và phóng các hình có nhiều vật/nhãn. Kiểm khoảng trắng, chữ bao quanh hình, caption và sự gắn kết của tiêu đề–đề–hình. Giữ các cặp bài đối chiếu (cùng dữ liệu, khác điều kiện) trên cùng trang khi có thể.

TeX, log và báo cáo ở `build/classroom/`, được ignore. Chỉ khi build thành công hai PDF mới được chép vào `publications/`. Khi thay đề/hình, kiểm lại PDF cuối thay vì coi ảnh đẹp ở độ phóng lớn là đủ.
