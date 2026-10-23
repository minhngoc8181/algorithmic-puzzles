# Algorithmic Puzzles & Strategic Problem Solving

**Ngân hàng tuyển chọn v0.1 · Phân tích & Thiết kế Giải thuật · Sinh viên năm 4 chuyên ngành Kỹ thuật Phần mềm**

Đối tượng: sinh viên lập trình tốt, có nền tảng Olympic Tin học/ICPC. Mục đích: luyện *lựa chọn mô hình, chiến lược và chứng minh*, không phải ôn lại coding patterns.

**Cách đọc**: mỗi bài có mã `AP-xx`, mô tả đủ để hình dung vấn đề, độ khó sơ bộ (3 = vừa khó; 4 = khó; 5 = thử thách sâu), và nguồn họ bài. Một số mục là *đề tóm tắt* để chọn bài; trước khi phát worksheet cần biên tập thành đề đầy đủ, kiểm tra mọi giả thiết và chuẩn bị lời giải riêng. Không có lời giải trong tài liệu này.

**Mã nguồn**: `SGI` = tái sử dụng bộ *Strategic Games, Invariants & Mathematical Puzzles* (2026); `ENC` = tái sử dụng bộ *Mã hóa & Biểu diễn thông tin* (2026); `LEV` = thuộc họ bài có mặt trong sách/giáo trình Levitin; `CLS` = classic algorithmic/combinatorial puzzle; `OJ` = cảm hứng từ các OJ kinh điển (được diễn đạt lại); `ADP` = biến thể mới dành cho khóa học. Các mã **không có nghĩa đề chép nguyên văn từ nguồn**.

**Chu trình cho một bài**: (1) tìm chiến lược bằng tay; (2) phát biểu bất biến/chặn dưới/phản ví dụ; (3) tổng quát thành thuật toán, nêu đúng-sai và độ phức tạp; (4) tùy chọn lập trình kiểm thử hoặc chứng minh độ tối ưu.

## A. Selection, Information & Decision Trees (AP-01–09)

### AP-01 — 25 con ngựa và 5 làn đua · 4 · SGI
25 con ngựa có tốc độ đôi một khác nhau, không mệt; mỗi lượt chỉ đua tối đa 5 con và chỉ biết thứ tự đến đích, không biết thời gian. Xác định **ba con nhanh nhất theo đúng thứ tự** với số cuộc đua ít nhất, kể cả chứng minh không thể ít hơn. Mở rộng: top-*k* trong *n* phần tử với các phép so sánh nhóm.

### AP-02 — 12 đồng xu, 3 lần cân · 4 · SGI/LEV
Có 12 đồng, đúng một đồng có khối lượng khác nhưng không biết nặng hơn hay nhẹ hơn. Cân thăng bằng hai đĩa, tối đa 3 lần; xác định đồng khác biệt và chiều khác biệt. Mở rộng: thiết kế cây quyết định cho *n* đồng và giải thích chặn dưới thông tin.

### AP-03 — 1.000 lọ độc, 10 chuột, 24 giờ · 3 · SGI
Trong 1.000 lọ có đúng một lọ độc; chuột uống phải độc sẽ chết đúng 24 giờ sau. Chỉ được thử đồng thời một đợt và mỗi con có thể uống hỗn hợp từ nhiều lọ. Tìm cách nhận biết lọ độc trong mọi trường hợp. Mở rộng: cần tối thiểu bao nhiêu chuột cho *N* lọ?

### AP-04 — 1.000 lọ độc, 5 chuột, 72 giờ · 4 · SGI
Cùng bài AP-03 nhưng được thử ở các giờ 0, 24, 48; mỗi chuột chết đúng 24 giờ sau **lần đầu** uống độc và chỉ các chuột còn sống mới có thể tiếp tục thử. Có xác định chắc chắn trong 72 giờ không? Mở rộng: với *m* con chuột và *r* đợt thử, phân tích số trạng thái phân biệt được.

### AP-05 — Tòa nhà 100 tầng và 2 quả trứng · 4 · CLS/LEV
Có tầng ngưỡng *T*: thả trứng từ tầng cao hơn *T* thì vỡ, thả từ tầng không cao hơn *T* thì không vỡ; trứng không vỡ dùng lại được. Chỉ có 2 quả, cần xác định *T* (cho phép *T* = 0 hoặc 100) với số lần thả tệ nhất nhỏ nhất. Tổng quát cho *n* tầng, *k* trứng.

### AP-06 — Hai mươi câu hỏi và một lời nói dối · 5 · CLS/ADP
Một người nghĩ ra số nguyên trong 0..15. Trước khi chơi, bạn phải viết một danh sách cố định các câu hỏi chỉ trả lời Có/Không; người trả lời có thể nói sai **nhiều nhất một** câu. Tìm số câu hỏi ít nhất bảo đảm tìm đúng số, chứng minh tối ưu và thiết kế hệ câu hỏi. So sánh với phiên bản câu hỏi thích nghi theo câu trước.

