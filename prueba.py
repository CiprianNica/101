def make_identity_matrix(col: int, row: int)-> list[list]:
    matrix : list = []
    for i in range(0, row):
        matrix.append([])
        for j in range(0, col):
            matrix[i].append(1)
    return matrix

print(make_identity_matrix(5, 4))