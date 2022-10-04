def compress(elems):
    """Возвращает строку - количество вхождения каждого элемента"""
    res = ''
    i, j = 0, 1
    while i < len(elems):
        while j < len(elems) and elems[i] == elems[j]:
            j += 1

        if j - i > 1:
            res += elems[i] + str(j - i)
            i = j
        else:
            res += elems[i]
            i += 1
        j += 1
    return res


def main():
    chrs = ["a", "b", "b", "c", "c", "c"]
    chrs2 = ["a", "b", "c"]
    chrs3 = ["c", "c", "c"]

    print(compress(chrs3))


if __name__ == '__main__':
    main()