### AP-07 — Ai là người nổi tiếng? · 3 · LEV
Trong *n* người, nếu tồn tại người nổi tiếng thì mọi người khác đều biết người ấy, còn người ấy không biết ai. Chỉ được hỏi câu nhị phân “A có biết B không?”. Thiết kế thuật toán tìm đúng người nổi tiếng hoặc kết luận không có; tối ưu số câu hỏi ở trường hợp xấu nhất.

### AP-08 — Người nhanh nhì của giải đấu · 4 · CLS
Từ *n* người có thứ hạng sức mạnh khác nhau, chỉ được so sánh hai người một lúc, tìm người mạnh nhất và người mạnh nhì với số so sánh tối thiểu. Với *n* là lũy thừa của 2, chứng minh chặn dưới và nêu chiến thuật đạt chặn.

### AP-09 — Hai tù nhân và một đồng xu được lật · 4 · SGI
64 đồng xu trên bàn cờ 8×8 có mặt ngửa/sấp bất kỳ. A được biết một ô bí mật, phải lật **đúng một** đồng; B chỉ thấy cấu hình cuối và phải đoán đúng ô bí mật. Hai người có thể thống nhất trước. Xây dựng giao thức và nêu điều kiện để mở rộng cho 2^k ô.

## B. Divide, Decrease & Transform (AP-10–18)

### AP-10 — Phủ bàn cờ thủng bằng tromino · 3 · SGI/LEV
Bàn cờ 2^n × 2^n bị bỏ đúng một ô tùy ý. Có thể phủ toàn bộ các ô còn lại bằng các mảnh chữ L gồm 3 ô không chồng nhau không? Xây dựng thuật toán đệ quy và đánh giá độ phức tạp.

### AP-11 — Đa số trong một hội đồng · 3 · CLS
Trong dãy *n* phiếu màu, xác định có màu nào xuất hiện quá n/2 lần hay không, với phép toán nguyên thủy chỉ là so sánh bằng giữa hai phiếu. Đưa ra cách chia đôi, rồi tìm phương án tiết kiệm bộ nhớ hơn; phân biệt tìm ứng viên và kiểm chứng.

### AP-12 — Một dải đất vàng lớn nhất · 3 · CLS
Một con đường gồm các ô liên tiếp có mức lợi nhuận dương hoặc âm; chọn một đoạn không rỗng có tổng lớn nhất. Giải theo chia để trị, so với cách quét tuyến tính và chứng minh hai cách cho cùng kết quả.

### AP-13 — Hai điểm gần nhau nhất trên bản đồ · 4 · LEV
Có *n* điểm phân biệt trong mặt phẳng; tìm cặp có khoảng cách Euclid nhỏ nhất. Hãy thiết kế thuật toán tốt hơn so sánh mọi cặp và giải thích vì sao chỉ cần xét số lượng hữu hạn điểm lân cận khi ghép hai nửa.

### AP-14 — Có bao nhiêu cặp vượt mặt? · 3 · CLS
Cho hai bảng xếp hạng chứa cùng *n* người, mỗi bảng không có đồng hạng. Đếm số cặp người đổi thứ tự tương đối giữa hai bảng trong O(n log n). Mở rộng: từ số này suy ra ít nhất bao nhiêu lần đổi hai người kề nhau để biến bảng này thành bảng kia.

### AP-15 — Đai ốc và bu lông không có thước · 4 · CLS
Có *n* bu lông và *n* đai ốc với kích thước phân biệt, ghép thành từng cặp; chỉ có thể thử **một đai ốc với một bu lông** rồi biết nhỏ, bằng hay lớn, không được so hai vật cùng loại. Tìm các cặp hiệu quả hơn O(n²) trong kỳ vọng; thảo luận trường hợp tệ nhất.

### AP-16 — Tìm phần tử thiếu trong bảng nhân đôi · 3 · ADP
Một dãy đã sắp xếp chứa 2n+1 số; mọi giá trị trừ đúng một giá trị xuất hiện hai lần liên tiếp, còn giá trị đó chỉ xuất hiện một lần. Tìm giá trị lẻ chỉ dùng O(log n) phép đọc phần tử. Mở rộng: thay điều kiện “liền kề” bằng “bất kỳ”.

### AP-17 — Đường chân trời của thành phố · 4 · CLS/ADP
Trên trục phố, tòa nhà i chiếm khoảng nửa mở [l_i,r_i) và cao h_i. Nhìn từ xa, đường chân trời có độ cao lớn nhất của các tòa bao phủ mỗi tọa độ. Hãy xuất tất cả điểm mà độ cao thay đổi theo thứ tự tăng của x. Thiết kế thuật toán chia để trị và phân tích bước gộp hai đường chân trời đã có.

