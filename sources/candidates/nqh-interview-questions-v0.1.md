# Kho tham khảo NQH: "Các câu hỏi phỏng vấn" — nguyên văn đề

**Nguồn:** chuỗi 45 bài blog "Các câu hỏi phỏng vấn [1]–[45]" của Ngô Quang Hưng (NQH), Blog Khoa Học Máy Tính (procul.org), 23/06/2005 – 26/10/2012. Bản lưu cục bộ: `G:\My Drive\Archives\NQH`.

**Nội dung:** 115 câu hỏi, mã `NQH-###` trùng đúng số thứ tự của tác giả (lấy từ thẻ `<ol start=…>` của HTML). Văn bản bên dưới là **nguyên văn** từ phần thân bài, kể cả lỗi chính tả và lỗi đề của tác giả. Công thức LaTeX giữ nguyên dạng ` $…$`. Dòng bắt đầu bằng `>` là đoạn dẫn của tác giả, không đánh số. Bình luận và lời giải của độc giả nằm ở [nqh-interview-comments-v0.1.md](nqh-interview-comments-v0.1.md), cũng nguyên văn.

> [!IMPORTANT]
> Đây là kho ứng viên, chưa đăng ký trong `sources/registry.json`, chưa có `PZ-xxxx`, chưa review. Nội dung thuộc tác giả gốc; chỉ dùng làm nguồn tham khảo nội bộ. Provenance không in ra ấn phẩm.

## Lưu ý về dữ liệu

- Câu 11: đề ghi "đánh số từ 1 đến 100" nhưng có 500 cửa và 500 người. Lỗi của nguồn, giữ nguyên.
- Câu 94 chỉ là video YouTube (`4s2uczTGRfU`, blog Gil Kalai). Bản lưu không có đề dạng chữ.
- Câu 113 không nằm trong danh sách đánh số của HTML; tác giả ghi số 113 trong văn bản, tôi chỉ chuyển thành tiêu đề `NQH-113` (bỏ tiền tố "113.").
- Các câu 55 và 102 cùng ý tưởng (NQH nói câu 102 là biến thể của câu 55).
- Câu 4: NQH ghi ở bài [12] rằng mỗi lần dùng căn bậc hai là một lần dùng số 2.
- Câu 40 (bài [14]) hỏi số nguyên tố xen kẽ 1 và 0; câu 41 là bài gossip; câu 42 là số tự mô tả. Bình luận dùng đúng các số này.
- Câu 47, 56, 64, 84: đề hoặc lời giải trong bình luận còn tranh cãi, xem file bình luận.

## Phân nhóm gợi ý (biên tập, chưa duyệt)

| Nhóm | Các câu |
|---|---|
| Logic, đố mẹo | 4, 5, 7–9, 12, 13, 19, 22, 23, 32, 55, 57, 58, 62, 65, 66, 83, 85, 102 |
| Cân, đo, đong, chia, thời gian | 7, 10, 14, 15, 21, 24, 33, 74, 75, 78 |
| Xác suất | 16, 17, 56, 86, 93, 104, 109, 110 |
| Trò chơi, chiến lược | 15, 56, 61, 63, 76, 77, 84, 86, 101, 103 |
| Tổ hợp, bất biến, quy nạp | 3, 34, 41, 46, 54, 59, 60, 67–69, 80–82, 95–97, 99, 100 |
| Hình học, chuyển động | 9, 10, 18, 30, 36, 43–45, 47, 70–72, 79, 90, 92, 96 |
| Số học, đại số | 6, 11, 26, 31, 40, 42, 64, 69, 113 |
| Thiết kế giải thuật | 1, 3, 25, 35, 37–39, 73, 89, 91, 98, 105–107, 111, 112, 115 |
| Lập trình C/C++ cụ thể (lệch mục tiêu sách) | 2, 27–30, 49–53, 87, 88, 108, 111, 112, 114 |
| Mã hóa, bảo mật | 48, 113 |

---


## Bài [1] — 23/06/2005

> Microsoft nổi tiếng là có các câu hỏi phỏng vấn nhân viên mới mang tính kỹ thuật theo dạng đố “mẹo” (đa số là về thuật toán hoặc lập trình C/C++). Có nhiều bộ sưu tập các câu hỏi dạng này đã từng được hỏi ở các cuộc phỏng vấn ở Microsoft. Gần đây Google cũng phỏng vấn theo kiểu tương tự. Mỗi câu trả lời chỉ được cho khoảng 5-10 phút suy nghĩ. Đôi khi người ta quan tâm đến quá trình suy nghĩ của bạn hơn là bản thân câu trả lời.

> Trong chuỗi bài này tôi sẽ nêu chọn lọc một số câu hỏi tôi thích nhất. Các câu hỏi được chọn không nhất thiết là khó nhất, tiêu chuẩn là gọn gàng và đẹp.

### NQH-001

Cho một danh sách liên kết đơn (simple linked list) hữu hạn. Có hai trường hợp: một là cuối danh sách trỏ về NULL, hai là trỏ về một phần tử đã gặp – tạo nên một vòng tròn trong danh sách.
Ví dụ trường hợp 1: A –> B –> C –> D –> NULL.
Ví dụ trường hợp 2: A –> B –> C –> D –> E –> F –> C.
Cho trước một con trỏ vào một danh sách liên kết đơn L nào đó, hữu hạn nhưng có thể có độ dài tùy ý. Làm thế nào để kiểm tra nhanh nhất nếu danh sách L thuộc trường hợp 1 hay trường hợp 2, với điều kiện là ta chỉ được dùng vài chục bytes bộ nhớ.

### NQH-002

Cho một chuỗi ký tự s bao gồm nhiều từ. Viết một đoạn chương trình C đảo thứ tự các từ.
Ví dụ: với input là “this is a nice blog” thì output là “blog nice a is this“.

### NQH-003

Cho hai dãy số đã xếp thứ tự tăng dần A và B, mỗi dãy có n phần tử. Xét tập hợp sau:

S = { A[i] + B[j] | 1 < = i, j <= n }.
Chú ý rằng S có thể có đến n2 phần tử. Viết một chương trình in ra n số lớn nhất trong S. Chương trình phải chạy trong thời gian O(n).

## Bài [2] — 24/06/2005

### NQH-004

Chỉ với các phép tính cộng, trừ, nhân, chia, các hàm lượng giác, phép lũy thừa, và phép lấy căn, cùng với ba số 2, làm thế nào để viết một biểu thức định trị ra 2005? (Gợi ý: 2005 không có gì đặc biệt, số nguyên dương nào cũng được.) [Câu này tôi biết qua chị Hà Dương, lúc giải ra rất thích! Đơn giản và độc đáo]

### NQH-005

Bụt, diêm vương, và Tèo đứng trước mặt bạn. Bụt và diêm vương cái gì cũng biết. Tèo thì cái biết cái không. Bụt luôn nói thật, diêm vương luôn nói dối. Với 3 câu hỏi có/không, mỗi câu chỉ hỏi một trong ba đối tượng, xác định ai là ai.

### NQH-006

Cho a và b là các số nguyên dương, nguyên tố cùng nhau. Tìm công thức tính số nguyên lớn nhất không thể viết dưới dạng ax+by, trong đó x và y là các số nguyên không âm.

## Bài [3] — 07/07/2005

