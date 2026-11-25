4. Массивы (списки)

4.1 Изменение элементов массива

1. В массиве заменить все числа, большие данного числа,
на среднее арифметическое всех чисел массива.

arr = [10, 25, 5, 40, 15]
x = 20

avg = sum(arr) / len(arr)

for i in range(len(arr)):
    if arr[i] > x:
        arr[i] = avg

print("Среднее арифметическое:", avg)
print("Измененный массив:", arr)

2. Дан массив. Заменить все числа, меньшие
последнего элемента массива, на первый элемент.

arr = [12, 5, 20, 3, 10]
first = arr[0]
last = arr[-1]

for i in range(len(arr)):
    if arr[i] < last:
        arr[i] = first

print("Измененный массив:", arr)

3. Поменять местами наибольший и наименьший элементы массива.

arr = [10, 3, 45, 2, 18]

min_idx = arr.index(min(arr))
max_idx = arr.index(max(arr))

# Меняем местами элементы по индексам
arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]

print("Результат:", arr)

4.2 Поиск, условия и агрегация

1. Определить, содержит ли массив данное число $x$.

arr = [4, 8, 15, 16, 23, 42]
x = int(input("Введите x: "))

if x in arr:
    print("Число присутствует в массиве")
else:
    print("Число отсутствует")

    
2. Найти количество четных чисел в массиве.

arr = [1, 2, 3, 4, 5, 6, 7, 8]

count = 0
for num in arr:
    if num % 2 == 0:
        count += 1

print("Количество четных чисел:", count)

3. Найти количество чисел в массиве, которые делятся на 3,
но не делятся на 7.

arr = [3, 21, 9, 14, 12, 42, 15]

count = 0
for num in arr:
    if num % 3 == 0 and num % 7 != 0:
        count += 1

print("Количество элементов:", count)

4. Определите, каких чисел в массиве больше: которые
делятся на первый элемент массива или которые делятся
на последний элемент массива.

arr = [2, 4, 5, 6, 8, 10, 3]
first = arr[0]
last = arr[-1]

count_first = 0
count_last = 0

for num in arr:
    if num % first == 0:
        count_first += 1
    if num % last == 0:
        count_last += 1

if count_first > count_last:
    print("Больше чисел, делящихся на первый элемент")
elif count_last > count_first:
    print("Больше чисел, делящихся на последний элемент")
else:
    print("Количество одинаковое")

    
5. Найдите сумму и произведение элементов массива.

arr = [1, 2, 3, 4, 5]

total_sum = sum(arr)

product = 1
for num in arr:
    product *= num

print("Сумма:", total_sum)
print("Произведение:", product)

6. Найдите сумму четных чисел массива.
arr = [1, 2, 3, 4, 5, 6, 7, 8]

even_sum = 0
for num in arr:
    if num % 2 == 0:
        even_sum += num

print("Сумма четных чисел:", even_sum)