### AP-18 — Tìm đồng xu giả từ nhiều chồng · 4 · LEV/ADP
Có *m* chồng đồng xu, mỗi chồng có ít nhất *m* xu. Một chồng có xu nặng 9 g, tất cả các chồng còn lại nặng 10 g; cân điện tử trả về khối lượng chính xác. Chỉ được cân **một lần**, được lấy số xu khác nhau ở mỗi chồng. Xác định chồng giả và mở rộng cho nhiều giả thuyết trọng lượng.

## C. Dynamic Programming & Optimal Play (AP-19–27)

### AP-19 — Hàng đồng tiền không được nhặt sát nhau · 3 · LEV
*n* đồng tiền xếp trên một hàng, đồng thứ *i* có giá trị *a_i* có thể âm hoặc dương. Chọn tập đồng xu sao cho không có hai vị trí kề nhau và tổng giá trị lớn nhất; được chọn tập rỗng. Nêu công thức truy hồi và tái tạo một nghiệm tối ưu.

### AP-20 — Hai người lần lượt nhặt tiền ở hai đầu · 4 · OJ/CLS
Các đồng xu mang giá trị nguyên được xếp thành hàng. A và B luân phiên lấy đúng một đồng ở một trong hai đầu; cả hai tối ưu hóa tổng tiền của mình. Tìm số tiền A có thể bảo đảm nếu đi trước; vì sao greedy lấy đồng lớn hơn trước mắt có thể sai?

### AP-21 — Sáp nhập các khối slime · 4 · OJ
Có *n* khối với kích thước dương xếp thành hàng. Mỗi bước chỉ ghép được **hai khối kề nhau**, tạo khối kích thước x+y và tốn phí x+y. Tính tổng phí nhỏ nhất để thành một khối. So sánh với biến thể được chọn hai khối bất kỳ (không yêu cầu kề).

### AP-22 — Tách gói chocolate để bán · 4 · ADP
Tấm chocolate w×h ô được phép cắt theo các đường thẳng qua toàn bộ một mảnh hiện tại; mỗi mảnh chữ nhật a×b có giá thị trường v(a,b). Có thể bán bất kỳ mảnh chưa cắt. Tìm giá trị lớn nhất thu được từ tấm gốc. Biến thể: giới hạn đúng k lần cắt.

### AP-23 — Xóa chuỗi bằng một máy in kỳ lạ · 4 · CLS
Ban đầu một dãy dài *n* ký tự trắng. Trong một lượt, máy được chọn một đoạn liên tiếp và in **một ký tự duy nhất** lên mọi vị trí trong đoạn, đè lên ký tự cũ. Tìm số lượt ít nhất để tạo chuỗi đích. Chứng minh vì sao số nhóm ký tự liên tiếp khác nhau chưa chắc là tối ưu.

### AP-24 — 100 bậc thang có ô cấm · 3 · OJ/ADP
Từ bậc 0 đến bậc *n*, mỗi bước được nhảy 1, 2 hoặc 3 bậc; một số bậc bị cấm. Đếm đường đi không chạm ô cấm, rồi thay đổi: mỗi cú nhảy có chi phí phụ thuộc vị trí và tìm đường rẻ nhất. Có thể dùng cùng một mô hình trạng thái cho hai mục tiêu không?

### AP-25 — Các viên kẹo phân chia có giới hạn · 4 · OJ
Có *n* trẻ, trẻ i nhận số kẹo nguyên trong [0,a_i]; phải chia đúng K viên, không thừa. Đếm số cách chia theo thứ tự người nhận (mod một số nguyên tố). Tìm thuật toán nhanh hơn O(nK²).

### AP-26 — Chọn nhóm bạn tối ưu · 4 · OJ
Có *n* người; mỗi cặp có thể hợp tác hoặc không. Chia mọi người thành các nhóm không rỗng, không giao nhau để tối đa hóa tổng điểm cộng tác nội bộ, cho phép điểm âm. Với n≤16, thiết kế subset DP và tránh đếm lặp các phân hoạch cùng loại.

### AP-27 — Ghép cặp trên bàn tiệc · 4 · OJ
Có n người phía A và n người phía B, mỗi cặp được phép hoặc bị cấm. Đếm số ghép cặp hoàn hảo với n≤20 (mod M). Đưa ra công thức DP theo tập con và giải thích khi nào bài chỉ tìm sự tồn tại thì thuật toán đồ thị khác phù hợp hơn.

## D. Greedy, Exchange & Online Decisions (AP-28–36)

### AP-28 — Khỉ mang 3.000 quả chuối · 4 · SGI
Có 3.000 quả ở đầu đường dài 1.000 km; mỗi chuyến khỉ chỉ chở tối đa 1.000 quả, và mỗi km di chuyển (cả đi lẫn về) tiêu tốn đúng 1 quả; được gửi chuối dọc đường, đại lượng liên tục. Tìm lượng đến chợ lớn nhất, phân đoạn khi chi phí biên thay đổi. Mở rộng: sức chở C, ban đầu B, quãng đường D.

