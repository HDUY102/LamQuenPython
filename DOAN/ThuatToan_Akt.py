def nhanMaTran(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Ma trận không hợp lệ.")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def chuyenViTriMaTran(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


def power_of_matrix_with_transpose(matrix, k):
    rows, cols = len(matrix), len(matrix[0])
    if rows != cols:
        raise ValueError("Lỗi.")

    if k == 1:
        return matrix

    transposed_matrix = chuyenViTriMaTran(matrix)
    result = matrix

    for _ in range(k - 1):
        result = nhanMaTran(result, transposed_matrix)

    return result


# Ví dụ
matrix = [[2, 1], [1, 1]]
k = 3
result = power_of_matrix_with_transpose(matrix, k)
print(result)
