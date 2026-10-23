# Mô hình dữ liệu

Mọi bản ghi là JSON UTF-8 có `schema_version`. Validator (`python tools/puzzles.py validate`) kiểm tra các ràng buộc mô tả dưới đây.

## `project.json`: sổ đăng ký đường dẫn

| Khóa | Giá trị | Vai trò |
|---|---|---|
| `default_edition` | `classroom` | ấn phẩm dùng khi không truyền `--edition` |
| `puzzles` | `knowledge/puzzles` | ngân hàng bài |
| `taxonomy`, `cards` | `knowledge/…` | tri thức dùng chung |
| `sources` | `sources/registry.json` | danh mục nguồn kèm checksum |
| `editions` | `editions` | cấu hình ấn phẩm |
| `publications` | `publications` | nơi phát hành PDF |
| `assets`, `build` | thư mục tương ứng | |

Code đọc mọi đường dẫn từ file này. Muốn dời một thư mục thì chỉ cần sửa ở đây.

## Một bài: `knowledge/puzzles/PZ-xxxx/`

Tên thư mục phải trùng với `id` (`PZ-` + 4 chữ số). ID độc lập với số thứ tự trong sách.

### `puzzle.json`

| Trường | Ý nghĩa |
|---|---|
| `id`, `title` | ID ổn định và tên bài |
| `statement` | Đề bài (LaTeX inline `$…$`). `{{DATA}}` là chỗ renderer chèn bảng hoặc chuỗi sinh từ `instance` |
| `instance` | Dữ kiện có cấu trúc (`kind`; `columns` + `records` cho bảng; hoặc tham số như `n`, `heaps`, `grid`…). Đề có `{{DATA}}` thì bắt buộc có `instance` |
| `aliases` | Tên gọi khác; `show` và `search` đều nhận alias |
| `figure_id` | Hình `assets/figures/<figure_id>_tikz.tex`, hoặc `null` |
| `figure_model` | Mô hình hình học vẽ chính xác từ dữ liệu (ví dụ `buildings`) |
| `difficulty.stars` | Số sao, từ 1 đến 5 |
| `difficulty.rationale`, `target_population`, `basis`, `status`, `assessed_on` | Căn cứ đánh giá độ khó ([rubric](../knowledge/difficulty-rubric.md)) |
| `analysis.concept_ids`, `technique_ids`, `prerequisite_ids` | Nhãn lấy từ [taxonomy.json](../knowledge/taxonomy.json), không trùng lặp |
| `analysis.concept_roles`, `technique_roles` | `{nhãn: vai trò}`; vai trò thuộc `primary`, `supporting`, `alternative`, `verification`, `generalization`. Khóa phải là nhãn đã gán cho bài |
| `analysis.cognitive_level` | `C1`–`C4`, hoặc `null` nếu chưa đánh giá |
| `analysis.status`, `rationale` | `not-assessed`, `suggested` hoặc `reviewed`. Khác `not-assessed` thì phải có `rationale` |

### `solution.json`

| Trường | Ý nghĩa |
|---|---|
| `answer`, `outline` | Đáp số ngắn và hướng giải |
| `teaching_notes` | Gợi ý tổ chức lớp, phần khởi động. Chỉ in trong bản giảng viên |
| `pedagogical_notes` | Tư duy cần rèn, lỗi thường gặp, liên hệ với bài khác. Chỉ in trong bản giảng viên |
| `proof`, `complexity`, `optimality` | Để `null` khi chưa biên soạn |
| `scope` | `answer-only`, `answer-and-outline` hoặc `full-proof` (phải có `proof`) |
| `status` | `draft` hoặc `reviewed` (phải có reviewer + ngày trong `review.json`) |
| `evidence` | `{source_id, record_index}` trỏ tới một bản ghi trong nguồn JSON đã đăng ký, hoặc `null` |

`scope` và `status` là hai trục độc lập: một hướng giải đã được đọc kỹ vẫn chưa phải là chứng minh đầy đủ.

> [!IMPORTANT]
> Knowledge card lưu **SHA-256 của bytes file `solution.json`**. Mọi chỉnh sửa file này, kể cả chỉ đổi định dạng, đều buộc phải đối chiếu lại các card liên quan.

### `review.json`

`statement`, `solution`, `taxonomy`, `figure`: trạng thái của từng khía cạnh. `reviewer`, `reviewed_on`: người review và ngày review. `notes`: ghi chú.

### `provenance.json`

`author`, `created_on` (với bài mới). `catalog_headings`: mục tương ứng trong catalog ứng viên. `external_sources`: nguồn ngoài, có định vị cụ thể. `external_source_status`: `not-recorded`, `partial` hoặc `verified`.

## Tri thức chung

- **`taxonomy.json`**: gồm `concepts` và `techniques` (mỗi mục có `id`, `label`, `definition`), `cognitive_levels`, `assignment_roles`. Có thể thêm nhãn mới, nhưng không đổi ID của nhãn đang được dùng.
- **`cards/KC-*.json`**: gồm `claim`, `conditions`, `when_to_use`, `reasoning`, `pitfalls`, `examples`, `evidence` (`puzzle_id` + hash đề + hash lời giải), và `status` (`draft` hoặc `reviewed`).

## Ấn phẩm: `editions/<id>/edition.json`

| Trường | Ý nghĩa |
|---|---|
| `id` | Trùng tên thư mục, dạng kebab-case |
| `title`, `edition` | Tên và năm ấn bản |
| `output_name` | Tên file phát hành: `publications/<output_name>-student.pdf` và `-instructor.pdf` |
| `expected_count` | Phải bằng tổng số bài được chọn |
| `sections[].puzzle_ids` | Danh sách ID theo thứ tự in; mỗi ID chỉ xuất hiện một lần |
| `pedagogy.difficulty_order` | `nondecreasing-within-section`: số sao trong mỗi phần không được giảm |
| `layout` | Font, các hình đặt cạnh hoặc ẩn, `puzzle_layouts` (chế độ đặt hình, `width_mm`, `crop`, `raster_path`), `minimum_raster_ppi` |
| `renderer`, `renderer_dependencies` | Script sinh LaTeX và các module nó dùng (đều được tính vào checksum) |
| `pagination` | Các điểm ngắt trang thủ công |

`raster_path` tính tương đối từ `assets/figures/` và có thể trỏ sang `../masters/` để dùng PNG gốc. Validator kiểm tra độ phân giải thực (ppi) theo kích thước in và phần bị crop.