### AP-29 — Bốn người qua cầu ban đêm · 3 · SGI/LEV
Bốn người mất 1, 2, 5, 10 phút nếu đi một mình; cầu chở tối đa 2 người/lượt, phải mang một chiếc đèn pin, lượt của hai người mất thời gian của người chậm hơn. Tìm tổng thời gian nhỏ nhất rồi xét *n* người có thời gian khác nhau.

### AP-30 — Nối những sợi dây tốn phí · 3 · CLS
Có *n* đoạn dây có độ dài khác nhau; mỗi lần nối hai đoạn hiện có tốn phí bằng tổng độ dài của chúng và tạo một đoạn dài bằng tổng đó. Tìm tổng chi phí tối thiểu. Giải thích vì sao cách nối hai đoạn ngắn nhất trước hoạt động; so sánh với AP-21.

### AP-31 — Đặt cảm biến để quan sát các đoạn đường · 3 · CLS
Trên trục số có *n* đoạn đóng [l_i,r_i]. Một cảm biến đặt tại tọa độ x quan sát đúng mọi đoạn chứa x. Tìm số cảm biến ít nhất để mỗi đoạn được quan sát; yêu cầu chứng minh greedy và dựng phản ví dụ cho chiến thuật đặt tại trung điểm.

### AP-32 — Nộp bài đúng hạn để lấy phần thưởng · 4 · CLS
Có *n* công việc, mỗi việc tốn đúng 1 đơn vị thời gian, có hạn chót nguyên d_i và phần thưởng p_i nếu hoàn thành không muộn hơn hạn. Chỉ làm một việc tại một thời điểm. Chọn và sắp thứ tự để tổng thưởng lớn nhất; chứng minh thuật toán.

### AP-33 — Vòng tròn các trạm xăng · 3 · CLS
Có *n* trạm trên vòng tròn, mỗi trạm cung cấp a_i lít; đi từ trạm i tới trạm i+1 tốn b_i lít. Xe có bình không giới hạn, khởi hành với bình rỗng từ một trạm được chọn và lấy xăng tại đó. Nếu tổng nhiên liệu đủ, hãy tìm một trạm xuất phát cho phép đi trọn vòng mà không âm nhiên liệu.

### AP-34 — Đổi tiền theo mệnh giá kỳ lạ · 3 · CLS
Với các mệnh giá nguyên dương có chứa 1 và mỗi loại tiền không giới hạn, tìm cách đổi số tiền S bằng ít đồng nhất. Khi nào tham lam chọn mệnh giá lớn nhất không tối ưu? Tạo một hệ mệnh giá nhỏ nhất (theo số loại hoặc S) mà cách tham lam thất bại.

### AP-35 — Thuê hay mua giày trượt tuyết? · 4 · CLS
Mỗi ngày trượt, có thể thuê với phí 1 hoặc mua vĩnh viễn với phí B. Không biết trước số ngày D sẽ trượt, quyết định trực tuyến trước mỗi ngày. Xây dựng chiến lược có tỉ lệ chi phí so với phương án biết trước D nhỏ nhất trong trường hợp xấu nhất; so sánh chiến lược ngẫu nhiên.

### AP-36 — Chọn lịch biểu diễn có thưởng · 4 · CLS/ADP
Có n tiết mục, tiết mục i chạy trong khoảng thời gian nửa mở [s_i,f_i) và mang về thưởng p_i>0. Chỉ được nhận các tiết mục không chồng thời gian. Greedy chọn tiết mục kết thúc sớm nhất giải tốt bài tối đa **số lượng**, liệu còn đúng với bài tối đa **tổng phần thưởng**? Dựng phản ví dụ và thiết kế thuật toán chính xác.

## E. Sets, Combinatorics & Group Selection (AP-37–45)

### AP-37 — 100 tù nhân và 100 hộp · 5 · SGI
Quản ngục đặt một hoán vị ngẫu nhiên 100 số vào 100 hộp. Mỗi tù nhân phải tìm số của mình trong tối đa 50 hộp, không thể giao tiếp khi đã bắt đầu; cả nhóm thắng chỉ nếu tất cả thành công. Tìm chiến thuật có xác suất thành công >30% và tính chính xác xác suất. Mở rộng cho 2n hộp.

### AP-38 — Rút găng tay trong bóng tối · 3 · LEV/CLS
Trong ngăn kéo có 8 găng trái và 8 găng phải, tất cả cùng một cỡ nhưng không thể phân biệt bằng tay bên trái/phải khi rút. Hỏi rút bao nhiêu chiếc để chắc chắn có ít nhất một cặp trái-phải, trong tình huống bất lợi nhất. Biến thể: găng có nhiều màu, chỉ ghép cặp cùng màu.

### AP-39 — Hai đội có tổng sức mạnh bằng nhau · 4 · CLS
Có 40 người với năng lực nguyên không âm a_i. Chia thành hai đội, mỗi người vào đúng một đội, để độ lệch tổng năng lực nhỏ nhất. Thiết kế thuật toán exact nhanh hơn duyệt 2^40 tập; đánh giá giới hạn khả thi khi tăng số người.

