[] Dữ liệu được dump từ Mongo về
    - Dữ liệu thường có các fields:
        + id: str
        + source: str (url/file)
        + content: str
        + has_embedding: bool
    - Mỗi role có quyền read, search, insert, update, delete, embed
    - Mỗi row dữ liệu sẽ có checkbox nhằm thao tác hàng loạt cho việc delete, embed
    - Các fields có thể update: source, content
    - Tính năng search_by_query dùng retrieval bằng milvus
    - Tính năng search_by_content dùng bm25 hoặc regex
[] Dữ liệu hội thoại dump từ elastic search về
    - Dữ liệu thường có các fields:
        + query: str
        + context: str
        + distance: float
