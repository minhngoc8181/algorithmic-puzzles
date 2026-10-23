# Kho tham khảo NQH: bình luận và lời giải của độc giả — nguyên văn

Đi kèm [nqh-interview-questions-v0.1.md](nqh-interview-questions-v0.1.md). Trích nguyên văn phần bình luận của 45 bài "Các câu hỏi phỏng vấn [1]–[45]" (Blog Khoa Học Máy Tính, procul.org), theo thứ tự thời gian trong từng bài. Giữ nguyên chính tả, kể cả bình luận không dấu và công thức bị cắt cụt do lỗi hiển thị của blog (HTML `<` `>`).

> [!WARNING]
> Bình luận của độc giả **không phải đáp án chính thức**. Nhiều lời giải sai hoặc chưa đầy đủ. Chỉ các câu trả lời của NQH (Ngô Quang Hưng, Administrator, NQH) mới đáng tin ở mức tác giả xác nhận. Cần kiểm chứng độc lập trước khi dùng.


## Bài [1] — 11 bình luận

**Phan Duy Hùng** · 16/11/2008 at 2:26 am

> Hôm nay em được biết đến các câu hỏi phỏng vấn này, suy nghĩ mãi xin nêu ra cách giải tạm chấp nhận được cho bài 1:

> Lưu lại vị trí bắt đầu Linked List, sau đó duyệt list, khi duyệt tới node nào thì đảo chiều liên kết của nó lại: A->B thì B->A

> nếu node của chúng ta là null –> Linked List loại 1

> nếu node của chúng ta trở về vị trí bắt đầu: Linked List loại 2, lúc này ta lại duyệt Linked List 1 lần nữa theo cách duyệt như vậy sẽ cho trở lại Linked List ban đầu

> Mong anh Hưng và các bạn chỉ bảo cách nhanh nhất để thực hiện yêu cầu trên

> 0

> 0

**Ngô Quang Hưng** · 19/11/2008 at 10:26 am

> Chào Hùng,

> Cách giải rất hay! Về asymptotic thì không có cách nào nhanh hơn (đều cần O(n) bước). Nhưng, có cách không cần phải “sửa” bất kỳ link nào trong link list cả.

> 0

> 0

**donnghi** · 11/07/2009 at 11:52 am

> Hi thầy Hưng (do em không biết dùng từ nào phù hợp hơn ^^),

> Bài 1.Ta có thể thấy, nếu rơi vào trường hợp 1 và list đủ dài thì dù ta nhanh tới mấy thì thời gian cũng không thể chấp nhận được (và do đó không biết thuộc TH1 hay TH2), do đó em định cận là thời gian hợp lý phụ thuộc vào tốc độ tính toán, nếu quá thời gian mà không tìm ra NULL thì dừng và quyết định thuộc trường hợp 2, nếu tìm ra NULL thì hiển nhiên là trường hợp 1.

> Bài 2.Bài này em chia làm hai giai đoạn: giai đoạn 1 em đơn thuần đảo toàn bộ xâu, trong ví dụ thì xâu trở thành: « golb ecin a si siht ». Giai đoạn 2 em đọc từng từ vào một biến tạm rồi đảo từng từ đọc được sau đó ghép vào một xâu chung, ví dụ đọc xong từ « golb » em sẽ đảo thành « blog » rồi ghép vào đầu xâu. Làm tiếp tục em sẽ có kết quả.

> Bài 3.Bài này ngoài hai mảng A và B lưu mảng được sắp của đầu bài, em dùng thêm một mảng, mảng C chẳng hạn với ý nghĩa: C[i] lưu chỉ số j sao cho A[i] + B[j] là kết quả nếu ta chọn A[i].

> Khởi tạo: C[i] = 1 với mọi i (A[1] lớn nhất, sau đó là A[2], …)

> Giả sử ta đang xét A[i], ta so sánh tổng A[i] + B[C[i]] với A[i + 1] + B[C[i + 1]] và A[i – 1] + B[C[i – 1]]. Ta có 3 trường hợp xảy ra:

> TH1.Tổng A[i] + B[C[i]] lớn nhất, ta in tổng và tăng C[i + 1].

> TH2.Tổng A[i + 1] + B[C[i + 1]] lớn nhất, ta in tổng và tăng C[i + 1], đồng thời chuyển xuống xét vị trí i + 1.

> TH3.Tổng A[i – 1] + B[C[i – 1]] lớn nhất, ta in tổng và tăng C[i – 1], đồng thời chuyển con trỏ lên vị trí i – 1.

> Ta cần lưu ý giá trị cận như i – 1 vượt mảng, còn giá trị mảng C thì không cần.

> Độ phức tạp: O( 2n ).

> 0

> 0

**pl** · 11/07/2009 at 10:10 pm

> bạn donnghi thử dùm mình cái test này nhá

> A: 10 9 8 7 -100

> B: 100 10 10 10 10

> 0

> 0

**donnghi** · 12/07/2009 at 6:15 am

> Cảm ơn bạn đã tìm ra lỗi của giải thuật, trong TH3 ta chưa in kết quả và bổ sung một vòng lặp kiểm tra điều kiện leo lên trong khi vẫn phát hiện ra giá trị lớn nhất là i – 1.

> Độ phức tạp O( 2n ).

> 0

> 0

**Clairsang** · 31/10/2010 at 2:24 pm

> Mình có cuốn Cracking The Coding Interview 4ed, bản đẹp. Bạn nào thích thì gửi email vào clairsang@gmail.com mình sẽ reply đính kèm.

> 0

> 0

**Phuc Nguyen** · 24/03/2011 at 5:21 am

> Hi thầy Hưng.

> Hôm nay em đọc bài này, thấy câu 1 chưa ai giải nên em comment luôn. Cách giải ko phải do em nghĩ ra, nên ko biết có… vô duyên quá ko

> Trong cuốn Elements of Programming có 1 chương về Transformations với Orbits. Trong đó có thuật toán (tổng quát hơn tí xíu) để xét coi chu kỳ của 1 hàm kết thúc hay lẩn quẩn. Thuật toán sẽ dừng nếu chu kỳ hữu hạn.

> Nôm na là như vầy: Cho 2 biến lần lần theo giá trị trong danh sách. Biến A mỗi lần đi 2 bước, biến B mỗi lần đi 1 bước. Nếu danh sách ko có vòng thì biến A luôn đi nhanh hơn và cuối cùng sẽ đụng NULL trước. Nếu danh sách có vòng, sẽ đến lúc cả 2 biến A và B cùng vào vòng. Vì A đi nhanh hơn 1 bước nên sau mỗi bước lặp, khoảng cách giữa 2 biến sẽ giảm 1, tức là chắc chắn có lúc A=B.

> 2

> 0

**pjthon** · 24/03/2011 at 10:05 am

> @Phuc Nguyen: hi, cách giải bạn nói gọn thật, complexity $O(n)$ (A=B, ý bạn chắc so sánh addresses của hai biến?). Nhưng sao không thấy cần dùng đến “vài chục bytes” bộ nhớ như anh Hưng nói nhỉ.

> Trước đó em mới nghĩ được cách với complexity $O(n \log n)$, n là độ dài thật sự của list. Ngoài ra nếu $n = 2^{100}$ thì cần đến những $100 * 4 = 400$ Bytes bộ nhớ (giải sử address 4 bytes)

> Cách của em như này: list $X$ lưu addresses của các elements có index $2^i$ trong quá trình duyệt list. Nếu gặp NULL thì là list loại 1. Với mỗi element khác NULL của list, check xem address của element này có trong list $X$ chưa. Nếu có rồi thì là list loại 2.

> 0

> 0

**Ngô Quang Hưng** · 24/03/2011 at 11:32 am

> Lời giải Phuc Nguyen ghi là chính xác rồi!

> @Pjthon, tôi viết “vài chục bytes” thật ra ý là tổng bộ nhớ ta cần không phụ thuộc vào n.

> 0

> 0

**zyx** · 15/01/2013 at 10:27 pm

> Câu 3 anh Hưng có gợi ý gì không ạ?

> 0

> 0

**Administrator** · 17/01/2013 at 11:49 pm

> @zyx, tôi không biết cái hint này có giúp nhiều không. Giả sử ta có n điểm trên trục x, và n điểm trên trục y. Mỗi tổng A[i] + B[j] có thể được đại diện bởi một điểm trong không gian 2 chiều. Ta quét đường thẳng với slope bằng -1 từ vô cực về. Điểm đầu tiên ta gặp là (A[n], B[n]). Điểm kế tiếp ta gặp sẽ là (A[n], B[n-1]) hoặc (A[n-1], B[n]), vân vân. Ta cần tìm điểm dừng để cho có tổng cộng n điểm nằm trên đường thẳng này. Đường thẳng này cùng lắm là đến điểm $(A[\sqrt n], B[\sqrt n])$ là phải dừng. Sau đó dùng binary search tìm threshold dừng …

> 1

> 0

## Bài [2] — 3 bình luận

**k40** · 11/12/2006 at 4:45 am

> 5.

> Hỏi người thứ nhất:

> Bạn có phải là Tèo không

> Nếu nhận được câu trả lời là Không thì đây có thể là Tèo hoặc Bụt (không là DV)

> Nếu nhận được câu trả lời là Có thì đây có thể là Tèo hoặc Diêm vương (ko Bụt)

> Trường hợp nhận được câu trả lời là không

> hỏi người thứ hai:

> người vừa trả lời có phải là Diêm vương không?

> KHÔNG suy ra người thứ hai là Bụt hoặc Tèo suy ra người thứ ba là Diêm vương

> hỏi Diêm vương câu cuối người đầu tiên là bụt/Tèo để kết luận

> CÓ suy ra người hai là Diêm vương hoặc Tèo (không là Bụt)

> vậy người cuối người thứ hai có phải là Bụt không để kết luận

> CÓ suy ra thứ tự Bụt Diêm vương Tèo

> Không suy ra Tèo Diêm vương Bụt

> Trường hợp nhận được câu trả lời là có

> hỏi người thứ hai:

> người vừa trả lời có phải là Bụt không?

> KHÔNG suy ra người thứ hai là Bụt hoặc Tèo không là Diêm vương

> hỏi người cuối người đầu tiên có phải là Bụt không

> có suy ra kết quả DV Bụt Tèo

> không suy ra DV Tèo Bụt

> CÓ suy ra người hai là Diêm vương hoặc Tèo (không là Bụt) suy ra Bụt ở cuối

> vậy người Bụt người đầu tiên có phải là DV không để kết luận

> CÓ suy ra thứ tự DV Tèo Bụt

> Không suy ra Tèo DV Bụt

> 0

> 0

**dan** · 09/09/2007 at 9:22 am

> 4. 22:2 cơ số x-1 sẽ cho ra trị là x

> 1

> 1

**pdt** · 01/03/2008 at 6:31 pm

> câu cuối là a+b+ab thì phải

> 0

> 0

## Bài [3] — 15 bình luận

**Anonymous** · 14/07/2005 at 9:49 pm

> Bác Hưng có nhớ nhầm không đấy? Câu số 9 là câu tôi bị hỏi, sau đó đố lại bác :-) 

> Viết bởiMinh Nguyễn

> 0

> 0

**Anonymous** · 18/07/2005 at 8:35 am

> Cau hoi 8 :
> Hien nhien la khong co cach bieu dien truc tiep ngay thang, vi vay cach duy nhat la dua ra 1 cach ma hoa va 1 thuat toan giai ma.
> Sau day la 1 loi giai:
> Tui chep len hop 1 cac so : 0 1 2 3 4 5
> Hop 2 chep cac so : 4 5 6 7 8 9
> Cach giai ma nhu sau :
> Lay con so N o phia tren hinh lap phuong theo thu tu hop 1 roi hop 2.
> Vi du con so tren hop 1 la 1, con so tren hop 2 la 4 thi ta co so N=14.
> Neu N<31 thi dao nguoc vi tri cac chu so cua N, vi du N=14 thi se tro thanh 41.
> Ngay trong thang D se bang N modulo 31.

> Viết bởiHung

> 0

> 0

**Ngô Văn Chấn** · 01/02/2007 at 10:50 pm

> Về câu số 9: Đó là hai điểm cực bắc và cực nam của quả địa cầu.

> Còn câu số 7 thực ra là một bài toán cổ của Trung Quốc( đốt hai que hương.)

> 0

> 0

**Ngô Văn Chấn** · 01/02/2007 at 10:56 pm

> e nhầm chút: ko có cực nam

> 0

> 0

**Ngô Quang Hưng** · 02/02/2007 at 7:17 am

> Câu 9: không chỉ có điểm cực Bắc. Còn **vô số** các điểm khác nữa.

> 0

> 0

**anh123** · 11/02/2007 at 7:19 pm

> câu 9: cực Bắc và đường vĩ tuyến cách cực Nam 1km

> 0

> 0

**anh123** · 11/02/2007 at 8:01 pm

> câu 7: Một sợi dây với 1 điểm cháy sẽ tốn 1h để cháy hết.

> Vậy nếu trên sợi dây lúc nào cũng có 4 điểm cháy thì sẽ

> tốn 15 phút để cháy hết.==> ta có thể đốt hết 1 sợi trong

> 15 phút.

> Cách làm: ta đốt 2 sợi cùng lúc nhưng 1 sợi lúc nào cũng có

> 4 điểm cháy cón 1 sợi chỉ có 1 điểm cháy. Khi sợi 4 điểm

> cháy cháy hết thì ta dập tắt sợi thứ 2. Lúc đó ta có đoạn

> dây còn lại của sợi thứ 2 cháy trong 45 phút.

> 1

> 0

**anh123** · 11/02/2007 at 8:25 pm

> Bổ sung câu 9:

> Ban đầu ta ở vĩ tuyến P. Sau khi ta đi xuống phía Nam 1km,

> ta ở vĩ tuyến Q và ở điểm A. Nếu vĩ tuyến Q có độ dài là

> ước số của 1km thì sau khi ta đi về phía Tây 1km ta vẫn ở A

> Khi đó ta sẽ về điểm xuất phát khi đi về phía Bắc 1km.

> Có vô số vĩ tuyến P như vậy.

> 0

> 0

**andes** · 31/10/2007 at 7:29 pm

> Câu số 8 có thể biểu diễn ngày bằng số hệ 6 cũng được, không biết anh Hưng trả lời MS thế nào?

> 0

> 0

**Ngô Quang Hưng** · 01/11/2007 at 5:34 am

> **andes**: vẫn hệ số 10, nhưng số 6 dùng làm số 9 được và ngược lại.

> 0

> 0

**tunguyen** · 15/05/2011 at 4:32 am

> Câu 7: đốt cháy dây 1 cả 2 đầu, dây 2 một đầu. Khi dây 1 cháy hết thì vừa đúng 30 phút, dây 2 còn 30 phút nữa thì cháy hết, vậy ta đốt tiếp đầu còn lại của dây hai ngay khi dây 1 cháy hết thì tròn 45 phút khi dây 2 cháy hết.

> Anh Hưng cho biết có dc ko nhé, và còn cách nào khác nữa không?

> 1

> 0

**NQH** · 15/05/2011 at 6:15 am

> Tôi không biết cách nào khác.

> 0

> 0

**Thành** · 16/05/2011 at 9:39 pm

> Câu số 8 bố trí như thế này được không anh.

> Mỗi hình lập phương có 6 mặt. Ta bố trí các số như sau:

> Lập phương 1: 1, 2, 3, 4, 5, 6

> Lập phương 2: 1, 2, 7, 8, 9, 0

> 0

> 0

**Nhanh** · 16/05/2011 at 9:41 pm

> @Thành: 07, 08, 09 không được.

> 0

> 0

**abc** · 17/05/2011 at 10:05 am

> câu 8 :

> 1 bên là : 0 1 2 3 4 5

> bên còn lại : 0 1 2 6 7 8

> 0

> 0

## Bài [4] — 9 bình luận

**Anonymous** · 08/07/2005 at 1:55 pm

> Nhân tiện đọc bài về mấy câu phỏng vấn của MS của anh Hưng, em nghe giang hồ đang “chửi” nhau ầm ầm về cách tuyển người của MS. Mấy hôm trước ở CNet có bài Microsoft’s personnel puzzle . Đại để là chỉ trích MS về cách tuyển người kiêu ngạo. Theo bài báo đó thứ tự xếp hạng của MS trong 100 Best Companies to Work for in America tụt từ thứ 8 năm 98 xuống 57 vào năm nay.
> Nhân cái bài báo đó mà bên Slashdot dân tình nêu mấy ý kiến khá là hay trong đó có một bài của 1 anh tự xưng là cựu cán bộ MS
> Anh này phân tích 2 điểm lợi trong cách tuyển người của MS. Thứ nhất là tạo cơ hội công bằng cho tất cả mọi người không phân biệt xuất thân từ trường xịn hay trường thấp. Thứ hai và quan trọng nhất là tìm ra được người thực sự có thể làm được việc và đóng góp cho cty.
> Hai điểm tai hại của cách tuyển dụng này là nó được áp dụng cho toàn bộ cty điều này sẽ không thích hợp cho một số công việc ko cần kiến thức công nghệ sâu. Thứ hai là cách làm này áp dụng cả cho những cán bộ đang làm việc cho MS, tức là nếu chuyển sang nhóm khác thì cũng phải interview như người bình thường.

> Mà để đối phó với các câu hỏi của MS cũng không phải là khó lắm. Có quyển “How Would You Move Mount Fuji?” là cẩm nang ôn tập trước phỏng vấn :-). Với lại gú gồ cũng ra khối câu trả lời.

> Năm ngoái em có được tham gia phỏng vấn của Google với MS. Em thấy Google còn khiếp hơn MS. Em bị quay 2h với 2 người mỗi người 1h. Toàn technical questions, với viết code lên trên bảng luôn. Được cái Google cho bọn được mời đến phỏng vấn 1 bữa ăn thịnh soạn :-)). MS thì phỏng vấn online luôn, dùng cái MS Online Meeting thì phải. Cũng code online luôn cho người ta xem. Nói chung là mấy cái trò phỏng vấn đấy căng thẳng bỏ xừ.

> Em nghĩ là cách làm của MS phù hợp nếu MS muốn tuyển software developer. Cứ lập trình siêu, tư duy tốt, thông minh thì phù hợp với job đó. Chẳng cần phải PhD làm gì cả. Nếu như có PhD thì có khi là xin làm ở MS Research thì phù hợp hơn.

> Viết bởiBạch Hưng Nguyên

> 0

> 0

**Anonymous** · 08/07/2005 at 2:46 pm

> Hồi xưa tôi phỏng vấn MS thì có hai vòng. Vòng 1 bằng điện thoại hoặc có người đến trường làm. Sau khi qua vòng 1 thì vòng 2 phỏng vấn ở Redmon, cả ngày luôn. Không phải chỉ bị “quay” hai giờ mà bị quay cả ngày, hết nhóm này đến nhóm khác. Nhóm nào thích mình thì nhận. Ăn ở thì MS trả tiền. 

> Viết bởiNgô Quang Hưng

> 0

> 0

**Anonymous** · 18/07/2005 at 10:09 am

> Cau 11 :
> Tat ca cac cua deu dong. 

> Viết bởiHung

> 0

> 0

**Anonymous** · 18/07/2005 at 7:52 pm

> Dear bác Hùng,

> Tôi đang ở SG, connection rất chậm nên sẽ reply bác sau (3 tuần nữa).

> Về câu 11, có một số cửa mở đấy. 

> Viết bởiNgô Quang Hưng

> 0

> 0

**Anonymous** · 19/07/2005 at 1:31 pm

> Vang cua so 1 hien nhien la mo, tui da khong tinh den truong hop khi la boi so cua X^k (k chan) (X nguyen to). Nghi nhanh qua nen thay so tap hop con
> luon la 2^n chan nen tra loi bua the. Hen xem loi giai cua bac :) 

> Viết bởiHung

> 0

> 0

**Son** · 06/01/2008 at 12:07 am

> các cửa mở là các số chính phương.

> Do các cửa mở có số thứ tự có số ước số là lẻ.

> Số ước số của 1 số m = X1^a1 * X2^a2 * … * Xn^an (Xi là số nguyên tố) là (a1+1)(a2+1)…(an+1).

> m có số ước số lẻ nên ai là số chẵn.

> 0

> 0

**rung** · 22/01/2008 at 6:28 pm

> Câu 12 để đến 3 năm không có người trả lời cũng kì Thử nhé,

> Cách giải của câu này là dùng… tay. Cụ thể là:

> Vào phòng 2 bật 2 công tắc 2 và 3. Châm 1 điếu thuốc. Hút hết điếu thuốc rồi tắt công tắc 3. Qua phòng 1 sẽ thấy 2 bóng tắt và 1 bóng sáng. Bóng sáng hẳn là của công tắc 2 rồi. Sờ 2 bóng tắt tìm bóng nào còn nóng. Bóng này là của công tắc 2, bóng còn lại là của công tắc 1.

> Sẽ cố tìm câu trả lời cho câu hỏi 10.

> 0

> 0

**rung** · 22/01/2008 at 7:09 pm

> Sửa câu trên một chút: bóng tắt mà còn nóng là của công tắc 3.

> Trả lời cho câu hỏi 10:

> Nhát cắt đi qua tâm của 2 hình chữ nhật.

> Có điều tôi thắc mắc là đây có phải là cách duy nhất không.

> 0

> 0

**donnghi** · 13/07/2009 at 12:37 am

> Nhát cắt đi qua tâm là duy nhất: Giả sử tồn tại một nhát cắt chia đôi hình chữ nhật nhưng không đi qua tâm, khi đó từ tâm của hcn ta kẻ đường thẳng cùng phương với đường thẳng ban đầu, đường thẳng thứ hai cũng chia hình chữ nhật ra hai nửa bằng nhau, dẫn tới mâu thuẫn.

> 0

> 0

## Bài [5] — 2 bình luận

**Hanh** · 15/03/2010 at 1:34 pm

> 13. Tèo nghe thấy trước, vì càng lên cao không khí càng loãng => khả năng truyền âm giảm ( biên độ và tần số ), nhưng chắc là không thể nhận biết được…

> 15. a cắt làm 3 phần( mà theo a là đã bằng nhau) cho b và c nhận trước, phần còn lại của a => a đã xong. Nếu b, c cùng chọn chung một phần thì cho b chia mỗi phần trong hai phần đó làm 2 phần( mà theo b là đã bằng nhau) rồi cho c chọn => b, c cũng cảm thấy không bị thiệt, tức là đã có công bằng.

> 0

> 0

**Tuan** · 15/05/2011 at 4:50 am

> Cau 14 kho qua, ko biet bac co nho nham ko :D. Gia su co 5 dong gia, 5 dong that, lam sao de can 3 lan tim ra dc 5 dong gia day?

> 0

> 0

## Bài [6] — 7 bình luận

**Anonymous** · 13/07/2005 at 6:35 am

> Câu 17 : Đơn giản thôi, vì Tèo yêu Tấm hơn yêu Cám 

> Viết bởiTrần Anh Hùng

> 0

> 0

**Anonymous** · 13/07/2005 at 6:10 pm

> *Câu 17 : Đơn giản thôi, vì Tèo yêu Tấm hơn yêu Cám * 

> Câu trả lời hợp tình, nhưng tôi e rằng không hợp lý. 

> Viết bởiNgô Quang Hưng

> 0

> 0

**Anonymous** · 14/07/2005 at 6:06 am

> Câu 18: ruồi có vận tốc không đổi là 5000km/h đi trong khoảng t/g là T.

> Ruồi bẹp dí khi hai xe chạm nhau, tức là 50T+30T=100 ==> T=1,25 ===> ruồi bay: 5000×1,25=6250km  

> Viết bởiThế Anh

> 0

> 0

**Anonymous** · 17/07/2005 at 10:14 am

> Cau 17 :
> Nha Cam ——- Nha Teo —-Nha Tam.
> khoang cach giua 2 bus bang gap doi khoang cach giua nha Teo va nha Tam. (Gia su gan nha Teo co 2 ben bus doi dien va khi ca 2 bus cung den 2 ben cung luc thi Teo chon bus den nha Tam truoc) 

> Viết bởiHung

> 0

> 0

**lebinh** · 09/07/2006 at 11:35 pm

> Câu 17:

> Các xe buýt theo hướng nhà Cám đến lúc: 6h, 7h, 8h, 9h, …

> các xe buýt theo hướng nhà Tấm đến lúc: 6h45′, 7h45′, 8h45′, 9h45′, …

> Tèo ra bến xe buýt trong khoảng 6h-6h45 thì gặp xe buýt theo hướng nhà Tấm, trong khoảng 6h45-7h thì theo hướng nhà Cám –> Tèo đi thăm Tấm gấp 3 lần thăm Cám.

> 0

> 0

**River** · 14/09/2008 at 11:23 pm

> 16. Nên đổi cứa. Tỉ lệ thắng khi đó sẽ là 2/3

> 0

> 0

**Tuan** · 15/05/2011 at 4:53 am

> 16. Nen doi cua, ti le thang tang tu 1/3-> 1/2.

> 0

> 0

## Bài [7] — 6 bình luận

**Anonymous** · 03/11/2005 at 9:23 am

> Hôm nay tôi thấy một bài này dành cho học sinh tiểu học, tương tự như bài số 21.

> Bài 1/99 – Trò chơi cùng nhau qua cầu

> (dành cho học sinh khối Tiểu học)

> Bốn người cần đi qua một chiếc cầu. Do cầu yếu nên mỗi lần đi không quá hai người, và vì trời tối nên phải cầm đèn mới đi được. Bốn người đi nhanh chậm khác nhau, qua cầu với thời gian tương ứng là 10 phút, 5 phút, 2 phút và 1 phút. Vì chỉ có một chiếc đèn nên mỗi lần qua cầu phải có người mang đèn trở về cho những người kế tiếp. Khi hai người đi cùng nhau thì qua cầu với thời gian của người đi chậm hơn. Ví dụ sau đây là một cách đi:

> + Người 10 phút đi với người 5 phút qua cầu, mất 10 phút.

> + Người 5 phút cầm đèn quay về, mất 5 phút.

> + Người 5 phút đi với người 2 phút qua cầu, mất 5 phút.

> + Người 2 phút cầm đèn quay về, mất 2 phút.

> + Người 2 phút đi với người 1 phút qua cầu, mất 2 phút. 

> Người viết: freshJunior

> 0

> 0

**Anonymous** · 03/11/2005 at 12:13 pm

> 24 phút nhiều quá, chỉ cần 17 

> Người viết: NQH

> 0

> 0

**Anonymous** · 04/11/2005 at 8:13 am

> Học hơn chục năm sau để giảm đi bảy phút kể ra cũng đáng, anh Hưng nhỉ? Đùa vậy thôi. Tôi rất thích đọc blog của anh, nên tính viết một hai câu chọc, gọi là làm quen, và nhân tiện cảm ơn anh về những bài viết rất có giá trị.

> Chúc anh mạnh khoẻ, và luôn có những bài viết hay. 

> Người viết: fresh_Junior

> 0

> 0

**MIVN** · 16/01/2006 at 6:20 am

> Bài 19 :

> 1$không đi đâu cả .Bởi vì ba người bỏ ra 9*3=27;

> Bồi lấy 2 ==>Tổng số còn lại là 25=Tiền phòng

> Còn dữ kiện 27+2 không liên quan đến 30

> Bai20:

> (i)Nếu biết hơn nủa số nguời nói thật (k>=1) thì chỉ hỏi một trong số người nói thật về những người còn lại .Số câu hỏi cần thiết n-k Số câu hỏi sẽ giảm xuống

> cau 21:

> thời gian la 17 .

> Xin các bác cho ý kiến

> 0

> 0

**khue** · 27/03/2008 at 7:42 pm

> Xin nhờ các cao thủ giải giùm bài 21 trong trường hợp tổng quát với ạ:

> Bài toán