### AP-40 — Ba quả cân để cân mọi số nguyên · 4 · CLS/LEV
Bạn có cân đĩa và một bộ quả cân nguyên, mỗi quả đặt được ở cùng đĩa với hàng hoặc đĩa đối diện. Chọn *k* quả cân để cân chính xác được mọi khối lượng nguyên từ 1 đến M bằng một lần đặt. Với k cố định, giá trị M lớn nhất có thể bảo đảm là bao nhiêu? Nêu bộ quả cân và chứng minh tính tối ưu.

### AP-41 — Ghép đôi theo điều kiện chấp nhận · 4 · CLS
Có *n* sinh viên và *n* vị trí thực tập; sinh viên i chỉ chấp nhận một số vị trí trong tập S_i. Khi nào tồn tại cách phân công sao cho mỗi sinh viên nhận một vị trí được chấp nhận và mỗi vị trí được gán đúng một người? Tìm thuật toán và điều kiện đặc trưng bằng các tập con.

### AP-42 — Phủ bảng có lỗ bằng domino · 4 · CLS/LEV
Bảng ô vuông có một số ô bị bỏ đi. Các ô còn lại phải được phủ bằng domino 1×2, không đè hoặc chồng. Điều kiện cân bằng số ô đen/trắng có đủ không? Đưa ra phản ví dụ; giải bài toán tổng quát bằng mô hình ghép cặp.

### AP-43 — Chuyến thang máy ít nhất · 4 · OJ
Có *n* người có cân nặng w_i và thang máy sức chở X. Mỗi chuyến vận chuyển một nhóm có tổng cân nặng ≤X; mỗi người đi đúng một lần. Với n≤20, tìm số chuyến tối thiểu. Bài này khác bài bin packing xấp xỉ ở điểm nào?

### AP-44 — Kho báu chỉ mở khi đủ bốn người · 5 · CLS/ADP
Bảy nhà thám hiểm cùng khóa một hòm bằng nhiều ổ khóa độc lập; mỗi ổ chỉ cần một chìa tương ứng để mở, và có thể sao nhiều bản của mỗi chìa. Hãy chọn số ổ khóa **ít nhất** và phân chìa sao cho **bất kỳ bốn** người cùng hợp tác đều mở được toàn bộ hòm, nhưng **không một nhóm ba người nào** mở được. Tổng quát hóa cho n người với ngưỡng t.

### AP-45 — Chọn đoàn đại biểu nhỏ nhất · 4 · CLS/ADP
Có m ủy ban và n ứng viên; ứng viên i có thể đại diện cho những ủy ban trong tập S_i. Hãy chọn ít người nhất sao cho mọi ủy ban đều có người đại diện. Thử tham lam chọn người phủ nhiều ủy ban chưa có đại diện nhất, dựng phản ví dụ, so sánh với lời giải exact khi m≤20. Bài toán thuộc họ Set Cover.

## F. Game Theory, Minimax & Grundy (AP-46–54)

### AP-46 — Năm con sói và một con cừu · 3 · SGI
Nếu sói ăn cừu nó sẽ biến thành cừu; sói ưu tiên sống hơn ăn. Mọi con biết người khác hoàn toàn lý trí. Phân tích hành động hợp lý khi có n sói, bắt đầu từ các trạng thái nhỏ, giả thiết rõ quy tắc giải quyết khi có nhiều lựa chọn.

### AP-47 — Năm cướp biển chia 100 đồng vàng · 4 · SGI
Năm cướp biển có thứ bậc cao-thấp; mỗi vòng thủ lĩnh đưa ra cách chia 100 đồng, cả nhóm bỏ phiếu, nếu không được thông qua thủ lĩnh bị loại. Phân tích cân bằng bằng suy luận ngược **với đúng luật ngưỡng phiếu và ưu tiên đã ghi trong bộ SGI**; biến thể thay luật sẽ cho đáp án khác.

### AP-48 — Nim và phiên bản lấy viên cuối thì thua · 3 · SGI/LEV
Nhiều đống đá, một lượt lấy số dương viên từ đúng một đống; chơi theo cả hai luật “lấy viên cuối thắng” và “lấy viên cuối thua”. Mô tả trạng thái thua, nước thắng và vì sao đoạn cuối của hai luật không giống nhau.

### AP-49 — Wythoff và hai đống đá · 5 · SGI
Hai đống a,b. Một lượt lấy bất kỳ số dương viên từ một đống, **hoặc** lấy cùng số dương viên từ cả hai; người lấy viên cuối thắng. Tìm và chứng minh đặc trưng các trạng thái thua; giải bài tổng quát với a,b rất lớn.

