# ③ Ấn phẩm

Mỗi thư mục con là một **ấn phẩm**. Ấn phẩm chọn bài từ ngân hàng chung, xếp bài vào các phần và quy định dàn trang. Nội dung bài không bị chép vào đây. Build phát hành hai PDF vào `publications/`.

| ID | Tên | PDF phát hành |
|---|---|---|
| [classroom](classroom/README.md) | Câu đố giải thuật (bản dạy học) | `publications/algorithmic-puzzles-{student,instructor}.pdf` |

## Mở rộng ấn phẩm hiện có

Thêm ID vào `sections[].puzzle_ids` trong `classroom/edition.json` và tăng `expected_count`. Số bài trên bìa và trên tiêu đề bản giảng viên được renderer tự cập nhật. Tên file PDF không chứa số bài, nên không phải đổi tên khi sách lớn dần.

## Tạo ấn phẩm mới

ID ấn phẩm đặt theo mục đích, viết thường, nối bằng gạch ngang, ví dụ `olympiad` hay `workshop-intro`.

```bash
cp -r editions/classroom editions/olympiad        # Windows: Copy-Item -Recurse editions\classroom editions\olympiad
```

1. Trong `edition.json`, sửa `id` (trùng tên thư mục), `title` và `output_name` (vd. `algorithmic-puzzles-olympiad`, phải khác với các ấn phẩm khác). Sau đó sửa `sections` và `expected_count`.
2. Xóa các mục `layout.puzzle_layouts` và `pagination` không còn dùng, thêm bố cục cho bài mới.
3. Nếu cần, chỉnh màu, chữ bìa và font trong `renderer.py`.
4. Build: `python tools/puzzles.py build --edition olympiad`.

Validator kiểm tra: ID bài có tồn tại và không trùng, tổng số bài khớp `expected_count`, số sao không giảm trong mỗi phần (nếu bật), đủ font và hình, và hình đạt ngưỡng ppi.