### NQH-007

Cho hai sợi dây dài, làm bằng các vật liệu khác nhau, có mật độ vật chất khác nhau ở các điểm khác nhau của từng sợi. Cho biết mỗi sợi dây cháy trong đúng một giờ thì hết. Dùng hai sợi dây (và diêm) để đo 45 phút.

### NQH-008

Cho hai hình lập phương. Ta phải gán các chữ số 0-9 (mỗi mặt một số) ra sao để có thể dùng hai hình lập phương biểu diễn được tất cả các ngày trong tháng.

### NQH-009

Những điểm nào trên quả địa cầu (giả sử là đúng hình cầu) có tính chất sau đây: đi về phía Nam 1km, sau đó về phía Tây 1km, sau đó về phía Bắc 1km thì quay lại điểm cũ.

> (Cả ba câu này tôi được hỏi khi phỏng vấn làm intern ở Microsoft hồi hè 1998.)

## Bài [4] — 08/07/2005

### NQH-010

Cho một mảnh giấy hình chữ nhật với một lỗ hổng hình chữ nhật ở giữa.
Hỏi: Dùng dao cắt mảnh giấy một nhát như thế nào để có hai nửa có diện tích bằng nhau?

### NQH-011

Có 500 cái cửa nằm dọc theo một hành lang đánh số từ 1 đến 100. Lúc đầu các cửa đều đóng. Có 500 người xếp hàng đi dọc hành lang. Anh thứ nhất mở tất cả các cửa; anh thứ hai chuyển trạng thái (mở thành đóng, đóng thành mở) các cửa 2, 4, 6, …; anh thứ ba chuyển trạng thái các cửa 3, 6, 9, …; cứ như vậy đến anh thứ 500 chuyển trạng thái cửa 500.
Hỏi: cuối cùng có bao nhiêu cửa đóng?

### NQH-012

Có hai căn phòng nằm cạnh nhau nhưng không thông nhau, và đứng bên này không thấy bên kia. Phòng 1 có ba cái đèn bóng tròn. Phòng 2 có ba công tắc của ba đèn ở phòng 1. Bạn là người lạ, được dẫn vào phòng 2 trước, được quyền nghịch ngợm tắt mở công tắc tùy ý. Sau đó bạn được sang phòng 1 kiểm tra đèn.
Hỏi: nghịch thế nào ở phòng 2 để biết công tắc nào tương ứng với đèn nào?

## Bài [5] — 09/07/2005

> Có một dạo mailing list vnsa đố vui với nhau khá nhiều, tôi còn nhớ vài câu:

### NQH-013

Tí ở tầng 3, Tèo ở tầng 33 của một chung cư. Một hôm hứng chí cả hai ra ban công hét lên cùng một lúc.
**Hỏi**: ai nghe thấy tiếng của người kia trước?

### NQH-014

Có 10 đồng tiền, thật có giả có. Cho một cái cân đĩa không có quả cân. Các đồng thật nặng bằng nhau, các đồng giả nặng bằng nhau và nhẹ hơn các đồng thật.
Hỏi: cân ba lần và chỉ ra các đồng giả.

### NQH-015

Ba người cần chia một cái bánh sao cho ai cũng thỏa mãn về phần bánh của mình.
Hỏi: tìm giải pháp chia bánh với giả thiết ai cũng tin rằng mình cắt bánh công bằng.

## Bài [6] — 10/07/2005

### NQH-016

(Bài toán Monty Hall) Monty Hall làm MC của một trò chơi trên truyền hình. Có ba cái cửa chắn trước người chơi. Đằng sau một trong các cánh cửa là phần thưởng. Bạn chọn một trong ba cánh cửa. Monty Hall xem đằng sau hai cánh còn lại và mở một cửa không có phần thưởng.
Hỏi: bạn sẽ giữ chọn lựa cũ hay đổi sang cửa còn lại để lấy phần thưởng? Tại sao?

### NQH-017

Tèo yêu hai cô gái Tấm và Cám. Cả ba sống trên cùng một con đường, Tèo ở đoạn giữa. Các xe buýt đi cả hai chiều của con đường, mỗi chiều một tiếng một lần có xe buýt đến (tốc độ đều). Sáng sáng Tèo ra bến xe buýt và đón xe nào đến trước thì đi về hướng ấy. Sau một thời gian dài thì Tèo đi thăm Tấm gấp ba lần đi thăm Cám.
Hỏi: sao lại thế được?

### NQH-018

Có hai xe tải đứng đối diện nhau, cách nhau 100km. Xe 1 có tốc độ 50km/h, xe 2 có tốc độ 30km/h, một con ruồi đậu trên mũi xe 1 bay qua bay lại giữa hai mũi xe với tốc độ 5000km/h. Cả hai xe và con ruồi đều xuất phát cùng một lúc.
Hỏi: đến khi con ruồi bị đè bẹp gí giữa hai xe (đụng nhau) thì con ruồi bay được bao xa?

## Bài [7] — 03/11/2005

### NQH-019

Ba người thuê một phòng khách sạn. Họ đưa cho anh bảo vệ 30 đô. Anh bảo vệ đưa cho người quản lý, nhưng người quản lý trả lại 5 đô vì giá phòng chỉ có 25. Cầm 5 đô, không biết làm sao chia cho 3 người, anh bảo vệ cầm lấy 2 đô xem như tiền boa, còn lại đưa mỗi người 1 đô.
Mồi người bỏ ra 10 đô, lấy lại 1 đô, vị chi là mỗi người 9 đô – tổng cộng 27 đô. Anh bảo vệ lấy 2 đô nữa là 29 đô. Vậy còn 1 đô đi đâu?

### NQH-020

Có n người, trong đó một số luôn nói thật, một số lúc thật lúc dối không biết đâu mà lường. Ta phải phỏng vấn đám người này và chỉ ra tất cả những người luôn nói thật. Những người này biết thông tin thật/dối của tất cả những người còn lại. Các câu hỏi chỉ có thể ở dạng: “hỏi anh A xem anh B thuộc loại nào”.
(i) Nếu biết trước hơn nửa số người thuộc dạng luôn nói thật, tìm chiến thuật phỏng vấn chỉ cần n-1 câu hỏi.
(ii) Có tồn tại chiến lược phỏng vấn nào không nếu chỉ có ít hơn nửa luôn nói thật?
(iii) Giả sử ta tìm được 1 anh nói thật. Dĩ nhiên ta có thể hỏi anh này n-1 câu để biết tất cả những người còn lại thuộc loại nào. Có cách nào tốt hơn không?

### NQH-021

An, Bình, Chung, Dung phải qua cầu khỉ vào buổi tối. Chỉ có một cái đèn pin. Tối đa là hai người đi cùng một lúc, và phải có đèn mới qua/lại được. Họ đi với tốc độ khác nhau. Nếu hai người cùng đi thì cả hai phải đi bằng tốc độ người đi chậm hơn.
An cần 1 phút.
Bình cần 2 phút.
Chung cần 5 phút.
Dung cần 10 phút.
Dĩ nhiên là phải có người cầm đèn đi ngược lại để đón người kế qua nếu cần!
Hỏi: ít nhất họ cần bao nhiêu phút để cả 4 qua được cầu?

## Bài [8] — 04/11/2005

### NQH-022

