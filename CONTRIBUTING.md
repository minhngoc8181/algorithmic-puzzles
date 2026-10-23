# Hướng dẫn cộng tác

Tài liệu này dành cho các giảng viên cùng soạn ngân hàng câu đố. Mục tiêu: nhiều người làm song song mà không giẫm chân nhau, và mọi thay đổi đều truy vết được qua Git.

## 1. Nguyên tắc cốt lõi

1. **Một bài = một thư mục** `knowledge/puzzles/PZ-xxxx/`. Sửa bài nào thì chỉ đụng tới thư mục của bài đó.
2. **ID là vĩnh viễn.** Không đổi và không dùng lại ID, kể cả khi bài bị bỏ khỏi một ấn phẩm. Số thứ tự trong sách chỉ do `edition.json` quyết định.
3. **Nguồn đã đăng ký là bất biến.** Validator kiểm SHA-256 của mọi file trong `sources/registry.json`.
4. **Đề không chứa gợi ý phương pháp.** Đọc [docs/editorial-style.md](docs/editorial-style.md) trước khi soạn.
5. **PDF chỉ sinh ra từ build.** Không sửa tay file trong `publications/`; chạy `python build.py` để cập nhật.

## 2. Quy trình Git

```bash
git switch main && git pull
git switch -c puzzle/<mo-ta-ngan>        # vd. puzzle/thap-ha-noi-bien-the, review/pz-0031, edition/olympiad
# … soạn, kiểm tra …
python tools/puzzles.py index
python tools/puzzles.py validate
python -m unittest discover -s tests
git add -A && git commit -m "PZ-0061: thêm bài Tháp Hà Nội biến thể"
git push -u origin HEAD                  # rồi mở Pull Request vào main
```

- Nhánh chính là `main`. Nên bật *branch protection* trên GitHub để mọi thay đổi phải qua Pull Request và có ít nhất một người duyệt.
- GitHub Actions ([.github/workflows/validate.yml](.github/workflows/validate.yml)) tự chạy validate, kiểm `INDEX.md` và chạy toàn bộ test cho mỗi PR.
- Commit message mở đầu bằng ID bài hoặc phạm vi thay đổi: `PZ-0031: …`, `taxonomy: …`, `edition: …`, `tools: …`.
- Chỉ người phụ trách phát hành mới chạy `python build.py` và commit PDF mới, để tránh xung đột trên file nhị phân.

## 3. Thêm bài mới

```bash
python tools/puzzles.py new "Tên câu đố" --author "Họ tên"
```

Lệnh tạo thư mục với ID kế tiếp, kèm bốn file nháp đã hợp lệ:

| File | Cần làm |
|---|---|
| `puzzle.json` | Viết `statement` (dùng `$…$` cho công thức; đặt `{{DATA}}` nếu có bảng dữ kiện trong `instance`). Điền `difficulty.stars` + `rationale` và `analysis.concept_ids` / `technique_ids`, lấy nhãn từ [taxonomy.json](knowledge/taxonomy.json) |
| `solution.json` | Viết `answer`, `outline`, `teaching_notes`, `pedagogical_notes`; thêm `proof` nếu có chứng minh đầy đủ |
| `provenance.json` | Ghi `external_sources` (sách, bài báo, đề thi gốc, có vị trí cụ thể), hoặc ghi rõ đây là sáng tác mới |
| `review.json` | Để trống cho đến khi có người thứ hai review |

Muốn đưa bài vào sách, thêm ID vào `sections[].puzzle_ids` và tăng `expected_count` trong [editions/classroom/edition.json](editions/classroom/edition.json).

Nếu đáp số tính được bằng máy, hãy thêm một test kiểm chứng vào [tests/test_puzzle_answers.py](tests/test_puzzle_answers.py). Đây là cách rẻ nhất để bắt lỗi đề.

**Trùng ID:** nếu hai PR cùng tạo `PZ-0061`, người merge sau đổi tên thư mục của mình sang ID trống kế tiếp, sửa trường `id` / `puzzle_id` trong cả bốn file, rồi chạy lại `index`.

**Lấy bài từ catalog ứng viên:** chọn một mục trong [sources/candidates/catalog-72-v0.1.md](sources/candidates/catalog-72-v0.1.md), tạo bài như trên, rồi ghi heading tương ứng vào `provenance.json → catalog_headings`.

## 4. Review

| Trường | Giá trị | Ràng buộc |
|---|---|---|
| `solution.status` | `draft` → `reviewed` | `reviewed` phải có `review.reviewer` + `review.reviewed_on` |
| `solution.scope` | `answer-only`, `answer-and-outline`, `full-proof` | `full-proof` phải có `proof` |
| `analysis.status` | `not-assessed` → `suggested` → `reviewed` | `reviewed` phải có người review |
| `card.status` | `draft` → `reviewed` | áp dụng cho knowledge card |

Người review **không** được là tác giả của bài. Test chạy qua không có nghĩa là bài đã được review. Validator từ chối mọi trạng thái `reviewed` thiếu người review hoặc ngày review.

Nếu bạn sửa đề hay lời giải của một bài đang làm bằng chứng cho knowledge card, validator sẽ báo `Stale knowledge evidence`. Khi đó hãy đọc lại card và cập nhật hash trong `evidence`.

## 5. Hình minh họa

Xem [assets/README.md](assets/README.md). Tóm tắt: hình dùng để in đặt trong `assets/figures/` (JPG ≥ 300 ppi ở kích thước in, kèm wrapper `<ID>_tikz.tex`); PNG gốc đặt trong `assets/masters/`. Hình không được chứa đáp án hay gợi ý cách giải.

## 6. Cái gì lên Git

| Lên Git | Không lên Git (`.gitignore`) |
|---|---|
| `sources/`, `knowledge/`, `editions/`, `assets/`, `docs/`, `tools/`, `tests/` | `build/`: LaTeX, log, manifest |
| `publications/*.pdf`: hai bản PDF phát hành | `local/`: nháp, ảnh chờ duyệt của từng máy |
| `knowledge/puzzles/INDEX.md` (sinh tự động nhưng commit để tiện duyệt) | cache Python, file tạm LaTeX, cấu hình IDE |

> [!CAUTION]
> Bản giảng viên có đáp án. Nếu repository để **public**, sinh viên có thể đọc được đáp án. Hãy để repo ở chế độ private, hoặc chỉ phát hành bản giảng viên qua kênh riêng.