### AP-50 — Chocolate có ô bị đầu độc · 4 · SGI/LEV
Một bảng m×n ô có ô góc dưới trái bị độc. Mỗi lượt chọn một ô còn lại và ăn ô đó cùng mọi ô còn lại vừa **không nằm thấp hơn** vừa **không nằm bên trái** ô ấy (vùng phía trên-phải), đúng luật Chomp. Người buộc phải ăn ô độc thua. Với m,n>1, xác định ai có chiến thuật thắng và phân biệt chứng minh tồn tại với xây dựng nước đi hiệu quả.

### AP-51 — Chia một đống thành hai đống khác nhau · 4 · CLS
Khởi đầu một đống n viên. Mỗi lượt phải chọn một đống và chia thành **hai đống kích thước dương khác nhau**; không được chia bằng nhau. Người không còn lượt hợp lệ thua. Tìm trạng thái thắng-thua cho n≤N rồi đưa ra lời giải tổng quát hoặc giả thuyết có kiểm chứng.

### AP-52 — Bowling trên một hàng quân · 4 · CLS
Có n quân xếp liên tiếp. Một lượt loại đúng 1 quân hoặc 2 quân kề nhau; các phần còn lại tách thành những đoạn độc lập. Người không có nước đi thua. Xây dựng trạng thái Grundy của một đoạn độ dài n và quyết định ai thắng với dãy các đoạn tùy ý.

### AP-53 — Vẽ đường giữa các điểm: Sprouts · 5 · SGI
Bắt đầu có n điểm; mỗi lượt nối hai đầu mút hợp lệ bằng một cung không cắt đường cũ, đặt thêm một điểm trên cung, bậc mỗi điểm tối đa 3. Xác định những chặn có thể chứng minh cho tổng số lượt đến khi dừng. Phân biệt chứng minh bound và giải game tối ưu.

### AP-54 — Chọn một đỉnh rồi khóa hàng xóm · 4 · ADP
Hai người luân phiên chọn một đỉnh chưa bị loại trong đồ thị; khi chọn v thì v và toàn bộ láng giềng của v bị loại. Người không còn nước đi thua. Với đồ thị đường đi, chu trình, cây nhỏ và đồ thị bất kỳ, phân tích trạng thái, thử nghiệm minimax và liệu kết quả có liên quan maximal independent set hay không.

## G. Invariants, Encoding & Impossibility (AP-55–63)

### AP-55 — 15-puzzle tráo 14 với 15 · 3 · SGI
Từ cấu hình 15-puzzle chuẩn giải được, chỉ đổi chỗ hai quân đánh số 14 và 15, giữ nguyên ô trống. Có thể đạt cấu hình mới bằng các bước trượt hợp lệ không? Mở rộng để phát hiện mọi trạng thái giải được trên bảng m×n.

### AP-56 — Những người lính tiến lên lưới · 5 · SGI
Bên dưới một đường ngang của lưới vuông là vô hạn quân, phía trên trống. Một quân được nhảy qua quân bên cạnh sang ô trống kế tiếp (dọc hoặc ngang) và loại quân bị nhảy qua. Có thể đưa một quân lên cao vô hạn không? Tìm trọng số thế năng phù hợp và chặn hàng cao nhất.

### AP-57 — Bảng đèn với phép cộng modulo 2 · 4 · SGI
Trên bảng m×n các bóng đèn, một lần nhấn tại ô tác động lên ô ấy và các ô lân cận theo một mặt nạ cho trước, đổi tắt/bật. Xác định tập trạng thái có thể đạt từ trạng thái ban đầu, đếm số nghiệm nếu có và tìm số lần nhấn nhỏ nhất trong trường hợp m,n nhỏ.

### AP-58 — Giải mã lỗi bit duy nhất · 4 · ENC
Thiết kế mã nhị phân cho phép mã hóa 4 bit dữ liệu bằng 7 bit truyền, sao cho nếu nhiều nhất 1 bit bị đảo thì người nhận vẫn sửa được lỗi và khôi phục dữ liệu. Giải thích chặn dưới bằng số quả cầu Hamming và vì sao không thể dùng 6 bit theo mô hình này.

### AP-59 — Sắp 2^k trạng thái không làm chớp đèn · 3 · ENC
Có k công tắc. Liệt kê toàn bộ 2^k cấu hình sao cho mỗi cấu hình chỉ khác cấu hình ngay trước ở đúng một công tắc. Tạo thuật toán xếp thứ tự, giải mã vị trí của một cấu hình, và xét liệu cấu hình cuối có thể cách cấu hình đầu một bit không.

### AP-60 — Biến đổi Burrows–Wheeler và giải ngược · 4 · ENC
Cho một xâu kèm ký tự kết thúc duy nhất và thứ tự từ điển. Xét các vòng quay, sắp theo từ điển, xuất cột cuối. Tìm thuật toán khôi phục xâu chỉ từ cột cuối và chứng minh tính đúng đắn.

### AP-61 — Hoán vị nằm trong một số nguyên · 4 · ENC
Với n phần tử phân biệt, biểu diễn mỗi hoán vị bằng một dãy chữ số có miền giá trị thay đổi theo vị trí (Lehmer code). Từ mã suy ra thứ hạng từ điển của hoán vị và thực hiện phép ngược; tối ưu tìm phần tử thứ k chưa dùng.