Có ba hộp kẹo, một toàn kẹo dừa, một toàn sô cô la, hộp còn lại thì nửa này nửa nọ. Nhãn tất cả các hộp đều dán sai. Giả sử ta có một cục kẹo của một hộp, đoán tất cả các hộp xem là gì.

### NQH-023

Cho biểu thức 101 – 102 = 1, di chuyển một chữ số hoặc ký hiệu (-, =) sao cho nó biến thành đẳng thức.

### NQH-024

Cho một ly sữa và một ly cà fê cùng thể tích chất lỏng. Múc 1/10 ly cà fê đổ vào ly sữa, sau đó múc 1/10 ly sữa cà fê đổ vào ly cà fê. Giả sử cà fê và sữa hòa tan tuyệt đối.
Hỏi: sau khi đổ thì phần trăm cà fê và sữa ở hai ly ra sao?

## Bài [9] — 18/01/2006

### NQH-025

Cho một dãy số **A** gồm *n* số thực: $A[1], \dots, A[n]$. Một *dãy con* của **A** là một dãy liên tục các phần tử của **A**. Ví dụ: dãy $A[2], A[3], \dots, A[25]$ là một dãy con của **A**. Tìm một thuật toán chạy trong thời gian $O(n)$ để in ra dãy con có tổng lớn nhất của **A**. (Chú ý là **A** có thể lẫn lộn các số âm, dương.)

### NQH-026

Định nghĩa $\log^{(i)} n = \log \log \dots \log n$ ( $i$ lần), và

$\log^*n = \min\{ i \geq 0 \ : \ \log^{(i)} n \leq 1 \}$

**Hỏi**: trong hai hàm $\log^*(\log n)$ và $\log(\log^*n)$ thì hàm nào tăng nhanh hơn khi $n$ lớn?

### NQH-027

Viết một đoạn chương trình C để xác định xem máy chạy chương trình là big-endian hay little-endian.

## Bài [10] — 04/05/2006

### NQH-028

Viết một đoạn chương trình C để biết stack của một máy grow down hay grow up?

### NQH-029

Cho chuỗi $S_1 = \{ a, b, c, d, \dots, x, y, z, aa, ab, ac, \dots \}$. Biết rằng chuỗi này có ánh xạ một-một đến chuỗi $S_2 = \{1, 2, 3, 4, \dots \}$. Viết một chương trình để chuyển một phần tử của $S_1$ thành một phần tử tương ứng của $S_2$. Viết chương trình chuyển theo chiều ngược lại.

### NQH-030

Cho một hình vuông đơn vị, mô tả các điểm trong hình vuông này mà nằm gần tâm hơn cạnh ngoài.

## Bài [11] — 29/05/2006

### NQH-031

Có bao nhiêu số 0 ở đằng cuối của biểu diễn thập phân của $n!$?

### NQH-032

Khi ta soi gương, giơ tay trái lên thì hình nhân trong gương giơ tay phải của hắn. Tuy nhiên, khi ta cúi đầu thì hình nhân trong gương cũng cúi đầu. Tại sao gương “lật” trái/phải, nhưng không “lật” trên/dưới?

### NQH-033

Có 9 túi đựng tiền, mỗi túi chứa ít nhất 100 đồng tiền, trong đó có một túi chứa toàn tiền giả. Các đồng tiền thật đều nặng 100 grams. Các đồng tiền giả đều nặng 90 grams. Cho một cái cân đĩa (1 đĩa và đồng hồ chỉ cân nặng), cân **1 lần** để xác định túi nào chứa tiền giả?

## Bài [12] — 29/05/2006

> Lần trước có vẻ chưa “đủ đô” :-), tiếp tục nhé

### NQH-034

