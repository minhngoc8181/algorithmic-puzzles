# ② Tri thức

Đây là nguồn chính của nội dung. Ấn phẩm, tìm kiếm và mọi mở rộng sau này đều đọc từ đây.

| Thành phần | Vị trí |
|---|---|
| Ngân hàng bài, mỗi bài một thư mục | [puzzles/](puzzles/), mục lục [puzzles/INDEX.md](puzzles/INDEX.md) |
| Taxonomy: 21 concept, 43 technique, 4 mức cognitive | [taxonomy.json](taxonomy.json) |
| Knowledge cards | [cards/](cards/) |
| Rubric độ khó | [difficulty-rubric.md](difficulty-rubric.md) |

Ý nghĩa từng trường: [docs/data-model.md](../docs/data-model.md).

## Mô hình kiến thức

Mỗi bài nối tới **concept**, **technique**, **prerequisites** và **cognitive demand** qua khối `analysis` trong `puzzle.json`. Độ khó và mức hoàn thiện lời giải là các trường riêng.

| Thành phần | Câu hỏi cần trả lời |
|---|---|
| Concept | Cấu trúc hoặc khái niệm nào làm bài có ý nghĩa? |
| Technique | Thao tác/phương pháp nào được dùng trong lời giải? |
| Prerequisites | Người học phải biết gì trước khi bắt đầu? |
| Cognitive demand | Đề yêu cầu thực hiện, lựa chọn, phát hiện/chứng minh hay khái quát? |
| Difficulty | Bài khó đến mức nào với đối tượng và kinh nghiệm cụ thể? |

Nhãn hiện ở trạng thái `suggested`, đã đối chiếu với outline và có rationale. `concept_roles` / `technique_roles` phân biệt phương pháp chính (`primary`) với phương pháp bổ trợ, phương pháp thay thế, cách kiểm chứng hoặc cách khái quát. Prerequisites đang để rỗng và cognitive để `null` vì **chưa đánh giá**, không có nghĩa là bài không cần kiến thức nền. Vị trí chương trong sách không thay thế nhãn kỹ thuật.

Taxonomy phục vụ môn giải thuật. Có thể thêm nhãn khi bài mới cần, nhưng không đổi ID nhãn đang được dùng.

## Knowledge cards

Card là **nguyên lý dùng lại được** rút ra từ nhiều bài:

- [Dung lượng quan sát](cards/KC-OBSERVATION-CAPACITY.json): phân biệt chặn đếm thông tin với việc xây dựng lịch thử hợp lệ.
- [Ràng buộc ghép](cards/KC-MERGE-CONSTRAINTS.json): nối dây bất kỳ và sáp nhập khối kề nhau dẫn tới hai miền nghiệm khác nhau.
- [Lịch sử cây đấu loại](cards/KC-TOURNAMENT-HISTORY.json): lưu chứng cứ so sánh để tìm phần tử lớn nhì.

`evidence` của card ghi hash đề và hash file lời giải. Khi bài liên quan thay đổi, validator buộc phải đối chiếu lại card. Cả ba card đang ở mức `draft`.

## Gợi ý dùng lại tri thức

- **Ra đề theo chủ đề:** `python tools/puzzles.py search --concept C-games --json`
- **Tìm cặp bài đối chiếu:** đọc `examples` trong các card, hoặc tìm theo cùng một technique.
- **Ấn phẩm mới:** chọn ID trong một edition ở [editions/](../editions/README.md). Không cần chép nội dung bài.
