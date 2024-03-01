#В матрице найти среднее арифметическое элементов последних двух столбцов
from random import randint

matritsa = [[randint(1, 10) for i in range(4)]#stolbtsov
            for i_stroka in range(3)]#kolvo strok
print('Матрица: ', matritsa)

sum_in_stroka = [sum(stolbets[-2:]) for stolbets in matritsa]
print('Суммы для последних двух элементов каждой строки: ', sum_in_stroka)
srednee = sum(sum_in_stroka) / len(sum_in_stroka) / 2
print('Среднее арифметическое элементов последних двух столбцов равно', srednee)