Có ba bình nước có dung tích rất lớn, chứa x, y, và z lít nước theo thứ tự. Trong đó, x, y, z là các số nguyên dương. (Dung tích của các bình lớn hơn x, y, z nhiều. Ta cần sớt nước giữa các bình để có một bình trống. Không được đổ nước ra ngoài. Tuy nhiên, mỗi lần san nước từ bình A sang bình B thì ta phải nhân đôi thể tích nước trong bình B. Ví dụ: nếu x, y, z = 4, 6, 3, thì ta có thể làm như sau

4 6 3

8 2 3

5 2 6

5 4 4

5 8 0

**Chứng minh rằng**: với x, y, z bất kỳ ta đều có thể san nước để có bình trống.

### NQH-035

Thằng Tí có một ma trận vuông A (kích thước n x n) chứa toàn các số thực dương. Tèo muốn tìm tổng các số trên đường chéo chính. Tèo được quyền hỏi Tí tổng các số trong một ma trận vuông con bất kỳ của A, nhưng mỗi lần hỏi thì tốn 1 đô la. **Hỏi:** Tèo phải tốn ít nhất bao nhiêu đô la để biết được số cần tìm? (Ví dụ: n đô la dĩ nhiên là đủ!)

### NQH-036

Tèo phải gán màu cho các điểm trong mặt phẳng
1
\mathbb{R}^2

. Mỗi điểm một màu. Hai điểm cách nhau 1 đơn vị phải khác màu nhau. **Chứng minh** rằng Tèo cần ít nhất 4 màu và nhiều nhất 7 màu.

> (À quên, câu tôi thích nhất là câu số 4 vẫn chưa có ai giải – chú ý rằng mỗi lần dùng căn bậc 2 là mỗi lần dùng một số 2)

## Bài [13] — 31/05/2006

> Một sinh viên của tôi vừa phỏng vấn với Google và Yahoo. Ba câu hỏi sau đây còn “nóng hổi”:

### NQH-037

Cho một linked list (danh sách liên kết) và pointer đến đầu linked list. Ta không biết trước tổng số phần tử trong list là bao nhiêu. Viết một function trả về pointer đến một phần tử ngẫu nhiên trong list (uniform distribution), mà chỉ được duyệt qua linked list 1 lần. (Nghĩa là không được đếm tổng số phần tử n, chọn ngẫu nhiên từ 1 đến n, rồi duyệt lần 2 để trả về con trỏ ngẫu nhiên.)

### NQH-038

Cho một array **A** các ký tự trong một bộ ký tự nào đó, và một tập **S** của vài ký tự. Viết một function chạy trong thời gian tuyến tính, trả về sub-array nhỏ nhất của **A** chứa tất cả các ký tự trong **S**.

### NQH-039

Cho một ma trận m hàng n cột. Các con số trên các hàng đều tăng dần từ trái sang phải, và trên các cột đều tăng dần từ trên xuống dưới. Viết một thủ tục tìm một số xem nó có trong ma trận không? Thời gian chạy là bao nhiêu? (**Lưu ý**: đây là phiên bản 2-D của binary search.)

## Bài [14] — 15/06/2006

### NQH-040

Có bao nhiêu số nguyên tố có dạng thập phân hoán chuyển giữa 0 và 1, bắt đầu và kết thúc bằng 1 (nghĩa là dạng 1010…101)?

### NQH-041

Có n người, mỗi người có một bí mật riêng. Họ gọi điện thoại lẫn nhau, mỗi lần gọi thì hai đối tượng trao đổi **tất cả** các bí mật mà hai đối tượng biết. Cần ít nhất bao nhiêu cuộc gọi để mọi người biết mọi bí mật?

### NQH-042

Tìm số nguyên có dạng ABCDEFGHIJ, trong đó A là tổng số chữ số 0 trong số nguyên này, B là tổng số chữ số 1, vân vân.

## Bài [15] — 17/06/2006

> Hôm nay có chuyên đề về … kiến

### NQH-043

Có một sợi dây cao su, một đầu buộc vào tường, đầu kia buộc vào một chiếc xe đi xa khỏi tường với tốc độ 100m/h. Giả sử sợi dây có độ giãn vô hạn và giãn đồng nhất (uniformly). Một con kiến bò trên sợi dây từ trong tường về hướng chiếc xe với tốc độ 1m/h. Con kiến có bao giờ đi tới đụng chiếc xe không? Tại sao?

### NQH-044

Bốn con kiến nằm ở bốn đỉnh một hình vuông đơn vị. Mỗi con đi về hướng con kề nó theo chiều kim đồng hồ. Tốc độ các con kiến bằng nhau. Mỗi con đi được bao xa thì gặp đối tượng?

### NQH-045

Không dùng máy tính, số nào lớn hơn giữa $e^{\pi}$ và $\pi^e$?

## Bài [16] — 19/06/2006

### NQH-046

Cho số thực $x$ bất kỳ, chứng minh rằng trong dãy số $x, 2x, 3x, \dots, (n-1)x$ có ít nhất một số nằm trong khoảng $1/n$ của một số nguyên.

### NQH-047

Tuyết bắt đầu rơi trước nửa đêm. Đến nửa đêm có một xe ủi tuyết đi ủi trên đường. Xe đi được một dặm trong 1 giờ đầu tiên, và 1/2 dặm trong giờ thứ hai. Tuyết bắt đầu rơi từ khi nào? (Giả sử xe ủi đi với tốc độ tỉ lệ nghịch với chiều cao của tuyết.)

### NQH-048

An cần gửi một nhẫn kim cương cho Bình. An và Bình mỗi đứa có vài cái khóa cùng chìa cho chúng (mỗi khóa một chìa). An có một cái hộp thừa lớn để bỏ nhẫn vào. Hộp có móc tròn khá lớn để tròng khóa vào. Làm thế nào để An gửi nhẫn cho Bình một cách bảo đảm?

## Bài [17] — 29/08/2006

> Vài câu hỏi về ngôn ngữ C.

### NQH-049

Tại sao C không có nested functions?

### NQH-050

Làm thế nào để gọi một hàm trong C nếu ta có tên hàm chứa trong một string cho trước? (Ví dụ: ta biết func_name = "some_name", làm thế nào để gọi hàm some_name?)

### NQH-051

Làm thế nào để allocate arrays hay structures lớn hơn 64K?

### NQH-052

Lệnh printf("%d"); sẽ in ra cái gì, tại sao?

### NQH-053

Trong các định nghĩa sau đây, cái gì là const?

```
const char* variable;
const* char variable;
char* const variable;

```

## Bài [18] — 22/09/2006

> Lần trước có đến 5 câu, lần này chỉ 1 để giữ trung bình 3 câu mỗi lần. Câu này rất phản trực quan, và là nội dung một định lý nằm trong hầu hết các sách về real analysis với một ít measure theory trong đó.

### NQH-054

Có tồn tại một mớ đoạn mở (open intervals) trên trục các số thực với tổng chiều dài (measure) hữu hạn sao cho một số hữu tỉ bất kỳ đều thuộc về một trong các đoạn mở này? (**Gợi ý**: không những tồn tại “mớ” đoạn mở này, mà tổng chiều dài của chúng có thể nhỏ tùy ý!)

## Bài [19] — 02/10/2006

### NQH-055

Có 30 sinh viên đứng thành vòng tròn. Họ nhắm mắt lại. Giáo sư Tèo đội cho mỗi người một cái mũ. Tổng cộng có 20 mũ đen, 10 mũ trắng. Sau đó các sinh viên được quyền mở mắt. Họ thấy các mũ khác nhưng không biết mình đang đội mũ màu gì. Họ không được quyền trao đổi thông tin.
Giáo sư Tèo nói: “*Ít nhất một trong số các bạn đang đội mũ đen*“.

Sau đó giáo sư Tèo ra lệnh: “*Sinh viên nào đã xác định được rằng mũ mình đang đội là màu đen thì ngồi xuống*“.

Dĩ nhiên, chẳng ai ngồi xuống vì không ai biết mình đang đội mũ màu gì.

Một phút sau, giáo sư Tèo lập lại lệnh trước: “*Sinh viên nào đã xác định được rằng mũ mình đang đội là màu đen thì ngồi xuống*“.

Vẫn không ai di động. Giáo sư Tèo lập lại lệnh này, mỗi phút một lần, trong vòng 30 phút kế tiếp.

**Câu hỏi 1**: cái gì xảy ra? Khi nào?

**Câu hỏi 2**: khi giáo sư Tèo nói “*Ít nhất một trong số các bạn đang đội mũ đen*” thì các sinh viên có thêm thông tin gì không? Vì rõ ràng là mỗi sinh viên đều biết là có mũ đen trong đám.

### NQH-056

Tôi xào một bộ bài thật kỹ, sau đó từ từ mở bài từng lá một. Bạn có quyền bảo tôi “dừng” lúc nào cũng được. Nếu lá kế tiếp (sau khi bạn bảo dừng) có màu đỏ (cơ hoặc rô) thì bạn thắng. Nếu đen thì bạn thua. Nếu bạn không nói “dừng” thì bạn thua. **Hỏi**: bạn có thuật toán nào làm cho bạn thắng với xác suất hơn 50% không? Xác suất lớn nhất là bao nhiêu?

### NQH-057

501 cặp vợ chồng đi dự một buổi tiệc. Đến cuối tiệc, Tấm (một cô vợ) bảo những người khác ghi lại tổng số người họ đã bắt tay trong tiệc. Các con số được ghi ra là: 0, 1, 2, …, 1000. Giả sử không có ai bắt tay vợ/chồng mình. **Hỏi**: Tấm bắt tay bao nhiêu người?

## Bài [20] — 21/11/2006

> Giáo sư Peter Winkler có một quyển sách về đố vui cực hay. Tôi sẽ trích ra vài câu hỏi trong quyển này ở vài posts tới cho “các câu hỏi phỏng vấn”. Có vài câu hỏi trong chuỗi “các câu hỏi phỏng vấn” có trong sách, nhưng tôi biết chúng qua các nguồn khác. Quyển sách này tôi mới mua hôm qua. Khó mà đặt nó xuống.

### NQH-058

Cô giáo vào lớp học ngày đầu tiên của năm mới, thấy hai chú nhóc trông giống hệt nhau ngồi bàn đầu, tên là Trần văn Tí và Trần văn Tèo.

“*Các em sinh đôi hả*“, cô giáo hỏi.

“*Dạ không phải*“, Tí và Tèo đồng thanh trả lời.

Cô giáo kiểm tra học bạ thì thấy Tí và Tèo có cùng cha mẹ và được sinh ra cùng ngày. Làm thế nào có thể thế được?

### NQH-059

Cả nước trong tình trạng thiếu xăng. Có một con đường vòng (tròn) rất dài. Các trạm xăng nằm rải rác trên đường. Tèo muốn lái xe hơi một vòng trên đường và quay lại chỗ cũ. Tổng cộng số xăng trên tất cả các trạm cộng lại vừa đủ cho chuyến đi này. Chứng minh rằng, từ một bình xăng rỗng, có một trạm xăng mà nếu Tèo bắt đầu đi từ đó thì sẽ kết thúc được chuyến đi.

### NQH-060

Một hình chữ nhật được phân hoạch thành nhiều hình chữ nhật nhỏ. Mỗi hình chữ nhật nhỏ này hoặc có chiều dài nguyên hoặc có chiều rộng nguyên (hoặc cả hai). Chứng minh rằng hình chữ nhật lớn cũng có tính chất tương tự.

## Bài [21] — 24/11/2006

### NQH-061

Có 100 tờ tiền đô la xếp thành một hàng dài trên bàn. Tổng giá trị của chúng là một số lẻ đô la. An và Bình chơi trò chơi như sau: họ luân phiên nhau lấy một trong hai tờ tiền ở đầu hàng hoặc cuối hàng. An lấy trước. Ai lấy nhiều tiền hơn thì thắng. Ai chắc chắn sẽ thắng? Chiến lược thắng ra sao?

### NQH-062

Có năm mươi cái đồng hồ để trên bàn. Các đồng hồ đều chạy tuyệt đối chính xác. Chứng minh rằng có một thời điểm mà tổng khoảng cách từ tâm bàn đến đỉnh các kim phút lớn hơn tổng khoảng cách từ tâm bàn đến tâm các đồng hồ.

### NQH-063

An và Bình thay phiên nhau chọn các số nguyên từ 1 đến 9. Số đã chọn không được chọn lại. Ai chọn được 3 số có tổng bằng 15 trước là thắng. Ai sẽ thắng?

## Bài [22] — 09/12/2006

### NQH-064

Giả sử

$f(x) = x^{x^{x^{\vdots}}} = 2$

(mũ x đến vô cùng). Vậy $x$ bằng bao nhiêu? Ví dụ, ta có thể lý luận như sau. Dễ thấy rằng $f(x) = x^{f(x)}$. Do đó $2 = x^2$, hay $x = \sqrt{2}$. Nhưng nếu $f(x) = 4$ thì, theo lý luận trên, $4 = x^4$ cũng dẫn đến $x = \sqrt{2}$. Sao lạ thế? $f(\sqrt{2}) = 2 = 4$ à?

### NQH-065

An và Bình nghĩ ra trò ảo thuật sau đây. An quay mặt đi. Cho một người bất kỳ xào một bộ bài, chọn ra năm lá đưa cho Bình. Bình xem năm lá này, lấy ra một lá giấu đi, rồi chuyền bốn lá còn lại cho An. An nhìn bốn lá này và đoán được lá bài Bình giấu là lá gì. Làm thế nào mà họ làm được?

### NQH-066

Có một cái đồng hồ mà kim giờ và kim phút giống hệt nhau. Có bao nhiêu thời điểm trong ngày mà nhìn đồng hồ này ta không thể biết được là mấy giờ?

## Bài [23] — 23/12/2006

### NQH-067

Có một mớ bánh ngọt với tổng cân nặng không hơn 2kg. Mỗi cái bánh nặng ít hơn 1kg. Chứng minh rằng ta có thể chia mớ bánh này ra thành nhiều nhất là 4 phần, mỗi phần có tổng cân nặng nhiều nhất là 1kg. (Không được cắt bánh ra.) Có thể nào luôn chia được thành nhiều nhất 3 phần thỏa điều kiện trên không?

### NQH-068

Cho n số nguyên dương đặt trên một đường tròn. Thay mỗi số bằng trị tuyệt đối của số đi sau trừ đi chính nó, theo chiều kim đồng hồ. Dừng lại khi tất cả các số bằng 0. Chứng minh rằng với n=5 thì ta có thể không dừng được. Với n=4 thì ta luôn dừng.

### NQH-069

Gọi S là một tập 10 số khác nhau giữa 1 và 100. Chứng minh rằng S có hai tập con không giao nhau với tổng bằng nhau.

## Bài [24] — 11/01/2007

### NQH-070

Tèo leo đỉnh Phan-xi-pang. Bắt đầu sáng thứ bảy từ chân núi đến tối thì lên đến đỉnh. Ngủ một đêm, sáng chủ nhật Tèo leo xuống, đến hoàng hôn thì đến chân núi. Chứng minh rằng có cùng một thời điểm (ví dụ như 1 giờ 2 phút chiều) trong ngày thứ bảy và chủ nhật mà Tèo ở cùng một độ cao.

### NQH-071

Có một tập hợp các điểm trên mặt phẳng. Không phải tất cả cùng nằm trên một đường thẳng. Chứng minh rằng có một đường thẳng chỉ đi qua hai điểm mà thôi.

### NQH-072

Có n điểm xanh và n điểm đỏ trên mặt phẳng, không có 3 điểm nào thẳng hàng, các điểm đều khác nhau. Chứng minh rằng có một cách ghép cặp 1-1 xanh đỏ sao cho các đoạn thẳng nối các cặp này không cắt nhau.

## Bài [25] — 01/03/2007

### NQH-073

Ta có n mẫu máu. Mỗi mẫu máu thuộc về một trong m nhóm máu. (Ta không biết chính xác m là bao nhiêu, và m không nhất thiết phải là hằng số.) Có một thiết bị mà nếu bỏ vào đó hai giọt máu từ hai mẫu máu khác nhau thì thiết bị sẽ cho biết hai mẫu máu có cùng nhóm máu hay không. Nếu bỏ vào thiết bị này hơn hai giọt máu thì câu trả lời không đáng tin cậy nữa.
Ta muốn trả lời câu hỏi sau đây: có hay không hơn n/2 mẫu máu thuộc về cùng một nhóm máu. Dùng thiết bị trên để thử, làm thế nào để trả lời câu hỏi này với tổng số ít nhất các phép thử? (Chỉ cần ít nhất về mặt asymptotic là được.) Ví dụ: cách dễ nhất là thử tất cả các cặp mẫu máu nhưng như vậy cần dùng đến $\Theta(n^2)$ phép thử.

Ngoài ra, ta cũng giả sử rằng mỗi mẫu máu có khá nhiều giọt.

## Bài [26] — 23/03/2007

### NQH-074

Phân hoạch tập hợp $\{1, 2, \dots, 16\}$ thành hai tập A và B sao cho tổng các phần tử trong A bằng tổng các phần tử trong B **và** tổng bình phương các phần tử của A và B bằng nhau **và** tổng lập phương của các phần tử của A và B bằng nhau.

### NQH-075

Một lão nông qua đời để lại cho 3 con 17 con trâu. Trong di chúc, ông muốn cho con trưởng 1/2, con kế 1/3, và con út 1/9 số trâu. Ba người con phân chia thế nào?

## Bài [27] — 27/04/2007

### NQH-076

Có một số $2^n$ ( $n$ lớn tùy ý) các anh lính đứng thành vòng tròn, cầm súng hướng mặt ra ngoài. Mỗi người có bộ nhớ kích thước bằng hằng số (nghĩa là memory space = O(1)) và chỉ có thể trao đổi thông tin với người đứng bên trái và người đứng bên phải. Giả sử thời gian được chia thành các thời điểm rời rạc: 0, 1, 2, 3, … Tại thời điểm số 0, ông tướng vỗ vai một anh lính nào đó và hạ lệnh “bắt đầu”.
Các anh lính phải trao đổi thông tin thế nào để tất cả bóp cò cùng một lúc?

### NQH-077

Có N anh cướp biển sắp bị xử chém. Họ xếp thành một hàng dài. Mỗi người đội một chiếc nón, xanh hoặc đỏ. Cướp biển số 1 chỉ thấy nón (và màu nón) của cướp biển số 2, 3, … N; cướp biển số 2 chỉ thấy nón của số 3, 4, … N; vân vân. Dĩ nhiên, vì thế mỗi cướp biển không biết màu nón mình đang đội và màu nón của các cướp biển đứng trước mình trong hàng.
Đao phủ bắt đầu chém từng cướp biển một, từ số 1 đến số N. Tuy nhiên, trước khi chém mỗi cướp biển thì đao phủ cho hắn một cơ hội: đoán màu nón của mình. Nếu nói đúng màu nón thì được tha. Tất cả các cướp biển đều nghe thấy nhau trả lời, nhưng không biết ai bị chém ai không.

Trước hôm ra xử bắn, bọn cướp biển họp lại và tìm một thuật toán trả lời để cho tổng số cướp biển bị chém là ít nhất trong trường hợp tệ nhất (in the worst case). Ví dụ: nếu cướp biển số 2k-1 trả lời bằng màu nón của cướp biển 2k, và cướp biển 2k lập lại câu trả lời này, thì tệ nhất cũng chỉ có một nửa số cướp biển bị chém.

Nếu bạn là cướp biển thì bạn thiết kế thuật toán thế nào?

## Bài [28] — 16/05/2007

### NQH-078

Bạn có 300 lít xăng và một cái xe tải. Xa tải chỉ chở được tối đa 100 lít xăng. Bạn muốn chở xăng đến bán ở chợ xăng cách khởi điểm 100 cây số. Vấn đề là xe tải chạy rất tốn xăng, mỗi cây số tốn 1 lít. Bạn được phép chở xăng để dọc đường rồi sau đó quay lại lấy để chở đi tiếp. **Hỏi**: Làm thế nào để bán được nhiều xăng nhất? (Nhớ là nếu bạn để xăng đâu đó dọc đường rồi quay lại lấy thêm xăng thì đoạn quay lại cũng tốn xăng.)

### NQH-079

Có một bàn cờ 8 x 8, các ô là các hình vuông đơn vị. Làm thế nào để cắt 3 mảnh giấy thỏa mãn điều kiện sau đây: với bất kỳ một ô X nào trên bàn cờ ta cũng có thể dùng 3 mảnh giấy để phủ bàn cờ sao cho

Ô X không bị phủ bất kỳ chỗ nào

Tất cả các ô còn lại đều bị phủ

Các mảnh giấy không có phần nào chồng lên nhau

Không có phần nào phủ ra ngoài bàn cờ

## Bài [29] — 17/07/2007

> Đề tài hôm nay là các số trên vòng tròn.

### NQH-080

25 hòn sỏi đen và 25 hòn sỏi trắng được xếp thành vòng tròn. Chứng minh rằng có một hòn sỏi mà hai hòn hai bên (trái, phải) đều trắng.

### NQH-081

Có n số thực nằm trên một vòng tròn với tổng không âm. Chứng minh rằng tồn tại một trong n số này, tạm gọi là số x, thỏa mãn điều kiện sau đây: với mọi k > 0 thì tổng của k số thực, kể từ x theo chiều kim đồng hồ, là không âm.

### NQH-082

Giả sử ta có n số nguyên trên một vòng tròn. Ta được phép làm một phép biến đổi, gọi là “**biến đổi tếu**“, như sau: tìm 3 số (a,b,c) nằm kề nhau liên tục trên vòng tròn, trong đó b < 0, và đổi chúng thành (a+b, -b, c+b). Mệnh đề sau đây đúng hay sai: *có thể gán n số nguyên vào một vòng tròn để ta có thể **biến đổi tếu** mãi mãi, không bao giờ bị kẹt*

## Bài [30] — 30/01/2009

### NQH-083

(Câu này do anh Nghị gửi hôm qua.) Có 15 cái túi, cần ít nhất bao nhiêu hòn sỏi để mỗi túi chứa số hòn sỏi khác nhau?

### NQH-084

(Câu này lấy bên Puzzle Toad.) Có hai điểm A và B nằm trong hình vuông đơn vị. B có thể bắn một tia laser ra theo hướng tùy thích. Tia laser này nếu đụng vào cạnh của hình vuông thì sẽ phản xạ lại (như phản xạ ánh sáng tuyệt hảo). A có quyền rải “vệ sĩ” trong hình vuông, mỗi vệ sĩ là một điểm trong hình. Nếu tia laser từ B bắn ra đi qua một vệ sĩ thì nó bị dừng lại (và vì thế không trúng A).
A cần bao nhiêu “vệ sĩ”, và đặt ở đâu, để cho không có bất kỳ tia laser nào từ B có thể bắn trúng A. Một số hữu hạn các vệ sĩ có đủ không?

## Bài [31] — 19/02/2009

> Cả hai câu hỏi đều rất hay.

### NQH-085

(Câu này do anh Minh gửi.) Có n tù nhân và một phòng biệt giam trong đó có 2 công tắc. Mỗi ngày, một tù nhân được chọn ngẫu nhiên và nhốt vào phòng. Hôm sau, tù nhân đó được thả ra khỏi biệt giam. Một trong số n tù nhân lại được chọn ngẫu nhiên và nhốt vào biệt giam. Tất cả sẽ được thả nếu một ngày nào đó có một tù nhân đoán đúng rằng tất cả các tù nhân đều đã từng vào biệt giam. Nếu đoán sai sẽ bị giết sạch. Các tù nhân không liên lạc được với nhau ngoại trừ hai cái công tắc.
Họ phải làm sao để được thả?

### NQH-086

(Câu này do anh Nghị gửi.) Có 100 tù nhân. Trong một căn phòng lớn có 100 cái hộp, mỗi hộp đựng tên một tù nhân. Các tù nhân được quyền bàn thảo kế hoạch với nhau trước. Sau đó, hoàn toàn không liên lạc với nhau nữa, từng tù nhân được dẫn vào phòng. Mỗi anh vào được mở xem 50 cái hộp tùy ý, sau đó phải rời phòng và để lại trạng thái mọi thứ trong phòng y hệt như cũ. Tất cả các tù nhân sẽ được thả nếu tất cả các tù nhân đều tìm thấy tên mình trong 50 cái hộp mà mình mở.
Kế hoạch của các tù nhân như thế nào để xác suất được thả là lớn hơn 30 phần trăm?

## Bài [32] — 04/03/2009

> Đây là mấy câu hỏi phỏng vấn kinh điển. Rất nhiều các câu hỏi PV của Microsoft và Google là biến thể của hai câu sau đây:

### NQH-087

Viết một hàm int significant_place(uint32_t x) bằng ngôn ngữ C, trả về vị trí của bit 1 cuối cùng bên trái của x (position of the most significant bit)

### NQH-088

Viết một hàm int count_ones(uint32_t x) bằng ngôn ngữ C, trả về tổng số bít 1 trong biểu diễn nhị phân của x. Hàm chạy càng nhanh càng tốt. (Có khá nhiều cách trả lời khác nhau cho bài này, mỗi cách có cái hay riêng. Quyển Beautiful Code có hẳn một chương về bài này.)

> **Cập nhật 4 tháng 3**: một sinh viên của tôi vừa phỏng vấn với Bloomberg chiều nay. Một trong số các câu hỏi là một câu hỏi kinh điển của cấu trúc dữ liệu:

### NQH-089

Giả lập một queue bằng 2 stacks, sao cho amortized cost của enqueue và dequeue là O(1).

## Bài [33] — 13/01/2010

> Cảm ơn bác Vũ Hà Văn cho câu hỏi số 90 rất dễ thương. Câu 91 là một sinh viên của tôi vừa phỏng vấn ở Google được/bị hỏi. Câu 92 chôm từ chùa THT, do bác Đàm Thanh Sơn truyền bá từ quyển sách thú vị của Mark Levi.

### NQH-090

Có 10 con kiến trên một que 1 mét. Từng con kiến bắt đầu bò sang trái hoặc phải tùy hỉ, dọc theo que, với tốc độ 1 mét/giờ. Khi hai con kiến đụng đầu nhau chúng sẽ đổi hướng. Khi một con bò đến đầu que thì nó rới xuống đất. Hỏi: khi nào thì tất cả kiến rơi xuống đất?

### NQH-091

Cho n dãy ký tự, mỗi dãy có n ký tự. Tìm dãy con chung lớn nhất của tất cả n dãy trong thời gian càng nhanh càng tốt. Ví dụ, ba dãy abcxyz, xabcfb, xyzabc có dãy con abc chung.

### NQH-092

Một người đi xe đạp hai bánh trong sân. Vết bánh trước và bánh sau tạo thành hai đường cong trơn khép kín không giao nhau. Chứng minh rằng diện tích hình vành khăn nằm giữa hai đường cong khép kín này là một hăng số chỉ phụ thuộc vào cái xe đạp, không phụ thuộc gì vào cơ bắp hay nghệ thuật của người đi.

## Bài [34] — 03/02/2010

### NQH-093

100 hành khách lên xe lửa đi chuyến Bắc Nam. Xe lửa có 100 ghế. Tèo lên trước, thay vì ngồi đúng số ghế của mình thì Tèo ngồi vào một nghế ngẫu nhiên. Các hành khách sau đó, từng người một, ngồi vào đúng ghế trên vé nếu ghế trống, nếu không thì ngồi vào ghế trống ngẫu nhiên. **Hỏi**: xác suất mà hành khách cuối cùng ngồi đúng ghế là bao nhiêu?

### NQH-094

Câu 94 lấy từ blog của giáo sư Gil Kallai. *(Nội dung là video YouTube 4s2uczTGRfU, bản lưu không có đề dạng chữ.)*

## Bài [35] — 26/05/2010

### NQH-095

Cho một ma trận vuông $n \times n$ chứa các số thực. Bạn được phép đổi dấu tất cả các số trên một hàng hoặc một cột bất kỳ, và đổi dấu kiểu đó bao nhiêu lần tùy hỉ. Có thể nào, sau một số hữu hạn các lần đổi dấu, biến ma trận này thành ma trận mà tổng mỗi hàng và tổng mỗi cột đều không âm?

### NQH-096

Mỗi mặt của một đa diện lồi có một con kiến bò. Kiến bò trên các cạnh của mặt, theo chiều kim đồng hồ. Mỗi con kiến bắt đầu ở một điểm tùy hỉ trên mặt của nó, và bò với vận tốc biến thiên tùy hỉ. Chứng minh rằng không có cách nào cho bọn kiến bò, mỗi con quay lại điểm khởi đầu của nó, mà không đụng vào nhau.

### NQH-097

Cho một thanh sô-cô-la kích thước $m \times n$, gồm $mn$ ô vuông. Ta muốn bẻ thanh này thành $mn$ ô để chia cho trẻ con. Mỗi bước, chọn một mảnh bất kỳ và bẻ đôi miếng này dọc hoặc ngang theo ranh giới tự nhiên. Chứng minh bẻ kiểu gì cũng cần cùng số bước.

## Bài [36] — 28/06/2010

> (Cảm ơn anh Nghị gửi câu 98 rất hay!)

### NQH-098

Cho một đồ thị, mỗi đỉnh có một bóng đèn và một công tắc. Chuyển trạng thái công tắc ở một đỉnh thì sẽ dẫn đến sự đổi trạng thái của bóng đèn ở đỉnh đó và tất cả các bóng đèn ở các đỉnh kề với đỉnh đó. **Hỏi**: nếu lúc đầu tất cả các bóng đèn đều tắt, thì có cách nào bật tất cả các bóng đèn với một đồ thị bất kỳ không?

### NQH-099

Có 2n+1 đôi bóng trong một bảng cúp thế giới. Mỗi đội chơi một trận với tất cả các đội còn lại. Một *vòng tam giác* là một bộ 3 đội A, B, C mà A thắng B, B thắng C, và C thắng A. **Hỏi**: số vòng tam giác tối thiểu phải là bao nhiêu? Số vòng tam giác tối đa có thể có là bao nhiêu?

### NQH-100

25 nghị gật ngồi quanh bàn tròn, bỏ phiếu (yes hoặc no) cho các luật lệ nghị quyết nghị định. Anh nghị gật nào cũng bỏ phiếu như sau: ở lần bỏ phiếu thứ n+1, nghị gật bỏ phiếu giống như phiếu thứ n nếu như phiếu thứ n của anh giống với ít nhất một trong hai phiếu thứ n của hai anh bên cạnh; nếu không thì phiếu thứ n+1 của nghị gật sẽ ngược lại với phiếu thứ n. **Hỏi**: chứng minh rằng bất kể phiếu đầu tiên bỏ thế nào, sau một khoảng thời gian hữu hạn các nghị gật sẽ không đổi trạng thái phiếu nữa.

> Thế là bộ các câu hỏi phỏng vấn đã đạt đến số 100! Khi nào đến số 1000 thì tôi ngưng

## Bài [37] — 23/11/2010

> (Câu 102 là một biến thể của một câu hỏi trước đây, nhưng dạng này kịch tính hơn một chút.)

### NQH-101

Bạn bị bịt mắt. Tèo đưa cho bạn một bộ bài 13 lá ngửa, các lá còn lại xấp. 13 lá bài ngửa nằm ngẫu nhiên trong bộ bài. **Hỏi**: Vẫn bịt mắt. Làm thế nào bạn có thể chia bộ bài đó làm hai xấp mà tổng số lá bài ngửa trong hai xấp bài là bằng nhau? (Bạn có thể lật các lá bài tùy hỉ trong tình trạng bị bịt mắt.)

### NQH-102

Một làng nọ có 100 dân, 23 người mắt xanh, 77 người mắt nâu. Mỗi người thấy màu mắt của tất cả 99 người còn lại, nhưng không biết màu mắt mình. Tất nhiên, họ không biết là có 23 xanh 77 nâu. Lệ làng nói rằng *ai biết màu mắt bản thân thì đúng nửa đêm hôm biết màu mắt phải ra giữa làng tự tử*. Tất cả dân làng đều cực kỳ thông minh, duy lý ;-), tuân thủ lệ làng, và đều biết là cả làng thông minh và tuân lệ làng. Một hôm có chú Tèo ở làng bên lon ton sang thăm. Buổi chiều họp toàn làng đứng lên phát biểu: *“ớ, làng này có bác mắt xanh!”*. **Hỏi**: chuyện gì sẽ xảy ra? Tại sao?

