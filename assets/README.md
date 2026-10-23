# Tài nguyên dùng chung

| Thư mục | Nội dung |
|---|---|
| `figures/` | Hình dùng để in: `<ID>_tikz.tex` (wrapper LaTeX hoặc hình vector TikZ) cùng file JPG mà wrapper tham chiếu. `ILL-STYLE.tex` là style chung cho hình vector, `COVER_tikz.tex` là bìa |
| `masters/` | PNG gốc, độ phân giải cao, giữ nguyên bytes. JPG trong `figures/` là bản nén từ đây |
| `fonts/` | Charis SIL và Inter, được nạp trực tiếp khi build |

## Thêm hình cho một bài

1. Ưu tiên hình vector (TikZ) cho những gì cần chính xác: số lượng, ô lưới, tọa độ, nhãn. Dùng tranh raster cho phần bối cảnh câu chuyện.
2. Với tranh raster: lưu PNG gốc vào `masters/<ID>.png`, xuất JPG vào `figures/<ID>.jpg`, rồi tạo `figures/<ID>_tikz.tex` chứa `\includegraphics[width=\linewidth]{<ID>.jpg}`.
3. Ghi `figure_id: "<ID>"` trong `puzzle.json`, và nếu cần thì thêm bố cục vào `editions/<id>/edition.json → layout.puzzle_layouts`.
4. Độ phân giải tối thiểu là 300 ppi ở kích thước in: `ppi = số pixel ngang sau crop / (chiều rộng in tính bằng mm / 25,4)`. Validator sẽ chặn build nếu hình không đạt. Không upscale để lách ngưỡng.
5. Hình không được chứa đáp án, nước đi thắng hay mô hình mà người học cần tự khám phá. Ảnh do AI tạo phải được kiểm tra số lượng và chi tiết trước khi commit. Ảnh chưa duyệt để trong `local/` (bị ignore).