> Trong đêm tối, một nhóm gồm N người lữ hành muốn vượt qua sông một cách nhanh nhất nhờ một cái cầu nhỏ bắc ngang sông. Do cái cầu quá hẹp và cũ kỹ nên đồng thời chỉ có thể cho phép hai người đi trên cầu. Mặt khác để đảm bảo an toàn khi vượt qua cầu cần phải dùng đèn phi để chiếu sáng đường đi, mà đoàn lữ hành này chỉ có 1 cái đèn pin.

> Mỗi lữ hành cần thời gian ti để đi qua cầu, i = 1, 2, .., N (ti là số nguyên dương không quá 100). Nếu hai người lữ hành cùng vượt qua sông, thì thời gian qua cầu sẽ là thời gian của người đi chậm hơn.

> Yêu cầu: Hãy xác định thời gian vượt sông nhanh nhất.

> Xin đa tạ, đa tạ!!!

> 0

> 0

**donnghi** · 12/07/2009 at 10:49 pm

> Bài 21:

> Lần 1: An và Bình cầm tay nhau qua cầu, mất 2 phút.

> Bình quay lại mất 2 phút. Tổng là 4 phút.

> Lần 2: Chung và Dung dắt nhau qua cầu, mất 10 phút.

> An quay lại mất 1 phút. Tổng là 15 phút.

> Lần 3: An và Bình lại dắt nhau qua cầu, mất 2 phút.

> Tổng là 17 phút.

> Bài toán tổng quát:

> Cách giải tối ưu là quy hoạch động (dynamic programming, và do đó ta viết được công thức), còn cách giải tự nhiên là tham lam (greedy).

> 0

> 0

## Bài [8] — 6 bình luận

**MIVN** · 16/01/2006 at 4:50 am

> Câu22:

> Bốc ở hộp kẹo tổng hợp .Nếu là kẹo dừa==>hộp kẹo dừa

> ==> Hộp có nhãn tổng hợp là socola==>…..

> cau 23 :

> 101-102=1;

> Thay vị trí của dấu trừ và dấu bằng

> 101=102-1;

> câu 24:gọi thể tích la V

> Múc 1/10 ly cà fê đổ vào ly sữa.THể tích của ly sữa lúc này la V +1/10*V=11/10*V

> sau đó múc 1/10 ly sữa cà fê đổ vào ly cà fê

> The tich của ly sữa còn lại là 11/10*V-1/10*11/10*V=0.99*V

> Do cà fê và sữa hòa tan tuyệt đối nên số thể tích múc ra tỉ lệ thuận với thể tích của mỗi chất trong dung dich .Nên thể tích của cà phê còn lại (trong cốc sữa )la:

> 1/10*V-1/10*1/10*V=0.09V

> THể tích của sữa là 0.99V-0.09V=0.9V

> ==>% ?

> Tính thể tích của sữa và cà phê bên cốc cà phê tương tự

> Xin mọi người cho ý kiến

> 0

> 0

**Ngô Quang Hưng** · 16/01/2006 at 4:56 am

> **Câu 23**: dấu = là một ký hiệu riêng rẽ, cho nên ta không thể dịch chuyển một vạch của nó. (Lời giải của bạn dĩ nhiên là chính xác nếu cho phép di chuyển 1 vạch của dấu =.)

> 0

> 0

**dryland** · 08/03/2006 at 10:30 am

> Câu 23: Hihi, dịch số 2 lên trên 1 tí thành 101 – 10^2 = 1

> 0

> 0

**T** · 15/11/2007 at 12:25 am

> Cách này không đúng vì hiểu phép tính thành dấu nhưng cũng vui:

> 100 = +100 : đúng

> -100 + 102 = 1 : đúng

> => -100 102 = 1 ?

> 0

> 0

**newbie** · 18/10/2012 at 10:10 am

> em xin phép xử câu 24

> khá đơn giản : vì 2 ly sữa và cafe cùng thể tích, và sau khi đổ qua múc về thì thể tích 2 ly vẫn bằng nhau nên lượng cafe trong sữa và lượng sữa trong cafe bằng nhau.

> để cho dễ hình dung : giả sử sau khi đổ qua và múc về, ly sữa có x% cafe => ly sữa có (100-x)% sữa. cũng từ đó, vì sữa không tự biến mất nên suy ra lượng sữa bên ly cafe là x% ( để đảm bảo tổng lượng sữa trong cả 2 ly là 100% so với ban đầu ), và lượng cafe trong ly cafe là (100-x)%. kết luận là hàm lượng sữa trong cafe bằng hàm lượng cafe bên sữa.

> * nếu ta tính toán dựa vào nồng độ thì có thể sẽ không chính xác vì chưa chắc 2 thứ cafe và sữa hòa tan hoàn toàn vào nhau, có thề múc chỗ này thì nồng độ cao, chỗ kia thì nồng độ thấp.

> * hình như đây là 1 bài toán dân gian của Nga thì phải, hồi nhỏ em đã được đố câu này rồi, lúc đó là nước và rượu vang thay vì sữa và cafe như ở đây.

> lần đầu tiên post bài, mong các thầy và các tiền bối góp ý.

> 0

> 0

**newbie** · 18/10/2012 at 10:14 am

> hic, lúc nãy đọc đề hơi vội. sót mất chi tiết sữa và cafe hòa tan hoàn toàn lẫn nhau, nên cái dấu * thứ nhất của em bị thừa.

> nhưng có hòa tan hay không hòa tan, tan ít hay tan nhiều thì cũng như nhau cả thôi.

> 0

> 0

## Bài [9] — 1 bình luận

**thienminh** · 15/05/2011 at 5:43 am

> 25. Tao chuoi B[i]=A[1]+\dots+A[i] voi i=1,…,n. Sau do tim 2 phan tu B[i] va B[j] (i<j) sao cho B[j]-B[i] lon nhat, chu y hoac B[j]=max{B}, hoac B[i]=min{B}, hoac ca 2 deu dung (?).

> 0

> 0

## Bài [10] — 0 bình luận

## Bài [11] — 8 bình luận

**tuyenbk83** · 29/05/2006 at 7:33 pm

> 31. So chu so 0 o cuoi n! la [n/5]+[n/25]+[n/125]+[n/625]+….

> 32. Tai vi khi minh dung thi khai niem ben phai va ben trai phu thuoc huong minh nhin ve phi nao. Khi ta xoay nguoi nguoc lai thi huong phai va trai thay doi. trong khi huong len xuong khong thay doi khi minh dung o bat cu dau.

> 0

> 0

**lihavim** · 29/05/2006 at 7:42 pm

> 33. Đánh số các túi từ 1->9. Túi thứ i lấy i đồng.

> Như thế nếu đem cân, tất cả sẽ nặng 45×100=4500 grams.

> Nhưng nó sẽ bị thiếu mất L grams. Dựa vào L để biết đc túi thứ mấy thiếu.

> 0

> 0

**dang_ky** · 29/05/2006 at 10:23 pm

> 32. Trả lời của bạn tuyenbk83 chưa thỏa đáng

> 0

> 0

**T** · 16/11/2007 at 2:04 am

> 33. Nhưng lỡ 8 túi còn lại loại trừ túi đựng toàn tiền giả có tiền giả thì sao? Bài toán đâu có nói rõ chuyện này.

> 0

> 0

**T** · 17/04/2008 at 8:52 am

> ban: ‘lihavim’ ban co the giai thich ro hon duoc ko?

> 0

> 0

**minhbui85** · 29/09/2008 at 10:41 pm

> Nếu chỉ lấy mỗi túi 1 đồng tiền thì không xác định được.Do đó như lời bạn lihavim cũng đánh số các túi từ 1 đến 9, túi thứ i lấy i đồng. Đem tất cả lên cân sẽ được kết quả L(gram).Bạn giả sử túi thứ 1 là giả, như thế cứ lần lượt túi thứ 2….túi n.Chỉ bằng các phép tính đơn giản cho đến khi tìm được kết quả bằng L(gram) thì sẽ tìm ra túi giả.

> 0

> 0

**Nguyễn Huy Tân** · 17/06/2009 at 9:58 am

> + Câu 33 : câu hỏi chưa rõ ràng , các túi có ít nhất 100 đồng tiền , lỡ có nhiều hơn thì chịu . Còn cách làm của các bạn là đúng rồi , nếu các túi đều có số đồng tiền bằng nhau .

> 0

> 0

**donnghi** · 13/07/2009 at 1:27 am

> Câu 32: phụ thuộc vào hệ quy chiếu.

> 0

> 0

## Bài [12] — 0 bình luận

## Bài [13] — 9 bình luận

**resvictory** · 01/06/2006 at 6:57 am

> 37. Đi từ đầu danh sách, lưu lại phần tử đầu tiên làm kết quả tạm thời. Đi đến phần tử thứ 2 và chọn phần tử này làm kết quả với xác suất 1/2… Tại phần tử thứ i chọn phần tử này với xác suất làm kết quả với xác suất 1/i.

> Giả sử danh sách có n phần tử, xác suất để phần tử thứ i được chọn sẽ là 1/i * i/(i+1) * … * (n-1)/n = 1/n

> 38. Với mỗi i ( 1

> 0

> 0

**Ngô Quang Hưng** · 01/06/2006 at 7:05 am

> Các bạn đọc lại cái này khi post lời bình. Có vẻ post của bạn resvictory bị cắt.

> 0

> 0

**resvictory** · 01/06/2006 at 7:10 am

> Em xin được post lại phần bị cắt:

> 38. Với mỗi i ( 1<= i <= n = length(A) ) gọi f(i) là giá trị nhỏ nhất thoả mãn đoạn A[i..f(i)] chứa S (trường hợp A[i..n] không chứa S ta coi f(i) = infinity). Ta thấy f(1) <= f(2) <= … f(n). Để giải bài toán trong thời gian tuyến tính ta quét A từ trái qua phải:

> (1)best = infinity;

> (2)for i = 1 to n do

> (3){

> (4) f(i) = f(i-1);

> (5) while ( A[ i..f(i) ] chưa chứa S) f(i)++;

> (6) best = min( best, f(i) – i + 1);

> (7)}

> Việc kiểm tra tại (5) được thực hiện bằng một mảng đánh dấu để đảm bảo độ phức tạp O(n).

> 39. Thực hiện tìm kiếm trong 2-D sorted array có thể được thực hiện trong thời gian O(m + n).

> Gọi ma trận cần tìm là a(i, j). Thực hiện tìm kiếm từ dưới lên trên (i giảm dần) và từ trái qua phải j tăng dần.

> bool search(k) {

> j = 1;

> for i=m to 1 do {

> while (a[i,j] < k) j++;

> if ( a[i, j] = k)

> return true;

> }

> return false

> }

> 0

> 0

**Ngô Quang Hưng** · 01/06/2006 at 7:20 am

> Hình như vẫn còn khoảng trống. Để tôi sửa lại xem sao. Đúng rồi, khi dùng **& #60;** thay cho **<** đừng để khoảng trống giữa & và #60;

> 0

> 0

**Mg9H** · 06/06/2006 at 8:28 pm

> Câu số 39 độ phức tạp là O (logm + logn) thui. Làm tương tự như binary search trên mảng 1 chiều:

> bool search (value, r1, c1, r2, c2) {

> if (r1 > r2 || c1 > c2) return false;

> r_mid = (r1 + r2 + 1) / 2;

> c_mid = (c1 + c2 + 1) / 2;

> if (A [r_mid][c_mid] == value) return true;

> if (A [r_mid][c_mid]

> 0

> 0

**Mg9H** · 06/06/2006 at 8:30 pm

> Câu số 39 độ phức tạp là O (logm + logn) thui. Làm tương tự như binary search trên mảng 1 chiều:

> bool search (value, r1, c1, r2, c2) {

> if (r1 > r2 || c1 > c2) return false;

> r_mid = (r1 + r2 + 1) / 2;

> c_mid = (c1 + c2 + 1) / 2;

> if (A [r_mid][c_mid] == value) return true;

> if (value > A [r_mid][c_mid])

> return

> search (value, r_mid + 1, c1, r2, c_mid) ||

> search (value, r1, c_mid + 1, r_mid, c2) ||

> search (value, r_mid + 1, c_mid + 1, r2, c2);

> else

> return

> search (value, r_mid, c1, r2, c_mid – 1) ||

> search (value, r1, c_mid, r_mid – 1, c2) ||

> search (value, r1, c1, r_mid, c_mid);

> }

> (ủa, cái này ko có preview ạ ?)

> hic, hi vọng lần này ko bị lỗi nữa :-w

> 0

> 0

**Administrator** · 06/06/2006 at 8:55 pm

> 1. Good idea, to^i se~ ti`m mo^.t comment preview plugin. DDi.nh update le^n WordPress 2.0.3 ma` chu+a co’ tho+`i gian

> 2. Thay vi` , ba.n du`ng <code> … </code>

> 0

> 0

**rec** · 21/10/2012 at 11:53 pm

> @Mg9H: Tại sao là O (logm + logn) trong khi giải thuật của bạn suy ra T(n, m) = 3T[(n,m)/4] + c(n, m)?

> 0

> 0

**rec** · 23/10/2012 at 4:50 am

> @Resvictory: Biến j của bạn phải tái tạo bằng 1 với mỗi lần lặp của i (nghĩa là j=1 trong thân của for) khi đó chi phí sẽ là O(n*m), tức là đa thức bậc 2.

> 0

> 0

## Bài [14] — 4 bình luận

**twoask** · 16/06/2006 at 3:16 pm

> Anh Hưng, em nghĩ câu số 41 thì chính là thuật toán Breadth-First Search, cũng chính là cách mà Distance Vector routing protocol áp dụng. Thuật toán (chưa optimized) này dừng trong O(diameter) rounds và số lượng message là O(diameter * E) với E là tổng số cạnh. Ở đây nếu giả sử tất cả liên thông thì E = n * (n – 1) / 2.

> 0

> 0

**lihavim** · 16/06/2006 at 4:24 pm

> 41. Em chưa có nhiều kiến thức về mấy cái thuật toán nên mấy cái twoask nói em ko hiểu, chỉ biết đó là đồ thị thôi :D. Không biết E=n*(n-1)/2 có phải là số lượng cuộc gọi ít nhất của cái anh nói ko? Em có nghĩ cách nói chuyện nói theo kiểu vòng tròn, như thế số lượng cuộc gọi là 2n-3.

> 0

> 0

**Ngô Quang Hưng** · 16/06/2006 at 5:28 pm

> Bài này hao hao như distance vector routing, nhưng không phải. Nó gọi là bài toán gossip (gossip problem), đã được giải độc lập bởi nhiều người (ít nhất 5 bài báo khác nhau) từ hồi thập niên 70. Câu trả lời là f(1)=0, f(2)=1, f(3)=3, và f(n)=2n-4 với n>=4. Tìm cách đạt được 2n-4 không khó, chứng minh 2n-4 là cách tốt nhất thì khó hơn một chút, nhưng cũng không phải quá đáng, có thể dùng làm bài tập lớp graph theory.

> 0

> 0

**lihavim** · 18/06/2006 at 10:22 pm

> 42. Đó là số 6210001000.

> 0

> 0

## Bài [15] — 12 bình luận

**lihavim** · 17/06/2006 at 3:47 pm

> 43. Ko biết câu này có đố mẹo ko nhỉ

> Có thể gặp được nếu con kiến bò trước khi chiếc xe chuyển động, đề bài ko cho bắt đầu chuyển động cũng lúc :D.

> 44. Nếu vận tốc của mỗi con đều bằng nhau thì không bao giờ nó gặp. Còn nếu vận tốc mỗi con khác nhau thì nó gặp lúc nào là … tùy hứng của nó :D.

> 45. Chưa học đến e, mới biết mỗi \pi nên ko biết :).

> 0

> 0

**jalfal** · 17/06/2006 at 8:35 pm

> 44. Moi con di duoc *bao xa* —> canh hinh vuong

> 0

> 0

**jalfal** · 17/06/2006 at 9:24 pm

> sorry nha, cau tra loi truoc cua jalfal sai roi. Luc do ko biet nghi sao ma jalfal lai tra loi cau 44 ngo ngan nhu vay

> Cau 45: Khong biet cai nay jalfal co chung minh Ok khong:

> http://img19.imageshack.us/my.php?image=eandpi3nr.png

> Cau 43: Ko gap duoc xe vi cai nay:

> http://img19.imageshack.us/my.php?image=kienvaxe7er.png

> Con cau 44 jalfal van dang…si nghi :p

> 0

> 0

**Ngô Quang Hưng** · 18/06/2006 at 7:25 am

> Câu 44: vận tốc kiến bằng nhau. Gợi ý: vì luôn hướng về một con kiến đang bò, quĩ đạo sẽ cong chứ không thẳng.

> 0

> 0

**Mg9H** · 18/06/2006 at 7:03 pm

> Cau 45 jalfal lam sai ngay tu dau roi, PI = e^(log_e_PI) chu dau fai PI = e^(log_PI_e) dau

> 0

> 0

**Mg9H** · 18/06/2006 at 7:30 pm

> 45. Co 1 cach hoi lang nhang la xet ham f(x) = x ^ (C/x) voi C la constant = Pi * e.

> Lay dao ham` ra se co’ f’ = (1 – ln x) * x^something, luc day’ thay dc ham` f’ doi tu` duong sang am khi x chay qua gia tri e => f nghich bien voi x >= e, vay e^PI > PI^e

> 0

> 0

**twoask** · 21/06/2006 at 1:27 pm

> anh Hưng, em thử nhé

> Câu 43: vì đề cho giả sử sợi dây có độ giãn đồng nhất, cho nên 1 điểm nào đó trên sợi dây nếu cách chiếc xe khoảng cách x m sau giờ đầu tiên thì sẽ cách chiếc xe 2x sau giờ thứ 2 (giả sử điểm đó không chuyển động). Vì con kiến di chuyển với tốc độ 1m/giờ nên tại thời điểm ta đặt con kiến vào sợi dây, nếu nó cách chiếc xe dưới 1m thì nó sẽ bắt kịp chiếc xe, ngược lại thì khoảnh cách càng ngày càng xa. Không biết như thế có đúng ko ạ?

> Câu 44: vì tính chất đối xứng của 4 con kiến, nên tại thời điểm con kiến 4 chạm con 3 thì con cũng chạm con 2… cho nên điểm chạm nhau của 4 con kiến phải là tâm của hình vuông. Ngoài ra khi 1 con kiến di chuyển thì con đuổi theo nó cũng điều chỉnh hướng, vì thế mỗi con kiến sẽ di chuyển theo hình vòng cung cho đến khi di chuyển đến tâm. Đường cung này sẽ có chu vì bằng 1/4 đường tròn với bán kính a/2 với a là đơn vị của hình vuông. Khoảng cách này bằng 1/4 * 2 * PI * a / 2 = 1/4 * PI * a.

> Câu 45: Mg9H đã giải, mặc dù cách này chưa đơn giản lắm, mà em thì cũng chưa nghĩ ra cách nào hay hơn

> 0

> 0

**lihavim** · 21/06/2006 at 3:36 pm

> Hơ, bài 44 là 1 hình vòng cung sao? Thế mà em ngồi mường tượng ra, thì nó đi ko có đúng theo cung tròn, nếu vẽ đường đi của 4 con kiến ta được một cái xoáy

> 0

> 0

**Ngô Quang Hưng** · 21/06/2006 at 5:54 pm

> Đúng rồi, đường đi của mỗi con kiến là hình logarithmic spiral, không phải cung tròn. Gợi ý:

> khoảng cách mỗi con kiến đi bằng đúng chiều dài cạnh hình vuông.

> phương trình polar cho một logarithmic spiral có dạng

> 1
> r = a e^{b\theta}

> với các hằng số

> 1
> a, b

> nào đó

> Ta phải chứng minh rằng quĩ đạo kiến có dạng này, sau đó giải phương trình để tính chiều dài quĩ đạo kiến. Đó là nếu các bạn muốn thật sự chặt chẽ. Cũng có cách lý luận ra chiều dài mà không cần giải phương trình!

> Gợi ý câu 43: con kiến sẽ đụng chiếc xe!

> 0

> 0

**shinichi_kudo_vn** · 21/06/2006 at 10:40 pm

> cau 44: Xet he toa do gan voi 1 con kien. Trong he toa do nay thi con kien o huong nguoc chieu kim dong ho va gan voi con kien nay nhat se chuyen dong thang. Vi cac con kien chuyen dong deu va do tinh doi xung nen cac con kien phai gap nhau cung 1 luc va di cung 1 quang duong. Ma con kien chuyen dong thang se fai di mat 1 quang duong = ca.nh hi`nh vuong de gap con kien dung yen trong he toa do gan voi no’.

> cau 45: xet ham log(x)/x, la ham giam voi x>=e, nen log(e)/e > log(pi)/pi => pi log(e) > e log(pi) => e^pi > pi^e

> 0

> 0

**Trần Quang Khải** · 03/07/2006 at 8:45 pm

> Em trả lời câu 43 như này anh xem được không nhé

> Giả sử tại thời điểm t tạo độ của chiếc xe và con kiến lần lượt là x và y

> ta có x = 100t (xe chuyển động đều).

> Xét trong khoảng detla t, do dây giãn đều nên

> delta y = (y / x)* delta x + 1* delta t

> -> delta y / delta t = (y / x) * (delta x / delta t) + 1

> cho delta t -> 0 ta có hệ pt vi phân sau

> x = 100t

> y’ = (y/x)* x’ +1

> => y’ – y/x = 1

> giải phương trình này ta có y = t* ln(t)

> khi x > e ^100 thì t ln(t) > 100t tức là y > x con kiến sẽ đuổi kịp chiếc xe.

> 0

> 0

**Trần Quang Khải** · 03/07/2006 at 8:51 pm

> Em gõ nhầm t > e^100.

> e^100 cỡ 10^32. Con kiến mấy cỡ hàng trăm tỉ tỉ tỉ giờ mới đuổi kịp cái xe!

> Trên thực tế có thể trả lời là không ngoại trừ con kiến đó là con kiến máy

> 0

> 0

## Bài [16] — 14 bình luận

**twoask** · 21/06/2006 at 10:02 pm

> Anh Hưng mô tả kỹ hơn câu số 48 được không ạ? Nghĩa là chìa khóa của An có mở được khóa của Bình (và ngược lại) không? Cái hộp có đủ để bỏ 1 số chìa hoặc khóa vào đó ko?

> Em nghĩ bài này không khó. Chỉ việc áp dụng một security protocol đơn giản. Nhưng em muốn hiểu rõ bài toán để xem nên áp dụng symmetric hay asymetric protocol :-).

> 0

> 0

**Ngô Quang Hưng** · 22/06/2006 at 7:02 am

> Không, mỗi khóa chỉ có một chìa.

> 0

> 0

**Mg9H** · 22/06/2006 at 10:35 am

> Em ko hiểu như thế nào thì gọi là bảo đảm? Làm thế này có đc ko ạ

> +) An gửi cái hộp kèm theo 1 cái khóa (ko kèm chìa) cho Bình

> +) Bình nhận đc, bỏ 1 cái khóa (ko kèm chìa) vào trong hộp và dùng khóa của An để khóa hộp lại, sau đó gửi lại cho An.

> +) An mở khóa (vì cái khóa dùng để khóa hộp là khóa của An) rồi cho nhẫn vào hộp, dùng khóa của Bình gửi để khóa hộp, gửi sang cho Bình.

> +) Bình lôi chìa khóa của mình ra rung đùi mở hộp lấy nhẫn ra đeo

> 0

> 0

**jalfal** · 22/06/2006 at 1:18 pm

> Cai’ nay` co’ phai ung dung mot “public key encryption scheme” khong anh Hung? Em thay Mg9H tra loi cung duoc, nhung neu co mot nguoi nua o giua An va Binh thi cach cua Mg9H coi nhu thua ?

> 0

> 0

**Ngô Quang Hưng** · 22/06/2006 at 2:06 pm

> Ừ, cách của Mg9H cũng được. Nếu làm thế thì có lẽ đơn giản nhất là cho Bình gửi khóa (của Bình) cho An. An dùng khóa đó khóa hộp nhẫn gửi cho Bình. Nghĩa là An không cần khóa hay chìa, đúng kiểu PKE như Jalfal nói.

> Lúc đầu tôi định đố theo hướng khác, nhưng câu này có lẽ chỉ đến vậy mà thôi.

> 0

> 0

**lihavim** · 23/06/2006 at 2:35 am

> 47. Tuyết rơi ~46ph trước nửa đêm.

> Gọi a0 là chiều dày mà tuyết rơi thêm đc trong 1h

> a là chiều dày tuyết lúc nửa đêm

> => Thời gian tính từ khi tuyết bắt đầu rơi đến nửa đêm: a/a0

> Chiều cao của tuyết:

> Lúc nửa đêm: a =>vận tốc xe v1

> 1h: a+a0 => v2

> 2h: a+2*a0 => v3

> Vi vận tốc xe tỷ lệ nghịch với chiều dày tuyết nên ta có:

> a*v1=(a+v0)*v2=(a+2*a0)*v3

> Từ đó suy ra:

> a/a0= v2/(v1-v2) (1)

> a/a0= (2*v3)/(v1-v3) (2)

> Mặt khác, ta có: v1+v2=2*(v2+v3) => v1=v2+2*v3 (3)

> Thay (3) vào (1), (2):

> a/a0= v2/(2*v3) (1′)

> a/a0= (2*v3)/(v2+v3) (2′)

> như vậy ta chỉ cần tìm tỷ số v2 và v3 sẽ đc a/a0

> Từ (1′) và (2′) ta đưa đc về phương trình đẳng cấp bậc 2 của v2 và v3.

> Đặt v3=k*v2

> Giải tính đc: k=(1+sqrt(17))/8

> =>a/a0 = 4/(1+sqrt(17)) ~ 46 phút.

> Hix, viết dài dòng thật, ko biết có làm nhầm chỗ nào ko

> 0

> 0

**twoask** · 23/06/2006 at 2:47 pm

> Anh Hưng, em nghĩ giải pháp cho câu 48 chưa thuyết phục lắm. Vấn đề ở đây là ta đang giả sử có 1 người trung gian đang muốn lấy chiếc nhẫn, nhưng bắt buộc phải gửi cái hộp đi. Ta tạm gọi người này là MIT (Man-in-the-middle). Như thế, nếu Bình gửi cho An chiếc hộp có khóa trong đó (và chiếc hộp này không khóa), thì MIT hòan tòan có thể (1) tự đánh cho mình chiếc chìa của khóa này hoặc (2) thay bằng khóa của chính anh ta. Nếu dùng cách (1) thì khi anh ta nhận được chiếc hộp từ An, anh ta dùng chiếc chìa để mở khóa, lấy chiếc nhẫn ra rồi khóa lại như cũ. Nếu dùng cách (2) thì anh ta mở khóa ra, lấy chiếc nhẫn, rồi khóa lại bằng khóa của Bình. Em nghĩ câu hỏi này dùng PKI nhưng áp dụng vào câu hỏi vui vui này thì không ổn lắm.

> 0

> 0

**jalfal** · 23/06/2006 at 7:37 pm

> PKE thi phai rat quan tam den man-in-the-middle, tuy nhien jalfal thay doi voi cau hoi nay, cach nay cua Mg9H la tot nhat roi. Khong biet co con cach nao de cai thien huong cua Mg9H hay khong.

> 0

> 0

**twoask** · 23/06/2006 at 8:14 pm

> Cách của Mg9H vẫn bị man-in-the-middle attack, bởi vậy tôi mới nói.

> 0

> 0

**Ngô Quang Hưng** · 24/06/2006 at 6:03 am

> Twoask nói đúng. Có thể chữa lại lời giải như sau: An gửi cho Bình cái hộp đựng nhẫn và khóa nó với khóa K1. Bình nhận được hộp, khóa thêm khóa K2 vào và gửi ngược lại cho An. An mở khóa K1 gửi lại cho Bình. Bình dùng chìa của K2 mở hộp.

> 0

> 0

**Mg9H** · 24/06/2006 at 12:10 pm

> Cách giải hay quá Mặc dù vậy cũng ko chống đc kiểu man-in-the-middle kia (ko hiểu sao lại viết tắt là MIT ạ?). Người ở giữa – C – (MIT) nhận đc hộp lần đầu, giữ lại, gửi 1 cái hộp khác khóa bằng khóa của anh ta cho Bình, kệ cho bình xử thế nào thì xử, còn bản thân C khóa hộp bằng khóa K3 của chính hắn, send lại cho A, A mở khóa K1, gửi lại cho Bình, qua tay C, C dùng chìa của anh ta mở khóa K3 và lấy nhẫn.

> Theo ý kiến của em nếu giữa A và B ko có 1 sự thỏa thuận trước, thì kiểu gì C cũng có cách lấy đồ thôi

> 0

> 0

**Ngô Quang Hưng** · 24/06/2006 at 1:58 pm

> :-), nói túm lại câu đố của tôi chưa ổn. Vấn đề là sự ví von giữa khóa/chìa vật lý và public/private keys trong cryptography chỉ có ý nghĩa trong một phạm vi hẹp. Ví dụ, khó mà dùng khóa/chìa vật lý để làm digital signature, authentication.

> Tuy nhiên, chắc chắn là một câu hỏi loại này rất thích hợp cho một interview. Người phỏng vấn có thể đặt ra các scenarios về MiM (không phải MiT) để xem interviewee phản ứng thế nào.

> 0

> 0

**Thang Pham** · 07/12/2010 at 3:45 am

> Thực ra chỉ cần dùng phương pháp K1, K2 của anh Hưng ở trên, cộng với việc khi An gửi thì An ký tên bên ngoài hộp, khi Bình nhận được hộp có chữ ký của An thì Bình cũng ký 1 chữ lên đó rồi mới lắp khoá K2. Tất nhiên là An với Bình đều phải biết chữ ký của nhau từ trước ^^.

> 0

> 0

**ivanhoe** · 25/06/2006 at 7:56 pm

> Giải câu 46 nè

> Chia tập số thực ra làm n lớp tương ứng với phần thập phân thuộc vào các khoảng [0, 1/n], [1/n,2/n],…, [n-1/n,1].

> Nếu trong các số x,2x,..,(n-1)x có 1 số có phần thập phân nằm trong 2 khoảng hoặc [0,1/n] hoặc [n-1/n] thì xong.

> Trường hợp còn lại, áp dụng nguyên lý Diricle với n-1 số x,2x,…, (n-1)x cho n-2 khoảng còn lại ta có ít nhất 2 số có phần thập phân nằm trong cùng 1 khoảng.

> Hiệu của 2 số này là 1 trong n-1 số x,2x,…,(n-1)x và nằm trong khoảng 1/n của 1 số nguyên

> 0

> 0

## Bài [17] — 5 bình luận

**catusf** · 31/08/2006 at 5:46 am

> > 49. Tại sao C không có nested functions?

> Hãy hỏi designer của ngôn ngữ C.

> > 50. Làm thế nào để gọi một hàm trong C nếu ta có tên hàm chứa trong một string

> > cho trước? (Ví dụ: ta biết func_name = “some_name”, làm thế nào để gọi hàm

> > some_name?)

> No answer.

> > 51. Làm thế nào để allocate arrays hay structures lớn hơn 64K?

> Cái này phụ thuộc hệ thống. Trong Win32 hay mainframe, câu này trở thành ngớ ngẩn.

> > 52. Lệnh printf(“%d”); sẽ in ra cái gì, tại sao?

> Không xác định, vì không có giá trị của biến. Như vậy mỗi lần chạy chương trình sẽ có kết quả khác nhau.

> > 53. Trong các định nghĩa sau đây, cái gì là const?

> Cái này:

> char* const variable;

> 0

> 0

**Nguyên** · 31/08/2006 at 1:31 pm

> 49. Có 1 stack thôi, làm sao để nested function access được local variables của outer function? Automatic-type nested function để ở đâu đây.

> 50. Bí. Chỉ nghĩ được tới dùng ## preprocessor nhưng mà ## đâu có evaluate variable. Cách khác thì dùng nm để list tất cả symbols trong executable rồi tìm địa chỉ của hàm từ tên ra dùng nhưng mà nếu mà executable đã bị strip thì chịu.

> 51. Chắc hồi máy/compiler cũ. Bây giờ malloc ào ào mấy chục MB mà thấy bị gì

> 52. Theo như bài “Lỗi định dạng chuỗi” thì sẽ in ra giá trị của tiếp theo trên stack.

> 53.

> const char* variable;

> 0

> 0

**Nguyên** · 31/08/2006 at 1:36 pm

> sao lạ quá, 53 bỏ vô 3 hàng hiện ra chưa tới 1 hàng

> a. chỗ variable chỉ tới sẽ readonly

> b. thấy lạ lạ; ‘* char variable;’ đâu có ý nghĩa

> c. variable sẽ readonly

> 0

> 0

**ducha** · 08/09/2006 at 11:30 pm

> 50.

> C1) So sanh’ string voi*’ tung*` ten ham` roi goi. ham` tuong ung*’

> C2) Dat ham` trong 1 lib, vd libfnc.so :

> void functionToCall();

> Sau do’ trong chuong trinh chinh':

> int main() {

> void (*fptr)();

> void *handle;

> char * str = “functionToCall”;

> handle = dlopen(“./libfnc.so”,RTLD_LAZY);

> fptr = dlsym(handle,str);

> if (fptr!=NULL) (*fptr);

> }

> 53) char * const variable;