### NQH-103

Vua Hùng xây cho Mỵ Nương 17 cái phòng nằm liền nhau. Các phòng thông nhau. Mỗi đêm Mỵ Nương ở một phòng. Đêm hôm sau thì sang một phòng kề bên, tùy hứng nàng. Sơn Tinh đến cầu hôn. Vua Hùng bảo: mỗi ngày chú đến gõ cửa một phòng, và chỉ một mà thôi. Nếu đúng phòng Mỵ Nương ở hôm đó thì lấy được vợ. Sơn Tinh chỉ có 30 ngày để gõ cửa trước khi về núi. **Hỏi**: tư vấn cho Sơn Tinh đê.

## Bài [38] — 16/03/2011

### NQH-104

Bạn có 2 cái lọ và 100 viên bi trong đó có 50 viên đỏ và 50 viên xanh. Giả sử mỗi lọ đủ lớn để đựng hết số bi. Hãy dàn xếp 100 bi vào 2 lọ sao cho, nếu ta lấy ngẫu nhiên một lọ và chọn ngẫu nhiên một bi trong lọ thì xác suất được bi đỏ là tối đa.

### NQH-105

Cho $n$ cặp số $(a_i, b_i), i \in [n]$. Bạn không có quyền tráo đổi các con số giữa các cặp, nhưng bạn có quyền hoán chuyển $a_i \leftrightarrow b_i$. Hãy thiết kế một thuật toán hoán chuyển bên trong từng cặp, và hoán chuyển vị trí của các cặp, sao cho cuối cùng thi ta có $a_1 \leq \cdots \leq a_n$ và $b_1 \geq \cdots \geq b_n$. Thuật toán in ra **“không tồn tại”** nếu mà không tồn tại một cách hoán chuyển như vậy. (Credit: bài chôm từ TCS stackexchange.)

