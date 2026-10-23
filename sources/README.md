# ① Nguồn

Tầng này chứa tài liệu tham khảo bên ngoài và các ứng viên chưa biên tập. File đã đăng ký được giữ nguyên bytes: `validate` so SHA-256 với [registry.json](registry.json), và `.gitattributes` tắt chuyển đổi xuống dòng để checksum giống nhau trên mọi hệ điều hành.

| File | Nội dung |
|---|---|
| [registry.json](registry.json) | Danh mục nguồn: `id`, `kind`, `path`, `sha256` |
| [technical-references.json](technical-references.json) | Tài liệu học thuật hỗ trợ một số kết quả tổng quát |
| [candidates/catalog-72-v0.1.md](candidates/catalog-72-v0.1.md) | 72 ứng viên tuyển chọn (`SRC-CATALOG-72`). Đây là **kho dự trữ để mở rộng ngân hàng**. Một ứng viên chỉ được tính là đã nhập khi đã trở thành bài trong `knowledge/puzzles/` |

## Quy tắc

- Khi tìm được nguồn gốc của một bài, ghi vào `knowledge/puzzles/PZ-xxxx/provenance.json → external_sources` kèm định vị cụ thể (sách, trang, mã bài, URL), rồi cập nhật `external_source_status`.
- Muốn thêm một nguồn cục bộ: đặt file vào thư mục phù hợp trong `sources/`, rồi thêm một mục vào `registry.json` kèm `sha256`. Tính hash bằng lệnh:

  ```bash
  python -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" <file>
  ```

- Không đổi ID bài khi phát hiện nguồn mới.