> 0

> 0

**hoangtran** · 05/10/2006 at 9:05 pm

> Em chỉ thú vị với câu 50: Sử dụng function pointer

> 0

> 0

## Bài [18] — 0 bình luận

## Bài [19] — 5 bình luận

**thangdn** · 02/10/2006 at 10:21 pm

> 55. 20 sinh viên mũ đen ngồi xuống sau lệnh thứ 20 của giáo sư Tèo

> Chứng minh quy nạp, một nhóm có n người đội mũ đen sẽ ngồi xuống sau lệnh thứ k.

> + Trường hợp n=1 là hiển nhiên.

> + Giả sử đúng tới n=k. Xét nhóm có k+1 sv mũ đen, tới lần gọi thứ k +1 sv A đội mũ đen bất kỳ sẽ suy ra mình đội mũ gì. Sv A suy luận, giả sử anh ta đội mũ trắng -> trong nhóm có đúng k người mũ đen -> họ sẽ ngồi xuống sau lần gọi thứ k(giả thiết quy nạp) -> trái thực tế

> Khi giáo sư Tèo nói “Ít nhất một trong số các bạn đang đội mũ đen” sv có thêm thông tin. Có lẽ liên quan đến “đồng bộ hoá” suy nghĩ (chỗ này em vẫn còn mơ hồ)

> 56. Em nghĩ thuật toán “Dừng, ngay khi số quân đỏ còn lại nhiều hơn số quân đen còn lại.” cho xác suất lớn hơn 50% nhưng chưa chứng minh được.

> 57. Tấm bắt tay 500 người.

> Người có 1000 bắt tay và người không bắt tay ai là một cặp vợ trồng. Loại cặp này và trừ số lượng bắt tay mỗi người còn lại đi 1, ta thu được bài toán tương tự với 500 cặp. Tương tự cho tới khi còn đúng một cặp. Không ai bắt tay ai. Qua 500 lần, số bắt tay của Tấm giảm về 0 -> Đpcm

> Mong mọi người cho ý kiến!

> 0

> 0

**lihavim** · 03/10/2006 at 9:09 am

> 55. Chắc do trình độ còn có hạn nên bài anh thangdn em ko hiểu đc nhiều :).

> Em thử trả lời theo cách hiểu của em về cái đề này xem sao: Sẽ chẳng có chuyện gì xảy ra cả. Sinh viên không biết có bao nhiêu cái mũ màu gì. Họ có thể nhìn thấy các mũ khác nên họ có thể thấy các chiếc mũ đen khác => Họ không chắc chắn đc về mũ của mình.

> Thông tin “Ít nhất một trong số các bạn đang đội mũ đen” + việc thấy các mũ đen khác làm cho sinh viên ko chắc chắn về màu của mũ mình :).

> 56.Khi chưa mở con nào, xác suốt thắng là 50%. Khi đã lật đc một số con bài, nếu số bài đã lật đó có số con đen nhiều hơn thì xác suất thắng sẽ lớn hơn 50%. Xác suốt lớn nhất là 100% khi đã lật nửa bộ bài và toàn đen.(Lý thuyết về xác suất em chưa học, chắc phải lên 12 mới học, thế nên em nói dựa theo cái gì nghĩ đc :D).

> 57.Theo cách em hiểu về bài làm của anh thangdn (ko biết có đúng ko? :D) thì anh cho là trong 1 cặp vợ chồng, nếu chồng bắt tay 1 người rồi thì vợ sẽ ko bắt tay người đó nữa và một đôi vợ chồng bắt buộc phải bắt tay với người khác?

> Tuy nhiên, em lại hiểu đề theo kiểu khác (vì đề không hề giới hạn). Có thể chồng bắt tay rồi, vợ vẫn có thể bắt tay lại.

> Em đưa ra 1 ví dụ như sau, có 5 cặp vợ chồng, chồng đánh số từ 1->5, vợ đánh số từ 1′->5′ (trong đó, 1′ là vợ của 1, xếp đứng sau 1,…).

> 1 bắt tay từ 2->5′ (8 lần bắt tay).

> 1′ bắt tay từ 2′->5′ (7 lần bắt tay).

> …

> Đến 5 là 0 lần bắt tay.

> Và khi đó Tấm sẽ là 5′, người không ghi kết quả. Ta có bảng kết quả lần lượt là 0, 1, 2…, 8. Và khi đó, số lần bắt tay của 5′ sẽ phụ thuộc vào sự hứng thú của 5′ :D.

> 0

> 0

**Ngô Quang Hưng** · 03/10/2006 at 9:51 am

> 56. Em nghĩ thuật toán “Dừng, ngay khi số quân đỏ còn lại nhiều hơn số quân đen còn lại.” cho xác suất lớn hơn 50% nhưng chưa chứng minh được.

> Nếu bạn chịu khó tìm thì sẽ thấy là tôi có viết về câu hỏi tương tự câu này trên blog rồi. Quay lại với thuật toán trên của bạn. Để tính xác suất của thuật toán này, ta có thể tính đại khái như sau. Giả sử có 2n lá bài, n đen, n đỏ:

> 1. Tổng số các cách xào bài là

> 1
> (2n)!

> (chú ý rằng các lá bài đều khác nhau).

> 2. Ngay lúc bạn hô dừng, đã có (k+1) lá màu đen và k lá màu đỏ được mở,

> 1
> k \leq n-1

> . Trong cái “prefix” chiều dài (2k+1) này thì có một lá đen ở cuối. Trong cái prefix chiều dài 2k trước lá cuối thì, bất kỳ prefix nào của cái prefix (dài 2k) này cũng đều có tổng số lá đen luôn luôn ít hơn hoặc bằng tổng số lá đỏ. Như vậy, để dừng ở vị trí 2k+1 **và** lá bài tới là lá bài đỏ, ta cần những điều kiện sau đây:

> - Chọn k+1 lá đen, k lá đỏ. Số cách chọn là
> 1
> \binom{n}{k+1}\binom{n}{k}

> - Chọn k lá đen trong số k+1 vừa chọn để làm prefix. Số cách chọn là
> 1
> k+1

> - Xếp 2k lá đen/đỏ thỏa điều kiện trên. Số cách xếp là
> 1
> k!k!\frac{1}{k+1}\binom{2k}{k}

> (gợi ý: xem các số Catalan)

> - Chọn một lá bài đỏ trong số (n-k) lá đỏ còn lại.

> - Xếp (2n-2k-2) các lá đen/đỏ còn lại vào cuối cùng. (lại giai thừa)

> Từ đó bạn tính được xác suất thắng: tổng số sequences làm bạn thắng chia cho 2n giai thừa. Dĩ nhiên, phải tính tổng cho k đến n-1 và estimate cái tổng này. Cần một ít kiến thức về (ước) tính tổng các binomial coefficients kiểu này (cũng không khó khăn gì lắm vì chúng đơn giản lẫn nhau).

> Cái phân tích vừa nêu không hẳn là đã liên quan đến một lời giải tốt cho câu hỏi này :-). Tôi chỉ ghi ra vì phân tích thuật toán của **thangdn** là một bài tập tốt.

> 0

> 0

**Ngô Quang Hưng** · 03/10/2006 at 9:56 am

> 55. Chắc do trình độ còn có hạn nên bài anh thangdn em ko hiểu đc nhiều

> **lihavim** có thể nghĩ về thuật toán đó như thế này: mỗi sinh viên S đếm tổng số mũ đen mà S thấy, gọi số này là **x**. Sinh viên S sẽ ngồi xuống ở phút thứ **x+1** nếu như chưa có ai ngồi xuống ở các phút trước đó.

> 0

> 0

**jalfal** · 03/10/2006 at 4:01 pm

> 55. Câu giải thích của thangdn đã thỏa đáng. Sau phút thứ 20, 20 sinh viên sẽ xác định được mình đội mũ đen.

> Giáo sư cho thêm giả thiết “có ít nhất 1 người đội mũ đen” là để giả thangdn có thể chứng minh được với n=1 thì sinh viên đó có thể biết mình đội mũ màu đen. Nếu không có giả thiết này, n=1 chưa chắc đúng.

> 56. Một thuật toán để tỉ lệ thắng tăng cao là sau một “se-ri” bài đen thì gọi dừng. Ví dụ: Sau khi lật được 10 lá bài đen liên tiếp thì gọi dừng. Sát xuất lá bài tiếp theo (thứ 11) cũng là đen là (1/2) ^ 11. Với chuỗi n lá bài đen, tỉ lệ thắng càng cao khi n càng lớn.

> 0

> 0

## Bài [20] — 7 bình luận

**mudzot** · 24/11/2006 at 2:27 pm

> 58. 2 anh em có thể sinh cùng ngày nhưng khác năm

> 59. Nghe thú vị nhưng trong thời gian ngắn em chưa nghĩ ra được

> 60. Quy nạp theo số hinh chữ nhật con. Vì ta có thể cắt đôi 1 hình cn có tính chất trên thành 2 hình cn cùng tính chất với số mảnh của phân hoạch nhỏ hơn số mảnh ban đầu : kiếm 1 mảnh nằm ở góc, giữ lại cạnh nguyên của nó, cắt dọc theo cạnh còn lại.

> 0

> 0

**Ngô Quang Hưng** · 24/11/2006 at 2:33 pm

> Bạn Mudzot: hai anh em đó sinh cùng ngày cùng tháng cùng năm.

> 0

> 0

**qaz** · 24/11/2006 at 5:32 pm

> 58. 2 anh em sinh này sinh ba, sinh bốn,…

> 0

> 0

**lihavim** · 25/11/2006 at 3:10 am

> Hì, thử làm 59 phát :).

> Gọi K(i) là khoảng cách (km) từ trạm thứ i đến trạm thứ i+1. X(i) là số lít xăng bơm được ở trạm thứ i. Để cho dễ, quy ước cứ 1l đi được 1km.

> Như vậy, theo gt, Tổng K(i) = tổng X(i).

> Trước tiên, chứng minh, tồn tại một trạm, mà từ đó ta có thể đi đến được trạm kế tiếp.

> Giả sử, từ tất cả các trạm, ta không thể đi được đến trạm kế tiếp, khi đó K(i) > X(i). Khi đó, tổng K(i) > tổng X(i), trái giả thiết. Vậy, tồn tại một trạm mà từ đó ta có thể đi đến được trạm kế tiếp.

> Cứ tiếp tục, khi đến xe đến được một trạm x nào đó, số xăng còn dư là D, thì ta cộng:

> X(x)= X(x) + D.

> Và lại trở lại bài toán trên với số trạm giảm đi 1.

> 0

> 0

**lihavim** · 25/11/2006 at 3:13 am

> Anh mudzot nói rõ câu 60 chút được không? Em không hiểu rõ lắm

> 0

> 0

**ducha** · 25/11/2006 at 1:14 pm

> 59. livahim chưa tính đến trường hợp K(i+1) > X(i+1)+ X(i), khi đó dù X(i) >K(i) cũng không thể xuất phát từ chặng (i). Ngoài ra dùng quy nạp không ổn vì phải di chuyển liên tục, không được nhảy chặng.

> Đặt Y(i) = X(i)-K(i). Như vậy Y(i) có dấu +,- hoặc =0. Ta sẽ chứng minh tồn tại chặng J thỏa mãn: Y(J), Y(J) + Y(J+1), Y(J) + Y(J+1) + Y(J+2), … đều >=0. (để dễ hình dung, dùng J+1 thay vì (J+1) mod n)

> Ta sẽ chia n chặng thành các đoạn kế tiếp nhau như sau:

> Đoạn “-” gồm các chặng mang dấu “-“, hoặc bắt đầu từ một chặng mang dấu “+” cho đến khi tổng các chặng

> 0

> 0

**Ngô Quang Hưng** · 25/11/2006 at 2:10 pm

> 59 qui nạp được đấy.

> Nếu các bạn dùng các dấu nhỏ hơn và lớn hơn thì lưu ý cái này.

> 0

> 0

## Bài [21] — 10 bình luận

**lihavim** · 25/11/2006 at 2:52 am

> 61. Như thế nào là thắng ạ?

> 62. Hình dạng bàn và cách để đồng hồ là bất kỳ sao ạ?

> 63. Chỉ thắng được khi gặp được người trình độ chơi kém hơn, vì sẽ có cách chặn. Tuy nhiên, có thể làm xác suất thắng tăng lên (nếu người kia gặp sơ suất :D).

> Phân tích 15, ta có 8 cách:

> 15 = 1+5+9 = 1+6+8 = 2+4+9 = 2+5+8 = 2+6+7 = 3+4+8 = 3+5+7 = 4+5+6

> Ta thấy, số 5 xuất hiện 5 lần, có thể cặp với bất cứ số nào. Như thế, người đầu tiên nên chọn số 5. Sau đó, dựa vào bảng các giá trị phân tích được và giá trị của người thứ hai, để chọn những số làm giảm khả năng cặp số của người kia. Tuy nhiên, người thứ hai vẫn có thể chặn ngược lại người thứ nhất :).

> 0

> 0

**Ngô Quang Hưng** · 25/11/2006 at 9:02 am

> 61. Sorry, Ai lấy nhiều tiền hơn thì thắng.

> 0

> 0

**dang_ky** · 30/11/2006 at 4:35 am

> 61. Em nghĩ đến dynamic programming + heuristic function, giống như việc xây dựng một decoder cho Speech Recognizer hay Text Translator.

> Và kết quả là sẽ không có lời giải tối ưu, chỉ là heuristic thôi (ví dụ nếu kéo thành 10000 đồng tiền, thì không thể dựng được 1 giải thuật tối ưu)

> 63. 15 = 1+5+9 = 1+6+8 = 2+4+9 = 2+5+8 = 2+6+7 = 3+4+8 = 3+5+7 = 4+5+6

> Người đầu sẽ thắng, với cách tìm cách chiếm lấy 3 trong 4 vị trí 2,4,6,8 ở góc bàn, đó là các tử huyệt, chiếm được 3 vị trí thì người thứ 2 chạy đằng trời

> Trên đường chiếm được 3 trong 4 vị trí nói trên, người thứ 2 không thể ngăn được người thứ nhất

> 0

> 0

**trang2** · 04/12/2006 at 7:06 pm

> 63. 7 6 2 la thang roi.

> 61. co thuat toan toi uu, rat don gian, keo len den 100 000 dong tien cung duoc.

> 0

> 0

**Ngô Quang Hưng** · 04/12/2006 at 7:21 pm

> 61. co thuat toan toi uu, rat don gian, keo len den 100 000 dong tien cung duoc.

> Một câu hỏi liên quan: nếu có một số lẻ các tờ tiền thì thế nào?

> 0

> 0

**trang2** · 05/12/2006 at 1:54 am

> 61. Danh dua vao so troi vay .

> 0

> 0

**lihavim** · 06/12/2006 at 9:00 am

> @dang_ky: Anh có thể đưa ra một lý dụ về cách lấy được 3 trong 4 “tử huyệt” đó không?

> @trang2: Đâu có được lấy 1 lần 3 số đâu mà thắng dễ thế nhỉ? 7 chỉ có trong 2 bộ, nếu người 1 lấy 7, người 2 lấy 3, người 1 lấy 6 (hoặc 2), người 2 lấy 2 (hoặc 6)?

> 0

> 0

**trang2** · 06/12/2006 at 2:12 pm

> xin loi, minh cu nghi la 2 so cung duoc.

> 0

> 0

**k40** · 08/12/2006 at 3:42 am

> Câu 61:

> vì số tờ tiền là chẵn nên ta có thể chia đánh số thứ tự từ 1 đến 100 theo đúng thứ tự sắp xếp

> tính tổng giá trị các tờ tiền có số thứ tự là lẻ

> tính tổng giá trị các tờ tiền có số thứ tự là chẵn

> giả sử tổng giá trị của dãy lẻ lớn hơn

> vậy người đi trước sẽ lấy tờ số 1

> người đi thứ hai bắt buộc phải lấy tờ tiền thuộc dãy chẵn là 2 hoặc 100

> sau khi người thứ hai lấy xong thì lại lộ ra một tờ thuộc dãy lẻ là 3 hoặc 99

> cứ như vậy thì người đi trước sẽ chiến thắng (An đi trước)

> 0

> 0

**k40** · 08/12/2006 at 4:05 am

> Câu 63

> xếp các con số vào ô vuông 3×3 như sau sẽ nhận được lời giải không ai chiến thắng

> 2 7 6

> 9 5 1

> 4 3 8

> tổng các số trên mỗi hàng, hoặc cột, hoặc đường chéo đều bằng 15, nếu cả hai người đều thông minh tuyệt đỉnh thì sẽ không có ai thắng được cả.

> Nếu người đi đầu chọn số 5 thì người đi sau bắt buộc phải chọn số chẵn, và sẽ có kết quả hòa.

> Nếu người đi đầu chọn số ở góc ví dụ là 2 thì người thứ hai bắt buộc phải chọn số 7 hoặc 9 ở cạnh số 2 mới có hy vọng gỡ hòa.

> 0

> 0

## Bài [22] — 14 bình luận

**dongta** · 10/12/2006 at 12:17 am

> 64. Một quy tắc vàng là nếu một ngụy biện sử dụng “dễ thấy rằng” thì ngụy biện đấy sai ở chỗ “dễ thấy rằng”. Trong trường hợp này, nếu x khác 1 thì f not well-defined (-> vô cùng). Cho nên, không thể nói f=x^f.

> 66. 132 thời điểm (assume ta phân biệt được am & pm).

> 0

> 0

**Ngô Quang Hưng** · 10/12/2006 at 12:51 am

> 64. “Dễ thấy rằng” f(x) không luôn tiến đến vô cùng. Nếu đặt f_n(x) giống như f(x) nhưng chỉ có n xuất hiện của x thì f(x) là giới hạn của dãy f_n(x) khi n tiến đến vô cùng.

> Với x bằng căn hai, f_n(x) là dãy tăng và bị chặn trên. (Tại sao?)

> Một câu hỏi khác liên quan: với giá trị dương nào của x thì f(x) well-defined?

> 0

> 0

**An Vinh** · 15/02/2013 at 4:23 am

> Em xin trả lời cái câu hỏi khác trước: Nếu chỉ xét f(x) và x trên R thì f(x) well-defined khi và chỉ khi 0 < x <= e^(1/e).

> Khi đó chứng minh được là 0 < f(x) B” và có B đã suy ra có A.

> 0

> 0

**An Vinh** · 15/02/2013 at 4:34 am

> (Reply đầu của em bị nuốt mất chữ nên em post lại)

> Em xin trả lời cái câu hỏi khác trước: Nếu chỉ xét f(x) và x trên R thì f(x) well-defined khi và chỉ khi $0 < x < e^\frac{1}{e}$.

> Khi đó chứng minh được là $0 < f(x) < e$.

> Từ đó em suy ra câu trả lời của 64 là: do không tồn tại x sao cho f(x) = 4 nên mệnh đề nhưng " $f(\sqrt{2})=4$" là sai, dẫn tới không có nghịch lý như trên.

> Theo em, về logic, các lập luận trong 64 sai ở chỗ: chỉ có "A $\Rightarrow$ B" và có B đã suy ra có A.

> 0

> 0

**dongta** · 10/12/2006 at 3:09 am

> - Anh Hưng nói rất đúng. Em đã phát biểu hơi hồ đồ. Với x=sqrt(2) thì bằng quy nạp, có thể thấy f_n tăng và bị chặn trên bởi 2=sqrt(2)^2. f(x) is well-defined iff xe thì f(x)=c vô nghiệm.

> 0

> 0

**dongta** · 10/12/2006 at 3:10 am

> Anh Hưng nói rất đúng. Em đã phát biểu hơi hồ đồ. Với x=sqrt(2) thì bằng quy nạp, có thể thấy f_n tăng và bị chặn trên bởi 2=sqrt(2)^2. f(x) is well-defined iff xe thì f(x)=c vô nghiệm.

> 0

> 0

**dongta** · 10/12/2006 at 3:11 am

> chẳng hiểu sao đoạn giữa lại bị truncated???

> 0

> 0

**lihavim** · 10/12/2006 at 7:59 am

> 66. Nếu như bị giam kín, không phân biệt được ngày và đêm thì làm sao biết được mấy giờ nhỉ?

> 0

> 0

**Ngô Quang Hưng** · 10/12/2006 at 7:59 am

> dongta xem cái thông báo sẽ hiểu tại sao. Tôi lười chưa có thời gian sửa cái vụ annoying này.

> 66. Nếu như bị giam kín, không phân biệt được ngày và đêm thì làm sao biết được mấy giờ nhỉ?

> Lihavim: nếu không phân biệt được am, pm thì có gấp đôi số thời điểm không biết giờ.

> 0

> 0

**lihavim** · 11/12/2006 at 3:13 am

> Cho cháu hỏi thêm chút liên quan đến câu 66. Định nghĩa thời điểm ở đây là như thế nào ạ? Trong 24 giờ có bao nhiêu thời điểm theo như định nghĩa thời điểm trên?

> 0

> 0

**Ngô Quang Hưng** · 11/12/2006 at 6:47 am

> Lihavim: Trong 24 giờ có vô hạn các thời điểm.

> 0

> 0

**lihavim** · 11/12/2006 at 7:55 am

> Hum, có vẻ cháu hơi chậm hiểu, vẫn chưa thể nào hiểu được bài 66. Theo như chú nói trên, nếu không phân biệt được am và pm thì gấp đôi 132. Vậy con số này ở đâu ra ạ?

> Trên một cái đồng hồ được chia làm 12 vạch, thì ta chỉ biết kim nó chỉ từ số 1 đến số 12. Như vậy, theo cháu nghĩ mọi thời điểm trong ngày, ta đều không biết được lúc xem đó là bao nhiêu giờ chứ nhỉ?

> 0

> 0

**Ngô Quang Hưng** · 11/12/2006 at 8:40 am

> Lihavim: khi kim giờ chỉ vào khoảng giữa giờ x và giờ x+1 thì kim phút phải nằm ở đúng tỉ lệ đó trên vòng tròn. Do đó, trong đa số các trường hợp thì nhìn qua ta biết ngay kim nào là kim giờ, kim nào là kim phút.

> 0

> 0

**haison3000** · 13/12/2006 at 6:59 am

> bai 65: Muc dich la 4 la bai con lai co the chi ra duoc la bai thu 5 da bi dau di. Co 2 thong tin can neu ra la:

> – thu tu cua la bai : 2,3,4 …, J,Q,K,A => 13 kha nang

> – hinh cua la bai: co, ro, chuon, bich = > 4 kha nang