### NQH-106

Cho ba dãy, mỗi dãy gồm $k$ cặp số nguyên dương $A = \{(x^a_1, y^a_1), \dots, (x^a_k, y^a_k)\}$, $B = \{(y^b_1, z^b_1), \dots, (y^b_k, z^b_k)\}$, và $C = \{(z^c_1, x^c_1), \dots, (z^c_k, x^c_k)\}$. Ta có thể chứng minh được rằng không tồn tại nhiều hơn $k^{3/2}$ điểm $(x,y,z)$ sao scho $(x,y) \in A$, $(y, z) \in B$, và $(z,x) \in C$. Gọi các điểm này là các *điểm ba màu*. Với inputs là $A, B, C$, để in ra các điểm ba màu thì thời gian chạy $O(k^3)$ là tầm thường. Và, ta biết trong trường hợp tệ nhất thì cần $\Omega(k^{3/2})$. **Hỏi:** thiết kế thuật toán với thời gian chạy càng nhanh càng tốt để in ra toàn bộ các điểm ba màu. Có thể đạt tới $O(k^{3/2})$ được không?

## Bài [39] — 30/08/2011

### NQH-107

Viết một thủ tục (bằng C hay Python) làm tác vụ sau đây. Cho một chuỗi ký tự p[0..m-1], tính chuỗi số ms[0..m-1], trong đó ms[i] bằng chiều dài của hậu tố (suffix) chung dài nhất của hai chuỗi p[0..m-1] và p[0..i]. Tất nhiên, yêu cầu là viết mã gọn và chạy nhanh.

