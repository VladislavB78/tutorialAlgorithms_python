def diagonal_sum(mat):
    """Возвращает сумму диагональных элементов квадратной матрицы"""
    res = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j or i + j == len(mat) - 1:
                res += mat[i][j]
    return res


def main():
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    print(diagonal_sum(mat))


if __name__ == '__main__':
    main()
