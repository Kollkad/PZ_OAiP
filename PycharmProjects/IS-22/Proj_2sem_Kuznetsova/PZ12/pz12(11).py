#В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.
from random import randint

n = int(input("Введите количество элементов в последовательности: "))
posled = [randint(1, 10) for _ in range(n)]
print("2. Список элементов", posled)

firstthird_2 = list(filter(lambda x: x[0] < (len(posled) // 3), enumerate(posled)))
srednee = sum(map(lambda x: x[1], firstthird_2)) / len(firstthird_2)

print('2. Первая треть элементов списка:', firstthird_2)
print('2. Среднее арифметическое первой трети:', srednee)