> Lưu ý, các bạn có thể hiển thị mã đẹp bằng cách bỏ chương trình vào cặp [code lang="Python"] và [/code] Thay Python bằng C nếu viết bằng C.

## Bài [40] — 09/11/2011

> Một sinh viên khoa tôi mới đi phỏng vấn tháng rồi. (Anh ta sẽ làm việc ở Groupon.) Có câu hỏi sau đây rất hay.

### NQH-108

Viết wrapper functions Malloc() và Free() dùng malloc() và free() sao cho Malloc() luôn trả về một con trỏ “memory word aligned”, nôm na là con trỏ trỏ đến địa chỉ chia hết cho 4. (Ta không thể bắt malloc() trả về một địa chỉ như vậy được.)

## Bài [41] — 31/01/2012

### NQH-109

Chọn 3 điểm ngẫu nhiên trên đường tròn, xác suất có tam giác vuông là bao nhiêu?

### NQH-110

Chọn 3 điểm ngẫu nhiên trên đường tròn, xác suất có tam giác nhọn là bao nhiêu?

## Bài [42] — 31/03/2012

### NQH-111

Cho một cây nhị phân với cấu trúc đỉnh như sau:
struct BTNode {
    int data;
    BTNode* left;
    BTNode* right;
}

viết hàm void foo(BTNode* root) nhận vào con trỏ đến gốc cây và in ra các node trên cây theo thứ tự *inorder* mà chỉ được dùng O(1)-không gian. (Do đó, các loại giải pháp dùng recursion hay dùng stack là không được phép.)

