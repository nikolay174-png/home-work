def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('количество строк матрицы:'))
m = int(input('количество столбцов матрицы:'))
value = input(f'значения матрицы:')
print('-------' * m)
matrix = get_matrix(n, m, value)