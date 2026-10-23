# Toolchain build PDF

## Thành phần

| Công cụ | Phiên bản đã kiểm tra | Ghi chú |
|---|---|---|
| Python | 3.14 (tối thiểu 3.11) | chỉ dùng thư viện chuẩn |
| MiKTeX | 26.5 / XeTeX 4.18 (Windows) | hoặc TeX Live ≥ 2024 |
| latexmk | 4.88 | không bắt buộc; build gọi `xelatex` trực tiếp |

Font **Charis SIL** (thân bài) và **Inter** (tiêu đề, nhãn) được nạp từ `assets/fonts/` qua `fontspec`. Vì vậy không cần cài font vào máy, và mọi máy đều dùng cùng một bộ font.

Các gói LaTeX: `fontspec geometry amsmath amssymb mathtools booktabs enumitem needspace tikz` (cùng các thư viện TikZ `arrows.meta calc positioning shapes.geometric`) và `xcolor graphicx fancyhdr lastpage titlesec hyperref adjustbox wrapfig`.

## Cài đặt

### Windows: MiKTeX dùng chung

```powershell
python tools/setup_tex.py
```

Script dùng WinGet cài MiKTeX cho tài khoản hiện tại, cập nhật gói, bật chế độ tự cài gói thiếu và cài latexmk (dùng Perl đi kèm Git for Windows nếu có). MiKTeX được cài vào `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64` và thêm vào PATH, nên các project khác trên máy cũng dùng được. Sau khi cài, mở lại terminal hoặc IDE rồi kiểm tra bằng `xelatex --version`. Thông tin cài đặt được ghi vào `build/toolchain/`.

Nguồn chính thức: [MiKTeX download](https://miktex.org/download), [quản lý gói bằng CLI](https://docs.miktex.org/manual/miktex-packages.html), [tự cài gói thiếu](https://miktex.org/kb/just-enough-tex).

### Linux / macOS: TeX Live

```bash
sudo apt install texlive-xetex texlive-latex-extra texlive-pictures texlive-fonts-recommended   # Debian/Ubuntu
brew install --cask mactex-no-gui                                                              # macOS
```

## Build

```bash
python build.py                       # validate → render → XeLaTeX ×2 → phát hành vào publications/
python build.py --render-only         # dừng sau bước sinh LaTeX
python build.py --no-release          # biên dịch nhưng giữ PDF trong build/
python tools/puzzles.py build --edition <id>   # build một ấn phẩm khác
```

Các bước:

1. Validate toàn bộ hệ thống; có lỗi thì dừng.
2. Render `build/<edition>/tex/{student,instructor}.tex`, rồi kiểm tra bản sinh viên không lộ ID nội bộ hay placeholder chưa thay.
3. So checksum mọi file đầu vào trước và sau khi render. Nếu renderer làm thay đổi file nào thì báo lỗi.
4. Biên dịch trong thư mục tạm. Build thất bại nếu log có `Overfull \hbox`, `Missing character` hoặc cảnh báo `wrapfig`.
5. Chỉ khi cả hai PDF đều thành công mới chép vào `build/<edition>/pdf/` và phát hành sang `publications/<output_name>-{student,instructor}.pdf`. Build hỏng không bao giờ ghi đè PDF đã phát hành.

## Đối chiếu giữa các máy

`build/<edition>/manifest.json` ghi checksum đầu vào/đầu ra và phiên bản XeLaTeX. Thư mục `logs/` giữ `xelatex-version.txt` cùng các file `.log` và `.fls`. MiKTeX cập nhật gói liên tục, nên cùng một phiên bản bộ cài chưa chắc đã cho cùng phiên bản từng gói. Khi PDF giữa hai máy khác nhau, hãy so các file này trước.