### NQH-112

Tiếp theo câu trước, giả sử cây nhị phân cho trước là cây tìm kiếm nhị phân: data bên trái nhỏ hơn gốc và nhỏ hơn data bên phải. Viết hàm BTNode* bar(BTNode* root), sắp xếp lại các con trỏ, để biến cây nhị phân này thành một danh sách liên kết kép và vòng lặp (circular doubly-linked list). Hàm trả về con trỏ vào phần tử đầu của danh sách. Ở đây, ta sẽ hiểu left là con trỏ về phần tử trước (previous) và right trả về phần tử sau (next) trong danh sách liên kết kép.

## Bài [43] — 18/04/2012

### NQH-113

Tính cube root modulo $2^n$: cho $a$ và $n$, tính nhanh $x$ sao cho $a = x^3 (mod\;2^n)$.

> Thiệt ra đây không phải câu hỏi phỏng vấn (có nơi nào phỏng vấn mà hỏi những câu dạng này không nhỉ?) mà là của một anh đồng nghiệp hỏi tôi hôm nay. Tôi thấy nó thú vị và thích hợp với những ai đang theo học lớp crypto của Stanford nên gửi lên đây.

## Bài [44] — 13/10/2012

> (Cập nhật 15/10: Hôm trước gõ thiếu một dòng, đã sửa lại.)

### NQH-114

Hàm tìm kiếm nhị phân sau đây bị vấn đề gì, sửa ra sao?
bool binary_search(const vector<int>& sorted_vec, int key) {
    size_t mid, left = 0, right = sorted_vec.size()-1;
    while (left <= right) {
        mid = left + (right-left)/2;
        if (key > sorted_vec[mid])
            left = mid+1;
        else if (key < sorted_vec[mid])
            right = mid-1;
        else
            return true;
    }
    return false;
}

## Bài [45] — 26/10/2012

### NQH-115

Cho hai dãy số đã sắp xếp theo thứ tự tăng dần. Mỗi dãy dài n. Cho một tham số 1 ≤ k ≤ n, thiết kế thuật toán trả về số nhỏ thứ k trong tập 2n số.
