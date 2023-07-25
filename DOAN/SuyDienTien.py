# Khởi tạo cơ sở tri thức
kb = {
    ('is_a', 'cat', 'animal'),
    ('is_a', 'dog', 'animal'),
    ('is_a', 'animal', 'organism'),
    ('has', 'cat', 'fur'),
    ('has', 'dog', 'fur'),
    ('eats', 'cat', 'meat'),
    ('eats', 'dog', 'meat')
}


def backward_chaining(kb, query):
    # Kiểm tra xem truy vấn có trực tiếp xuất hiện trong cơ sở tri thức hay không
    if (query,) in kb:
        return True

    # Tìm tất cả các luật có kết quả là truy vấn
    for premise, conclusion in kb:
        if conclusion == query:
            # Kiểm tra xem các điều kiện trong luật có thể suy ra truy vấn hay không
            if all(backward_chaining(kb, p) for p in premise):
                return True

    # Nếu không tìm thấy luật hoặc giả định nào có thể suy ra truy vấn, trả về False
    return False