> 1. Thu tu la bai. Co the dung 1 cai total order cho cai la bai, vd: 2 13 kha nang nen An co the nhin vao thu tu nay ma doan ra con so tren la bai thu 5.

> 2. Hinh cua la bai: em van dang suy nghi

> 0

> 0

## Bài [23] — 10 bình luận

**dongta** · 23/12/2006 at 12:40 pm

> 67. Ta có thể chia thành 3 phần như sau:

> – Đánh số cân một số bánh là a_1, a_2,…, a_n sao cho sum(a_i) là lớn nhất và không quá 1.

> – Với các bánh còn lại, cũng đánh số b_1,…,b_m sao cho sum(b_j) là lớn nhất và không quá 1. (*)

> – Các bánh còn lại nặng không quá 1kg.

> Giả sử không phải vậy thì sum(a_i)+sum(b_j) mâu thuẫn (*). Còn nếu không có bánh nào nặng hơn 0.5 thì ta có thể đánh số bánh này là b_(m+1) -> cũng mâu thuẫn (*).

> 0

> 0

**dongta** · 23/12/2006 at 3:02 pm

> 69. Co 2^10 tap con tat ca. Moi tap con co tong khong qua 1000 => phai co 2 tap con co tong giong nhau.

> 0

> 0

**Ngô Quang Hưng** · 24/12/2006 at 8:58 am

> Dear Dongta: 69 – còn điều kiện 2 tập con không giao nhau nữa.

> 0

> 0

**dongta** · 24/12/2006 at 9:45 am

> Nếu A & B là 2 tập con có tổng bằng nhau thì A\B & B\A sẽ là 2 tập con không giao nhau có tổng bằng nhau.

> Còn câu 68 thì em chỉ có thể giải mechanically

> 0

> 0

**rilwis** · 27/12/2006 at 2:41 am

> @dongta: Cách giải câu 67 của anh hay quá. Nhưng lập luận của anh đâu cần câu cuối cùng.

> Em nhận thấy cách giải có thể cải tiến 1 chút:

> Chọn ra một số mẩu bánh (nhóm A) sao cho tổng khổi lượng của chúng lớn nhất và không vượt quá 1.

> Số bánh còn lại chia làm 2 nhóm bất kì B và C.

> Khi đó 2 nhóm B và C đều có khối lượng 1kg, giả sử B > 1kg; do A + B + C

> 0

> 0

**Ngô Quang Hưng** · 27/12/2006 at 6:35 am

> rilwis: please read this to fix the missing text problem

> 0

> 0

**rilwis** · 27/12/2006 at 2:52 pm

> Vâng anh, em chỉnh lại thế này (không hiểu sao em chỉnh 1 lần rồi nhưng gửi không được nên dùng lời vậy):

> Chọn một số mẩu bánh (nhóm A) sao cho tổng khổi lượng của chúng lớn nhất và không vượt quá 1.

> Số bánh còn lại chia làm 2 nhóm bất kì B và C.

> Khi đó 2 nhóm B và C đều có khối lượng không quá 1kg. Thật vậy nếu 1 trong 2 nhóm có khối lượng vượt quá 1kg, giả sử là B; do tổng khối lượng của A + B + C không quá 2 kg nên tổng khối lượng của A và C nhỏ hơn 2kg, vi phạm cách chọn nhóm A.

> Vậy luôn chia được thành 3 nhóm thỏa mãn yêu cầu.

> 0

> 0

**rilwis** · 27/12/2006 at 2:54 pm

> Chết, em ghi nhầm, sửa lại thành:

> Chọn một số mẩu bánh (nhóm A) sao cho tổng khổi lượng của chúng lớn nhất và không vượt quá 1kg.

> Số bánh còn lại chia làm 2 nhóm bất kì B và C.

> Khi đó 2 nhóm B và C đều có khối lượng không quá 1kg.

> Thật vậy nếu 1 trong 2 nhóm có khối lượng vượt quá 1kg, giả sử là B; do tổng khối lượng của A + B + C không quá 2 kg nên tổng khối lượng của A và C nhỏ hơn 1kg, vi phạm cách chọn nhóm A.

> Vậy luôn chia được thành 3 nhóm thỏa mãn yêu cầu.

> Cho em hỏi có thể chỉnh sửa trực tiếp bài mình đã gửi rồi không?

> 0

> 0

**Ngô Quang Hưng** · 27/12/2006 at 4:50 pm

> Xin lỗi rilwis, tôi không có account của user thường nên không kiểm tra ngay cho bạn được xem có edit được comment của mình không. Bạn xem xem dưới comment có option “edit this” không? Nếu không có thì là không được.

> 0

> 0

**trang2** · 06/01/2007 at 9:38 am

> 68. Truong hop n=5, nhan thay sau buoc 1, so cac so le tren vong se luon la chan (0, 2 hoac 4 so le). Neu ta bat dau bang 2 hoac 4 so le thi se ko bao gio ta co the dat duoc 0 so le ca. Vi cach duy nhat de dat duoc 0 so le la phai co 0 hoac 5 so le.

> Truong hop n=4, co the nhan thay rang sau mot vai buoc, cac so tren vong se bien thanh so chan. Neu ta chia doi cac gia tri do va thi ta van duoc mot bai toan tuong duong nhung gia tri lon nhat trong vong da bi giam di (it nhat) 1 nua. Do gia tri lon nhat la huu han nen se den luc tat ca la 0.

> 0

> 0

## Bài [24] — 7 bình luận

**novice** · 12/01/2007 at 2:04 am

> 70. Dựa vào tính chất hàm số f(x)liên tục trên [a,b] có f(a)f(b)

> 0

> 0

**novice** · 12/01/2007 at 2:07 am

> xin lỗi không hiểu vì sao em viết đầy đủ mà khi submit lại bị thiếu mất.”Dựa vào tính chất hàm số f(x)liên tục trên [a,b] có f(a)f(b)

> 0

> 0

**Ngô Quang Hưng** · 12/01/2007 at 6:00 am

> Sorry, xem Lưu ý về viết lời bình trong blog

> 0

> 0

**novice** · 12/01/2007 at 8:20 pm

> 71. Chứng minh phản chứng. Giả sử không tồn tại đường thẳng nào đi qua chỉ 2 điểm và các điểm không nằm trên cùng một đường thẳng. Từ giả thiết ta thấy tồn tại 3 điểm không thẳng hàng (nếu không tồn tại thì tất cả các điểm nằm trên 1 đường). Từ 3 điểm này xét 3 đường thẳng đi qua 2 điểm trong 3 điểm. Vì không có đường thẳng nào chỉ đi qua hai điểm nên trên mỗi đường thẳng chúng ta lại thấy tồn tại ít nhất 1 điểm trong tập hợp ngoài những điểm chúng ta đang xét. Xem xét tiếp 3 điểm này với cách tương tự như 3 điểm ban đầu với chú ý rằng 3 đường thẳng mới và 3 đường thẳng cũ không trùng nhau. Với cách lập luận như trên thì nếu giả thiết không tồn tại đường thẳng nào thỏa mãn thì quá trình trên lẽ tiến đến vô hạn như vậy tập hợp điểm là vô hạn. Vậy mâu thuẫn với giả thiết tập điểm chúng ta xét là hữu hạn.

> 0

> 0

**nguyendz** · 20/01/2007 at 1:06 am

> 72. Xet 4 diem tren 1 duong thang, thu tu nhu sau, xanh xanh do do. Khong co cach nao noi 1 xanh 1 do de cac doan thang khong cat nhau.

> 0

> 0

**Ngô Quang Hưng** · 20/01/2007 at 6:00 am

> 72. Xin Lỗi, tôi viết thiếu giả thiết là không có 3 điểm nào thẳng hàng

> 0

> 0

**1001001** · 05/04/2009 at 3:04 pm

> 72. Trong số các cách nối các điểm xanh – đỏ với nhau, tồn tại 1 cách nối sao cho tổng độ dài các đoạn thẳng được tạo thành là bé nhất. Ta chứng minh cách nối đó thỏa yêu cầu. Thật vậy, giả sử có 2 cặp điểm tạo thành 1 cặp đoạn thẳng cắt nhau, ta có thể thay cách nối để tạo thành 1 cặp đoạn thẳng với độ dài bé hơn (mâu thuẫn).

> vd cặp đoạn thẳng X-Đ cắt nhau:

> X X

> . .

> .

> . .

> Đ Đ

> thay đổi thành

> X X

> . .

> . .

> Đ Đ

> 0

> 0

## Bài [25] — 6 bình luận

**uyvu** · 01/03/2007 at 7:38 pm

> Số lần thử tối đa: [(n+1)/2]*[(n+1)/2]

> 0

> 0

**Ngô Quang Hưng** · 02/03/2007 at 4:54 am

> [(n+1)/2]*[(n+1)/2] thì vẫn là

> 1
> \Theta(n^2)

> thôi.

> 0

> 0

**Bach Hung Nguyen** · 02/03/2007 at 6:55 am

> Em nghi la can O(n/2) phep thu.

> 0

> 0

**Ngô Quang Hưng** · 02/03/2007 at 11:14 am

> Hi Nguyên:

> 1
> \Theta(n)

> có thể làm được, hơi mẹo một chút.

> 0

> 0

**trang2** · 05/03/2007 at 1:47 pm

> Ta chia bài toán thành 2 bước, bước 1 là thử tìm mẫu máu duy nhất “có thể” xuất hiện hơn n/2 lần trong dãy, bước 2 đơn giản chỉ là kiểm tra xem mẫu đó có thực sự xuất hiện > n/2 lần ko ?

> Bước 1:

> Chia n mẫu ban đầu thành n/2 cặp, rồi so sánh các cặp với nhau. Cặp nào ko giống nhau thì loại ra luôn, ko xét nữa, chỉ xét những cặp giống nhau thôi.

> Trong trường hợp ko có cặp giống nhau nào thì có thế kết luận là ko thể có > n/2 mẫu giống nhau đc.

> Trong trường hợp tìm được k>0 cặp giống nhau, thì nếu thực sự có > n/2 mẫu giống nhau, thì có hơn k/2 cặp giống nhau là mẫu đó. Do đó ta có thể thu nhỏ bài toàn về tìm xem trong k cặp, có hơn k/2 cặp có cùng mẫu máu ko ? Tiếp tục tìm đến khi còn 1 cặp thì dừng. Trả về mẫu máu duy nhất còn lại.

> Bước 2:

> Dựa vào mẫu máu kết quả của bước 1, dùng n bước thử để kiểm tra xem nó có xuất hiện đúng n/2 lần ko ?.

> Độ phức tạp của bước 1 là O(n) vì sau mỗi lần chia cặp + thử, k bài toán là O(n)

> 0

> 0

**Ngô Quang Hưng** · 05/03/2007 at 6:40 pm

> Trang2: nice solution!

> 0

> 0

## Bài [26] — 5 bình luận

**tvhvt** · 23/03/2007 at 11:24 am

> 75. câu này dễ quá. con trưởng: 9, con kế: 6, con út: 2. Mượn 1 con trâu tưởng tượng của hàng xóm.

> 0

> 0

**thangdn** · 23/03/2007 at 11:43 am

> 74. Bài này em có làm qua hồi cấp 2

> 1, 4, 6, 7, 10, 11, 13, 16

> 2, 3, 5, 8, 9, 12, 14, 15

> 0

> 0

**tungnvn** · 13/04/2007 at 6:25 pm

> Chúng ta thử nêu thuật toán để lập trình 2 bài này xem? Tôi thấy khá hay.

> 0

> 0

**machine** · 18/01/2010 at 9:16 am

> 75. Em k mượn con trâu tưởng tượng vì thấy nó…ảo quá.

> Em thấy vầy.

> 1/2 = 1/3 nhân 3/2

> 1/3 = 1/9 nhân 3

> Gọi a là 1/9 số trâu

> a + 3a + 3*3*a/2 = 17

> a = 17/8.5 =2

> 2-6-9 tương ứng với số trâu của con út-con kế- con trưởng

> 0

> 0

**Duy** · 19/01/2010 at 8:25 am

> 75: Theo đúng lời cha, ba ngừơi con làm như sau:

> (a) Người con trưởng hưởng 1/2 của 17 = 8 con.

> (b) Người con thứ hưởng 1/3 của 17 = 5 con.

> (c) Người con út hưởng 1/9 của 17 = 1 con.

> Như vậy số trâu còn dư ra la 3 = 17 – (8 + 5 + 1) con, mỗi người thêm một con. Không ai tranh dành ai.

> Tóm lại: 9, 6, 2 (or 2,6, 9)

> 0

> 0

## Bài [27] — 10 bình luận

**instcode** · 28/04/2007 at 10:03 am

> 77. Cướp biển chỉ cần dùng dùng *1-bit* error detection algorithm. Hi sinh thằng cướp đầu tiên để tính even parity với cặp (Xanh, Đỏ) ~ (0, 1)

> 0

> 0

**lihavim** · 28/04/2007 at 6:26 pm

> 77. Chả hiểu anh instcode nói gì nên em đưa cách của em, chết cũng nhiều nhưng sống được hơn một nửa.

> Với N=1 thì cơ hội sống là 50%.

> Với N=2 thì dùng cách của đề bài.

> Với N>=3 Khi đó sẽ chia theo nhóm, mỗi nhóm 3 người. Dư bao nhiêu (1 hay 2) thì đưa về trên.

> Xét trong từng nhóm 3 người: (1) (2) (3)

> Người (1) chịu hi sinh *_*, nhìn (2) và (3), nếu 2 thằng kia khác màu nhau thì nói là đỏ, nếu giống thì nói là xanh.

> Như thế, thằng (2) nhìn thằng đỏ mà đoán cái mình và thằng (3) nghe thằng (2) mà đoán cái của mình.

> 76. Cháu không hiểu đề lắm. Cái ô nhớ là hằng số đó có thể lưu trữ cái gì? Có phải anh lính này nói cho anh lính kia thời gian để bắn?

> 0

> 0

**haison3000** · 29/04/2007 at 8:26 pm

> 76. Gia su x la anh linh bi ong tuong vo vai. Bai toan dc giai neu tat ca anh linh deu biet vi tri tuong doi cua minh so voi anh linh x (goi p(l) la khoang cach cua anh linh l so voi x theo chieu kim dong ho). Vi khi do anh linh x se truyen tin hieu khai hoa toi nguoi ben trai, nguoi do lai tiep tuc truyen tin hieu sang nguoi ben trai, …. de cung nhau khai hoa luc 2^n-p(l) ke tu khi nhan dc tin hieu khai hoa tu x.

> De l biet duoc p(l), l truyen tin hieu theo chieu kim dong ho toi x, khi x nhan dc se truyen tin hieu tro lai cho l. Thoi gian tu khi l nhan duoc tin hieu hoi am = 2 * p(l).

> Khong biet co cach nao don gian hon khong.

> 0

> 0

**ducha** · 01/05/2007 at 4:05 pm

> 77. Dùng 1 và 0 để mã hoá 2 màu. Người đầu tiên nói tổng số màu (0 or 1 in binary field) của những người đứng trước. Những người tiếp theo dựa theo tổng số màu hiện tại (phải nhớ màu những người trước nói) và tổng số màu những người đứng trước mình (tự đếm) để tính ra màu của mình. Kết quả tệ nhất là N-1.

> Chắc đây cũng là cách instcode nói.

> 0

> 0

**giahanh** · 03/05/2007 at 6:41 am

> Các bác dùng từ “mã hoá”, “0 và 1″ nghe nó Tin học quá, mấy em cướp biển chắc không hiểu đâu quanh năm đi cướp không có online đâu. Em nói lại đơn giản thế này (chắc cũng giống cách của ducha thôi!) em đầu tiên sẽ đếm số mũ xanh đứng trước mình nếu là số chẵn sẽ nói mũ mình là xanh, ngược lại nói là đỏ, em thứ 2 sau khi biết màu của em thứ nhất xong sẽ đếm số mũ xanh của những người đứng trước mình để biết được mũ mình đang đội là màu gì, em thứ 3 biết được màu mũ của em thứ 2 và thứ nhất xong sẽ đếm số mũ xanh còn lại để biết được màu mũ của mình…và như vậy tồi nhất chỉ hi sinh em đầu tiên thôi!

> Trình bày như thế này chắc mấy em cướp biển dễ hiểu hơn các bác nhỉ!:D

> Phải nói là anh Hưng có câu hỏi hay quá!Em nghĩ trong các cuộc thi học sinh giỏi nên dùng những dạng câu hỏi thế này.

> 0

> 0

**lihavim** · 04/05/2007 at 2:46 am

> Hehe, bây giờ mới thực sự hiểu cách giải đó, đúng là chỉ ngỏm có 1 người

> 0

> 0

**minhpq** · 10/01/2009 at 8:21 am

> hix. nếu N của câu hỏi là số dân 80 triệu người của việt nam thì…..sặc tiết. mà kòn của thèng Trung Qủa thì cũng đi ăn cắp vài trăm triệu chú. nói chung là chỉ trên mặt lý thuyết thôi. kòn tui thì có cách đơn giản hơn : ví dụ ước lượng 5 giấy trả lời thì 2 người đằng trước là xanh đổ. 10 giây trả lời thì 2 bác trước là đỏ đỏ. …. quá đơn giản mà hiệu quả …. haha…

> 0

> 0

**Khoa Trần** · 14/11/2009 at 1:52 pm

> 76. Bài này em liên tưởng tới phương pháp flooding & TTL trên network. Ông tướng chỉ cần nói số $n$ với anh lính. Anh này truyền $n-1$ sang 2 anh 2 bên. Mỗi anh khi nhận được một số thì lại tiếp tục truyền như vậy. Khi nào truyền số 0 hoặc nhận được số 0 thì bóp cò

> 0

> 0

**Khoa Trần** · 14/11/2009 at 1:55 pm

> 76. Nhầm lẫn 1 tí, ông tướng phải bảo anh lính truyền số $2^{n-1}$

> 0

> 0

**Ngô Quang Hưng** · 14/11/2009 at 8:50 pm

> Chào Khoa, Bộ nhớ là O(1) thì không truyền số $2^{n-1}$ được.

> 0

> 0

## Bài [28] — 5 bình luận

**dongnl** · 17/05/2007 at 2:04 am

> 78. Giả sử chỉ có 200 lít xăng thì giải pháp như sau:

> – Lượt 1: chở 100 lít xăng từ điểm xuất phát, đến cây số 33 1/3 km, để lại 33 1/3 lít xăng, sau đó quay lại điểm xuất phát.

> – Lượt 2: chở 100 lít xăng từ điểm xuất phát, đến cây số 33 1/3 km, nhặt 33 1/3 lít xăng ở đó, đi về đích.

> Theo cách này, xe tải mang đến đích được 33 1/3 lít xăng.

> Với 300 lít xăng thì một giải pháp (chưa chứng minh được là tối ưu) như sau:

> – Lượt 1: chở 100 lít xăng từ điểm xuất phát, đến cây số 25 km, để lại 50 lít xăng, quay lại điểm xuất phát.

> – Lượt 2: chở 100 lít xăng từ điểm xuất phát, đến cây số 25 km, nhặt 25 lít xăng ở đó, đến cây số 50 km, để lại 25 lít xăng, quay lại điểm xuất phát.

> – Lượt 3: chở 100 lít xăng từ điểm xuất phát, đến cây số 25 km, nhặt 25 lít xăng ở đó, đến cây số 50 km, nhặt 25 lít xăng ở đó, đi về đích.

> Theo cách này xe tải mang đến đích được 50 lít xăng.

> Không biết ai có thể có giải pháp tổng quát với x lít xăng bất kỳ thì tốt quá.

> 79. Câu hỏi tổng quát hơn có thể là: cho một hình gốc tạo bởi các ô vuông đơn vị, chọn một mảnh giấy sao cho với bất kỳ một ô vuông nào trong hình gốc có thể dùng mảnh giấy phủ lên hình gốc không che ô vuông đã chọn, không phủ thừa ra ngoài mà diện tích không được phủ là ít nhất.

> Với trường hợp hình chữ nhật, chia làm 4 hình chữ nhật con bằng nhau, khi đó bất kỳ một ô X nào trên hình gốc cũng phải thuộc 1 trong 4 hình chữ nhật con. Vì vậy chọn mảnh giấy phủ có hình của 3 hình chữ nhật con hợp lại (hình chữ L).

> Khi hình gốc cụ thể là bàn cờ 8×8, chọn 3 mảnh giấy hình chữ L là hợp của 3 hình 4×4, 3 hình 2×2, 3 hình 1×1 thì sẽ đảm bảo yêu cầu phủ kín, không thừa và không che ô vuông đơn vị bât kỳ.

> 0

> 0

**lihavim** · 17/05/2007 at 3:40 am

> 78. Không biết xài chương trình có ăn gian không nhỉ?

> Với bước nhảy 1 và 2 thì số xăng có thẻ đua về là 52. Trình tự như sau:

> -Chở 100 lít xăng đến km số 1, để lại 98 lít, về và chở tiếp.

> Xe cuối cùng (ce thứ 3) đến km số 1 mất 1 lít, còn 99 lít. Bơm đầy và cứ tiếp túc từng km như thế, cuối cùng đêm về đích được 52 lít.

> Tương tự, bước nhảy 2 km một lần cũng thế.

> 0

> 0

**holo** · 17/05/2007 at 8:30 am

> Với 100 lít : ta chỉ có một cách là chở hết và đem thẳng tới đích.

> Với 200 lít : gọi a là vị trí sau 2 lượt chuyển xe còn 100 lít. KHi đó số xăng do lượt 1 cung cấp tại vị trí tối đa là 100 – 2a, lượt 1 là 100 – a, do đó vị trí a tối ưu là (100 -2a) + (100 – a) = 100 => a = 33+ 1/3 km.

> Với 300 lít : ta cần tìm vị trí tối ưu a’ để dịch chuyển mà tại đó ta còn 200 lít.

> lượt 1,2 tối ưu cũng chỉ cung cấp được 100 – 2a’

> lượt 3 tối ưu cung cấp được 100 – a’ do đó vị trí tối ưu là

> 2(100 – 2a’) + 100 – a’ = 200 => a’= 20 km;

> Như vậy ta thấy số xăng tối đa có thể dich chuyển được là 20 + 33 + 1/3 = 53+1/3 lít

> Bài toán có thể giải tổng quát với n lít xăng > 200

> 0

> 0

**choconlangthang** · 17/05/2007 at 10:11 am

> 78.

> Tất cả bài giải trên đều dựa vào giả định xe chở xăng trong bình xăng xe (hoặc xe lấy xăng trực tiếp từ cái xi-tẹc nó đang chở, :D). Tuy nhiên tôi không thấy điều này trong đề bài!

> 0

> 0

**lihavim** · 19/05/2007 at 2:56 am

> @choconlangthang: Xe hết xăng dừng lại láy trong tẹc dùng thì có sao?

> 0

> 0

## Bài [29] — 12 bình luận

**dvl_vn** · 24/07/2007 at 2:10 am

> 80. Em nghĩ thế này: 25 hòn sỏi trắng xếp vòng tròn sẽ tạo ra 25 khe để sếp các hòn sỏi đen vào đó. Để không có hòn sỏi nào mà hai hòn kề nó đều trắng thì: không có hai khe nào liền nhau bị bỏ trống, và các khe có sỏi đen phải có không ít hơn 2 hòn sỏi đen. Số khe phải có sỏi đen là 25/2+1=13 khe. Do 13*2=16>25. Nên điều kiện để không có hòn sỏi nào có hai hòn kề nhau là trắng là không thể. Suy ra điều ngược lại là đúng.

> 0

> 0

**trang2** · 27/07/2007 at 10:46 am

> Neu em nho ko nham thi 2 cau 81 va 82 anh Hung deu da do trong blog nay roi, chi la duoi dang khac thoi.

> 0

> 0

**Ngô Quang Hưng** · 27/07/2007 at 10:51 am

> @Trang2: cũng có thể. Bây giờ tôi chỉ dùng bộ nhớ 10KB (trong đầu) chứ không kiểm tra lại xem 80 câu trước có trùng hay không. Tôi nghĩ là không trùng lặp, nhưng cũng không đảm bảo 100% được.

> 0

> 0

**npson** · 27/07/2007 at 1:26 pm

> Nhìn ngon quá nhưng mà đắt dã man, lần nào cũng đi qua ngó 1 cái chơi thôi, đụng vào thì híc…

> 0

> 0

**dongta** · 30/07/2007 at 9:38 am

> Có vẻ các câu hỏi này đã được trả lời gọn gẽ trên http://www.vnqf.org/forums/riddles_and_interview_questions/702-cac_so_tren_vong_tron.html

> Cho em xin phép post mấy câu toán đố chưa trả lời của anh Hưng lên trên đấy nhé?

> 0

> 0

**Ngô Quang Hưng** · 30/07/2007 at 9:39 am

> Ừ, dongta cứ post lại, ghi lại nguồn blog KHMT là được.

> 0

> 0

**dongrus** · 15/08/2007 at 7:11 am

> ->80 : Phan chung , gia su ko co vien bi nao co tinh chat nhu tren (hai vien bi canh no deu la trang)

> Dat goc i=0 tai 1 vien bi trang bat ki , nhan thay rang khi i tang len i chia 4 du 2 thi vi tri do la bi den , i chia 4 du 0 (chia het :D) thi vi tri do la bi trang .Suy ra vi tri i=48 (chia het cho 4) la bi trang => Vo ly .Vay ton tai bi co tinh chat tren

> 0

> 0

**Linh** · 05/12/2008 at 11:13 pm

> Sư phụ nào giải giúp em bài này với.Thầy em đố mà nghĩ hoài ko ra:

> trong 1 thành phố đang có bệnh dịch . thành phố có 10^5 người

> biết 1% dân số bị nhiễm bệnh

> có 1 trung tâm xét nghiệm.Mỗi ngày trung tâm xét nghiệm tối đa 10^3 mẫu xét nghiệm

> (mỗi mẫu xét nghiệm này có thể của >=1 người )

> nếu trong 1 mẫu cỡ m bất kì ( m>=1) mà có nhiều hơn 1 người nhiễm bệnh thì kết quả xét nghiệm sẽ sai.

> ví dụ: mẫu xét nghiệm cỡ 4 ( người 1, người 2, người 3, người 4) mà người 2 và người 4 nhiễm thì nó sẽ cho kết quả sai

> tìm phương án xét nghiệm và số ngày xét nghiệm ít nhất để tìm ra toàn bộ người nhiễm bệnh?

> nghe thầy nói là dù dân số có tiến đến vô cực thì kết quả cũng vậy, tức là kết quả ko phụ thuộc số dân.Trong bài này cho 10^5 cho dễ

> 0

> 0

**1001001** · 04/04/2009 at 4:53 pm

> 80. Em xét các bộ ba (x,y,z) (x,y,z thuộc tập {trắng, đen}) theo chiều kim đồng hồ để chỉ màu của bộ 3 bi liên tiếp nhau thuộc vòng tròn. Có tất cả 50 bộ như vậy.

> 1 bộ ba (x,y,z) được gọi là trắng phải nếu z trắng. Số bộ như thế này là 25.

> 1 bộ ba (x,y,z) được gọi là trắng trái nếu x trắng. Số bộ như thế này là 25.

> Bài toán tương đương với việc chứng minh tồn tại 1 bộ ba vừa trắng phải vừa trắng trái.

> Ta giả sử kết luận của bài toán là sai.

> Nếu có 1 bộ không trắng phải và không trắng trái, ta có ngay mâu thuẫn bằng nguyên lí Dirichlet.

> Nếu 1 bộ luôn hoặc trắng phải, hoặc trắng trái, ta suy ra không tồn tại các bộ có dạng (đen, trắng, đen) và (đen, đen, đen). (*)

> Định nghĩa: 1 chùm là tập hợp các bi cùng màu liên tiếp nhau có độ dài (số phần tử) lớn nhất có thể, màu của chùm là màu của các bi đó.

