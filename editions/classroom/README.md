# Câu đố giải thuật: bản dạy học (`classroom`)

Ấn phẩm chính của dự án, gồm ba phần: **chiến lược & thông tin**, **trò chơi**, **thiết kế và phân tích giải thuật**. Trong mỗi phần, số sao không giảm. Mọi đề, hình và cả hai bản PDF tuân theo [docs/editorial-style.md](../../docs/editorial-style.md).

```bash
python build.py      # chạy từ thư mục gốc repository
```

Kết quả: [bản sinh viên](../../publications/algorithmic-puzzles-student.pdf) và [bản giảng viên](../../publications/algorithmic-puzzles-instructor.pdf).

| File | Vai trò |
|---|---|
| [edition.json](edition.json) | Chọn bài, chia phần, bố cục hình, ngắt trang |
| [renderer.py](renderer.py) | Sinh LaTeX. Thân bài khoảng 11 pt, nhãn 10 pt, caption 9.5 pt |
| [TYPOGRAPHY.md](TYPOGRAPHY.md) | Quy tắc dàn trang và danh sách kiểm tra khi xem PDF |

## Hai bản tài liệu

- **Bản sinh viên**: có bìa vàng kim/xanh ngọc, tranh minh họa và câu hỏi không dẫn tới phương pháp giải. Dùng dạng tổng quát khi cần học sinh phát hiện quy luật; dùng bộ số cụ thể khi cần kết quả để kiểm chứng.
- **Bản giảng viên**: đáp số, hướng giải, cách tổ chức dạy học và ý nghĩa sư phạm. Không có bìa, mục lục, hình đề hay ID ngân hàng.

## Chế độ đặt hình

`text-only` dùng cho đề có bảng hoặc chuỗi dữ kiện. `data-inline` đặt một hình có nhãn mang đủ dữ kiện ngay tại vị trí bảng. `model_kind: buildings` vẽ đúng tọa độ các tòa nhà mà không vẽ đường bao đáp án. Phần lớn tranh dùng JPG đạt 300 ppi khi in; khi JPG thiếu pixel ở kích thước đã chọn thì dùng PNG gốc trong `assets/masters/`.
