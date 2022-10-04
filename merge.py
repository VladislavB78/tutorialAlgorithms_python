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


def main():
    first = [1, 20, 30]
    second = [30, 40]

    print(merge(first, second))


if __name__ == '__main__':
    main()