> Theo nhận xét (*), ta suy ra các chùm màu trắng luôn có độ dài không ít hơn 2. Mặt khác nếu có 1 chùm có độ dài lớn hơn 2 thì ta có ngay kết luận bài toán là đúng. Vậy các chùm trắng luôn bằng 2 suy ra số bi trắng là chẵn. (mâu thuẫn)

> *Ngoài lề: Giáo sư Hưng ơi! Em là học sinh du học mới qua mĩ học undergraduate, 1st semester, chuyên ngành CS. Em có 1 số thắc mắc về cách học, có thể trao đổi với giáo sư qua mail được không ạ?

> 0

> 0

**1001001** · 04/04/2009 at 8:39 pm

> Bài 82 em thấy hơi giống 1 bài IMO năm nào đó?

> Chắc là không tồn tại và cách chứng minh là xét 1 thuần biến nào đó?

> 0

> 0

**1001001** · 05/04/2009 at 6:18 am

> 81. Gọi P(n) là mệnh đề được phát biểu bởi bài toán.

> Ta chứng minh bằng qui nạp P(n) đúng.

> P(1), P(2) đúng

> Giả sử P(n) đã đúng, ta chứng minh P(n+1) đúng.

> Gọi n+1 số thực trên vòng tròn theo thứ tự chiều kim đồng hồ là a[1], a[2]… a[n+1]. (Ta qui ước a[n+1+i]:=a[i] với i thuộc {1,…n+1})

> Gọi k là chỉ số thỏa mãn a[k]>=0. Mệnh đề P[n] đúng cho dãy (a[1], a[2]…a[k-1], a[k]+a[k+1], a[k+2]..a[n+1]) (a[1] và a[n+1] có thể không tồn tại) tức tồn tại h sao cho:

> a[h]>=0

> a[h]+a[h+1]>=0

> …

> a[h]+….+a[k-1]>=0

> và a[h]+…+a[k]>=0 (vì a[k]>=0)

> a[h]+….+a[k]+a[k+1]>=0

> a[h]+…+a[h+n]>=0

> Vậy P[n+1] đúng. Ta có đpcm.

> 0

> 0

**3cham** · 31/05/2010 at 2:47 pm

> 82. Nhận thấy sau mỗi phép đổi tổng của vòng tròn không đổi. Do vậy ta đặt các số vào vòng tròn sao cho tổng vòng tròn là số âm. Như vậy, sau mỗi phép biến đối, tổng của vòng tròn luôn luôn là 1 số âm, tức là luôn tồn tại 1 vị trí i sao cho a[i] < 0. Vậy ta có thể biến đổi vô hạn.

> 0

> 0

## Bài [30] — 17 bình luận

**Tuấn Anh** · 30/01/2009 at 3:09 pm

> Em xin trả lời câu 1.

> Có 15 cái túi, mỗi túi đựng số viên sỏi khác nhau, cho nên minimum sẽ là đựng lần lượt 0, 1, 2, …, 14. Như thế phải có ít nhất 14 viên sỏi được dùng. Bây giờ ta cho mỗi túi đựng 1 viên trừ túi thứ nhất. Sau đó làm như sau: lấy túi 1 bỏ vào trong túi 2, lấy túi 2 bỏ vào trong túi 3, … túi 14 bỏ vào trong túi 15. Như thế số viên sỏi trong các túi lớn sẽ được cộng dồn từ các túi nhỏ và tạo thành dãy 0, 1, 2, …, 14 (túi 1 đựng 0 viên, túi 2 đựng 1 viên, túi 3 đựng 2 viên gồm của chính nó và của túi 2, …, túi 15 đựng 14 viên gồm của chính nó và các túi trước). Vậy cần nhỏ nhất 14 viên sỏi.

> 0

> 0

**Hoàng** · 30/01/2009 at 8:04 pm

> Lâu rồi mới thấy anh Hưng đăng các câu hỏi phỏng vấn

> Câu 1 Tuấn Anh giải khéo léo quá!

> Câu 2, A rải luôn một vệ sĩ nằm trùng với B thì B có bị “tịt ngòi” luôn không nhỉ?

> 0

> 0

**Ngô Quang Hưng** · 31/01/2009 at 11:43 am

> @ Tuấn Anh: chính xác!

> @ Hoàng: nếu vệ sĩ đặt ở B thì tia laser không “đi qua”, và vì thế không bị chặn.

> 0

> 0

**Tuấn Anh** · 31/01/2009 at 6:31 pm

> Câu 2 em giải thế này:

> Kí hiệu các mặt phẳng chứa cạnh hình vuông là MP1, MP2, MP3, MP4, MP5 (trùng với MP1), … MP(n) trùng với MP(n mod 4). Gọi B1 là đối xứng của B qua MP1, B2 là đối xứng của B1 qua MP2, … B(n) là đối xứng của B(n-1) qua MP(n).

> Như thế ta có cách xây dựng 1 tia phản xạ n lần từ B bắn trúng A như sau: Nối A với B(n) cắt MP(n) tại điểm C(n), nối C(n) với B(n-1) cắt MP(n-1) tại C(n-1), …, nối C2 với B1 cắt MP1 tại C1, khi đó tia sáng từ B chiếu tới C1 sẽ bị phản xạ tới C2, C3, … C(n) và tới A.

> Theo cách xây dựng trên, ta chỉ quan tâm tới hướng của tia cuối cùng, tức B(n) tới A. Nếu ta chỉ ra được 1 dãy các điểm B(k) sao cho số các hướng của từng điểm tới A là vô hạn và không trùng nhau thì điểm A sẽ không cách nào phòng bị được.

> Để ý rằng 2 lần phép đối xứng trục bằng 1 phép đối xứng tâm, 2 lần đối xứng tâm được 1 phép tịnh tiến. Như thế tức sau 4 lần đối xứng trục ta có 1 phép tịnh tiến. Nghĩa là điểm B4 là tịnh tiến của B, B8 là tịnh tiến của B4, … Lưu ý luôn là vecto tịnh tiến bằng 2 lần đường chéo của hình vuông. Do đó các điểm B(4k) sẽ nằm cách đều nhau trên 1 đường thẳng.

> Từ đây suy ra, nếu A không nằm trên đường thẳng qua B và song song với đường chéo chứa vecto tịnh tiến đó thì các đường nối A với các điểm B(4k) sẽ có hướng khác nhau, suy ra A sẽ bị bắn chết. Nếu A nằm trên đường thẳng đó, thì ta chỉ cần thay đổi thứ tự các MP đối xứng, thay vì MP1, MP2, … sẽ là MP2, MP3, …, lúc này nhận được các điểm B(4k) nằm trên đường thẳng song song với đường chéo còn lại, nên A cũng sẽ bị xử vì không nằm trên đó.

> Chỉ còn trường hợp cuối cùng, khi A nằm cùng lúc trên cả 2 đường thẳng đó, tức là trùng với B. Bài toán trở thành liệu điểm B có bảo vệ được chính mình?

> Trường hợp này em chưa xử lí được, nên nhờ mọi người giải quyết nốt.

> 0

> 0

**Đức** · 16/02/2009 at 3:47 am

> Câu 83 và câu trả lời của Tuấn Anh lại một lần nữa được xử lý theo “kiểu Trạng Quỳnh”. Ai cũng biết đơn giản thì số sỏi ít nhất sẽ là: 0+1+2+…+14. Theo câu trả lời của TA, nếu như các túi không lồng được vào nhau thì sao?

> Thiết nghĩ, những câu hỏi thế nào ko nên đưa lên blog KHMT.

> 0

> 0

**trungkstn** · 17/02/2009 at 7:52 pm

> Coi các cạnh là gương phẳng.

> Ảnh của A qua các gương là vô số nên B có vô số hướng để bắn trúng A. Do đó không thể đặt một số hữu hạn các vệ sỹ được.

> Em nghĩ là thế

> 0

> 0

**Trung T. Nguyen** · 18/02/2009 at 7:04 am

> Bác Đức ơi,

> Tôi mà là manager đi phỏng vấn tuyển programer, nếu tôi lấy lời giải chuẩn là cái “ai cũng biết là đơn giản” ấy thì thằng programer giỏi nó sẽ coi thường công ty tôi. Thế mới là KHMT. Bao giờ lời giải này đăng trên blog kiểm toán hay hành chính công bác chỉ trích cũng chưa muộn.

> 0

> 0

**bolzano_1989** · 18/02/2009 at 7:55 am

> Đáp án câu 83 như bạn Tuấn Anh rõ ràng không thỏa mãn trong mọi trường hợp .

> @Trung T. Nguyen : Cho em hỏi là chả nhẽ sĩ diện công ty quan trọng hơn mục tiêu kiếm programer giỏi sao ?

> 0

> 0

**Ngô Quang Hưng** · 18/02/2009 at 8:42 am

> Hà hà,

> Một số bác có vẻ không “hài lòng” với câu trả lời này nhỉ? Trong ngữ cảnh của một cuộc phỏng vấn thì rất đơn giản: người được hỏi có thể hỏi ngược lại rằng “các túi có lồng vào nhau được không?” và các câu hỏi tương tự.

> Còn nếu cần “thỏa mãn trong mọi trường hợp” thì đáp án 1+…+14 cũng không đúng. Nhỡ mỗi viên sỏi to bằng quả núi thì sao

> Bản thân câu trả lời là gì không quan trọng bằng việc mình xử lý tình huống, giải quyết vấn đề như thế nào.

> 0

> 0

**Trung T. Nguyen** · 18/02/2009 at 1:17 pm

> bolzano_1989

> Thằng programmer giỏi không bao giờ nghĩ là nhỡ cái túi thế này cái túi thế khác nên lời giải này sai ta đừng đưa ra nữa. Chỉ có thằng kiểm toán giỏi hay thằng chuyên duyệt giấy phép xây dựng giỏi mới hay cứng nhắc thế thôi. Như bác Hưng đã viết, mấy cái bài này không chủ yếu nhằm xem thằng nào suy luận như parser, mà xem thằng nào có năng khiếu giải quyết vấn đề.

> 0

> 0

**bolzano_1989** · 18/02/2009 at 8:28 pm

> Cảm ơn mọi người .

> 0

> 0

**Đức** · 19/02/2009 at 2:11 am

> @bác Hưng: sỏi nào to bằng quả núi nhỉ? Thường thì khi ra bài toán, sẽ có một số assumption mà người ra đề và người giải đã ngầm thoả thuận. Ngược lại, việc ra đề sẽ mất rất nhiều câu để định nghĩa mọi thứ.

> @bác Trung: em thấy thằng programmer nào mà nó xử lý theo kiểu “trạng Quỳnh” là em cho điểm trừ ngay. Bác muốn “cty ko bị coi thường” thì ra câu khác hơn, đánh vào khả năng của programmer.

> Cuối cùng, vì đây là câu hỏi phỏng vấn nên có thể nói trả lời vô tội vạ, chủ yếu là cách nói như thế nào, tâm lý của interviewer thôi.

> Chúc các bác sức khoẻ.

> 0

> 0

**Hà Quang Hồng** · 03/11/2009 at 12:52 pm

> Câu hỏi này được hỏi ở phỏng vấn nào đấy ạ?VÀ đáp án cuối cùng là gì?Anh Hưng ghi câu hỏi mà chẳng đưa ra được câu trả lời khiến mọi người tâm phục gì cả!

> 0

> 0

**Ngô Quang Hưng** · 03/11/2009 at 2:00 pm

> Tôi sưu tầm câu hỏi không phải là để khoe mình thông thái, và cũng không phải để thách thức ai cả. Các bạn thấy thú vị thì nghĩ lời giải và bàn luận, không thì thôi. Tại sao lại phải tâm phục khẩu phục gì?

> 0

> 0

**Hà Quang Hồng** · 03/11/2009 at 2:16 pm

> Vấn đề ở đây chỉ là cách diễn đạt và cách hiểu thôi. Mục đích của cuối của em vẫn là biết được câu trả lời chính xác của câu hỏi đó. Phải chăng câu hỏi đó chỉ để kiểm tra khả năng phản biện cách trả lời và việc giải thích được cách trả lời một cách hợp lý không ạ?

> 0

> 0

**Hà Quang Hồng** · 03/11/2009 at 2:28 pm

> Em vừa đỗ cao học máy tính ĐHQG hà Nội, Đăng kí chuyên nghành KHMT. Đăng kí học xong thì mấy thằng bạn bảo là không nên học nghành này vì nghành này được đào tạo theo chuẩn quốc tế, học rất vất vả và tính ứng dụng của nó không cao lắm vì vậy mà sẽ không có nhiều thời gian để làm ngoài. Thực ra chính vì theo chuẩn QT nên em cũng muốn thử sức mình hơn, mong là sẽ là động lực để mình cố gắng. Nhất là em cũng muốn trình độ tiếng anh của mình sẽ nâng cao hơn. Nhưng cũng đang lo là sở thích của mình sẽ không được vì thứ 7 này không biết có qua được vòng phỏng vấn không.Ai có biết thông tin gì về các câu hỏi của vòng phỏng vấn bên ĐHQG Hà nội ko ạ?

> 0

> 0

**picasa** · 07/11/2009 at 5:05 am

