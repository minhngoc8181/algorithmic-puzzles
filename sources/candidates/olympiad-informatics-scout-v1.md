# Olympic Tin học — nguồn bổ sung để nghiên cứu puzzle hóa (vòng 2)

**Ngày:** 2026-10-24. **Trạng thái:** bản khảo sát nguồn, chưa phải đề bài hoặc lời giải được thẩm định. **Repository đích:** `minhngoc8181/algorithmic-puzzles`, khu vực đề xuất `sources/candidates/`.

## Phương pháp

- Phân biệt **nguồn cấp cuộc thi** (chỉ mới nhận diện kho đề) với **ứng viên cấp bài** (có link trực tiếp). Không suy luận nội dung từ nhan đề nếu chưa đọc đề.
- Ưu tiên dạng có thể giải bằng suy luận trên ví dụ nhỏ: interactive, giao thức thông tin, trò chơi chiến lược, dựng cấu hình, bất biến, parity, đồ thị và tối ưu vận chuyển.
- So với `knowledge/puzzles/INDEX.md` (60 bài) và `sources/candidates/catalog-72-v0.1.md` (72 ứng viên). Trùng hoặc gần không đồng nghĩa là không thể viết puzzle khác; cần so cơ chế, mục tiêu, chứng minh và lời giải.
- Trong mọi lượt tiếp theo, ghi `competition`, `year`, `original_url`, `archive_url`, `task_name`, `statement_checked`, `editorial_checked`, `similar_PZ_AP`, `puzzle_seed`, `novelty_confidence`, `license_notes`.

## Kho nguồn chính cần thu thập định kỳ

| Nhóm | Nguồn (điểm vào) | Mức khai thác | Lưu ý |
|---|---|---|---|
| International Olympiad in Informatics (IOI) | https://ioinformatics.org/ và https://oj.uz/problems/source/ioi | Toàn bộ năm, đặc biệt interactive/communication | Ưu tiên đề PDF chính thức, tài liệu grader, editorial |
| Asia-Pacific Informatics Olympiad (APIO) | https://oj.uz/problems/source/apio | Tất cả năm | Bài khu vực có insight tổ hợp và cấu trúc dữ liệu |
| Japanese Olympiad in Informatics (JOI) | https://www.ioi-jp.org/ và https://oj.uz/problems/source/joi | Final, Spring Camp, Open Contest | Cần tra cả bản tiếng Nhật và bản dịch |
| Polish Olympiad in Informatics (POI/OI) | https://oi.edu.pl/ | Các vòng OI toàn lịch sử | Rất nhiều bài chiến lược, constructive, mô hình lạ |
| Baltic Olympiad in Informatics (BOI) | https://oj.uz/problems/source/boi | BOI toàn lịch sử | Các bài game, truy vấn, đồ thị |
| Central European Olympiad in Informatics (CEOI) | https://oj.uz/problems/source/ceoi | CEOI toàn lịch sử | Problem statement/editorial theo năm |
| Croatian Open Competition in Informatics (COCI) | https://hsin.hr/coci/ | Các vòng theo mùa | Dạng bài dễ hạ xuống puzzle giấy-bút |
| European Girls' Olympiad in Informatics (EGOI) | https://egoi.org/ và https://oj.uz/problems/source/egoi | Mọi năm | Bài constructive và tư duy toán dễ diễn giải |
| European Junior Olympiad in Informatics (EJOI) | https://ejoi.org/ và https://oj.uz/problems/source/ejoi | Mọi năm | Hợp thiết kế puzzle trung học |
| USACO (Hoa Kỳ) | https://usaco.org/ và https://usaco.guide/ | US Open, Gold, Platinum, Silver | Bài thường có tình huống kể chuyện tốt |
| NOI/NOIP (Trung Quốc) | https://www.noi.cn/ và https://www.luogu.com.cn/ | NOI, NOIP, CSP-S, WC | Xác minh link gốc; nhiều bản dịch không chính thức |
| Vietnam VOI/HSGQG, VNOI Cup | https://oj.vnoi.info/ và https://vnoi.info/ | Các kỳ thi quốc gia, đội tuyển, VNOI Cup | Phân biệt đề quốc gia và đề OJ tái đăng |
| Australian Informatics Olympiad (AIO) | https://orac.amt.edu.au/ | Đề AIO theo năm | Đối tượng tương đối phù hợp puzzle học sinh |
| Singapore NOI | https://noisg.comp.nus.edu.sg/ | Theo năm | Tra archive và editorial nếu có |

