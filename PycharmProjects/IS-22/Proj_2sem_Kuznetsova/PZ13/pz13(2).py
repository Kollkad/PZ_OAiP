#Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и последних строках и столбцах
#матрицы Matr2 произвольного размера
from random import randint

Matr2 = [[randint(1, 10) for i in range(3, 7)]#stolbtsov
            for i_stroka in range(3, 7)]#kolvo strok
print('Матрица до ', Matr2)
Matr1 = [stroki[1:-1] for stroki in Matr2[1:-1]]
print('Урезанная матрица', Matr1)