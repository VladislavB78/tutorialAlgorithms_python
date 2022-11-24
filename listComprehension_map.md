<!--+ [Your text](#your-text)-->

## 1. Найти все числа от 1 до 1000, которые делятся на 17.
```python
res = [el for el in range(1, 1000) if el % 17 == 0]
```

## 2. Найти все числа от 1 до 1000, которые содержат 2.
```python
res = [el for el in range(1, 1000) if '2' in str(el)]
```
## 3. Найти все числа от 1 до 10000, которые являются палиндромом.
```python
res = [el for el in range(10, 10000) if str(el) == str(el)[::-1]]
```
## 4. Посчитать количество пробелов в строке.
```python
s = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
res = [s.count(' ')]
```
## 5. Есть любая последовательность непробельных символов латинского алфавита. <br/> Удалить все гласные из этого слова.
```python
s = "Asimplesentencehasthemostbasicelementsthatmakeitasentence:asubjectaverbandacompletedthought"
res = ''.join([el for el in s if el not in 'aeuioAEUIO'])
```
## 6. На входе строка со словами, разделенными через 1 пробел. <br/> Найти все слова, длина которых не больше 5.
```python
s = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
res = [word for word in s.split() if len(word) <= 5]
```
## 7. На входе строка со словами, разделенными через 1 пробел. <br/> Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.
```python
s = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
res = {key: val for key, val in zip(tuple(s.upper().split()), tuple(map(lambda el: len(el), tuple(s.split()))))}
```
## 8. На входе предложение со всеми пробельными и непробельными символами латинского алфавита. <br/> Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.
```python
s = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
res = {el.upper() for el in s if el.isalpha()}
```
## 9. На входе список чисел, получить список квадратов этих чисел.
```python
lst = [1, 3, 10, -4, 0]
res1 = [el ** 2 for el in lst]
res2 = list(map(lambda el: el ** 2, lst))
```
## 10. На входе список координат. <br/> Найти все точки, которые принадлежат прямой y = 5 * x - 2. <br/> На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0).
```python
lst = [(1, 1), (2, 3), (2, 8), (5, 3), (0, -2)]
res = {key: val for key, val in zip(tuple(filter(lambda x: x[1] == 5 * x[0] - 2, lst)), tuple(map(lambda el: (el[0]**2 + el[1]**2)**0.5, list(filter(lambda x: x[1] == 5 * x[0] - 2, lst)))))}
```
## 11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.
```python
res1 = [el ** 2 for el in range(2, 27, 2)]
res2 = list(map(lambda el: el**2, range(2, 27, 2)))
```
## 12. На входе список из координат точек на плоскости. <br/> Найти расстояние до самой удаленной точки от начала координат (0, 0) в первой четверти.
```python
lst = [(-1, 1), (2, 3), (-2, -8), (5, 3), (0, -2)]
res = max(list(map(lambda nums: (nums[0] ** 2 + nums[1] ** 2) ** 0.5, list(filter(lambda el: el[0] >= 0 and el[1] >= 0, lst)))))
```
## 13. На входе два списка чисел. Получить пары сумм и разниц.
```python
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
res = list(zip(list(map(lambda f, s: f+s, nums_first, nums_second)), list(map(lambda f, s: f-s, nums_first, nums_second))))
```
## 14. На входе список строк из чисел. <br/> Найти четные квадраты этих чисел. <br/> Ответ записать снова в список из строк, но уже отфильтровать все четные квадраты.
```python
lst = ['43141', '32441', '431', '4154', '43121']
res1 = [str(int(num) ** 2) for num in lst if int(num) % 2 == 0]
res2 = list(map(lambda el: str(int(el) ** 2), list(filter(lambda num: int(num) % 2 == 0, lst))))
```