## Ứng viên bài cụ thể và hướng puzzle hóa (danh sách đầu)

**Nhãn:** `X` = đã xác nhận kho đề và liên kết bài trực tiếp, phải đọc lại chi tiết khi biên tập; `V` = tên/link ứng viên cần kiểm tra lại trên OJ và đề PDF; `G` = gần hạt nhân bài trong repo. Mọi hướng puzzle hóa là ý tưởng biên tập chứ không phải tóm tắt chuẩn luật đề.

| # | Kỳ thi | Bài và nguồn | Hướng nghiên cứu / gợi ý chuyển thể | Nhãn | So với repo |
|---:|---|---|---|---|---|
| 1 | IOI 2024 | [Message](https://oj.uz/problem/view/IOI24_message) | Mã hóa thông tin khi kênh có phần bị kiểm soát; puzzle mật thư/giao thức hai người | X | Gần AP-58, nhưng cơ chế khác |
| 2 | IOI 2024 | [Sphinx's Riddle](https://oj.uz/problem/view/IOI24_sphinx) | Phục dựng màu/nhóm ẩn thông qua thí nghiệm có giới hạn | X | Gần AP-06/AP-09 về thông tin |
| 3 | IOI 2020 | [Mushrooms](https://oj.uz/problem/view/IOI20_mushrooms) | Phân loại nấm chỉ bằng loại thử nghiệm tương tác cho phép | X | Gần PZ-0004 về số phép thử |
| 4 | IOI 2022 | [Insects](https://oj.uz/problem/view/IOI22_insects) | Khám phá các loài côn trùng bằng thiết bị so sánh số loại hiện diện | X | Gần nhóm information |
| 5 | IOI 2018 | [Combo](https://oj.uz/problem/view/IOI18_combo) | Tìm tổ hợp bí mật theo câu hỏi về tiền tố | X | Gần AP-06 |
| 6 | IOI 2022 | [Prisoner Challenge](https://oj.uz/problem/view/IOI22_prison) | Thiết kế giao thức quyết định thông qua trạng thái hữu hạn | X | Gần PZ-0012/13 theo bối cảnh, khác bài |
| 7 | IOI 2023 | [Longest Trip](https://oj.uz/problem/view/IOI23_longesttrip) | Tìm đường đi dài trong cấu trúc chỉ khám phá được bằng truy vấn | X | Mới sơ bộ |
| 8 | IOI 2019 | [Split](https://oj.uz/problem/view/IOI19_split) | Chia mạng thành nhóm có kích thước yêu cầu | V | Gần PZ-0045 về chia nhóm, khác đồ thị |
| 9 | IOI 2019 | [Shoes](https://oj.uz/problem/view/IOI19_shoes) | Ghép đôi giày sau tối thiểu lần đổi chỗ kề nhau | V | Gần AP-14 (inversion), cơ chế khác |
| 10 | IOI 2021 | [Keys](https://oj.uz/problem/view/IOI21_keys) | Lộ trình thu chìa khóa và mở phòng; trạng thái thay đổi đường đi | V | Mới sơ bộ |
| 11 | IOI 2021 | [Mutating DNA](https://oj.uz/problem/view/IOI21_dna) | Chuyển chuỗi bằng thao tác trao đổi có giới hạn | V | Mới sơ bộ |
| 12 | IOI 2023 | [Robot Contest](https://oj.uz/problem/view/IOI23_robot) | Trò robot và chiến lược điều khiển | V | Mới sơ bộ |
| 13 | IOI 2023 | [Closing Time](https://oj.uz/problem/view/IOI23_closing) | Cách chọn vị trí/giờ để phục vụ số đối tượng tối đa | V | Gần nhóm tối ưu |
| 14 | IOI 2024 | [Nile](https://oj.uz/problem/view/IOI24_nile) | Ghép/cân bằng vật phẩm theo chi phí | V | Gần nhóm DP |
| 15 | IOI 2024 | [Hieroglyphs](https://oj.uz/problem/view/IOI24_hieroglyphs) | Thống nhất thứ tự/biểu diễn từ hai dãy ký hiệu | V | Gần AP-60/61 về encoding |
| 16 | IOI 2024 | [Tree](https://oj.uz/problem/view/IOI24_tree) | Ràng buộc trên một cây; tìm biểu diễn hoặc phân bổ tối ưu | V | Cần đọc đề |
| 17 | IOI 2022 | [Fish](https://oj.uz/problem/view/IOI22_fish) | Quy hoạch chọn ô trên lưới; tìm quy luật thủ công cho bảng nhỏ | V | Mới sơ bộ |
| 18 | IOI 2020 | [Biscuits](https://oj.uz/problem/view/IOI20_biscuits) | Đếm cách kết hợp các gói bánh theo lượng và quy tắc dùng | V | Gần AP-25 theo chủ đề |
| 19 | IOI 2020 | [Stations](https://oj.uz/problem/view/IOI20_stations) | Mã hóa nhãn các trạm để suy ra đường đi không cần toàn bản đồ | V | Có tiềm năng rất cao |
| 20 | IOI 2018 | [Werewolf](https://oj.uz/problem/view/IOI18_werewolf) | Đi qua mạng khi điều kiện cho phép chuyển dạng thay đổi | V | Mới sơ bộ |
| 21 | IOI 2018 | [Seats](https://oj.uz/problem/view/IOI18_seats) | Sắp chỗ và đánh giá thứ tự tối ưu | V | Gần nhóm hoán vị |
| 22 | IOI 2017 | [Simurgh](https://oj.uz/problem/view/IOI17_simurgh) | Tìm bộ cạnh bí mật trên đồ thị bằng phép thử cây | V | Có tiềm năng rất cao |
| 23 | IOI 2017 | [Prize](https://oj.uz/problem/view/IOI17_prize) | Tìm quà bí mật khi hỏi thứ hạng tương đối | V | Gần AP-01/AP-08 |
| 24 | IOI 2016 | [Messy](https://oj.uz/problem/view/IOI16_messy) | Khôi phục hoán vị bằng phép thêm/kiểm tra tập ký hiệu | V | Gần AP-61, khác mô hình hỏi |
| 25 | IOI 2016 | [Aliens](https://oj.uz/problem/view/IOI16_aliens) | Chụp/bao phủ các điểm bằng số lượt ít nhất | V | Gần AP-31 về cover |
| 26 | IOI 2015 | [Scales](https://oj.uz/problem/view/IOI15_scales) | Xác định thứ tự vật thể bằng một số phép so sánh đặc biệt | V | Gần PZ-0003/4 |
| 27 | IOI 2014 | [Game](https://oj.uz/problem/view/IOI14_game) | Trò chơi trên đồ thị, truy vấn và khả năng duy trì điều kiện | V | Mới sơ bộ |
| 28 | IOI 2013 | [Cave](https://oj.uz/problem/view/IOI13_cave) | Các công tắc bí mật điều khiển những cửa nào? | V | Có tiềm năng rất cao |
| 29 | IOI 2013 | [Robots](https://oj.uz/problem/view/IOI13_robots) | Phân công việc cho robot với các hạn chế tải trọng | V | Gần PZ-0046 nhưng khác |
| 30 | IOI 2012 | [Parachute Rings](https://oj.uz/problem/view/IOI12_rings) | Truy vết các cạnh của một vòng bí mật khi thêm cạnh | V | Cần kiểm tra tiêu đề bản gốc |

## Danh mục mở rộng theo từng quốc gia/khu vực (giai đoạn tuyển bài)

Các liên kết bên dưới dẫn đến **archive** và cần bóc tách task cụ thể ở vòng sau, không tính là ứng viên bài riêng:

1. **Ba Lan / POI:** lấy danh mục từng mùa từ [oi.edu.pl](https://oi.edu.pl/), ưu tiên các bài interactive/constructive/game, truy nguyên editorial tiếng Ba Lan.
2. **Nhật / JOI:** quét [JOI archive](https://www.ioi-jp.org/) và [oj.uz JOI](https://oj.uz/problems/source/joi); chia Final, Spring Camp, Open; loại các bài chỉ nặng cấu trúc dữ liệu.
3. **Croatia / COCI:** quét [HSIN COCI](https://hsin.hr/coci/) theo từng vòng; ưu tiên Bronze/Silver kiểu toán tổ hợp và bài có thế giới kể chuyện tự nhiên.
4. **BOI:** quét [BOI archive](https://oj.uz/problems/source/boi), nhất là bài giao thức giao tiếp và trò chơi.
5. **CEOI:** quét [CEOI archive](https://oj.uz/problems/source/ceoi); chú ý bài constructive và bài phép thử có nguồn tư duy mới.
6. **APIO:** quét [APIO archive](https://oj.uz/problems/source/apio), đặc biệt interactive, trò chơi, tối ưu trên cây có thể rút về n nhỏ.
7. **EGOI/EJOI:** quét [EGOI](https://egoi.org/) và [EJOI](https://ejoi.org/), bổ sung đề trình độ trung học.
8. **USACO:** lấy các năm 2010–2026 ở [USACO](https://usaco.org/), ưu tiên US Open, Gold/Platinum; đề Silver có puzzle hình thức rất tốt.
9. **Trung Quốc / NOI, NOIP, CSP-S:** lấy từ [NOI](https://www.noi.cn/) và đối chiếu [Luogu](https://www.luogu.com.cn/); không lấy tên Việt/Anh tự động làm tên gốc.
10. **Việt Nam / VOI, HSGQG, VNOI Cup:** quét [VNOJ](https://oj.vnoi.info/) và [VNOI](https://vnoi.info/), gắn nhãn riêng đề gốc và bản đăng lại.
11. **Australia / AIO:** tra [ORAC](https://orac.amt.edu.au/) và lựa các bài có thể mô phỏng trên giấy.
12. **Singapore / NOI:** tra [Singapore NOI](https://noisg.comp.nus.edu.sg/) và phân nhóm theo vòng thi.

## Chống trùng và tiêu chí chọn

- So trực tiếp với PZ-0003/0004/0009/0011/0012/0013/0017/0020/0031/0037/0038/0040/0045/0046/0048 và AP-01…AP-72, nhất là những bài cùng hạt nhân: identification-by-queries, coin-weighing, parity, XOR, merge-cost, game Grundy, interval covering, matching, partition.
- Có thể giữ biến thể gần nếu thay đổi luật tạo ra một **bất biến/chứng minh/chiến lược khác**; giải thích sự khác biệt cụ thể trong catalog.
- Tách `source_verified` / `statement_reviewed` / `puzzle_viable` / `solution_proven` / `originality_reviewed`. Không tự động nâng hạng một ứng viên thành bài sẵn sàng xuất bản.
- Đọc và trích dẫn nguồn gốc trước khi phóng tác; không sao chép nguyên văn đề/hình hoặc editorial dài vào sách khi chưa kiểm tra quyền sử dụng.

## Khuyến nghị thứ tự đọc sâu

**Wave A (interactive/information):** IOI 2024 Message, Sphinx; IOI 2020 Mushrooms, IOI 2022 Insects, IOI 2018 Combo, IOI 2017 Simurgh, IOI 2013 Cave, IOI 2016 Messy, IOI 2015 Scales, IOI 2020 Stations.

**Wave B (national/regional):** POI, JOI Spring Camp, COCI, APIO, BOI, CEOI; trích 15–30 task mỗi nguồn có URL gốc rồi lọc hạt nhân mới.

**Wave C (Vietnam & other):** VOI/HSGQG, VNOI Cup, NOI/NOIP, USACO, EGOI/EJOI, AIO, NOI Singapore; đối chiếu với hai catalog có sẵn trước khi phân loại.

**Tệp này lưu nghiên cứu ở `sources/candidates/`; không sửa `knowledge/`, `editions/`, `publications/` và không cập nhật registry nguồn đã đăng ký.**