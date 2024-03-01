import random
from random import randint
from functools import reduce
n = int(input("Введите количество элементов в последовательности: "))

posld = []
for i in range(n):
    posld.append(randint(1, 10))
print('1. Список элементов', posld)
firstthird = posld[:n//3]
srednee = sum(firstthird) / len(firstthird)
print("1. Первая треть элементов: ", firstthird)
print("1. Среднее арифметическое первой трети: ", srednee)

posled = [random.randint(1, 10) for _ in range(n)]
print("2. Список элементов", posled)
firstthird_2 = list(filter(lambda x: posled.index(x) < len(posled) // 3, posled))
print('2. Первая треть элементов списка:', firstthird_2)
print('2. Среднее арифметическое первой трети:', reduce(lambda x, y: x + y, firstthird_2) / len(firstthird_2))

#проврка
print('3. Список элементов', posld)
firstthird_3 = list(filter(lambda x: posld.index(x) < len(posld) // 3, posld))
print('3. Первая треть элементов списка:', firstthird_3)
print('3. Среднее арифметическое первой трети:', reduce(lambda x, y: x + y, firstthird_3) / len(firstthird_3))



#1вариант дефолт
#2новый список, новый способ
#3вариант с тем же списком, но новым способом(проверка соответствия ответа)





