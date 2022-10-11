# Matrix

+ [Sum of diagonal elements](#sum-of-diagonal-elements)

## Sum of diagonal elements

Возвращает сумму элементов главной и побочной диагонали квадратной матрицы

```python
def diagonal_sum(mat):
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
```