### AP-62 — Bảng ô bị cắt mất hai góc · 3 · SGI/LEV
Cắt hai góc đối diện của bàn cờ 8×8; có phủ phần còn lại bằng 31 domino 1×2 không? Tổng quát thành một bài toán về những ô mất đi và nhận xét điều kiện tô màu không phải lúc nào cũng đủ.

### AP-63 — Solitaire Bulgaria có chu kỳ? · 4 · LEV/CLS
Có n quân chia thành các đống dương. Mỗi vòng, lấy đúng một quân từ mỗi đống và gom thành một đống mới; đống rỗng biến mất. Chứng minh quá trình cuối cùng trở nên tuần hoàn; khi n là số tam giác, nghiên cứu cấu hình ổn định và tính duy nhất.

## H. Adversarial, Reductions & Boundary Cases (AP-64–72)

### AP-64 — Một bóng đèn và 100 tù nhân · 5 · SGI
100 người vào phòng một bóng đèn từng người một theo lịch do quản ngục chọn; biết trạng thái ban đầu là tắt. Mỗi người có thể chỉnh đèn, và lịch bảo đảm mọi người vào vô hạn lần nếu tiếp tục mãi. Xây dựng giao thức bảo đảm cuối cùng có người thông báo đúng “mọi người đã từng vào”. Nếu bỏ giả thiết fairness thì sao?

### AP-65 — Bài toán thuê 2 máy nhưng được đổi lịch · 4 · ADP
Có n công việc độc lập với thời lượng dương t_i, cần phân cho hai máy cùng tốc độ, không được ngắt công việc; mục tiêu nhỏ nhất thời điểm máy cuối hoàn tất. Phân tích một chiến lược tham lam theo thời lượng giảm dần, tạo phản ví dụ và tìm thuật toán exact cho n nhỏ.

### AP-66 — Hai thành phố bị chia cắt · 4 · CLS
Cho một đồ thị vô hướng liên thông, cần tìm một cạnh mà nếu phá bỏ thì mạng bị tách; tìm tất cả cạnh như vậy trong O(V+E). Biến thể: cần phá ít nhất bao nhiêu cạnh để ngắt liên lạc giữa hai đỉnh cho trước? Có thể sử dụng cùng một phương pháp không?

### AP-67 — Người đi ngẫu nhiên trong mê cung · 4 · ADP
Một robot ở trên đồ thị hữu hạn, tại mỗi bước chọn ngẫu nhiên đều một đỉnh kề, dừng khi đến đỉnh đích. Tính số bước kỳ vọng từ mỗi đỉnh hoặc phát hiện kỳ vọng vô hạn. Tách rõ trường hợp đồ thị có vùng không thể thoát và trường hợp đích đạt được xác suất 1.

### AP-68 — Tìm đường ngắn nhất trong thành phố có một vé giảm giá · 4 · OJ
Đồ thị có hướng có trọng số cạnh dương; được phép chọn **tối đa một** cạnh trên đường đi và trả chi phí bằng một nửa phần nguyên cho cạnh đó. Tìm tuyến rẻ nhất từ A đến B. Có bao nhiêu cách mô hình hóa bằng trạng thái hoặc ghép hai bài toán đường ngắn nhất?

### AP-69 — Bí mật trong 40 chiếc mũ · 4 · SGI/ADP
40 người đứng thành hàng, mỗi người thấy mũ của những người đứng trước, không thấy mũ mình và người sau; lần lượt trả lời từ cuối lên đầu, mọi người nghe được các câu trước. Chỉ có hai màu và 40 mũ được chọn độc lập đều xác suất. Tìm chiến lược tối đa **xác suất cả nhóm đều đúng**; tiếp theo đổi mục tiêu thành bảo đảm **số người đúng lớn nhất** và so sánh hai lời giải.

### AP-70 — Ai xứng đáng làm đội trưởng? · 4 · CLS/ADP
Có n người, kết quả các trận đấu đôi là một tournament (mỗi cặp có đúng một người thắng, không giả thiết tính bắc cầu). Tìm người có thể thắng mọi người khác qua đường đi độ dài tối đa 2 nếu tồn tại; phân tích chứng minh bằng người có nhiều trận thắng nhất và so với Condorcet winner.

### AP-71 — Chọn dự án với các khóa tiên quyết · 4 · ADP
Mỗi dự án có giá trị có thể âm hoặc dương; nếu làm dự án u thì bắt buộc phải làm mọi dự án tiền đề của u. Tìm tập dự án có tổng lợi ích lớn nhất. Chứng minh bài có thể giảm về min-cut/max-flow hoặc tìm cấu trúc đặc biệt cho đồ thị tiên quyết dạng cây.

