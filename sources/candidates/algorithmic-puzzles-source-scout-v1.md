# Khảo sát nguồn chuyển bài thi lập trình thành Algorithmic Puzzles — vòng 1

**Ngày khảo sát:** 23-10-2026. **Dự án đối chiếu:** [minhngoc8181/algorithmic-puzzles](https://github.com/minhngoc8181/algorithmic-puzzles) (`main`).

**Phạm vi:** Chỉ tìm kiếm, sàng lọc sơ bộ và đối chiếu ý tưởng; **chưa** sáng tác đề hoàn chỉnh, thử nghiệm đáp số/lời giải, kiểm chứng tính nguyên bản ngoài repo hoặc sửa repository. Tên và đường dẫn dẫn trực tiếp đến bài gốc; diễn giải puzzle hóa là định hướng biên tập, **không phải** phát biểu đề chuẩn.

Nguồn đối chiếu: `knowledge/puzzles/INDEX.md` (60 bài) và `sources/candidates/catalog-72-v0.1.md` (72 ứng viên, có phần giao nhau); mục có vẻ mới được so sánh **theo tên và lõi ý tưởng ở mức đầu tiên**, chưa được xác nhận mới tuyệt đối. **Trùng lõi** = cùng bài toán cơ bản dù cách kể khác; **Gần** = chia sẻ kỹ thuật/chủ đề nhưng có thể khác cơ chế thú vị; **Mới** = chưa thấy trùng trực tiếp trong hai danh mục; **Cần đọc** = liên kết nhận diện nhưng chi tiết đề chưa đủ kiểm chứng, không dùng để xuất bản ngay.

**A** = có tiềm năng tạo puzzle hấp dẫn (câu hỏi ngắn, cơ chế trực quan, insight tốt). **B** = có tiềm năng nhưng cần tìm biến thể/thu gọn. **C** = ít ưu tiên hoặc bị trùng. Đây là đánh giá biên tập sơ bộ, không phải xếp hạng khách quan hay chấm độ khó.

## Thống kê

- Tổng: **102** đề tham khảo, theo nguồn: Codeforces: 22, AtCoder: 18, VNOI/VNOJ: 22, LeetCode: 22, CSES: 10, IMO: 8.
- Ưu tiên: A: 67, B: 28, C: 7. Trạng thái đối chiếu: Mới: 75, Gần: 22, Cần đọc: 2, Trùng lõi: 3.

**Lưu ý:** IMO từ trang đề chính thức; IMO Shortlist khác IMO chính thức và nên được lập thành danh mục riêng. Một số bài VNOI khó đọc do hạn chế truy cập; đã gắn nhãn cần xác minh khi phù hợp. Không giả định mọi bài thi là tác phẩm mới tuyệt đối; nhiều vấn đề có gốc toán học cổ điển.

## Codeforces

| # | Bài gốc | Hạt nhân để puzzle hóa | Ưu tiên | Đối chiếu | Gần với bài hiện có |
|---:|---|---|:---:|---|---|
| 001 | [Bear and Prime 100](https://codeforces.com/contest/679/problem/A) | Bạn chỉ được hỏi số bí mật có chia hết cho một số hay không; thiết kế cây hỏi đoán tính nguyên tố | A | Mới | — |
| 002 | [Lost Numbers](https://codeforces.com/problemset/problem/1167/B) | Sáu số bí mật là hoán vị của một tập đặc biệt; chỉ được xem tích của hai ô | A | Mới | — |
| 003 | [Searching Local Minimum](https://codeforces.com/problemset/problem/1479/A) | Tìm một thung lũng trong dãy bí mật chỉ bằng vài lần hỏi độ cao | A | Mới | — |
| 004 | [Fixed Point Guessing](https://codeforces.com/problemset/problem/1698/D) | Tìm vị trí đứng đúng của hoán vị khi chỉ được xem các đoạn giới hạn | A | Mới | — |
| 005 | [Guess the Tree](https://codeforces.com/problemset/problem/2001/C) | Tái dựng cây vô hình với loại câu hỏi trả lời bằng một đỉnh | A | Mới | — |
| 006 | [Catch the Mole (Hard Version)](https://codeforces.com/problemset/problem/1990/E2) | Con chuột chũi trốn trên cây; đặt câu hỏi hợp lý để bắt kịp nó | A | Mới | — |
| 007 | [Corner Twist](https://codeforces.com/problemset/problem/1983/B) | Ma trận chữ số và phép xoay 2×2: trạng thái nào biến đổi được? | A | Gần | PZ-0031 / AP-57 (khác luật) |
| 008 | [Turtle and an Incomplete Sequence](https://codeforces.com/problemset/problem/1981/C) | Điền các ô số khuyết sao cho hai hàng xóm có quan hệ cây nhị phân | A | Mới | — |
| 009 | [Turtle and Multiplication](https://codeforces.com/problemset/problem/1981/D) | Tạo chuỗi dài mà mỗi tích của hai số kề nhau xuất hiện tối đa một lần | A | Mới | — |
| 010 | [Increasing Sequence with Fixed OR](https://codeforces.com/problemset/problem/1988/C) | Tìm dãy tăng dài nhất mà phép OR bit luôn giữ nguyên một con số đích | A | Mới | — |
| 011 | [Absolute Zero](https://codeforces.com/problemset/problem/1991/C) | Mỗi lượt chọn x và thay mọi số a bằng abs(a−x); có thể đưa tất cả về 0 không? | A | Mới | — |
| 012 | [MEXOR](https://codeforces.com/problemset/problem/2245/C) | Xếp hoán vị để các giá trị MEX và XOR của tiền tố đạt một điều kiện bí mật | A | Mới | — |
| 013 | [Coloring Game](https://codeforces.com/problemset/problem/1991/E) | Trò tô màu đồ thị: ai nên chọn màu, ai nên chọn đỉnh để luôn thắng? | A | Mới | — |
| 014 | [Grid Game](https://codeforces.com/problemset/problem/1991/I) | Thi đấu đánh dấu ô vuông trên bàn cờ với luật chọn và cấm | B | Mới | — |
| 015 | [Salyg1n and the MEX Game](https://codeforces.com/problemset/problem/1867/C) | Hai người thay đổi tập số, tranh nhau giá trị nguyên không âm nhỏ nhất bị thiếu | A | Mới | — |
| 016 | [Swap Game](https://codeforces.com/problemset/problem/1747/C) | Trò chơi trên dãy số với thao tác chuyển và giảm giá trị; xác định ai có chiến lược thắng | B | Mới | — |
| 017 | [Game on Permutation](https://codeforces.com/problemset/problem/1860/C) | Chọn số theo vị trí và độ lớn trong một hoán vị để thắng trò chơi | A | Mới | — |
| 018 | [Even-Odd Game](https://codeforces.com/problemset/problem/1472/D) | Hai đối thủ tranh các viên số nhưng được điểm theo tính chẵn lẻ khác nhau | B | Mới | — |
| 019 | [Vasya and Chess](https://codeforces.com/problemset/problem/493/D) | Trò chơi quân hậu di chuyển theo hướng bị giới hạn: ai có lợi thế? | A | Mới | — |
| 020 | [Fall Down](https://codeforces.com/problemset/problem/1669/G) | Thả những viên đá trên lưới chứa vật cản; yêu cầu dựng trạng thái cân bằng | C | Mới | — |
| 021 | [Different Differences](https://codeforces.com/problemset/problem/1772/C) | Sắp dãy số sao cho tạo được nhiều hiệu liên tiếp khác nhau nhất | B | Mới | — |
| 022 | [Yet Another Card Deck](https://codeforces.com/problemset/problem/1511/C) | Rút thẻ theo màu rồi chuyển lên đầu, theo dõi cách thay đổi thứ tự | C | Mới | — |

## AtCoder

| # | Bài gốc | Hạt nhân để puzzle hóa | Ưu tiên | Đối chiếu | Gần với bài hiện có |
|---:|---|---|:---:|---|---|
| 023 | [ABC347 D – Popcount and XOR](https://atcoder.jp/contests/abc347/tasks/abc347_d) | Chế tạo hai số có đúng a và b bit 1 nhưng XOR ra số C | A | Mới | — |
| 024 | [ABC336 F – Rotation Puzzle](https://atcoder.jp/contests/abc336/tasks/abc336_f) | Xoay các vùng lớn trên bảng số, biến về thứ tự chuẩn trong số lượt hạn chế | A | Gần | PZ-0028 (khác thao tác) |
| 025 | [ABC320 F – Fuel Round Trip](https://atcoder.jp/contests/abc320/tasks/abc320_f) | Lập kế hoạch nhiên liệu cho chuyến đi rồi quay lại với trạm tiếp tế một lần | A | Gần | PZ-0042 / AP-33 |
| 026 | [ABC309 F – Box in Box](https://atcoder.jp/contests/abc309/tasks/abc309_f) | Các hộp chữ nhật được phép xoay; liệu một hộp lọt hoàn toàn vào hộp khác? | A | Mới | — |
| 027 | [ABC301 E – Pac-Takahashi](https://atcoder.jp/contests/abc301/tasks/abc301_e) | Mê cung kẹo: ăn nhiều nhất nhưng vẫn về đích trước khi hết thời gian | A | Mới | — |
| 028 | [ABC244 D – Swap Hats](https://atcoder.jp/contests/abc244/tasks/abc244_d) | Sau lượng lần đổi chỗ khổng lồ, có thể đạt xếp mũ yêu cầu? | A | Gần | PZ-0028 (bất biến chẵn lẻ) |
| 029 | [ABC260 F – Find 4-cycle](https://atcoder.jp/contests/abc260/tasks/abc260_f) | Tìm bốn nút tạo một hình chữ nhật ẩn trong mạng kết nối hai nhóm | A | Mới | — |
| 030 | [ABC293 E – Geometric Progression](https://atcoder.jp/contests/abc293/tasks/abc293_e) | Tính tổng chuỗi tăng cấp số nhân cực dài mà chỉ biết số dư | B | Mới | — |
| 031 | [ABC317 C – Remembering the Days](https://atcoder.jp/contests/abc317/tasks/abc317_c) | Chuyến du lịch qua các đường không lặp thành phố, tối đa tổng độ dài | B | Mới | — |
| 032 | [ABC175 D – Moving Piece](https://atcoder.jp/contests/abc175/tasks/abc175_d) | Quân cờ đi theo hoán vị cố định, chọn thời điểm dừng để được điểm cao nhất | A | Mới | — |
| 033 | [ABC240 F – Sum Sum Max](https://atcoder.jp/contests/abc240/tasks/abc240_f) | Đồ thị vận tốc và quãng đường tích lũy; tìm đỉnh cao nhất không cần duyệt mọi bước | B | Mới | — |
| 034 | [ARC060 B – Digit Sum](https://atcoder.jp/contests/arc060/tasks/arc060_b) | Tìm hệ cơ số nhỏ nhất để một số có tổng chữ số theo yêu cầu | A | Mới | — |
| 035 | [DP J – Sushi](https://atcoder.jp/contests/dp/tasks/dp_j) | Mỗi lần chọn ngẫu nhiên một trong nhiều đĩa, kể cả đĩa rỗng: mất bao lâu để ăn hết? | A | Mới | — |
| 036 | [DP X – Tower](https://atcoder.jp/contests/dp/tasks/dp_x) | Xếp tháp đồ vật, mỗi vật chịu được sức nặng bên trên hữu hạn | A | Mới | — |
| 037 | [DP P – Independent Set](https://atcoder.jp/contests/dp/tasks/dp_p) | Tô trắng/đen các nút của cây sao cho không có cạnh nối hai nút đen | B | Gần | AP-54 (đồ thị độc lập, luật khác) |
| 038 | [DP V – Subtree](https://atcoder.jp/contests/dp/tasks/dp_v) | Đếm các tập nút liên thông trên cây chứa một nút được chỉ định | A | Mới | — |
| 039 | [DP T – Permutation](https://atcoder.jp/contests/dp/tasks/dp_t) | Đếm hoán vị có chuỗi dấu lớn hơn và nhỏ hơn cố định | A | Mới | — |
| 040 | [DP S – Digit Sum](https://atcoder.jp/contests/dp/tasks/dp_s) | Đếm các số đến một giới hạn lớn có tổng chữ số thỏa điều kiện | B | Mới | — |

## VNOI/VNOJ

| # | Bài gốc | Hạt nhân để puzzle hóa | Ưu tiên | Đối chiếu | Gần với bài hiện có |
|---:|---|---|:---:|---|---|
| 041 | [TST18 H – Trò chơi trên đa giác](https://oj.vnoi.info/problem/tst18_h) | Hai người lần lượt kẻ đường chéo không cắt nhau; nước kết thúc phụ thuộc hình tạo thành | A | Mới | — |
| 042 | [VNOI Cup 2022 Final D – Trò chơi tạo số](https://oj.vnoi.info/problem/vnoicup22_final_d) | Khai thác trò chơi tạo số; cần xác minh đầy đủ đề và luật trước khi biên tập | B | Cần đọc | — |
| 043 | [TST18 A – Nhảy lò cò](https://oj.vnoi.info/problem/tst18_a) | Bước trên vòng tròn theo các độ dài có quy tắc và tìm hành trình trở về | B | Mới | — |
| 044 | [VMHCN – Đếm hình chữ nhật](https://oj.vnoi.info/problem/vmhcn) | Các khung chữ nhật lồng nhau; tìm chuỗi khung dài nhất | A | Mới | — |
| 045 | [THSL – Slitherlink](https://oj.vnoi.info/problem/thsl) | Nối các cạnh lưới thành một vòng khép kín theo các gợi ý ô | A | Gần | Puzzle Slitherlink kinh điển ngoài kho |
| 046 | [CRECT – Đếm hình chữ nhật](https://oj.vnoi.info/problem/crect) | Đếm mảnh chữ nhật có đúng ba màu/loại ký hiệu khác nhau | A | Mới | — |
| 047 | [QBGAME – Trò chơi trên ma trận](https://oj.vnoi.info/problem/qbgame) | Nhặt các ô có điểm sao cho các ô được chọn không kề nhau | B | Gần | AP-19 (chọn không kề trên hàng) |
| 048 | [MAJMUN](https://oj.vnoi.info/problem/majmun) | Thay đúng một chỉ lệnh đi đường để đến gần đích nhất | A | Mới | — |
| 049 | [TCOCOLOR – Bảng màu](https://oj.vnoi.info/problem/tcocolor) | Tô màu lưới sao cho mỗi màu chỉ tạo đúng một vùng liên thông | A | Mới | — |
| 050 | [Minesweeper – Dò mìn](https://oj.vnoi.info/problem/minesweeper) | Khám phá bãi mìn bằng thử nghiệm chịu phạt; tìm chính sách thăm dò | A | Mới | — |
| 051 | [BEDAO OI6 A – Flagger](https://oj.vnoi.info/problem/bedao_oi6_a) | Xếp các lá cờ sao cho thỏa luật vị trí; chuẩn hóa thành câu đố lưới | B | Cần đọc | — |
| 052 | [VMROOK – N quân xe](https://oj.vnoi.info/problem/vmrook) | Đặt xe trên bàn cờ có ô cấm để không quân nào ăn nhau | A | Mới | — |
| 053 | [BEDAO M14 – Musketeers](https://oj.vnoi.info/problem/bedao_m14_musketeers) | Đặt ba mã trên bàn cờ sao cho không đe dọa nhau | B | Mới | — |
| 054 | [NK05EOPR – Đổi chỗ 0–11](https://oj.vnoi.info/problem/nk05eopr) | Tối thiểu hóa số đổi chỗ trong một hoán vị với tập cặp được phép hạn chế | A | Mới | — |
| 055 | [POINTS2 – Điểm và đoạn thẳng](https://oj.vnoi.info/problem/points2) | Hai người vẽ cạnh, ai làm đồ thị liên thông ngay sau lượt của mình thì thắng | A | Mới | — |
| 056 | [QBSORT – Sắp xếp các viên bi](https://oj.vnoi.info/problem/qbsort) | Đổi chỗ những viên bi kề nhau để gom mỗi màu vào một khối, dùng ít bước | A | Mới | — |
| 057 | [HSGSO20 – PERMSWAP](https://oj.vnoi.info/problem/hsgso20_permswap) | Nhìn chu trình hoán vị để tính số đổi chỗ tối thiểu sau cập nhật | B | Mới | — |
| 058 | [FC119 – SWAP](https://oj.vnoi.info/problem/fc119_swap) | Dùng ít nhất phép đổi ô kề nhau để tạo chuỗi đối xứng | A | Mới | — |
| 059 | [BGAME – Game on Board](https://oj.vnoi.info/problem/bgame) | Hai quân di chuyển trên bàn cờ, tranh trạng thái còn nước đi | B | Mới | — |
| 060 | [LQDRECT – Hình chữ nhật bốn góc](https://oj.vnoi.info/problem/lqdrect) | Tìm số hình chữ nhật có bốn góc cùng được đánh dấu | A | Mới | — |
| 061 | [NKCNT2 – Tam giác trên lưới](https://oj.vnoi.info/problem/nkcnt2) | Đếm hình tam giác trắng trong mạng ô tam giác | B | Mới | — |
| 062 | [KMP Friendly – Đi trong lưới](https://oj.vnoi.info/problem/kmp_friendly) | Đường đi phải/xuống chứa một mẫu ký tự trong lời nhắn đi đường | B | Mới | — |

## LeetCode

| # | Bài gốc | Hạt nhân để puzzle hóa | Ưu tiên | Đối chiếu | Gần với bài hiện có |
|---:|---|---|:---:|---|---|
| 063 | [24 Game](https://leetcode.com/problems/24-game/) | Dùng bốn quân số và bốn phép toán tạo kết quả 24 theo cách không hiển nhiên | A | Gần | Bài 24 kinh điển toàn cầu |
| 064 | [Chalkboard XOR Game](https://leetcode.com/problems/chalkboard-xor-game/) | Hai người xóa lần lượt một số, nhưng trạng thái XOR bằng 0 thay đổi người thắng | A | Mới | — |
| 065 | [Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/) | Một hàng ô sáng tắt tiến hóa mỗi đêm, dự đoán ngày thứ một tỉ | A | Gần | PZ-0031 (đèn, nhưng luật tự tiến hóa) |
| 066 | [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/) | Người ngồi sai cặp; ít nhất bao nhiêu lần đổi chỗ hai người bất kỳ? | A | Mới | — |
| 067 | [Minimum Moves to Reach Target Score](https://leetcode.com/problems/minimum-moves-to-reach-target-score/) | Chọn cộng một hoặc nhân đôi có hạn chế; tìm đường đến số đích nhanh nhất | B | Mới | — |
| 068 | [Zuma Game](https://leetcode.com/problems/zuma-game/) | Chèn bi màu để xóa các chuỗi ba viên liên tiếp; tối thiểu bao nhiêu viên cứu trợ? | A | Mới | — |
| 069 | [Grid Illumination](https://leetcode.com/problems/grid-illumination/) | Mạng đèn chiếu theo hàng, cột, chéo; hỏi một ô rồi tắt đèn gần đó | A | Gần | PZ-0031 (đèn, luật khác) |
| 070 | [Reach a Number](https://leetcode.com/problems/reach-a-number/) | Đi bước thứ i dài i sang trái hoặc phải; ít nhất mấy bước chạm đích? | A | Mới | — |
| 071 | [Can I Win](https://leetcode.com/problems/can-i-win/) | Hai người chọn số chưa dùng trong 1..m, ai chạm ngưỡng tổng trước thì thắng | A | Mới | — |
| 072 | [Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) | Trò loại vòng theo nhịp đếm, tìm người cuối cùng | B | Gần | Josephus cổ điển |
| 073 | [Super Washing Machines](https://leetcode.com/problems/super-washing-machines/) | Các máy giặt chuyền quần áo đồng thời cho máy kề bên; tối thiểu bao nhiêu lượt cân bằng? | A | Mới | — |
| 074 | [Stone Game II](https://leetcode.com/problems/stone-game-ii/) | Lấy tiền tố 1..2M đống đá, M biến đổi; ai có chiến thuật tối ưu? | A | Gần | AP-20 (lấy tiền hai đầu, luật khác) |
| 075 | [Stone Game III](https://leetcode.com/problems/stone-game-iii/) | Lần lượt lấy 1–3 quân ở đầu dãy kể cả quân mang điểm âm | B | Gần | AP-20 (lấy tiền hai đầu, luật khác) |
| 076 | [Stone Game VII](https://leetcode.com/problems/stone-game-vii/) | Mỗi lượt bỏ một đống ở đầu/cuối nhưng ghi điểm bằng tổng còn lại | A | Gần | AP-20/PZ-0027 (luật tính điểm khác) |
| 077 | [Cat and Mouse](https://leetcode.com/problems/cat-and-mouse/) | Mèo đuổi chuột trên đồ thị, có thể hòa; tìm chiến lược với thông tin hoàn hảo | A | Mới | — |
| 078 | [Mirror Reflection](https://leetcode.com/problems/mirror-reflection/) | Chiếu laser vào phòng gương hình vuông, chùm tia sẽ đến cảm biến nào? | A | Mới | — |
| 079 | [Minimum Incompatibility](https://leetcode.com/problems/minimum-incompatibility/) | Chia vật thành nhóm cùng kích thước không lặp màu, tối thiểu tổng độ phân tán | B | Gần | AP-26 (phân nhóm tối ưu, khác mục tiêu) |
| 080 | [Maximum Number of Achievable Transfer Requests](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/) | Chọn tối đa đề nghị chuyển người giữa tòa nhà mà mỗi nơi không đổi quân số | A | Mới | — |
| 081 | [Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) | Phát mũ duy nhất cho từng người từ danh sách chấp nhận; đếm phương án | B | Gần | AP-27 (đếm ghép cặp) |
| 082 | [Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/) | Chọn nhóm ít người nhất để phủ đủ bộ kỹ năng | C | Trùng lõi | AP-45/PZ-0048 (set cover) |
| 083 | [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/) | Nhấn một ô đổi trạng thái lân cận để tắt toàn bộ đèn | C | Trùng lõi | AP-57/PZ-0031 (Lights Out) |
| 084 | [Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) | Ghép trừ các hòn đá để phần còn lại nhỏ nhất, tương đương chia đôi | C | Trùng lõi | AP-39/PZ-0045 (partition) |

## CSES

| # | Bài gốc | Hạt nhân để puzzle hóa | Ưu tiên | Đối chiếu | Gần với bài hiện có |
|---:|---|---|:---:|---|---|
| 085 | [Coin Piles](https://cses.fi/problemset/task/1754) | Có hai chồng xu; mỗi lượt bỏ 1 ở đống này và 2 ở đống kia; bao giờ dọn sạch? | A | Gần | AP-49 (hai đống đá nhưng khác luật) |
| 086 | [Collecting Numbers II](https://cses.fi/problemset/task/2217) | Một hoán vị số 1..n cần mấy vòng đi từ trái sang phải để nhặt đúng thứ tự? | A | Mới | — |
| 087 | [Room Allocation](https://cses.fi/problemset/task/1164) | Khách vào và ra khác nhau; dùng ít phòng nhất mà không trùng lịch | B | Gần | AP-36 (đặt lịch) |
| 088 | [Counting Towers](https://cses.fi/problemset/task/2413) | Ghép các viên hình chữ nhật thành tháp rộng 2, cao n, đếm cách | A | Mới | — |
| 089 | [Monsters](https://cses.fi/problemset/task/1194) | Chạy khỏi mê cung khi nhiều quái vật đồng thời đuổi theo các đường ngắn nhất | A | Gần | AP-72 (đối thủ điều khiển nhánh; khác luật) |
| 090 | [Number Spiral](https://cses.fi/problemset/task/1071) | Tìm số ghi tại tọa độ cực xa của vòng xoáy số vô hạn | B | Mới | — |
| 091 | [Two Knights](https://cses.fi/problemset/task/1072) | Đếm cách đặt hai quân mã trên bàn n×n không tấn công nhau | B | Gần | BEDAO Musketeers (nguồn mới, chưa có trong repo) |
| 092 | [Missing Coin Sum](https://cses.fi/problemset/task/2183) | Cho các đồng xu mỗi đồng dùng tối đa một lần, số tiền dương nhỏ nhất không thể trả? | A | Mới | — |
| 093 | [Palindrome Reorder](https://cses.fi/problemset/task/1755) | Sắp lại chữ thành palindrome và giải thích khi nào không thể | C | Mới | — |
| 094 | [Creating Strings](https://cses.fi/problemset/task/1622) | Các chữ cái lặp nhau tạo được bao nhiêu hoán vị khác nhau? | C | Gần | AP-61 (mã hóa hoán vị, khác hướng) |

## IMO

| # | Bài gốc | Hạt nhân để puzzle hóa | Ưu tiên | Đối chiếu | Gần với bài hiện có |
|---:|---|---|:---:|---|---|
| 095 | [IMO 2024 P5 – Turbo the Snail](https://www.imo-official.org/problems/2024/) | Con ốc sên dò đường qua bản đồ có quái vật ẩn; dùng các lần thất bại để bảo đảm thoát | A | Mới | — |
| 096 | [IMO 2025 P6 – Matilda's Rectangular Tiles](https://www.imo-official.org/problems/2025/) | Xếp các hình chữ nhật sao cho mỗi hàng và mỗi cột trống đúng một ô | A | Gần | AP-42 (phủ domino có lỗ, khác dạng) |
| 097 | [IMO 2025 P5 – Inekoalaty Game](https://www.imo-official.org/problems/2025/) | Trò chơi chọn số thực luân phiên với điều kiện phụ thuộc tham số | B | Mới | — |
| 098 | [IMO 2025 P4 – Proper-Divisor Sequence](https://www.imo-official.org/problems/2025/) | Số sau là tổng ba ước thực sự lớn nhất của số trước; tìm tính chất chuỗi | A | Mới | — |
| 099 | [IMO 2025 P1 – Sunny Lines](https://www.imo-official.org/problems/2025/) | Dùng hệ đường thẳng đặc biệt phủ những điểm nguyên của lưới | B | Mới | — |
| 100 | [IMO 2026 P1 – Confucius's Number Blackboard](https://www.imo-official.org/problems/2026/) | Đổi hai số trên bảng bằng phép biến đổi liên quan gcd/lcm; khám phá đại lượng bất biến | A | Mới | — |
| 101 | [IMO 2026 P3 – Liu Bang and Xiang Yu's Stick](https://www.imo-official.org/problems/2026/) | Hai đối thủ lần lượt đánh dấu điểm cắt rồi tranh chọn các đoạn gỗ dài ngắn | A | Mới | — |
| 102 | [IMO 2026 P4 – Mulan's Triangle-Cutting Game](https://www.imo-official.org/problems/2026/) | Một người cắt tam giác, đối phương chọn phần giữ lại; ép xuất hiện góc mục tiêu | A | Mới | — |

## Nguyên tắc kiểm duyệt trước khi biến thành câu đố

1. Đọc phát biểu gốc và (nếu có) editorial, kiểm tra điều kiện miền giá trị và các trường hợp biên. Tên bài chưa thay thế việc đọc và giải.
2. Giải bản nhỏ bằng tay rồi tìm insight có thể phát biểu không dùng từ `DP`, `BFS`, `XOR`, `binary search` nếu không bắt buộc. Đề dành cho học sinh/sinh viên phải tự nhiên.
3. Tìm các bài tương đương qua Google, GitHub, Codeforces, AtCoder, VNOI, Puzzling Stack Exchange, sách và bài IMO; ghi chuỗi nguồn và nguồn sớm nhất tìm được.
4. So sánh mức `same puzzle` / `same mathematical core` / `technique overlap` / `genuinely distinct`. Đừng chỉ so tiêu đề.
5. Phải có lời giải tay ngắn gọn, chứng minh được hoặc câu hỏi khám phá có mục tiêu minh bạch; không chọn bài chỉ vì thuật toán phức tạp.
6. Ghi nguồn, tác giả/kỳ thi (khi biết), ngày truy cập, quyền tái sử dụng và ghi công. Không sao chép nguyên văn hoặc chuyển dịch nguyên văn khi chưa kiểm tra giấy phép.
7. Khi nhập vào repo, giữ đúng thiết kế `sources/` → `knowledge/` → `editions/` → `publications/`; không tạo dữ liệu bài xuất bản song song. Tuân thủ `AGENTS.md`, làm ở nhánh riêng, PR trước khi hợp nhất và chỉ push với sự cho phép.

## Các nơi tiếp tục đào sâu

- [Codeforces – tag interactive](https://codeforces.com/problemset?tags=interactive); tiếp tục với `constructive algorithms`, `games`, `combinatorics`, `bitmasks`, `math`, `brute force`.
- [AtCoder tasks](https://atcoder.jp/contests/) — đặc biệt `ARC`, `AGC`, `ABC F/G`, `Educational DP`, `Typical 90`, bài `Ex` và editorial.
- [VNOJ Problems](https://oj.vnoi.info/problems) — VNOI Cup, VNOI Wiki và đề tuyển chọn HSG/Olympic Tin học.
- [LeetCode Problems](https://leetcode.com/problemset/) — ưu tiên `Game Theory`, `Bit Manipulation`, `Math`, `Simulation`, `Design`.
- [CSES Problem Set](https://cses.fi/problemset/) — chú ý Introductory Problems, Mathematics, Interactive Problems.
- [IMO Official Problems](https://www.imo-official.org/problems/) — theo năm 2000–2026, C/G/N/A shortlist tách riêng.
- [USACO Guide](https://usaco.guide/) — xem đề, phân tích phương pháp, và liên hệ contest gốc.
- [AoPS (Art of Problem Solving)](https://artofproblemsolving.com/) — kiểm tra tính cổ điển của ý tưởng trước khi gọi “mới”.
- [Puzzling Stack Exchange](https://puzzling.stackexchange.com/) — dò xem biến thể câu đố đã xuất hiện dưới câu chuyện khác.
- [GitHub: Competitive Programming](https://github.com/topics/competitive-programming) — đào theo kho tuyển chọn và lời giải; áp dụng tìm kiếm code để tìm cả tên bài và kỹ thuật.

**Trạng thái:** danh mục nguồn nghiên cứu được lưu trong `sources/candidates/`, không phải puzzle đã duyệt hoặc đề được phép phát hành.