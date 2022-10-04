def merge(first, second):
    """Возвращает объединение двух упорядоченных массивов в один"""
    pA = pB = 0
    res = []
    while pA != len(first) and pB != len(second):
        if first[pA] <= second[pB]:
            res.append(first[pA])
            pA += 1
        else:
            res.append(second[pB])
            pB += 1

    while pA != len(first):
        res.append(first[pA])
        pA += 1
    while pB != len(second):
        res.append(second[pB])
        pB += 1

    return res


def squares(arr):
    """Возвращает массив возведённых в квадрат чисел, сохраняя упорядоченность"""
    i = 0
    while i < len(arr) and arr[i] < 0:
        i += 1

    pos = [el ** 2 for el in arr[i:]]
    neg = [el ** 2 for el in arr[:i]]
    neg.reverse()

    return merge(pos, neg)


def main():
    s = [0, 1, 2, 3, 4, 5]
    c = [-20, -15, -10, -5]

    print(squares(s))


if __name__ == '__main__':
    main()
