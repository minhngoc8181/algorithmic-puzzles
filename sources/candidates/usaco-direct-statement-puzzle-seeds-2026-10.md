# USACO — nguồn puzzle hóa đọc trực tiếp từ đề thi (2024)

**Ngày khảo sát:** 2026-10-24. **Nguồn chính thức:** [USACO January 2024](https://usaco.org/index.php?page=jan24results), [USACO December 2024](https://usaco.org/index.php?page=dec24results).

Bổ sung **15 bài gốc** có URL đến đề của Ban tổ chức, ưu tiên những luật có thể mô phỏng bằng tay (đây là **gợi ý phóng tác**, không phải đề hoàn chỉnh hay lời giải đúng đã chứng minh). Trang statement đã được mở, các luật tóm tắt dựa vào phần văn bản đọc được; chưa kiểm tra editorial, tính tối ưu puzzle hoặc quyền tái sử dụng. Vì thế phân biệt `statement_opening_read` với `solution_proven` (chưa đạt).

| # | Kỳ/nhóm | Bài gốc | Hạt nhân puzzle dự kiến (tóm lược luật) | Ưu tiên | Đối chiếu sơ bộ | Mức kiểm tra |
|---:|---|---|---|:---:|---|---|
| 01 | 2024-01 Platinum | [Island Vacation](https://usaco.org/index.php?page=viewproblem2&cpid=1380) | Đi ngẫu nhiên trên mạng đảo, mỗi cầu đi nhiều nhất một lần; hạ xuống mạng rất nhỏ và hỏi xác suất kết thúc | B | Khác PZ-0042 về mô hình đi đường | Đã đọc luật và ví dụ trên trang chính thức |
| 02 | 2024-01 Platinum | [Merging Cells](https://usaco.org/index.php?page=viewproblem2&cpid=1381) | Các tế bào nằm trên hàng, ngẫu nhiên ghép hai khối kề nhau, khối thắng giữ nhãn của khối lớn hơn; tìm xác suất nhãn cuối | A | Gần PZ-0040/AP-21 về ghép kề, nhưng ngẫu nhiên và danh tính nhãn | Đã đọc luật và ví dụ trên trang chính thức |
| 03 | 2024-01 Platinum | [Mooball Teams III](https://usaco.org/index.php?page=viewproblem2&cpid=1382) | Chia hai đội theo tọa độ sao cho ngăn cách bằng một đường ngang hoặc dọc; cần đọc tiếp mục tiêu chi tiết | B | Gần PZ-0045 về chia nhóm nhưng ràng buộc hình học | Đã đọc phần đầu luật chính thức |
| 04 | 2024-01 Gold | [Walking in Manhattan](https://usaco.org/index.php?page=viewproblem2&cpid=1377) | Bò đi trên các đường thẳng đứng/ngang vô hạn, gặp giao lộ thì rẽ theo chẵn lẻ thời gian đã đi; hỏi vị trí sau t bước | A | Mô phỏng quy tắc và parity, chưa thấy trùng trực tiếp | Đã đọc luật chính thức |
| 05 | 2024-01 Gold | [Cowmpetency](https://usaco.org/index.php?page=viewproblem2&cpid=1378) | Biết một số lần kỷ lục điểm năng lực xuất hiện đầu tiên; tìm hay đếm những dãy điểm có thể phù hợp lời nhớ | A | Gần nhóm suy luận thông tin nhưng cần đối chiếu | Đã đọc luật và ví dụ chính thức |
| 06 | 2024-01 Gold | [Nap Sort](https://usaco.org/index.php?page=viewproblem2&cpid=1379) | Đồng thời hai cách sắp xếp: tự lấy số nhỏ nhất tốn thời gian theo kích thước đống, hoặc giao trợ lý thức dậy sau đúng a_i giây | A | Mới sơ bộ: sắp xếp không đồng bộ và tối ưu lịch | Đã đọc luật chính thức |
| 07 | 2024-12 Platinum | [All Pairs Similarity](https://usaco.org/index.php?page=viewproblem2&cpid=1452) | Đánh giá mức giống nhau của những thẻ nhị phân bằng giao/hợp bit; chọn bộ thẻ nhỏ để thảo luận chiến thuật so sánh | B | Gần PZ-0017/PZ-0031 về bit nhưng khác mô hình | Đã đọc luật chính thức |
| 08 | 2024-12 Platinum | [It's Mooin' Time](https://usaco.org/index.php?page=viewproblem2&cpid=1453) | Đổi ký tự với chi phí từng vị trí để tạo ít nhất k mẫu con M rồi O; rút gọn thành bài sửa mật mã ít chi phí | B | Gần bài biến đổi chuỗi, cần sàng lọc insight | Đã đọc luật chính thức |
| 09 | 2024-12 Platinum | [Maximize Minimum Difference](https://usaco.org/index.php?page=viewproblem2&cpid=1454) | Xếp hoán vị 0..n-1 sao cho khoảng cách nhỏ nhất giữa hai vị trí kề nhau lớn nhất; thêm các vị trí cố định | A | Mới sơ bộ: cực trị hoán vị có chốt cố định | Đã đọc luật và ví dụ chính thức |
| 10 | 2024-12 Gold | [Cowdependence](https://usaco.org/index.php?page=viewproblem2&cpid=1449) | Chia dãy thành nhóm cùng nhãn, mỗi cặp trong nhóm cách nhau tối đa x vị trí; tối thiểu số nhóm | A | Có nét gần cảm biến/cover nhưng ràng buộc khác | Đã đọc luật và ví dụ chính thức |
| 11 | 2024-12 Gold | [Interstellar Intervals](https://usaco.org/index.php?page=viewproblem2&cpid=1450) | Tô các cặp đoạn đỏ rồi xanh có độ dài bằng nhau, các đoạn chọn không chồng; đếm hình tô thỏa các điểm màu bắt buộc | A | Mới sơ bộ: tiling 1D bằng cặp block màu | Đã đọc luật và ví dụ chính thức |
| 12 | 2024-12 Gold | [Job Completion](https://usaco.org/index.php?page=viewproblem2&cpid=1451) | Mỗi công việc có thời điểm muộn nhất được bắt đầu và thời lượng thực hiện; tối đa số việc làm được | B | Gần AP-32 lịch thưởng nhưng deadline áp dụng cho thời điểm bắt đầu | Đã đọc luật chính thức |
| 13 | 2024-12 Silver | [Cake Game](https://usaco.org/index.php?page=viewproblem2&cpid=1446) | Hai người có hai loại nước đi bất đối xứng: một người ghép hai bánh kề nhau, người còn lại lấy bánh ở hai đầu | A | Gần AP-20/AP-21/PZ-0027 nhưng thứ tự nước đi khác | Đã đọc luật và ví dụ chính thức |
| 14 | 2024-12 Silver | [Deforestation](https://usaco.org/index.php?page=viewproblem2&cpid=1447) | Chọn đốn nhiều cây nhất sao cho trong mỗi đoạn giám sát vẫn giữ tối thiểu t_i cây | A | Gần AP-31 cover nhưng dạng quota từng đoạn khác | Đã đọc luật và ví dụ chính thức |
| 15 | 2024-12 Silver | [2D Conveyor Belt](https://usaco.org/index.php?page=viewproblem2&cpid=1448) | Trên bảng ô mũi tên, đặt hướng cho ô chưa biết để giảm số ô mắc kẹt trong chu trình không ra khỏi bảng | A | Mới sơ bộ: đường thoát và chu trình có hướng | Đã đọc luật chính thức |

## Gợi ý biên tập

1. **Đáng dựng prototype trước:** `Cake Game`, `Maximize Minimum Difference`, `Interstellar Intervals`, `2D Conveyor Belt`, `Merging Cells`, `Cowmpetency` — chọn n nhỏ có lời giải tay vừa đủ bất ngờ.
2. **Tránh tái chế nguyên xi:** `Cake Game` và `Merging Cells` cần so rõ luật với PZ-0027 và PZ-0040; `Job Completion` với AP-32; `Deforestation` với AP-31.
3. Mở editorial chính thức, kiểm tra lời giải cực trị, tìm phản ví dụ với heuristic và thử vài biến thể nhỏ để chọn câu đố thực sự mới.
4. Không sao chép đề, biểu đồ hoặc lời giải nguyên văn vào ấn phẩm; ghi provenance đầy đủ khi tạo tri thức mới.

**Không sửa bất kỳ PZ hoặc AP hiện hữu trong nhánh nghiên cứu này.**
