# Arrays

+ [Squares of sorted array](#squares-of-sorted-array)
+ [Merge to sorted arrays](#merge-to-sorted-arrays)

## Squares of sorted array

Возвращает массив возведённых в квадрат чисел, сохраняя упорядоченность

```python
def merge(first, second):
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
```


## Merge to sorted arrays

Возвращает объединение двух упорядоченных массивов в один

```python
def merge(first, second):
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
```
