# String

+ [Compress](#compress)

## Compress

Возвращает строку - количество вхождения каждого элемента  ["a", "b", "b"] -> 'ab2'

```python
def compress(elems):
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
    print(compress(chrs))


if __name__ == '__main__':
    main()
```
