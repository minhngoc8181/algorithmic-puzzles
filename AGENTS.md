# Quy tắc cho trợ lý AI

Áp dụng cho mọi agent (Codex, Gemini, Antigravity, …) khi sửa repository này.

## Cấu trúc

- Nội dung bài chỉ nằm trong `knowledge/puzzles/PZ-xxxx/{puzzle,solution,review,provenance}.json`. Không tạo file tổng hợp song song.
- File đã đăng ký trong `sources/registry.json` là bất biến.
- `editions/<id>/` chứa cấu hình ấn phẩm. `publications/` chỉ chứa PDF do `python build.py` phát hành; không sửa tay.
- `build/` và `local/` bị ignore. Không dùng chúng làm nguồn dữ liệu.
- Bài mới tạo bằng `python tools/puzzles.py new`. Sau mỗi thay đổi nội dung, chạy `python tools/puzzles.py index`, `validate` và `python -m unittest discover -s tests`.
- Không tự đặt `status: reviewed` cho lời giải, nhãn hay card. Chỉ người review có tên mới được đặt.

## Biên tập

Tuân theo [docs/editorial-style.md](docs/editorial-style.md).

Đề cho sinh viên chỉ chứa luật và mục tiêu, không gợi ý phương pháp giải. Dùng dữ kiện tổng quát khi phù hợp; dùng bộ số cụ thể khi cần một kết quả kiểm chứng được. Giữ nguyên các phiên bản kinh điển (ví dụ sáu con ếch); không tăng số lượng nếu không có lý do sư phạm.

Khi một bài nằm ở ranh giới giữa các chương, ưu tiên chương chiến lược hoặc trò chơi; chương thiết kế giải thuật là lựa chọn sau cùng. Xếp chương theo mục tiêu học chính, nhưng vẫn giữ đầy đủ nhãn concept/technique trong ngân hàng. Việc lời giải dùng DP, đệ quy hay chia để trị không phải lý do để chuyển một bài chiến lược hoặc trò chơi sang chương giải thuật.

Chọn hình theo vai trò giúp hiểu đề. Ưu tiên tranh sinh động cho bài có câu chuyện; bỏ cảnh trang trí làm rối bên cạnh bảng dữ kiện. Khi bản thân dữ kiện là hình học, dùng mô hình chính xác và không vẽ đáp án. Ưu tiên vector cho số lượng, ô lưới, tọa độ và nhãn cần chính xác. Chỉ dùng ảnh tạo ngoài khi thật cần, và phải review trước khi đưa vào `assets/`. Caption trung tính, canh giữa theo hình.

Bản giảng viên là tài liệu tham khảo đơn giản: không bìa, mục lục, hình minh họa đề, thông tin ấn bản, ID ngân hàng. Provenance chỉ lưu nội bộ, không in ra trong ấn phẩm.

## Git

Làm việc trên nhánh riêng và mở Pull Request vào `main` (xem [CONTRIBUTING.md](CONTRIBUTING.md)). Chỉ push khi người dùng cho phép.