### AP-72 — Tìm lộ trình chắc thắng khi đối thủ điều khiển nhánh · 5 · ADP
Trò chơi hữu hạn trên đồ thị có hướng: A và B luân phiên di chuyển quân theo cạnh ra, người không có cạnh hợp lệ thua. Với đồ thị phi chu trình, phân loại trạng thái thắng/thua; với đồ thị có chu trình, thêm kết quả hòa và lập thuật toán tìm trạng thái thắng/thua/hòa. Phân biệt chính xác thắng cưỡng bức và “không thua”.

---

## Bản đồ khai thác trên lớp (teacher-only)

| Buổi/chủ điểm | Khởi động ngắn | Bài trọng tâm | Đối chứng / mở rộng |
|---|---|---|---|
| Search, selection & lower bounds | AP-07 | AP-01 | AP-08 / AP-02 |
| Information & coding | AP-03 | AP-04 | AP-06 / AP-09 |
| Divide-and-conquer | AP-10 | AP-15 | AP-13 / AP-14 |
| Optimal substructure | AP-19 | AP-20 | AP-21 / AP-23 |
| Greedy & exchange | AP-29 | AP-28 | AP-30 / AP-36 |
| Adversarial & online | AP-34 | AP-35 | AP-65 |
| Sets & combinatorial optimization | AP-38 | AP-41 | AP-39 / AP-43 |
| Game theory | AP-46 | AP-49 | AP-51 / AP-52 |
| Invariant & impossibility | AP-62 | AP-56 | AP-55 / AP-63 |
| Structural reductions | AP-42 | AP-71 | AP-66 / AP-72 |

### 14 bài đề xuất làm lõi (course anchors)

`AP-01, AP-02, AP-04, AP-05, AP-09, AP-10, AP-15, AP-20, AP-21, AP-28, AP-36, AP-39, AP-49, AP-56`.

### Rubric đánh giá thống nhất

1. **Model/constraints**: nêu đúng quyền truy cập thông tin, giả thiết, không tự thêm luật.
2. **Strategy**: nêu chiến thuật/tập trạng thái hoặc công thức truy hồi đủ chặt để triển khai.
3. **Correctness**: chứng minh tối ưu hoặc đúng; nếu không chứng minh được phải báo giới hạn.
4. **Lower bound/counterexample**: ít nhất một chặn dưới hoặc bác bỏ chiến lược sai phổ biến.
5. **Generalization**: chuyển đề bằng tay thành bài toán với tham số n,k, cấu trúc và độ phức tạp.
6. **Validation**: brute force kích thước nhỏ, property-based tests hoặc đối chiếu hai phương pháp khi hữu ích.

### Phân biệt ba loại sản phẩm giảng dạy tiếp theo

- **Catalog** (file này): đề tóm tắt/metadata/tuyển chọn, *chưa* phát trực tiếp cho sinh viên.
- **Student Worksheets**: đề hoàn chỉnh, tự chứa mọi điều kiện, không hé lộ kỹ thuật trong tên/mô tả, không gợi ý.
- **Instructor Pack**: lời giải, chứng minh, lower bound, phản ví dụ, mục tiêu tư duy, độ khó thực tế, test generator nếu hợp lý.

### Nguồn tham khảo và xuất xứ họ bài

1. A. Levitin, M. Levitin, *Algorithmic Puzzles* (Oxford University Press, 2011): https://academic.oup.com/book/40814 (150 bài có hints/solutions; nguồn tham khảo theo họ bài, không mặc định trích nguyên văn).
2. A. Levitin, *Introduction to the Design and Analysis of Algorithms*, 3rd edition, Pearson: https://www.pearson.com/en-us/subject-catalog/p/Levitin-Introduction-to-the-Design-and-Analysis-of-Algorithms-3rd-Edition/P200000003403
3. Jeff Erickson, *Algorithms* (free CC BY 4.0): https://jeffe.cs.illinois.edu/teaching/algorithms/index.html
4. Stanford CS161, course resources: https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/
5. AtCoder Educational DP Contest: https://atcoder.jp/contests/dp/tasks?lang=en (đặc biệt Deque, Slimes, Candies, Matching, Grouping)
6. CSES Problem Set: https://cses.fi/problemset/ (đặc biệt Elevator Rides, Removal Game, Money Sums, Flight Discount)
7. Hai bộ đã lưu trong thư viện: *strategic_games_invariants_worksheet_curated.md* và *ma_hoa_bieu_dien_olympiad_teacher.pdf*.

**Ghi chú biên tập**: Một số bài tái sử dụng có điều kiện rất cụ thể. Khi đưa vào Student Worksheet, cần lấy bản cuối cùng của bộ trước thay vì một bản cổ điển không tương thích. Các bài tham khảo sách Levitin được diễn đạt lại ở đây từ họ bài, không khẳng định là nguyên văn hoặc khẳng định mọi biến thể nằm trong sách. Các bài ADP là đề xuất thiết kế, cần được giải và kiểm chứng độc lập trước khi giao sinh viên.