> chú em cứ yên tâm hỏi dễ không ý mà! Trước anh cũng lo như chú nhưng chẳng có gi` cả!

> 0

> 0

## Bài [31] — 2 bình luận

**ZORO_NDK** · 17/11/2009 at 4:50 am

> câu 86 : cho thằng A núp góc của hình vuông và đặt sát trước nó 1 ku vệ sĩ thằng B bắn cỡ nào cũng hok trúng ^^

> ———-

> Huyết Phụng Thần lưu

> 0

> 0

**ZORO_NDK** · 17/11/2009 at 4:52 am

> xin lỗi nhầm hàng đó là câu trả lời của câu 84 ^^

> 0

> 0

## Bài [32] — 10 bình luận

**Khoa Trần** · 04/03/2009 at 3:37 am

> Chào anh Hưng, em giải thử bài 87: dùng logarithm để tìm vị trí bit cao nhất

> int significant_place(uint32_t x) {

> if (x > 0) {

> return ln(x) / ln(2);

> }

> return -1;

> }

> 0

> 0

**sontran** · 04/03/2009 at 3:56 am

> 87.

> if (x==0) return -1;

> ulong index=31;

> while ((x&(1UL<<31))==0) {–index; x<<=1;} return index;

> 0

> 0

**James Duy Trinh** · 04/03/2009 at 11:56 pm

> Cách của Khoa hay đấy

> tìm số mũ của x theo cơ số 2 = log (x) theo cơ số 2 = ln (x) / ln (x). Chạy sẽ nhanh.

> 0

> 0

**Nguyen Phuc Son** · 06/03/2009 at 8:26 am

> amortized cost la gi a ?

> 0

> 0

**Ngô Quang Hưng** · 06/03/2009 at 8:35 am

> Hi Sơn, xem ở đây. Đại khái, bất kể ta enqueue và dequeue thế nào, thì thời gian cần cho mỗi tác vụ (enqueue/dequeue) là hằng số, tính trung bình.

> 0

> 0

**XXX** · 09/03/2009 at 10:57 am

> Câu 89 là câu lấy từ cuốn Introduction to Algorithms ra, solution thì quá obvious, sao bọn Bloomberg lại interview dễ thế nhỉ.

> 0

> 0

**Tên: (bắt buộc)** · 11/03/2009 at 5:49 am

> Oh, my god! I don’t know how to do if i get those questions!

> 0

> 0

**minhdoan** · 15/03/2009 at 5:50 pm

> Mình có bài này rất nice, share mọi người làm cho fun.

> Bạn có 1 array[0..n-1], (n>=2). Hãy tìm max gap với amortized cost là O(n). Định nghĩa max gap có thể hiểu như sau:

> sort(a, a+n);

> maxgap=a[1]-a[0];

> for i:1-(n-1) maxgap >?= a[i]-a[i-1];

> return maxgap;

> Cheers,

> 0

> 0

**Hùng Phan** · 30/03/2009 at 12:54 am

> Hi anh Hưng, cám ơn anh Hưng đã recommend cuốn Beautiful code, em rất thích đọc những cuốn sách “explain how they think”

> 0

> 0

**langlv** · 24/02/2010 at 9:05 pm

> Hi, em không hiểu lắm cách của anh Khoa.

> Nếu t là vị trí bit cao nhất thì 2^t = x nếu x chỉ có 1 bit 1. Còn nếu x có nhiều bit 1 thì sao ạ ?

> 0

> 0

## Bài [33] — 14 bình luận

**Thu Huong** · 14/01/2010 at 10:22 am

> Cho em hỏi là với câu hỏi số 91 có phải ta sẽ tìm được trong O(n) với suffix tree đúng ko a?

> 1

> 0

**thichhoctoan** · 15/01/2010 at 7:10 am

> 90 : 1h.

> 4

> 0

**Ngô Quang Hưng** · 15/01/2010 at 7:24 am

> Hòa Thượng: 1h đúng là chặn trên tốt nhất có thể có nếu không còn thông tin nào khác.

> Tuy nhiên ta có thể có câu trả lời chính xác luôn nếu cho cả vị trí từng con và chiều (trái/phải) mà từng con kiến chọn. Trong trường hợp đó, bọn kiến có thể rơi trước 1 h.

> 0

> 0

**pandarbear** · 15/01/2010 at 8:48 am

> Để PB thử trả lời câu 90 xem nhá:

> Nếu các chú kiến đi cùng chiều thì không quá 1h các chú sẽ rơi xuống hết. Bây giờ xét 1 chú kiến đi ngược chiều với các chú còn lại. Khi chú này gặp chú đi ngước chiều đâu tiên, theo đề bài hai chú này sẽ đổi chiều. Giả sử kiến A đi từ bên trái qua bên phải, kiến B đi từ bên phải qua bên trái, thế thì khi gặp nhau A về bên trái, B về bên phải. Tuy nhiên về bản chất hai chú kiến là không phân biệt nếu ta thêm giả sử ở thời điểm gặp nhau ta không nhìn thấy chúng đụng độ, A vẫn đi tới đầu bên phải, B vẫn đi tới đầu bên trái. Tương tự xét cho một chú kiến bất kỳ trong đoàn ta thấy không quá 1 h tất cả sẽ rơi xuống đất.

> PB xin phép đưa thêm câu hỏi phụ, trong trường hợp có đụng độ hỏi có tối đa bao nhiêu đụng độ có thể xảy ra ?

> 6

> 0

**hung** · 07/01/2014 at 3:01 pm

> lúc đó tụi nó đã đi ngủ hết rồi

> 0

> 0

**thichhoctoan** · 15/01/2010 at 1:20 pm

> Bác Văn cấp cho mỗi con kiến một cái mũ đánh số từ 1 đến mười. Khi hai con kiến đụng độ nhau, thay vì đổi hướng, hai con kiến sẽ đổi mũ cho nhau. Trong bài toán mới này, hiển nhiên sau một giờ, cả mười con Kiến đều rơi vào mồm bác Văn đã há sẵn. Nếu có đo đạc trước, bác Văn còn có thể há mồm đúng lúc chúng rụng, khỏi bị bệnh há miệng mắc quai. Bài toán này dễ hơn bài cũ vì kiến chỉ đổi mũ, không đổi hướng. Để tìm lại bài cũ, ta chỉ cần xác định hoán vị đổi mũ. Hoán vị này còn được phân tích thành tích của các chuyển vị (transposition) tương ứng với các vụ đụng độ. Độ dài tối đa của một hoán vị là n(n-1)/2 trong trường hợp có n con kiến. Nhưng trong bài toán này, vì có một số kiến đi sang phải, một số đi sang trái, trong mỗi nhóm không chuyển vị với nhau, nên số lần đụng độ tối đa sẽ là $n^2/4$ nếu số kiến n là chẵn, và $(n^2-1)/4$ nếu n lẻ. Bác Văn thì không quan tâm lắm đến hoán vị, miễn là cả đàn kiến chui vào mồm là được.

> 2

> 0

**Duy** · 15/01/2010 at 5:51 pm

> 90:

> Tối thiều là tồng chiều dài của 10 con kiến (m) chia cho 1 (h) .

> Ví dụ: chiều dài một con kiến ~ 0.001 (m) x 10 con kiến ~ 0.01 (m) / 1 h ~ 0.01 (h).

> Tối đa là gần một giờ ~ 1 (h).

> 0

> 0

**Ngô Quang Hưng** · 15/01/2010 at 8:11 pm

> @Duy: độ dài các con kiến bằng … 0

> @Pandabear & Hòa Thượng: câu trả lời của PB và bác Hòa Thượng dĩ nhiên là chính xác. Quan sát mấu chốt là chỉ cần đổi tên kiến khi 2 con đụng nhau.

> Câu hỏi thêm rất hay của PB thì Hòa Thượng đã cho câu trả lời vừa rất đại số vừa rất tổ hợp, thật thú vị. Cảm ơn!

> @Hòa thượng: chắc bác muốn nói “chuyển vị kề” (adjacent transpositions), hay là tôi nhớ thuật ngữ không chuẩn.

> 0

> 0

**Duy** · 19/01/2010 at 7:37 am

> @Hưng: độ dài các con kiến có thể xem bằng 0 nếu như cái que dài hơn 1m gấp nhiều lần. Vì có nhiều loại kiến mà chiều dài của nó có thể lên đến 3-5cm!

> http://www.bbc.co.uk/nature/wildfacts/factfiles/3086.shtml

> Kiến ở New England này trung bình là 1cm

> 0

> 0

**Duy** · 19/01/2010 at 8:04 am

> 91: Lý thuyết thì dễ nhưng thực tế thì khó hơn nhiều khi mà chiều dài của chuỗi tăng lên đáng kể.

> Có một bài tương tự trên TopCoder cách đây vài năm (StringSearch)

> http://www.topcoder.com/longcontest/?module=ViewProblemStatement&rd=9958&pm=6164

> Có nhiều lời giải thực tế (practical approaches) thảo lụân khá hay:

> http://forums.topcoder.com/?module=Thread&threadID=510371&start=0

> 0

> 0

**Ngô Quang Hưng** · 21/01/2010 at 9:05 pm

> Cảm ơn anh Duy cho mấy cái links về bài String Search rất hay.

> 0

> 0

**Hoang Ha** · 22/01/2010 at 8:08 pm

> 92. Neu dung` loai xe freestyle, truc banh xe truoc co the vuong goc voi truc than xe. Dieu nay tao ra vet xe banh truoc la 1 vong tron va banh sau la mot diem. Vay it’ nhat thi dien tich can tim phai phu thuoc vao khoang cach cua 2 cai tam cua 2 banh xe –> phu thuoc vao` khung cua xe dap.

> 0

> 0

**BinhMinh** · 24/01/2010 at 5:08 am

> ở đây có rất nhiều bài toán/lời giải để practice. xin lỗi vì nó ko liên quan gì đến 3 bài toán ở trên

> http://code.google.com/codejam/

> 0

> 0

**convit** · 26/01/2010 at 12:40 am

> Theo tôi thì bài toán 91 là bài toán classical được biết đến với tên gọi là Longest Common Subsequence có thể Google để tìm thấy một số tài liệu nói về độ phức tạp của bài toán này và phương pháp dynamic programming để giải nó. Tôi thích bài toán 90 nhất vì nó phù hợp với các cuộc phỏng vấn kiểm tra trí tuệ hơn là kiến thức.

> 0

> 0

## Bài [34] — 6 bình luận

**Duy** · 03/02/2010 at 9:46 am

> 94: Yes, I can. Actually, everyone can

> Câu này không cần áp dụng lý thuyết toán học hay vật lý, chỉ cần dùng “giác quan” là có thể rút ra được nguyên lý của vấn đề…

> 0

> 0

**Sinh** · 03/02/2010 at 7:41 pm

> Hi anh Hưng,

> 1) Câu 93: có phải đáp án là 1/2?

> – Nếu Tèo ngồi vào đúng số ghế dành cho Tèo, thì chắc chắn người từ thứ 2 cho đến người cuối cùng (thứ 100) cũng sẽ ngồi đúng số ghế của mình.

> – Nếu Tèo ngồi vào số ghế của người thứ 100, thì bất kể những người tiếp theo ngồi như thế nào, chắc chắn người thứ 100 sẽ không thể ngồi vào số ghế của mình.

> – Nếu Tèo ngồi vào bất kì ghế nào khác hai ghế này, không giảm tổng quát, giả sử đó là số ghế của hành khách thứ i. Trong trường hợp này, tất cả những hành khách từ thứ 2 trở đi đến thứ (i – 1) sẽ ngồi đúng ghế của mình. Hành khách thứ i nếu chọn ngồi ghế số 1 thì chắc chắn người từ thứ (i + 1) trở đi cho đến người cuối cùng thứ 100 sẽ ngồi đúng số ghế của mình; còn nếu anh ta chọn ngồi ghế của người thứ 100, thì chắc chắn người thứ 100 không thể ngồi đúng ghế của mình. Nếu anh ta chọn ghế khác hai ghế này (thứ 1 và 100), giả sử là thứ j, vì ghế của người từ thứ 2 đến người thứ i đã được ngồi, nên j trong sẽ là ghế của một người từ thừ (i +1) đến thứ 100. Đến đây có thể coi vai trò của hành khách thứ i bây giờ giống như của Tèo lúc đầu nhưng với số ghế còn lại tính từ của người thứ (i + 1) đến người thứ 100. Cứ tiếp tục như vậy…

> Mỗi sự kiện xảy ra đều cho ra xác xuất để người cuối cùng có thể ngồi đúng ghế của mình là 1/2 => đáp án là 1/2.

> 2) Câu 94: có phải nếu làm theo cách “naive” thì sẽ thành công trong một nửa số lần thử (xác suất thành công là 1/2), nhưng chỉ cần biết trick thì thành công 100%? Nhờ hint của giáo sư Gil ở cuối video và…đáp án bài 93 mà có vẻ như em đã tìm ra được trick này.

> Cảm ơn anh Hưng vì đã ghép hai bài toán rất thú vị này lại (đều liên quan đến xác suất 1/2?).

> 0

> 0

**66.4.44.444** · 03/02/2010 at 7:59 pm

> 93. Bai nay la xich Markov.

> 0

> 0

**Ngô Quang Hưng** · 03/02/2010 at 8:05 pm

> Hello Sinh, đáp án chính xác. Có thể lý luận gọn hơn một chút mà không cần nhiều conditional probabilities như thế. Dùng ý tưởng tương tự như ý tưởng đổi tên kiến của bài đố kiến của bác Văn.

> 0

> 0

**Tuấn** · 04/02/2010 at 12:59 am

> Thay số 100 bằng số tự nhiên n Yêu cầu tương tự như của anh Hưng.

> Tính P(n).

> n=1 –> P(1)

> n =2 –> P(2) =1/2

> n>2: P(n)=1/n + 1/n*P(n-1) +1/n*p(n-1) +…. + 1/n*P(2)+1/n*0

> (qui nạp) —-> P(n) = 1/2 với mọi n>1

> 0

> 0

**pandarbear** · 04/02/2010 at 3:18 am

> Câu 93: PB thử diễn giải thế này cho bài 93

> Có 100 viên bi được đánh số từ 1 đến 100 được bỏ trong hộp đen. Luật chơi như sau. Người chơi bốc một viên bất kỳ. Nếu viên đó là số 1 thì người chơi thắng. Nếu Viên đó là 100 thì người chơi thua. Bốc các viên khác thì loại khỏi hộp, rồi bốc tiếp cho đến khi xác định người chơi thắng hay thua. ==> xác suất thắng là 1/2.

> 0

> 0

## Bài [35] — 11 bình luận

**Pham Tuan Vu** · 26/05/2010 at 7:42 pm

> 95. Gọi Smax là tổng giá trị tuyệt đối các phần tử ban đầu.

> Ở mỗi bước ta chọn hàng, hoặc cột có tổng S nhỏ nhất. Nếu S >= 0 thì không tồn tại hàng/cột âm, ta kết thúc thuật toán. Nếu S < 0 ta đổi dấu và tổng các phần tử của ma trận sẽ được tăng thêm 2*|S|.

> Do tổng các phần tử của ma trận không thể vượt quá Smax, nên số bước luôn hữu hạn (không thể lớn hơn 2xn). Vì vậy thuật toán trên đảm bảo đạt đến trạng thái không có hàng/cột âm.

> 2

> 0

**Pham Tuan Vu** · 26/05/2010 at 8:06 pm

> 97. Gọi f(m, n) là số bước bẻ thanh sô-cô-la m x n (m, n >= 1). Ta chứng minh f(m, n) = m x n – 1 (*).

> f(1, 1) = 0. Giả sử (*) đúng với mọi (m’, n’) < (m, n) (nghĩa là m’ < m hoặc m’ = m và n’ < n).

> Với mọi m’ (1 <= m’ < m), ta có 1 + f(m’, n) + f(m – m’, n) = m x n – 1.

> Với mọi n’ (1 <= n’ < n), ta có 1 + f(m, n’) + f(m, n – n’) = m x n – 1.

> Vậy f(m, n) = m x n – 1, không phụ thuộc cách bẻ.

> 0

> 0

**bachbk** · 27/05/2010 at 8:29 am

> 96. Hình như là liên quan tới định lý mặt cầu tóc của tô pô. Thêm nữa là đặc trưng Euler.

> 0

> 0

**Duc** · 27/05/2010 at 5:15 pm

> 97. Số miếng tối đa: mxn. Mỗi lần bẻ tổng số miếng tăng lên 1, vậy cần mxn-1 lần bẻ, bất kể thế nào.

> 0

> 0

**Katatunix** · 28/05/2010 at 9:39 pm

> Hi all,

> Về bài 96, dùng đặc trưng Euler là đủ: F + V = E + 2 (*).

> Phản chứng, giả sử lũ kiến đều bò về đích mà ko đụng nhau, ta có:

> – Khi lũ kiến về đích, cho chúng bò ngược lại với vận tốc biến thiên ngược lại lúc trước, thì cũng sẽ về đích mà ko đụng nhau (1).

> – Trên mỗi cạnh, luôn có đúng 2 con kiến bò trên đó ngược chiều nhau (tất nhiên là ko bò đồng thời) (2).

> – Tại thời điểm bắt đầu, tồn tại 1 đỉnh mà tất cả các cạnh nối với đỉnh đó đều có kiến. (3). Thật vậy, giả sử ko tồn tại đỉnh nào như vậy. Tức là xét cả V đỉnh thì đỉnh nào cũng có ít nhất 1 cạnh ko có kiến trong số các cạnh nối với đỉnh đó.

> Suy ra tổng số cạnh ko có kiến của cả đa diện là: P >= V * 1 = V.

> Tổng số cạnh có kiến của cả đa diện là: Q = F (số mặt = số kiến)

> Nhưng tổng số cạnh của đa diện lại là: P + Q >= V + F hay E >= V + F (mâu thuẫn với (*)).

> Vậy (3) đúng, từ (2) suy ra các con kiến trên các cạnh nối với đỉnh này đang cùng bò lại gần đỉnh hoặc đang cùng bò ra xa đỉnh. Nếu là ra xa, từ (1) ta có thể cho chúng quay đầu để bò lại gần đỉnh mà ko ảnh hưởng gì.

> Nói vui tí, rõ ràng trong tình huống này các con kiến “tiến thoái lưỡng nan”, ko có con nào dám bò đến đỉnh trước, vì phía cạnh kia luôn có 1 con kiến khác đang chờ “xử” nó.

> Vậy giả thiết phản chứng là sai.

> 0

> 0

**Giang** · 29/05/2010 at 8:58 am

> Lập luận từ việc đỉnh nào cũng có ít nhất một cạnh không có kiến trong số các cạnh nối với đỉnh đó dẫn đến tổng số cạnh không có kiến là P >= V*1 = V là không đúng bởi vì mỗi cạnh không có kiến nối với 2 đỉnh.

> 0

> 0

**Trung** · 29/05/2010 at 9:17 am

> Bài 96 chắc phải có thêm điều kiện chứ cứ cho bọn kiến xếp hàng bò, con này bò xong về đến chỗ xuất phát rồi mới cho con sau bắt đầu bò thì gặp nhau bằng niềm tin à?

> 0

> 0

**Katatunix** · 29/05/2010 at 8:10 pm

> @Giang: bạn nhận xét rất đúng, mình vẫn đang suy nghĩ tiếp. Phải nói bài này khó nhằn thật đấy.

> 0

> 0

**Katatunix** · 29/05/2010 at 8:15 pm

> @Trung: đề bài thế là đúng rồi, vì nếu 1 con kiến về đích thì nó nằm yên ko bò nữa, và như vậy sẽ cản trở con kiến sau, con kiến sau cần phải đi qua cạnh đó rồi thì con kiến trước mới được về đích.

> 0

> 0

**pandarbear** · 01/06/2010 at 7:11 am

> Câu 96:

> PB chứng minh không chặt lắm theo cách thức sau:

> Nhận xét 1:

> Do tất cả các chú kiến di chuyển theo cùng chiều kim đồng hồ, do đó hai chú kiến cùng đi qua một cạnh của đa giác sẽ có chiều ngược nhau. Kết quả là không thể tồn tại hai chú kiến có xuất phát điểm cùng một cạnh đi hết mồt vòng trên mặt đa giác mà mỗi chú chiếm hữu mà không đụng nhau.

> Nhận xét 2:

> Hai chú kiến ở hai mặt kề nhau, giả sử có một chú nằm trên cạnh tiếp giáp của hai mặt. Nếu không đụng nhau sau khi đi hết một vòng thì đường đi của hai chú kiến tương đương đường đi của chú nằm trên cạnh không kế cận trên đường bao của hai mặt.

> Lời giải:

> Xét một đa giác bất kỳ trên đa diện lồi, giả sử đa giác này có n cạnh. Thì số chú kiến tối thiểu sẽ là n + 1 chú. Giả sử n chú không thuộc mặt này sau khi đi hết một vòng không cắt nhau thì đường đi của các chú kiến tương đương với đa giác ấy. Nói cách khác thì n chú kiến không đụng nhau có thể xem tương đương với một chú kiến đi trên đa giác này có chiều ngược chiều kim đồng hồ. Vì thế chú kiến thứ (n+1) thuộc về đa giác trên chắc chắn sẽ đụng độ với chú kiến này.

> 0

> 0

**Lê Khắc Minh Tuệ** · 07/02/2013 at 3:24 am

> Bài 95:

> Tại mỗi bước, tìm một hàng (hoặc cột) bất kì mà tổng của hàng (cột) đó là số âm. Đổi dấu hàng (cột) này lại. Thuật toán này sẽ thực hiện trong hữu hạn bước và sẽ thu được một bảng mà tổng mỗi cột và mỗi hàng đều là số không âm. Thật vậy: tại mỗi lần đổi dấu hàng (cột) từ âm sang dương, tổng tất cả các số trên bảng sẽ tăng (tăng chặt). Mà ta thấy: tổng tất cả các số trên bảng bị chặn trên bởi một giá trị là tổng trị tuyệt đối tất cả các số trên bảng. Như vậy thuật toán sẽ thực hiện trong hữu hạn bước. Mà thuật toán này chỉ dừng lại khi không thể tìm thấy hàng hoặc cột nào có tổng là âm. Như vậy, khi thuật toán dừng lại, tất cả các hàng và cột đều có tổng không âm.

> 0

> 0

## Bài [36] — 7 bình luận

**duc** · 29/06/2010 at 11:29 pm

> Câu 98. Tôi nghĩ là không. Ví dụ đồ thị có 2 đỉnh và 1 cạnh.

> 0

> 0

**duc** · 30/06/2010 at 12:39 am

> - Đáp án trước là sai (tôi tưởng là bắt đầu với 1 trạng thái bất kỳ).

> – Nếu bắt đầu với trạng thái tất cả bóng đền đều tắt ta chỉ việc tới mỗi đỉnh bậc chẵn chuyển công tắc một lần là có thể bật được tất cả các bóng.

> 0

> 0

**Nhanh** · 30/06/2010 at 3:56 am

> Duc: vẫn sai.

> 0

> 0

**Mèo** · 30/06/2010 at 9:28 am

> Câu 98: Ta làm thế này ạ. Đánh số các đỉnh là 1, 2, …, N . Tại mỗi đỉnh k, tập hợp các đỉnh kề k cộng thêm chính k, ký hiệu là A(k). Ta cần tìm tập hợp S là tập con của 1, …, N có tính chất, ta gọi là tính chất M: giao của S với A(k) bất kỳ có số phần tử là lẻ. Ta đếm số các tập không như thế, nghĩa là số những tập S mà tồn tại đỉnh k để giao của S với A(k) là chẵn. Ta có thể đếm và chứng minh là số tập S như vậy không vượt quá 2^N – 1 (cái này không khó lắm, chỉ là em gõ công thức toán ở đây không được). Tập 1, .., N có 2^N tập con, vậy tồn tại tập con có tính chất M.

> Ta bấm lần lượt các công tắc của tập S đó lên, sẽ làm sáng tất cả các bóng đèn.

> 0

> 0

**Hieu M Nguyen** · 22/08/2010 at 10:36 am

> Câu 98 :

> Nhận xét 1: Nếu bài toán có nghiệm thì với mỗi công tắc tại 1 đỉnh chỉ cần bật 1 lần hoặc không bật lần nào (không cần bật/tắt quá 1 lần).

> Nhận xét 2:

> Với mỗi đỉnh u ta gọi số lần bật/tắt đèn tại đỉnh u đó là C(u) ( C(u) nhận 2 giá trị 0 hoặc 1 tương ứng vào nhận xét 1).

> Ta có trạng thái đèn tại đỉnh u sau khi dừng hết quá trình bật/tắt sẽ là C(v1) xor C(v2) xor C(v3) … xor C(u) = G(u)

> với v1, v2, v3 … là các đỉnh kề với đỉnh u và G(u) = 1 nếu đèn tại u sáng và = 0 nếu đèn tại u tối.

> Ban đầu các đèn đều tối hết và mục tiêu là để các đèn sáng hết –> G(u) sẽ phải = 1 với mọi u.

> Từ 2 nhận xét trên ta quy bài toán này về bài toán giải hệ phương trình nhị phân bậc nhất N ẩn, có thể giải = khử Gauss.

> Hệ PT có dạng

> C(v1,1) xor C(v1,2 ) xor … xor C(v1,k1) xor C(1) = 1

> …

> C(vn,1) xor (Cvn,2) xor … xor C(vn,kn) xor C(n) = 1

> Cấp độ của thuật toán là O(N^3).

> 0

> 0

**Hung** · 18/11/2010 at 2:59 pm

> Cau 100:

> Binh thuong khi 2 phieu YY / NN canh nhau thi se stable (khong bao gio thay doi trang thai). Neu co mot phieu ben canh, ma phieu do (gia su la Y) nam giua 2 phieu khac loai (tuc la NYNN hoac NNYN) thi phieu Y do se bi convert thanh N va sau do khong thay doi trang thai nua. Nhu vay vung cac phieu giong nhau lien ke nhau se expand neu ben canh co 1 phieu khac loai bi co lap. Cuoi cung ca ban tron se stable khi khong con phieu co lap nao nua.

> Co 1 truong hop ngoai le co ve nhu bai toan sai. Do la khi cac phieu nhan gia tri alternative YNYN. Sau moi luot tat ca cac phieu deu doi gia tri, va se cu nhu vay khong bao gio dung lai.

> 0

> 0

**T** · 18/11/2010 at 6:56 pm

> @Hung: Truong hop ngoai le ban noi’ khong xay ra, vi chung’ ta co’ mot so le? cac’ cu. nghi. gat. ^^

> 0

> 0

## Bài [37] — 47 bình luận

**RongChoi** · 23/11/2010 at 5:59 pm

> Theo cách cực đoan hóa, thay các số phức tạp bằng trường hợp đơn giản nhất (13 bằng 1 trong câu 101, 23 bằng 1 trong 102) thì hình như có thể tìm ra lời giải…

> 101. Nếu chỉ có 1 lá ngửa thì chỉ cần chia bộ bài 2 phần, 1 phần 1 quân và 1 phần 53 quân. Lật lá bài trong phần 1 quân thì dẫn đến 2 nửa cùng 1 quân ngửa khoặc cùng 0 quân ngửa Nếu chỉ có 2 lá ngửa thì làm tương tự cưng được … 13 lá ngửa thì cũng tương tự: chia 2 phần, 1 phần 13 quân, 1 phần 41 quân rồi lật tất cả các quân trong phần 13 quân.

> 102. Thay 23 bằng 1. Nếu chỉ có 1 người mắt xanh thì do anh ta thấy tất cả mắt nâu, anh ta sẽ suy ra mình mắt xanh và nửa đêm đó tự tử. Nếu có 2 người mắt xanh thì do họ nhìn thấy có người khác mắt xanh nên đêm đầu ngủ ngon. Nhưng sáng ra thấy cái ông mắt xanh kia cũng ngủ ngon mà chưa tự tử thì suy ra là không chỉ có ông ta mắt xanh (nếu thế ông ta đã tự tử như trường hợp đầu). Từ đó 2 người mắt xanh đều suy ra mình cũng mắt xanh và đêm đó cầm tay nhau xuống địa ngục. Lý luận như vậy thì nếu có 23 người mắt xanh thì sau 22 đêm tất cả vẫn vui vẻ nhưng đến đêm 23 tất cả họ đều tự tử vì luận ra mình cũng mắt xanh.

> 103. Chắc ST phải chơi trò dồn cô dâu vào chân tường Các phòng thông nhau không biết ST gõ cửa 1 phòng thì có nhìn trộm sang 2 phòng bên cạnh được? Cứ coi là có cho dễ

> Nếu vậy thì khi nào ST nhìn thấy MN ở phòng bên cạnh thì sẽ có thể dồn được. Giả sử ST đã thấy MN ở phòng bên cạnh, bên trái chẳng hạn. Thế thì đêm sau ST vẫn gõ phòng cũ, một là trúng đích, hai là biết chắc MN cách 2 phòng về phía trái; đêm sau dời sang 1 phòng về phía trái thì lại là một trúng hai là lại suy ra được MN cách 2 phòng về bên trái. Mỗi đêm dịch về phía trái 1 lần. Dồn mãi như vậy đến khi MN ko di chuyển về bên trái nữa thì buộc phải rơi vào bẫy của ST. Tổng cộng nhiều nhất là 17 đêm sẽ tóm được MN.

> Còn 13 đêm để ST tìm cách để biến cái “giả sử” trên kia thành sự thật, tức là nếu ko tóm được thì cũng nhìn thấy MN ở phòng cạnh bên. Đầu tiên ở phòng 1, nếu không thấy MN ở phòng bên cạnh thì đêm sau nhảy sang gõ phòng 3, nếu ko thấy MN ở phòng 2 hay 4 thì hôm sau nhảy sang phòng 5… như vậy cho đến phòng 17 sẽ tóm được hoặc thấy MN phòng bên cạnh. Nhưng mà như vậy thì chỉ cần 9 đêm thôi? Cộng thêm 17 đêm phía trên kia thì mới có 26 đêm? Có gì sai ko nhỉ?

> Trường hợp nếu ST không nhìn trộm sang các phòng bên cạnh được thì … chưa nghĩ ra. Sợ nhất ST gõ 1 phòng, MN ở phòng bên cạnh, hôm sau di chuyển sang trái MN di chuyển sang phải thì không dồn được. Chắc phải làm cách nào để biết MN ở cách ít nhất 2 phòng? 1 đêm dịch, một đêm không dịch? nhưng hình như cũng không được.

> Hay phụ thuộc tính chẵn lẻ? Giả sử MN ở cách 1 số các phòng chẵn. Như vậy ST dồn dần từ phòng 1 đến phòng 17. Mỗi ngày ST dịch 1, MN dịch 1 nên khoảng cách vẫn chẵn, tối đa 15 đêm sẽ bắt được? Nếu sau 15 đêm ko bắt được thì có nghĩa ST suy ra khoảng cách là lẻ, thế thì 1 ngày không thay đổi phòng để cho khoảng cách là chẵn rồi lại dồn, thêm 15 đêm nữa? Hình nhũ như vậy là được? Chắc tính cẩn thận sẽ ra 30

> (Sorry mọi người vì vừa nghĩ lẩn thẩn vừa viết ra luôn nên ý tứ lộn xộn)

> 1

> 0

**Tuong Vinh** · 26/11/2010 at 2:14 am

> Đối với câu 102, em có thắc mắc đối với trường hợp 2 người mắt xanh, nếu ngày thứ 2 vẫn còn thấy người mắt xanh thì em nghĩ những người mắt nâu cũng phải có cái suy nghĩ tương tự người mắt xanh còn lại, Dẫn đến là cả làng tự tử thì mới đúng chứ ạ???

> 0

> 0

**RongChoi** · 26/11/2010 at 6:04 am

> Nếu có 2 người mắt xanh: ở ngày thứ 2 những người mắt nâu thấy 2 ngưới mắt xanh trong khi những người mắt xanh chỉ thấy 1 . Do vậy chỉ những người mắt xanh mới luận ra mình mắt xanh.

> Những người mắt nâu thì bán tín bán nghi, mỗi người trong họ hiểu nếu đêm đó 2 ông kia không gặp Diêm Vương thì có nghĩa không chỉ có 2 người mắt xanh trên đảo, và do đó nhất thiết mình cũng mắt xanh và sẽ phải nhập hội vào đêm sau. Nhưng đêm đó 2 ông kia đi rồi thì những người mắt nâu suy ra mắt mình không xanh nên thoát nạn.

> Chỉ hy vọng anh Tèo đừng có đến mà nói thêm câu gì tương tự.

> 0

> 0

**hally** · 26/11/2010 at 9:12 am

> trường hợp 1 mắt xanh (X) – 99 mắt nâu (N)

> mắt nâu bất kỳ thấy 98 N và 1 X + thông báo có bác mắt xanh —>mắt nâu đó sẽ thấy 2 trường hợp (1) mình mắt nâu —> đêm thứ 1, mắt xanh tự vẫn.(2) mình mắt xanh—>đêm thứ 1 ko có chuyện ji cả. do đêm thứ 1 mắt xanh tự vẫn —>99 N còn lại biết mình ở trường hợp (1)—> cả làng tự vẫn.

> 0

> 0

**RongChoi** · 26/11/2010 at 11:11 am

> Vấn đề các bạn mắt nâu có thể nghĩ mình là người duy nhất mắt đen hay mắt hồng hồng tím tím như bạn gì nói nên không dẫn đến tuyệt chủng

> RC đang nghĩ là đến ngày thứ 10 lẻ 1 (túc thứ 11) tự nhiên có dịch mắt đỏ ào tới, làm nhiều nhất 1 bạn mắt xanh + tất cả các bạn mắt nâu bị đỏ mắt thì không biết có cứu được dân làng hay không

> 0

> 0

**hally** · 26/11/2010 at 1:16 pm

> uh nhỉ! mình ngu há!

> 0

> 0

**metallium** · 30/11/2010 at 1:42 pm

> Cháu có thắc mắc này mong các bác giải đáp ạ. Liệu có tồn tại sự tự mâu thuẫn (nghịch lý) trong câu hỏi và lời giải?

> Theo như lời giải của bác RC thì lập luận của những người mắt xanh không thể áp dụng đc với những người mắt nâu vì họ không có “cú hích đầu tiên”. Tức là xét trong trường hợp làng chỉ có 1 người mắt nâu thì vì không có ai nói cho người đó biết trong làng có người mắt nâu nên người đó cũng chưa đoán được màu mắt của mình. Dẫn đến các trường hợp khác cũng xảy ra. Cháu hiểu thế đúng ko ạ???

> Bây giờ tạm gác lập luận đó lại. Có những 23 người mắt xanh (và cả 77 người mắt nâu), chứ không phải 1, nên có thể ngay trong ngày đầu tiên ra cái lệ làng đấy, tất cả những người mắt xanh đều có thể thốt ra: “Trong làng mình có người mắt xanh”. Vậy thì khác gì việc chú Tèo nói ra??? Lúc này những người mắt xanh liệu còn có thể dùng lập luận như bác RC để đoán ra màu mắt của mình???

> Rõ ràng trường hợp chỉ có 1 người mắt xanh thì phải cần đến người ngoài, nhưng trường hợp có nhiều người như vậy thì không cần phải có, cháu nghĩ đấy là điểm yếu của đáp án và cũng là của câu hỏi luôn.

> 0

> 0

**Ngô Quang Hưng** · 23/11/2010 at 6:40 pm

> Các phòng thông nhau không biết ST gõ cửa 1 phòng thì có nhìn trộm sang 2 phòng bên cạnh được? Cứ coi là có cho dễ

> Hah hah, ST ăn gian.

> 0

> 0

**luong** · 23/11/2010 at 7:32 pm

> :-). This is called out-of-the-box thinking

> 0

> 0

**Đức** · 23/11/2010 at 10:35 pm

> 103: Dãy phòng hình tròn hay thẳng vậy anh Hưng ? Nếu tròn thì chỉ 3 phòng MN đã có thể trốn ST tới già luôn.

> 0

> 0

**Ngô Quang Hưng** · 23/11/2010 at 11:45 pm

> Thẳng, bạn Kan đã giải xong ở dưới

> 0

> 0

**RongChoi** · 26/11/2010 at 6:24 am

> Nếu là vòng thì cũng hay, nhưng phải cho phép ST mở 2 phòng mỗi ngày.

> Trường hợp “thô” nhất là ST dùng 1 phòng chặn làm tường, hôm nào cũng mở phòng đó. Khi đó, trở lại trường hợp bài toán gốc, và 30 ngày là đủ.

> Câu hỏi là ST làm tốt hơn được không? Tối thiểu bao nhiêu ngày thì tóm được MN?

> 0

> 0

**Kan** · 23/11/2010 at 11:33 pm

> 103)

> Kính gửi bác Hùng thứ 19,

> Cháu là Kan, hôm nay viết thư này gửi bác để xin em Mị Nương về làm vợ bằng cách giải câu đố duy lí của bác như sau:

> Mấy nhận xét ban đầu:

> 1) Cháu đánh số 17 phòng theo thứ tự từ phải qua trái:

> 01 – 02 – 03 – 04 – 05 …, 15 – 16 – 17.

> Điều cháu băn khoăn sẽ là: ngày thứ nhất, em Mị nhà bác ở phòng chẵn hay phòng lẻ?

> 2) Em Mị nếu ngày đầu ở phòng chẵn thì sau mỗi 2 ngày em í sẽ về lại phòng chẵn. Tương tự, nếu ngày đầu em í ở phòng lẻ thì sau mỗi 2 ngày em í sẽ về lại phòng lẻ.

> 3) Cháu cũng hiểu là cần phải dồn em í về 1 bên thì mới mong gặp được em, chứ không thì chả làm ăn gì được cả, hehe!

> Nên cháu xin giơ tay phát biểu như thế này:

> – Giả sử ngày 1 (n1) em Mị ở phòng chẵn. Nghĩa là: ngày lẻ em í ở phòng chẵn, còn ngày chẵn em í ở phòng lẻ.

> Vậy n1 cháu mở phòng 2 (P2), kí hiệu n1 = P2. Nếu có em í trong đó, cháu sẽ mừng lắm. Còn nếu không có, cháu cũng không lấy làm buồn vì còn tới 29 ngày nữa. Khi P2 trống, nghĩa là em có thể ở 1 trong các phòng chẵn P4, P6, P8…

> – n2: cháu muốn biết em Mị nhà bác n1 có ở P4 và n2 có di chuyển qua bên trái hay không? Cháu sẽ mở P3, n2 = P3. Nếu P3 trống nghĩa là em í đã di chuyển qua bên phải nếu n1 = P4.

> – n3 = P4. Khi P4 trống nghĩa là em í vẫn ở bên phải.

> – Cứ tương tự vậy, cháu sẽ dồn em í sang bên phải, n4 = P5, n5 = P6, …., n14 = P15, n15 = P16. Đến hôm rằm giữa tháng thế này mà cho đến P16 vẫn không thấy em thì nghĩa là: giả định của cháu ở trên là sai! Nghĩa là ngày thứ nhất, em Mị ở trong phòng lẻ, hay nói cách khác: ngày lẻ em í ở phòng lẻ, ngày chẵn ở phòng chẵn.

> – n16 = P16. Nếu P16 trống thì đương nhiên P17 cũng trống. Nghĩa là em í ở bên tay trái P16. Vậy cứ đúng quy tắc, ngày lẻ ở phòng lẻ, ngày chẵn ở phòng chẵn, cháu sẽ dồn em í qua bên trái bằng cách lần lượt mở tiếp:

> – n17 = P15, n18 = P14, n19 = P13, …, n28 = P4, n29 = P3. Nếu P3 vẫn trống thì có nghĩa là em í đang ở P1 và ngày hôm sau sẽ sang P2!

> – n30 = P2. Đã gặp được em, Mị ạ! (-:

> Vậy thưa bác Hùng thứ 19, cháu đã trình bày cách thức để gặp được em í trong tối đa 30 ngày. Vậy mong bác gả em í cho cháu, bác nhé!

> 5

> 0

**hally** · 26/11/2010 at 9:17 am

> Bác Kan tỉ mỉ nhỉ? đọc ý cuối của RongChoi trên kia là hiểu rồi!

> 2

> 0

**koreagerman** · 24/11/2010 at 3:10 am

> Bài 103 Kan giải hay quá!

> 0

> 0

**Thang Pham** · 24/11/2010 at 1:09 pm

> Em có cách giải đơn giản hơn Kan: Bắt đầu từ phòng thứ 2, cứ mỗi phòng Sơn Tinh mở 2 đêm liên tục. Nếu ban đầu Mị Nương ở phòng 1 thì đến đêm thứ 2 là gặp. Còn nếu Mị Nương ở phòng lớn hơn thì cũng không có cách nào đi về phía bé hơn được. Trừ 2 phòng đầu cùng thì còn 15 phòng, mỗi phòng 2 đêm, tốn tối đa là 30 đêm. Như vậy, Mị Nương có chạy đằng trời >:).

> 0

> 0

**RongChoi** · 24/11/2010 at 2:36 pm

> Đi sang phía bé được chứ? Hôm đầu MN phòng 4, hôm sau 3, hôm nau nữa 2 thì ST đã tót sang phòng 3 rồi

> 0

> 0

**Ngô Quang Hưng** · 24/11/2010 at 3:02 pm

> RongChoi nên đổi nick thành Thủy Tinh

> 0

> 0

**RongChoi** · 24/11/2010 at 4:37 pm

> Đã thế bổ sung thêm bài toán của anh Hưng:

> Bây giờ có thêm cả Thủy Tinh. Nhưng vẫn như xua kia, Vua Hùng vẫn ra luật thiên vị Sơn Tinh, cho ST mở cửa phòng trước, nếu không tìm được MN thì đến lượt TT, và TT bị ràng buộc chỉ được mở 1 trong 2 phòng cạnh phòng mới mở của ST mà thôi.

> Tìm chiến thuật cho ST

> 0

> 0

**Ngô Quang Hưng** · 24/11/2010 at 4:49 pm

> Cho Thủy Tinh một đồng xu

> 1

> 0

**RongChoi** · 24/11/2010 at 5:45 pm

> Có thêm Thủy Tinh nên với ST thì lần đầu rất rủi ro, nhỡ mở phòng cạnh MN thì gay.

> Tóm lại điều kiện bài toán thay đổi như sau:

> – Có thêm Thủy Tinh tranh tài, ai mở được phonhf MN trước thì được vua Hùng kén làm rể

> – ST chơi trước và được phép sửa sai thay đổi lựa chọn 1 lần (không nhất thiết lần đầu), kèm theo điều kiện ăn gian “ST gõ cửa 1 phòng thì vì mắt tinh như cú vọ nên có thể nhìn trộm sang 2 phòng bên cạnh”.

> – Thủy Tinh bị hạn chế chỉ được mở cứu cạnh phòng ST vừa mở.

> (RC cho thêm khả năng nhìn trộm như vậy là thương ST, để lỡ có thấy MN phòng bên cạnh thì còn có lời tạm biệt “Than ôi, đầu óc ta chỉ đến vậy, đành để nàng vào tay TT vây!” và để nàng MN thổ lộ tâm tình thật “tuy vưa cha ưng chàng,thiên vị chàng, nhưng thực lòng em lại thích và đã tìm cách thoát chàng để về với biển cả mênh mông :D”)

> Tuy nhiên, đáng tiếc thay, với những điều kiện ưu đãi trên thì hình như MN vẫn không thể thoát khỏi ST

> 0

> 0

**it4rb** · 24/11/2010 at 1:23 pm

> 102. Ủa, sau khi mấy cụ mắt xanh rủ nhau đi hết, mấy cụ mắt nâu chắc cũng tự luận được màu mắt của mình rồi đi theo cả làng cho vui chứ nhỉ?

> 0

> 0

**Thang Pham** · 24/11/2010 at 1:48 pm

> Có thể họ cho rằng mình mắt đỏ, hoặc hồng, nên vẫn quyết ko chết :))

> 0

> 0

**Nghia Nguyen** · 24/11/2010 at 4:15 pm

> Bài 101:

> Chia thành 2 nhóm. Trong đó nhóm thứ nhất có 13 lá, nhóm thứ hai có 39 lá.

> Gọi *a* là số lá ngửa thuộc nhóm 1, vậy:

> +Nhóm 1: *a* lá ngửa, 13-*a* lá sấp.

> +Nhóm 2: 13-*a* lá ngửa, 39 – (13 – *a*) = 26 + *a* lá sấp.

> Thay đổi mặt (sấp thành ngửa, ngửa thành sấp) của toàn bộ các quân bài thuộc nhóm thứ nhất:

> +Nhóm 1: 13-*a* lá ngửa, a lá sấp.

> +Nhóm 2: 13-*a* lá ngửa, 39 – (13 – *a*) = 26 + *a* lá sấp.

> 1

> 0

**Nam** · 24/11/2010 at 10:04 pm

> Đến ngày 22 và 23, cả làng trốn biệt ở nhà để tránh phải tự sát tập thể, sau rồi lại đâu vào đấy. Sau đó làng có lệnh cấm không được phát ngôn bừa bãi.

> 0

> 0

**Huân** · 27/11/2010 at 8:47 am

> Một vài người nào đó sẽ đứng lên đập chết chú Tèo với lý do “nói bậy”, những người còn lại sẽ ủng hộ theo, keke, cả làng coi như thoát họa lớn!

> 0

> 0

**t3chamngoan** · 30/11/2010 at 10:06 pm

> Em có một câu hỏi : một người duy lý sẽ làm gì sau khi biết là mình sẽ chết sau k ngày nữa?

> Do dân làng rất thông minh nên sẽ dễ dàng phán đoán được tình huống sẽ xảy ra như thế nào.

> Đối với bất kỳ một ông mắt nâu nào đó, thấy 23 ông mắt xanh còn lại, sẽ đoán đc tối đa là sau 24 ngày, mình sẽ chết

> Tương tự, ông mắt xanh sẽ biết là tối đa sau 23 ngày, mình sẽ chết.

> Thú vị ở chỗ, không một ai có thể biết được là những người kia có tự tử hết, trước hạn của mình, và nếu may rủi thì sẽ phải đợi đến ngay trước ngày mình chết.

> Theo wikipedia : chủ nghĩa duy lý là một phương pháp hoặc học thuyết “mà trong đó tiêu chuẩn về chân lý không có tính giác quan mà có tính trí tuệ và suy diễn lôgic”

> Vậy theo em nghĩ, thì cả làng sẽ tự tử ngay đêm đầu tiên, do nghĩ trước sau gì thì cũng chết =)). Chỉ khổ thân Tèo, vì câu nói mà hại cả trăm mạng người.

> 1

> 0

**metallium** · 30/11/2010 at 10:49 pm

> rất tiếc là họ ko đủ cơ sở để đoán đc 23 ngày sau họ sẽ chết để mà chết luôn từ ngày đầu tiên

> 0

> 0

**ThangNM** · 01/12/2010 at 12:38 am

> 102. Do chả ai biết số người mắt xanh là 23. Ai cũng thấy 99 người khác mắt xanh và nâu nên không cần chờ Tèo phát biểu họ cũng nhận ra điều đó.

> Cực đoan hóa trong trường hợp này của bác RongChoi ko đúng.

> Nếu chỉ có 1 mắt xanh thì sẽ khác.

> Có >1 mắt xanh sẽ khác.

> Tóm lại là cả làng vẫn sống yên ổn vì không ai biết chính xác màu mắt mình là gì.

> 0

> 0

**metallium** · 01/12/2010 at 1:59 am

> Bác ơi, bác có cách nào sửa lại đề cho chặt chẽ để cho cái đáp án của bác RC là đúng không ạ???

> 0

> 0

**Huân** · 01/12/2010 at 2:05 am

> @ThangNM: Nếu có 2 người mắt xanh, mỗi người trong họ sẽ thấy trong làng có 1 người mắt xanh. Họ sẽ nghĩ rằng người mắt xanh kia không thấy ai mắt xanh cả. Khi Tèo phát biểu rằng trong làng có người mắt xanh thì cả 2 đều duy lý rằng, người kia trước nay không biết trong làng có người mắt xanh, nay biết được mà không thấy ai cả ắt hẳn là chính mình. Đêm đó sẽ đi tự sát.

> Nhưng sáng mai, cả 2 người đều thấy người kia còn sống, như vậy rõ ràng ai cũng biết trong làng có người mắt xanh trước khi Tèo phát biểu. Và lúc này cả 2 hiểu rằng họ đều có mắt xanh.

> Giả sử trong làng có 3 người mắt xanh, mỗi người sẽ duy lý như khi trên và sau đó sẽ biết được mình mắt xanh.

> Tuy nhiên, duy lý như trên chỉ đúng nếu trước khi Tèo phát biểu dân làng chưa xem hết màu mắt của cả làng và sau khi nghe Tèo phát biểu thì bắt đầu đi đếm.

> Còn ở đây, thông tin trước khi Tèo phát biểu và sau khi phát biểu hình như không có gì thay đổi. Trước đó ai cũng biết là trong làng có người mắt xanh (người thì nghĩ tối đa 23, người thì nghĩ tối đa 24). Khi Tèo phát biểu thì cùng lắm họ đứng lên vỗ tay hoan hô anh Tèo nói đúng.

> Khi mà tất cả mọi người trong làng cùng lúc biết được chính xác tất cả những người khác vừa mới đếm xong số người mắt xanh của cả làng thì mới có chuyện tất cả những người mắt xanh sẽ tự tử sau .. ngày. Còn nếu không biết được cùng lúc thì không thể biết được màu mắt mình.

> 0

> 0

**metallium** · 01/12/2010 at 2:25 am

> cháu ko hiểu bác Huân nói gì luôn, rõ ràng 23 người mắt xanh đều biết có 22 người mắt xanh và 77 người mắt nâu trong làng mà ạ.

> Cơ mà cháu thấy thế này, cùng là một thông tin được dùng để suy luận đó là “Trong làng có người mắt xanh”, nhưng với 2 đối tượng phát biểu khác nhau thì cho các kết quá có vẻ khác nhau. Anh Tèo nói ra thì 23 ngày sau khi anh Tèo nói, những người mắt xanh tự tử, đó là theo lập luận của bác RC. Còn nếu kết luận kia tự do 23 người mắt xanh nói ra (thực ra thì họ cũng biết rồi) thì chả có chuyện gì xảy ra. Các bước lập luận chỉ cần dùng đến mệnh đề “Trong làng có người mắt xanh” mà ko cần phải quan tâm tới người phát biểu ra, như vậy có thể thấy lời giải của bác RC có vấn đề.

> Cháu thấy câu đố cần phải sửa lại, các bác giúp cháu đi. Cháu trót đem đi đố với đứa bạn rồi :((

> 0

> 0

**hally** · 01/12/2010 at 5:39 am

> Nghĩ là tuyên bố “có người mắt xanh” từ Tèo hay bất cứ ai trong làng vì thấy có người mắt xanh mà thốt ra đều có giá trị như nhau. Nhưng bắt buộc phải có tuyên bố mới có thông tin để dân làng suy luận. Đề ra do đó ko vấn đề gì.

> 0

> 0

**ThangNM** · 01/12/2010 at 5:50 am

> Theo mình thì sẽ không ai biết được màu mắt của mình là gì cả. Trừ phi biết đích xác số người màu xanh và số người màu nâu :P. Của bác RongChoi giống ngụy biện toán học nhỉ?

> 0

> 0

**Huân** · 01/12/2010 at 6:59 am

> Buổi chiều họp toàn làng đứng lên phát biểu: “ớ, làng này có bác mắt xanh!” – Xem buổi họp này là lần gặp mặt đầu tiên của cả làng đi!

> 0

> 0

**ThangNM** · 01/12/2010 at 3:15 am

> @Huân: Mình có cảm giác số 23 đưa ra để lừa. Làm gì có ai biết số đó đâu mà đoán.

> 0

> 0

**Huân** · 01/12/2010 at 7:02 am

> Không có con số này thì mọi người lấy cái gì mà “duy lý”!

> Smile!

> 0

> 0

**metallium** · 01/12/2010 at 7:30 am

> Cháu nghĩ là số tượng trưng thôi, lớn hơn 2 là đc ạ. Đẹp nhất là xét trong trường hợp làng có 10 người, 3 người mắt xanh và 7 người mắt nâu, nhưng chả làng nào có 10 người cả nên bài toán chuyển thành 100, 23 và 77 cho nó thực tế hơn thôi ạ (cháu nghĩ thế)

> Cháu kết lời giải của bác RC lắm, vì thế cháu trình bày lại với trường hợp 3 người ạ: Theo giả thiết thì ai có mắt xanh sẽ nhìn thấy 22 mắt xanh và 77 người mắt nâu. Tất nhiên là hôm đầu tiên và hôm thứ hai không có vấn đề gì xảy ra. Đến hôm thứ ba, những người mắt xanh sẽ thắc mắc rằng nếu chỉ có 2 người mắt xanh thì theo các suy luận ở TH1 và 2 thì họ đã tự tử hết rồi, đằng này họ vẫn sống sờ sờ –> chắc chắn vẫn còn người mắt xanh nữa. Vậy là những người mắt xanh ai cũng biết mình mắt xanh và đêm đó đi tự tử :-s

> Từ đó có thể áp dụng suy luận kiểu này cho số người mắt xanh là 4, 5, …

> 0

> 0

**metallium** · 01/12/2010 at 7:51 am

> ah mà cháu nhầm, lớn hơn 1 là đc rồi ạ ^^

> 0

> 0

**RongChoi** · 01/12/2010 at 5:48 am

> Điều quan trọng, là như metallium nói, là cần một cú hích, hay một thời điểm mốc. Việc ai nói không quan trọng, nhưng câu nói cần cả làng nghe. Thời điểm câu nói được phát ra cả làng đều ngầm coi (vì họ thông

> minh) là mốc 0.

> Vì cả làng thông minh nên sẽ không có ai phát ngôn bừa bãi trước làng. Do thế mà mới cần đến chú Tèo. Ý nghĩa của bài toán theo mình là “sự ngây thơ có thể ra một đòn chết mấy chục sự thông minh” Tất nhiên đó là ỹ nghĩa rút ra của một người ngây thơ, vì mình… thích sống lắm

> Mình nghĩ lời giải trưc quan như trên kia là OK. Còn để chứng minh chặt chẽ thì dùng qui nap cho mệnh đề “Nếu có n người mắt xanh thì đúng đến đêm thứ n tất cả họ sẽ đi gặp Diêm Vương”.

> Với n = 1 : đúng

> Giả sử đúng với n-1, giờ ta chứng minh mệnh đề đúng với n. Chứng minh: dễ thấy

> 0

> 0

**ThangNM** · 01/12/2010 at 5:51 am

> @RongChoi: Sao lại quy nạp được nhỉ?

> 0

> 0

**ThangNM** · 01/12/2010 at 6:00 am

> Nếu số người mắt xanh=1: Người mắt xanh thấy số người còn lại mắt nâu thì sẽ suy ra mình mắt xanh.

> Nếu số người mắt xanh =2: Người mắt xanh thấy chỉ có 1 người mắt xanh khác. Mà ko thấy đồng chí kia tự tử suy ra ít nhất có thêm người mắt xanh nữa.=> Chính là mình.

> Nếu số người mắt xanh =3. Người mắt xanh nhìn thấy 2 người kia mắt xanh. Tự suy luận ko thấy ai tự tử => số người mắt xanh phải lớn hơn 2 và mình mắt xanh.

> Nếu số người mắt xanh là =4. Thấy 3 người mắt xanh, ko thấy ai tự tử => Số người mắt xanh phải lớn hơn 3. Tự suy ra mình mắt xanh. Èo, có vẻ có lý nhỉ?

> ….

> 0

> 0

**t3chamngoan** · 01/12/2010 at 7:30 am

> Những người trong làng đó cũng suy nghĩ được như vậy chứ tại sao lại không có cơ sở? Như đã nói ở trên, nhóm thấy 23 ng mắt xanh thì sẽ dự đoán khả năng chết của mình là sau 24 ngày, nhóm thấy 22 người mắt xanh thì khả năng chết là sau 23 ngày.

> 0

> 0

**metallium** · 01/12/2010 at 7:48 am

> @2 bác Hally và Huân: sửa lại câu đố thành trong ngày đầu tiên họp làng và ra cái lệ oái oăm đấy, chú Tèo – khách mời từ làng bên đứng lên phát biểu: “Ớ, trong làng có người mắt xanh”. Như thế vẫn chưa giải quyết được vấn đề mệnh đề “làng có người mắt xanh” phụ thuộc vào người phát biểu nếu muốn áp dụng được lời giải của bác RC.

> @ bác RongChoi: cháu thử nói với bạn cháu giống như bác ở dưới nhưng nó ko chấp nhận vì nó kêu câu nói của Tèo không có giá trị cung cấp thêm thông tin trong trường hợp số người mắt xanh lớn hơn 1. Cháu thì vẫn thấy cần sửa lại đề, các bác nghĩ cho cháu đi ạ mà bác ra câu đố không có ý kiến gì ạ???

> 0

> 0

**Ngô Quang Hưng** · 01/12/2010 at 10:04 am

> @Metallium,

> Một câu đố vui thường sẽ có một “ngầm định” nho nhỏ, miễn là đừng ngầm định để lừa bạn đọc là được. Ngầm định ở đây là mọi người bắt đầu lý luận từ lúc Tèo phát biểu. Về mặt duy lý mà nói, cái ngầm định này suy ra một cách logic được cho nên không còn là ngầm định nữa; như các bác RC, Huân, hally đã chỉ ra: *“trước hôm Tèo phát biểu thì không có điều kiện khởi đầu để quy nạp”*.

> Tôi thấy câu đố như vậy là đủ … vui. Tôi tin rằng các bạn đọc đều hiểu logic nội tại của câu hỏi và câu trả lời. Việc phát biểu nó cho vuông vức không còn quan trọng lắm nữa. Còn nếu bắt bẻ câu hỏi thì ta cũng có thể bắt bẻ là “làm gì có làng nào có 100 người với 2 màu mắt”.

> Như tôi viết trong đề bài, câu này là một biến thể của một câu khác đã đố (số 55). Nếu bạn không thích biến thể kịch tính 102 thì có thể quay lại với câu 55.

> 0

> 0

**Nam** · 02/12/2010 at 12:58 am

> Ở biến thể này của bài toán thì mọi người có động lực để không biết màu mắt của mình để không phải chết vì nếu muốn biết thì hẳn mọi người đã chọn cách dễ nhất là hỏi nhau từ trước khi Tèo đến, và cả làng chết từ lâu rồi. Thế tức là hành động tự sát chỉ là miễn cưỡng, ai cũng muốn tránh. Để tránh việc biết màu mắt của mình thì mọi người chỉ việc từ chối tiếp nhận thông tin, khi không đủ thông tin thì sẽ thể không suy luận ra màu mắt của mình.

> Vậy bài toán trở thành tìm chiến lược hiệu quả nhất cho dân làng để đảm bảo mỗi người đều trốn tránh thành công thông tin, khiến không suy ra được màu mắt của mình. Chiến lược hiệu quả ở đây là hành động tốn ít công sức nhất, tránh ảnh hưởng đến cuộc sống nhiều nhất.

> Như thế biến thể có khi còn hay hơn cả bài toán gốc, phải không mọi người?

> 1

> 0

**pisac** · 01/12/2010 at 11:35 am

> May mà ông Tèo không tương cho một câu trong làng có người mắt tím

> 0

> 0

## Bài [38] — 4 bình luận

**koreagerman** · 17/03/2011 at 4:03 am

> 104: Theo em thì một lọ chứa một viên đỏ, lọ kia 49 viên đỏ + 50 viên xanh.

> 0

> 0

**Ngô Quang Hưng** · 17/03/2011 at 9:26 am

> Chính xác.

> 0

> 1

**Dung** · 30/03/2011 at 12:06 pm

> 105:

> 1.Trong $2n$ số, số lớn nhất là $a_n$ hoặc $b_1$ và số nhỏ nhất là $a_1$ hoặc $b_n$. Không mất tính tổng quát ta có thể chọn $(a_n, b_n)$ là cặp số có giá trị max lớn nhất và giá trị min nhỏ nhất trong các cặp số có cùng giá trị max lớn nhất.

> Nếu $b_n$ là số nhỏ nhất trong $2n$ số thì có thể bỏ tiếp tục sắp xếp với $(n-1)$ cặp còn lại. Nếu $b_n$ không phải là số nhỏ nhất thì $(a_1, b_1)$ là cặp số có giá trị min nhỏ nhất và giá trị max lớn nhất trong các cặp có cùng giá trị min nhỏ nhất.

> 2. Dễ thấy các cặp số có giá trị max lớn hơn $b_1$ nằm bên trái $(a_n, b_n)$ với thứ tự giảm dần của giá trị max, tăng dần của giá trị min. Tương tự các cặp số có giá trị min nhỏ hơn $b_n$ nằm bên phải $(a_1, b_1)$ theo thứ tự tăng dần của giá trị min và giảm dần của giá trị max. Giả sử ta đã sắp xếp đến cặp $i$ và $j$, $i<j$, tiếp tục lặp lại bước 2 với $b_i$, $b_j$ đóng vai trò của $b_1$, $b_n$ cho đến khi không còn cặp số nào được sắp xếp. Khi đó việc sắp xếp các cặp số ở giữa không liên quan đến các cặp số đã được sắp xếp vì tất cả các số đều nhỏ hơn $b_i, a_j$ và lớn hơn $b_j, a_i$. Quay lại bước 1 để sắp xếp các cặp ở giữa.

> Với các sắp xếp trên, nếu khi đặt một cặp vào đúng vị trí và vi phạm điều kiện thì đưa ra câu trả lời là không tồn tại.

> 0

> 0

**Lê Ngọc Minh** · 02/04/2011 at 2:05 pm

> 104. Chứng minh: gọi x là số bi đỏ trong lọ 1 và z là tổng số bi trong lọ 1. Xác suất xuất hiện bi đỏ là p = 1/2 (x/z + (50-x)/(100-z)). Nếu coi x, z là số thực, đạo hàm p theo x sẽ thấy p đồng biến với x khi z nhỏ hơn 50, nghịch biến với x khi z lớn hơn 50 và không phụ thuộc vào x khi z=50. Từ đó gợi ý ta chia làm 3 trường hợp:

> * z < 50: cần tăng x đến khi bằng z, xác suất được viết lại là p = 1-25/(100-z), giá trị z = 1 cực đại hoá xác suất

> * z > 50: gọi t = 100-z (số bi trong lọ 2), làm tương tự trường hợp 1

> * z = 50: xác suất luôn là 1/4 không phụ thuộc vào x

> Kết luận như comment trước, xác suất là 74/99

> 105. Giải thuật tham lam:

> (a[1], b[1]) = (min{a[1],b[1]}, max{a[1],b[1]})

> for i = 2 to n do

>         (a[i], b[i]) = (min{a[i],b[i]}, max{a[i],b[i]})

>         if a[i] < a[i-1] or b[i] > b[i-1] then

>                 a[i] <–> b[i]

>         if a[i] < a[i-1] or b[i] > b[i-1] then

>                 writeln(“Khong ton tai”);

>                 break;

> Chứng minh: Trong bước thứ i ta chọn giá trị nhỏ nhất có thể của a[i] và lớn nhất có thể của b[i], nếu giá trị này vẫn không chấp nhận được thì kết luận là “không tồn tại”.

> 0

> 0

## Bài [39] — 4 bình luận

**Le Ngoc Minh** · 02/09/2011 at 12:16 am

> Ý tưởng: duyệt ngược từ cuối về đầu xâu. Tại vị trí i, tìm hậu tố dài nhất của [0..i] và [0..m-1] –> tìm ra giá trị ms[i]. Với các vị trí còn lại trong đoạn hậu tố vừa tìm được, giả sử là [l+1..r], dựa vào đoạn tương ứng bằng nó để gán ms.

> i và l luôn giảm nên độ phức tạp là O(m).

> void findSuffix(char *p, int *ms, int m) {
>     int i, r, l;
>     ms[m-1] = m;
>     for (i = l = m-2; i >= 0; ) {
>         r = i;
>         while (l >= 0 && p[l] == p[m-r+l-1]) {
>             l--;
>         }
>         ms[i--] = r-l;
>         while (i > l) {
>             if (ms[m-r+i-1] < i-l) {
>                 ms[i] = ms[m-r+i-1];
>             } else if (ms[m-r+i-1] > i-l) {
>                 ms[i] = i-l;
>             } else {
>                 break;
>             }
>             i--;
>         }
>         if (i < l) {
>             l = i;
>         }
>     }
> }

> 0

> 1

**datnt** · 11/10/2011 at 11:44 pm

> Hi all,

> May I have your suggestion about the coding style ?

> At first, I’ve read some coding style instruction from some ones (whom I respect); and they suggest that we should not change the index of loop (i.e: for ) within the loop, is this rule should be considered against the above solution?

> As I see, the above solution, the code change the index while looping, at line number 9, and line number 18.

> Thank you in advance.

> 0

> 0

**NQH** · 12/10/2011 at 8:29 am

> @datnt,

> I’d generally agree that one should not change the looping variable inside a loop. “Programs should be written for people to read.” However, note that in the above code i, l are not really looping variables. The for loop should have been and was written with the same semantic as a while loop. Another slightly different solution to the above puzzle can be found here.

> 0

> 0

**datnt** · 17/10/2011 at 3:20 am

> Thank you so much.

> 0

> 0

## Bài [40] — 11 bình luận

**hoangtran** · 09/11/2011 at 10:45 pm

> void* Malloc(size_t size)
> {
>         void* mem;
>         void* addr = NULL;
>         if (mem = malloc(size + sizeof(void*) + 3)) {
>                 addr = (void*)(((unsigned int)mem + sizeof(void*) + 3) & ~(0x3));
>                 ((void**)addr)[-1] = mem;
>         }
>         return addr;
> }
> void Free(void* addr)
> {
>         if (addr)
>                 free(((void**)addr)[-1]);
> }

> 0

> 0

**NQH** · 09/11/2011 at 10:51 pm

> @hoangtran, bạn nhất định sẽ không sống thọ. Không cần đọc kỹ, chỉ cần thấy sizeof() + 3 là biết đúng!

> 0

> 0

**thaidn** · 10/11/2011 at 3:19 am

> @hoangtran: code của bạn đẹp quá ;-).

> 1
> addr = (void*)(((unsigned int)mem + sizeof(void*) + 3) & ~(0x3));

> tôi nghĩ chỗ này khi chạy trên 64-bit sẽ bị segmentation fault. đây là lỗi thường gặp khi chuyển các ứng dụng từ 32-bit sang 64-bit [1]. tôi nghĩ phải sửa lại vầy thì sẽ chạy đúng trên cả 32-bit lẫn 64-bit:

> 1
> addr = (void*)(((size_t)mem + sizeof(void*) + 3) & ~(0x3));

> size_t cũng có thể được thay bằng uintptr_t.

> [1] http://software.intel.com/en-us/articles/lessons-on-development-of-64-bit-cc-applications/

> 0

> 0

**hoangtran** · 11/11/2011 at 12:58 am

> lúc cast unsigned int thì /me đã thấy có vấn đề rồi nhưng vì để viết nhanh cho chạy trên máy mình nên bỏ qua. Mục đích chính của câu hỏi này là trả lời ý tưởng giải thuật thôi nhỉ

> 0

> 0

**thaidn** · 10/11/2011 at 3:21 am

> anh Hưng: thế anh chọn cái nào?

> 1. void *x;

> 2. void* x;

> Linus cũng chọn 1 đó ;-).

> 0

> 0

**NQH** · 10/11/2011 at 8:56 am

> Linus sắp tèo rồi :-), dĩ nhiên phải là void* ptr

> 0

> 0

**hoangtran** · 11/11/2011 at 12:57 am

> Agree với Linus là nên 1: void *ptr;

> Ví dụ sau sẽ confuse:

> int* pc, pd;

> pd không phải là pointer to int.

> 0

> 0

**thaidn** · 10/11/2011 at 3:57 am

> 1
> mem = malloc(size + sizeof(void*) + 3)

> nhờ một người bạn chỉ ra mới thấy chỗ này có nguy cơ tràn số nguyên (http://en.wikipedia.org/wiki/Integer_overflow). nếu mà size tiệm cận MAX_UINT thì phần bộ nhớ mà malloc trả về sẽ rất nhỏ so với ý định của người sử dụng.

> 0

> 0

**NQH** · 10/11/2011 at 8:58 am

> Ừ đúng. Một ví dụ đơn giản là tìm kiếm nhị phân, không nhớ đã bao giờ viết trên blog này chưa, mà có lẽ hầu hết chúng ta đều viết sai do bị int overflow.

> 0

> 0

**hoangtran** · 11/11/2011 at 1:01 am

> Thanks thaidn chỉ ra các lỗi về secure code. Vẫn biết là viết code cần secure nhưng phần lớn vì áp lực thời gian đều bỏ qua hết

> 0

> 0

**Cuong** · 07/12/2011 at 10:06 pm

> すごい！！！

> Em thích cái cách anh thêm sizeof(void*) để lưu lại địa chỉ gốc ở [-1].

> 0

> 0

## Bài [41] — 9 bình luận

**Thangola** · 01/02/2012 at 12:36 pm

> 109. Bé hơn 1%

> 110. ~50%

> 0

> 2

**TrietNM** · 01/02/2012 at 2:15 pm

> Gọi n là số điểm trên đường tròn.

> Để chọn 1 tam giác, ta có $C^{3}_{n}$ cách chọn.

> 109.

> Tam giác vuông có cạnh huyền qua tâm O của đường tròn:

> Để chọn 1 tam giác vuông ta có: $n*(n-2)$ cách chọn.

> Vậy xác suất chọn 1 tam giác vuông là $\frac{n*(n-2)}{C^{3}_{n}}$.

> Khi n đủ lớn thì xác suất gần như bằng 0.

> 110. Tam giác có 3 góc đều nhỏ hơn $\frac{\pi}{2}$

> Chọn đỉnh thứ nhất ta có: n cách

> Chọn đỉnh thứ 2 ta có: (n-2) cách

> Chọn đỉnh thứ 3 ta có: $\frac{1}{2}(n-\alpha)$ với $\alpha$ là const và $\alpha < \frac{n}{2}$

> Vậy xác suất có tam giác nhọn là $\frac{n*(n-2)*\frac{1}{2}(n-\alpha)}{C^{3}_{n}}$.

> Khi $n$ đủ lớn thì xác suất bằng $\frac{1}{2}$

> 0

> 1

**TrietNM** · 01/02/2012 at 3:03 pm

> 110. Em bị sai rồi, hình như 1/4 mới đúng

> xác suất hình như là $\frac {n(\frac{n}{2}-1)^{2}}{P^{3}_{n}}$

> Và khi n đủ lớn thì bằng 1/4.

> Không có sai gì không.

> 0

> 0

**NQH** · 01/02/2012 at 4:49 pm

> @Triết: 1/4 là đúng rồi. À, có cách tính trực tiếp không cần rời rạc hoá bài toán.

> 0

> 0

**Thangola** · 01/02/2012 at 11:10 pm

> Đúng là 1/4 thật. Hihi. Không khá về giải tích lắm nên phải vẽ hình ra mới tính được :”>

> 0

> 0

**The** · 02/02/2012 at 12:42 am

> @Triet: em chưa hiểu cách làm, mong anh chỉ rõ được ko ạ>!

> 0

> 0

**TrietNM** · 02/02/2012 at 6:40 am

> mình mới post lại bài này, mong bạn và mọi người góp ý thêm.

> http://trietnm.blogspot.com/2012/02/hai-cau-hoi-cua-thay-nqh.html

> 0

> 0

**Khoa** · 04/02/2012 at 2:51 am

> Lời giải bài 110 được giải thích ở đây nè: http://mathproblems.info/images/prob1.pdf

> Còn bài 109 thì chắc chỉ có anh Hưng mới đố

> 0

> 0

**GM** · 05/02/2012 at 1:17 am

> Cả 2 câu hỏi đều giải theo một cách:

> x,y là 2 số không âm với tổng x+y khong quá 2 \pi

> (vẽ hình ra!)

> Để co tam giác vuông thì:

> x = \pi hoặc

> y = \pi

> x+y = \pi

> ==> measure của 3 đoạn thẳng là 0. Nên xác suất là 0

> Để có tam giác nhọn thì x phải nhỏ hơn \pi, y phải nhỏ hơn \pi và x+ y phải lớn hơn \pi.

> Gộp tất cả các điều trên và điều kiện ban đầu. Vẽ hình ra sẽ thấy xác suất là 1/4 (= diện tích tam giác nhỏ/diện tích tam giác lớn)

> Lời giải trên thi học sinh lớp 7,8 có thể nghĩ ra được!

> 7

> 2

## Bài [42] — 3 bình luận

**Chấn Ngô** · 08/05/2012 at 9:32 am

> Hello a NQH,

> Em nghĩ bài này mình dùng cách duyệt cây theo giải thuật Moris Traversal, trong quá trình duyệt mình sẽ thay đổi tree, duyệt xong sẽ chuyển ngược về tree ban đầu. Ý tưởng chính là như sau:

> 1. Initialize current as root

> 2. While current is not NULL

> If current does not have left child

> a) Print current’s data

> b) Go to the right, i.e., current = current->right

> Else

> a) Make current as right child of the rightmost node in current’s left subtree

> b) Go to this left child, i.e., current = current->left

> Theo cách này thì ko yêu cầu thêm về bộ nhớ là hằng số (constant space).

> Em copy đoạn C++ code người # viết mọi người kiểm tra xem:

> #include
> #include

> /* A binary tree tNode has data, pointer to left child
>    and a pointer to right child */
> struct tNode
> {
>    int data;
>    struct tNode* left;
>    struct tNode* right;
> };

> /* Function to traverse binary tree without recursion and
>    without stack */
> void MorrisTraversal(struct tNode *root)
> {
>   struct tNode *current,*pre;

>   if(root == NULL)
>      return;

>   current = root;
>   while(current != NULL)
>   {
>     if(current->left == NULL)
>     {
>       printf(" %d ", current->data);
>       current = current->right;
>     }
>     else
>     {
>       /* Find the inorder predecessor of current */
>       pre = current->left;
>       while(pre->right != NULL && pre->right != current)
>         pre = pre->right;

>       /* Make current as right child of its inorder predecessor */
>       if(pre->right == NULL)
>       {
>         pre->right = current;
>         current = current->left;
>       }

>       /* Revert the changes made in if part to restore the original
>         tree i.e., fix the right child of predecssor */
>       else
>       {
>         pre->right = NULL;
>         printf(" %d ",current->data);
>         current = current->right;
>       } /* End of if condition pre->right == NULL */
>     } /* End of if condition current->left == NULL*/
>   } /* End of while */
> }

> /* UTILITY FUNCTIONS */
> /* Helper function that allocates a new tNode with the
>    given data and NULL left and right pointers. */
> struct tNode* newtNode(int data)
> {
>   struct tNode* tNode = (struct tNode*)
>                        malloc(sizeof(struct tNode));
>   tNode->data = data;
>   tNode->left = NULL;
>   tNode->right = NULL;

>   return(tNode);
> }

> /* Driver program to test above functions*/
> int main()
> {

>   /* Constructed binary tree is
>             1
>           /   \
>         2      3
>       /  \
>     4     5
>   */
>   struct tNode *root = newtNode(1);
>   root->left        = newtNode(2);
>   root->right       = newtNode(3);
>   root->left->left  = newtNode(4);
>   root->left->right = newtNode(5);

>   MorrisTraversal(root);

>   getchar();
>   return 0;
> }

> 0

> 0

**numos** · 08/11/2012 at 5:52 am

> Dear bạn Chấn Ngô,

> Mình thử check lời giải của bạn. Bạn in ra kết quả theo thứ tự trước Preorder trong khi yêu cầu bài toán là Inorder.

> Bản kiểm tra lại xem.

> Ý tưởng của mình để in theo thứ tự Inorder dùng O(1)-memory.

> 1. Initialize current as root

> 2. While current is not NULL

> 2.1. Print current’s data.

> 2.2. If current->left is NULL then current = current->right.

> Else

> {

> 2.2.1. Make the right child of the rightmost node in current->left is current->right.

> 2.2.2. current = current->left.

> }

> #include

> #include

> /* A binary tree tNode has data, pointer to left child

> and a pointer to right child */

> struct tNode

> {

> int data;

> struct tNode* left;

> struct tNode* right;

> };

> void Inorder(struct tNode *root)

> {

> struct tNode *current,*node;

> current = root;

> while(current != NULL)

> {

> printf(” %d “, current->data);

> if(current->left == NULL)

> {

> current = current->right;

> }

> else

> {

> /* Find the rightmost node of current->left */

> node = current->left;

> while(node->right != NULL)

> node = node->right;

> /* Set the right child of the rightmost node of current->left is current->right*/

> node->right = current->right;

> current = current->left;

> }

> } /* End of while */

> }

> /* UTILITY FUNCTIONS */

> /* Helper function that allocates a new tNode with the

> given data and NULL left and right pointers. */

> struct tNode* newtNode(int data)

> {

> struct tNode* tNode = (struct tNode*)

> malloc(sizeof(struct tNode));

> tNode->data = data;

> tNode->left = NULL;

> tNode->right = NULL;

> return(tNode);

> }

> /* Driver program to test above functions*/

> int main()

> {

> /* Constructed binary tree is

> 1

> / \

> 2 3

> / \

> 4 5

> */

> struct tNode *root = newtNode(1);

> root->left = newtNode(2);

> root->right = newtNode(3);

> root->left->left = newtNode(4);

> root->left->right = newtNode(5);

> Inorder(root);

> getchar();

> return 0;

> }

> 0

> 0

**Xuân Lương** · 20/08/2012 at 3:11 pm

> Hi GS. Hưng

> Bài 111 em nghĩ có thể giải dựa trên ý tưởng sau:

> – Về cơ bản thì ta dùng một con trỏ đi tuần tự ở nút gốc rồi rẽ sang trái cho tới khi chạm nút lá thì print data -> đi ngược lên nút cha -> print data -> rẽ phải …

> – Để giải quyết yêu càu không gian là O(1) thì ta có một con trỏ để duyện trong cây và một biến đi kèm để biết là con trỏ đó đã rẽ phải / trái mấy lần. Biến đó được cập nhật dựa trên cơ chế là:

> – Nếu con trỏ ở root thì foo = 1

> – Một lần rẽ trái thì foo = foo * 2

> – Một lần rẽ phải thì foo = foo * 2 + 1

> Với cách này, khi con trỏ chạy tới nút lá, ta gán nó trở về nút gốc và duyệt lại cho tới nút cha của nút cuối cùng mà nó đã trỏ tới. Việc này time-consuming nhưng có thể thỏa mãn yêu cầu về bộ nhớ?

> 0

> 0

## Bài [43] — 12 bình luận

**Nghị** · 18/04/2012 at 11:54 pm

> We can easily reduce to the case $a$ is odd. Write $a = 1 + 2b$. Then use the binomial expansion:

> $(1 + 2b)^{1/3} = 1 + \frac{1}{3}(2b) + \frac{(1/3)(1/3 - 1)}{2}(2b)^2 + \cdot$

> Since $(2b)^k = 0 \pmod{2^n}$ for $k \ge n$, the sum involves at most $n$ terms which can be iteratively computed.

> 1

> 0

**homotopie** · 20/04/2012 at 5:43 am

> Cách dưới mình thấy đúng rồi, nhưng cách này tại sao lại đúng ?

> 0

> 0

**Nghi** · 20/04/2012 at 1:14 pm

> The generalized binomial formula

> $(1 + x)^r = 1 + rx + \frac{r(r-1)}{1.2}x^2 + \frac{r(r-1)(r-2)}{1.2.3}x^3 + \cdots$

> , where $r$ is rational, holds for formal power series. One can prove this formula directly by defining derivatives for power series, proving a Taylor expansion formula and then applying it to $(1 + x)^r$. Another way is to observe that $(1 + x)^r$ can be uniquely expanded as a power series and then conclude that the expansion must be of the above form since that is what one gets from the expansion from real-valued functions (Newton binomial theorem).

> Here we are applying the formula to the ring $\mathbf{Z}/2^n$ and $r = \frac13$. It still holds because the generalized binomial coefficients $\frac{\frac13(\frac13-1)\cdots(\frac13-k+1)}{k!}$ have odd denominators.

> 1

> 0

**homotopie** · 20/04/2012 at 4:14 pm

> Mình không có ý hỏi cái khai triển Taylor kia, ý mình là bạn định nghĩa cái phép chia trên Z/2^n thế nào vì nó đâu phải là trường.

> 0

> 0

**Nghị** · 21/04/2012 at 2:16 am

> Mặc dù $\mathbb{Z}/2^n$ không phải là trường nhưng nó là một vành. Do đó một phân số sẽ có ý nghĩa nếu như mẫu số là lẻ. Trong công thức ở trên các hệ số binomial là các phân số với mẫu số lẻ. Ví dụ:

> $\frac{\frac13(\frac13-1)}{1.2} = -\frac19 = -(\mbox{ inverse of } 9),$

> $\frac{\frac13(\frac13-1)(\frac13-2)}{1.2.3} = \frac{5}{81} = 5\times(\mbox{inverse of } 81)$

> v.v.

> 0

> 0

**homotopie** · 21/04/2012 at 5:02 am

> Mình vẫn chưa thoả mãn, các số lẻ có nghịch đảo duy nhất trên Z/2^n nhưng vẫn không có nghĩa là có thể tính toán trên Z/2^n được, ít ra nó phải thoả mãn một số tính chất nữa như việc phân tích duy nhất ra thừa số.

> 0

> 0

**Nghị** · 21/04/2012 at 11:02 am

> Ta có thể tìm nghịch đảo của một số lẻ bất kỳ $x$ bằng thuật toán Euclid.

> 0

> 0

**homotopie** · 21/04/2012 at 12:47 pm

> Không, mình không có ý hỏi tính nghịch đảo như thế nào. Ý bạn có phải là các số lẻ có nghịch đảo duy nhất trên Z/2^n nên cái khai triển kia là xác định (điều này đúng), ý mình lại là có suy ra được cái khai triển kia trên Z/2^n hay không ?

> 0

> 0

**Nghị** · 22/04/2012 at 12:01 am

> Tôi không hiểu ý bạn lắm. Ở trên tôi có trình bày là ta có thể dùng formal power series để chứng minh khai triển đó cho $\mathbb{Z}/2^n$.

> 0

> 0

**homotopie** · 04/05/2012 at 6:05 am

> Ý mình là: mình không nghĩ rằng có thể suy ra được khai triển kia trên Z/2^n. Vì lý do: để tính toán (ở đây là khai triển Taylor) được trên một cấu trúc nào đó (ở đây là Z/2^n), thì các phép toán cần phải đúng cho mọi phần tử của cấu trúc, nếu Z/2^n là một trường thì mình hoàn toàn đồng ý, vì khi đó tính toán trên đó giống hệt như tính toán trên tập hữu tỉ. Do vậy, khi bạn định chứng minh khai triển kia qua power series, thì bạn cần giả thiết rằng mọi phần tử (mà không phải chỉ là các số lẻ) của Z/2^n là khả nghịch.

> 0

> 0

**Nghị** · 19/04/2012 at 1:49 am

> An easier way: assume $a$ odd as before. First, let $k = \frac{2^{n-1}+1}{3}$ if $n$ is even and $k = \frac{2^n+1}{3}$ if $n$ is odd. We have $3k = 1 \pmod{2^{n-1}}$. Now compute $x = a^k \pmod{2^n}$ by doubling.

> 3

> 0

**prime** · 19/04/2012 at 9:48 am

> Em biết cách này, nhưng mà không nhanh bằng cách ở trên (cách của bạn ở trên hình như cũng dùng để tính căn bậc 2 của p). Cách ở trên cũng có vẻ đơn giản hơn về tính toán.

> Ta dùng bổ đề Helsen. Giả sử luôn là a lẻ cho đơn giản. Dãy nghiệm $x_n$ là dãy nghiệm (lấy theo mod 2^n) được cho như sau:

> $x_0=1$

> $x_{n+1}= x_n$ nếu $2^{n+1}|x_n^3-a$

> $x_{n+1}=x_n+2^n$ nếu $2^{n+1} \not | x_n^3-a$

> 1

> 0

## Bài [44] — 14 bình luận

**xcode** · 13/10/2012 at 11:00 pm

> mid chưa được tính phải không anh ?

> Thêm vào dòng mid = left + (right – left)/2, sau cái while là được.

> 1

> 1

**noname** · 14/10/2012 at 2:39 am

> Theo em thì sai ở chỗ sorted_vec.size()-1. Sửa lại là

> bool binary_search(const vector& sorted_vec, int key) {

> size_t mid, left = 0, right = sorted_vec.size();

> while (left sorted_vec[mid])

> left = mid+1;

> else if (key < sorted_vec[mid])

> right = mid-1;

> else

> return true;

> }

> return false;

> }

> Trình còn non kém, nếu sai mong mấy bác chỉ giáo.

> 0

> 0

**noname** · 14/10/2012 at 2:41 am

> Á, á, copy paste làm sao mà mất tiêu cái đoạn chỗ từ while đến if rồi

> 0

> 0

**NQH** · 15/10/2012 at 9:18 am

> @noname: cần sửa cả right = mid - 1 nữa

> 0

> 0

**noname** · 16/10/2012 at 7:02 am

> Ồ, lỗi sai quả là thâm sâu. Em đó giờ rất ít chú ý đến phần kiểu dữ liệu, với lại e cũng ko nghĩ là ai lại truyền vào một dãy rỗng và bắt tìm kiếm, sau này phải cố gắng hơn mới được. Em nghĩ là bạn @Hiep ở dưới sửa chuẩn rồi.

> 0

> 0

**trietnn** · 14/10/2012 at 2:40 am

> Van de o mid..

> 0

> 0

**NQH** · 14/10/2012 at 9:41 am

> Ôi xin lỗi, tôi gõ thiếu cái dòng mid = left + (right-left)/2

> Câu hỏi đã được sửa. Lỗi không tầm thường, không nằm ở cái dòng gõ thiếu đó.

> 0

> 0

**Hiep** · 14/10/2012 at 9:58 am

> Em thấy right là size_t là unsigned int, như vậy right = mid – 1 sai khi mid = 0: và điều này xảy ra được. Hoặc là khi vector rỗng (khi đó right thực ra là (size_t)(-1)>0). Sửa lại bằng cách thay size_t bằng int.

> 0

> 0

**NQH** · 14/10/2012 at 10:08 am

> @Hiep bắt lỗi chuẩn rồi, nhưng tôi nghĩ sửa thành int chưa ổn lắm tại vì std::numeric_limits<int>::max() về nguyên tắc có thể nhỏ hơn vector<int>::max_size()

> 0

> 0

**Hiep** · 14/10/2012 at 6:27 pm

> Oh, em không để ý chút nào đến giới hạn trên. Một lời giải nữa là thay vì dùng “right” thì dùng “right +1″, và sửa những chỗ tương ứng. Khi đó nó gần giống với đáp án của bạn noname ở comment số 2:

> bool binary_search(const vector& sorted_vec, int key) {

> size_t mid, left = 0, right = sorted_vec.size();

> while (left sorted_vec[mid])

> left = mid+1;

> else if (key < sorted_vec[mid])

> right = mid;

> else

> return true;

> }

> return false;

> }

> 0

> 0

**Hiep** · 14/10/2012 at 6:38 pm

> Hic, copy paste có vấn đề (giống bạn noname ) do dùng “<” và “>”:

> bool binary_search(const vector& sorted_vec, int key) {
>     size_t mid, left = 0, right = sorted_vec.size();
>     while (left  < right) {
>         mid = left + (right-left-1)/2;
>         if (key > sorted_vec[mid])
>             left = mid+1;
>         else if (key < sorted_vec[mid])
>             right = mid;
>         else
>             return true;
>     }
>     return false;
> }

> 1

> 0

**NQH** · 16/10/2012 at 10:57 am

> @Hiep,

> Gần chuẩn rồi. Tôi nghĩ không cần right-left-1 (sẽ lại có lỗi!). mid = left + (right-left)/2 là đủ.

> À, các bạn viết code trên blog thì viết thế này:

> [code language=”cpp”]

> // C++ code goes here

> [/code]

> 0

> 0

**Hiep** · 17/10/2012 at 1:41 pm

> Uhm, em nghĩ mãi không hiểu right-left-1 sẽ có lỗi gì khi nó trong điều kiện (left < right) trong phần code em sửa. Em thấy -1 hay không có ảnh hưởng gì đâu, mid vẫn ở trong [left, right-1] mà. Đã chi li thì chi li cho chót

> 0

> 0

**NQH** · 17/10/2012 at 2:05 pm

> À đúng, xin lỗi tôi nhầm.

> 0

> 0

## Bài [45] — 15 bình luận

**Xuân Lương** · 26/10/2012 at 6:20 pm

> Hi GS. Hưng

> Bài này theo em dùng tư tưởng của merge sort khi trộn 2 dãy con. Với 2 biến chạy bắt đầu từ phần tử lớn nhất của 2 dãy. Ta lặp từ 1 tới k, ở mỗi bước lặp so sánh giá trị 2 phần tử ở vị trí của 2 biến chạy, phần tử nào lớn hơn thì cũng lớn hơn toàn bộ phần tử còn lại trong dãy kia. Thuật toán có độ phực tạp O(k) về thời gian.

> 0

> 0

**NQH** · 26/10/2012 at 6:41 pm

> @Xuân Lương, nếu k nhỏ thì làm vậy. Nếu k lớn, ví dụ cỡ căn n cho đến n/2 thì có cách tốt hơn.

> 0

> 0

**xiuaj** · 27/10/2012 at 12:21 am

> Theo em thì, chọn phần tử thứ k của dãy a . Đem so sánh với k phần tử đầu tiên của dãy b. Cách so sánh như sau . Nếu a[k] > b[k/2] thì k = k/2 làm tiếp ngược lại thì k = k/2 + k/4 .

> 0

> 0

**NQH** · 27/10/2012 at 10:27 am

> @xiuaj, ý tưởng này tương đối gần với ý tưởng tôi có; nhưng thiếu đa số các chi tiết, và độ phức tạp là bao nhiêu?

> 0

> 0

**zyx** · 27/10/2012 at 5:13 am

> Trong 2 dãy, dãy nào có phần tử đầu X lớn hơn thì tìm index nhỏ nhất j của phần tử lớn hơn X trong dãy kia. Rồi giảm k tùy theo index kia, và tìm tiếp.

> def bin_search(a, v, lo, hi):
>     """search for min j s.t. a[j] > v, j in lo..hi"""
>     if lo > hi:
>         return lo

>     mid = lo + (hi - lo)/2
>     if v < a[mid]:
>         return bin_search(a, v, lo, mid - 1)
>     else:
>         return bin_search(a, v, mid + 1, hi)

> def k_smallest(a, b, k):
>     ia, ib = 0, 0
>     while True:
>         if a[ia] > b[ib]:
>             a, b = b, a
>             ia, ib = ib, ia

>         # always working with: a[ia] <= b[ib]
>         j = bin_search(a, b[ib], ia, ia + k - 1) # j = argmin_i a[i] > b[0]

>         if j >= k:
>             return a[ia + k - 1]
>         else:
>             ia = j
>             k = k - j

> Lúc đầu em làm nhầm, vì tưởng slicing trong Python là reference, không ngờ nó copy cả list, chạy chậm kinh hoàng. Lỗi quá cơ bản.

> 1
> a = a[j:]

> 0

> 0

**zyx** · 27/10/2012 at 5:36 am

> Time complexity:

> worst case: $T(k) = \log(k) + T(k-1)$; $T(k) = \sum_{i=1}^k \log(k) = \log((k + 1)!) = O(k \log(k))$

> Khi 2 array đan xen nhau, ví dụ a = {0, 2, 4, 6}, b = {1, 3, 5, 7}

> best case: $O(\log(k))$

> Khi tất cả element của a nhỏ hơn b[0].

> average case: $T(k) = \log(k) + T(k/2); T(k) = \log(k) + \log(k/2) + \ldots log(1) \approx {\log^2(k)} - \log(k) \log(\log(k))$

> Không biết em estimate average complexity như thế có chính xác không. Xin anh Hưng chỉ giáo ạ.

> 0

> 0

**NQH** · 27/10/2012 at 10:30 am

> @xyz, cũng gần với ý tưởng tôi có. Nhưng worst-case là $\omega(k)$ thì chẳng hoá ra lại tệ hơn cả ý tưởng kiểu merge-sort?

> Lời giải của bạn và của xiuaj có một cái bottleneck là bắt đầu so sánh từ phần tử cuối của một trong hai dãy. Hãy bắt đầu từ một phần tử khác.

> 0

> 0

**numos** · 27/10/2012 at 4:09 pm

> E nghi loi giai nhu sau:

> Input: a[1..n], b[1..n], k

> Out: số nhỏ thứ k trong 2n số.

> Sol:

> 1. h = k; l1 = 1; r1 = k; l2 = 1; r2 = k.

> 2. while (h > 0) {

> 3. m1 = (l1 + r1) /2; m2 = (l2 + r2);

> 4. if (a[m1] > b[m2])

> 5. {

> 6. r1 = m1; l2 = m2;

> 7. }

> 8. else

> 9. {

> 10. l1 = m1; r2 = m2;

> 11. }

> 12. h = h/2;

> 13. }

> 14. if( a[r1] > b[r2]) return b[r2]

> 15. else return a[r1];

> Time complexity: T(k) = 1 + T(k/2) ->> T(k) ~ O(lg(n)).

> 1

> 1

**numos** · 28/10/2012 at 2:02 am

> Em xin sửa một chút:

> Trong dòng thứ 3:

> 3. m1 = (l1 + r1) /2; m2 = (l2 + r2);

> sửa lại là:

> 3. m1 = (l1 + r1) /2; m2 = (l2 + r2)/2;

> 0

> 0

**zyx** · 28/10/2012 at 4:38 am

> Thuật toán của bạn numos chạy trong O(log(k)), nhưng sẽ lỗi khi n = k = 2^i

> ví dụ trong test sau: n = 4, k = 4

> a = [0, 1, 2, 3], b = [1, 3, 4, 5]

> Thuật toán của bạn ra kết quả là 2, trong khi đúng là 3, vì khi so sánh bạn chọn số nhỏ hơn làm kết quả.

> Tôi thấy nếu sửa lại điều kiện h > 0 thành r1 + r2 > k + 1 (hoặc r1 + r2 > k – 1 với 0-based index) thì đúng hơn.

> r1, r2 có thể diễn giải là số phần tử trong a, b nhỏ hơn hoặc bằng kết quả cần tìm.

> Tôi code thuật toán của bạn bằng Python như sau:

> def k_smallest(a, b, k):
>     la, ra = 0, k - 1
>     lb, rb = 0, k - 1

>     while ra + rb > k - 1:
>         ma = la + (ra - la)/2
>         mb = lb + (rb - lb)/2

>         if a[ma] > b[mb]:
>             ra = ma
>             lb = mb
>         else:
>             la = ma
>             rb = mb

>     return b1 if a[ra] > b1 else a[ra]

> 0

> 0

**zyx** · 28/10/2012 at 4:41 am

> dòng 16: return b if a[ra] > b else a[ra]

> 0

> 0

**zyx** · 28/10/2012 at 4:43 am

> không hiểu sao b lại luôn ra là b1 nhỉ?

> 0

> 0

**NQH** · 28/10/2012 at 5:55 pm

> @numos, ý tưởng chuẩn; lời giải rất đẹp. (Tất nhiên để đánh chỉ số cho chính xác thì cần thử cẩn thật như zyx.)

> 0

> 0

**toannguyen** · 22/01/2013 at 9:12 am

> Em cũng muốn thử xem. Nhờ anh Hưng và các bạn kiểm tra hộ thuật toán cho em luôn ạ.

> Tạm gọi 2 dãy số là a[1..n] và b[1..n]

> Giả sử tất cả các số trong dãy đôi một khác nhau.

> Bây giờ bài toán yêu cầu cần lọc ra số thứ k. Em chuyển bài toán về dạng “chọn ra k số bé nhất”

> Từ yêu cầu của đề bài, ta sẽ cần phải chọn x số đầu tiên của dãy A và k-x số đầu tiên của dãy B (0<=x<k).

> Do các số trong dãy khác nhau đôi một, nên chỉ có duy nhất một vị trí của x thỏa mãn yêu cầu đề bài. Bây giờ, cần tìm vị trí x, kết quả sẽ là x số đầu tiên của dãy A và k-x số đầu tiên của dãy B.

> Thuật toán em chọn là chia nhị phân, độ phức tạp log(k).

> //C++ code

> int binary_search (){ //search for the position of x

> int left = 0; r = k;

> int temp = min(a[1], b[1]) – 1;

> a[0] = b[0] = min – 1;

> while ("") {

> int x = (left + right)/2;

> if (a[x] < b[k-x]) {

> if (b[k-x] b[k-x]

> if (a[x] < b[k-x+1]) return x;

> right = x – 1;

> }

> }

> Sau khi tìm đuợc vị trí x, ta dễ dàng xác định đuợc phần tử bé thứ k nhờ so sánh a[x] và b[k-x] và chọn số bé hơn.

> Thay đổi một chút sẽ giải quyết đuợc truờng hợp có các số giống nhau.

> 0

> 0

**toannguyen** · 22/01/2013 at 9:19 am

> Do copy paste từ compiler nên code bị lỗi. Em post lại code.

> int binary_search(){

> …. int left = 0; r = k;

> …. int temp = min(a[1], b[1]) – 1;

> …..a[0] = b[0] = min – 1;

> …..while (“”) {

> ……….int x = (left + right)/2;

> ……….if (a[x] < b[k-x]) {

> ……………if (b[k-x] < a[x+1]) return x;

> ……………left = x+1;

> ……….}

> ……….else {

> ……………if (a[x] < b[k-x+1]) return x;

> ……………right = x – 1;

> ……….}

> …..}

> 0

> 0

