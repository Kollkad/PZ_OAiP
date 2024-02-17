#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность
# из целых положительных и отрицательных чисел. Сформировать новый текстовый файл следующего вида,
# предварительно выполнив требуемую обработку элементов:

#Исходные данные:
#Колличество элементов
#Сумма элементов:
#Элементы до n-1 умножены на элемент n^

from random import randint

file_1 = open('file1.txt', 'w')
for number in (randint(-100, 100) for _ in range(10)):
    file_1.write(str(number) + '\n')
file_1.close()

file_1 = open('file1.txt', 'r')
soder = file_1.readlines()
file_1.close()

soder = [line.rstrip() for line in soder]
soder_int = [int(line) for line in soder]
#доп значения
stroka = ''
kolvo = 0

file_2 = open('file2.txt', 'w')
file_2.write('Исходные данные:')
for i in soder:
    stroka += str(i)
    stroka += ' '
file_2.write(stroka + '\n')

file_2.write('Количество элементов:')
file_2.write(str(len(soder)) + '\n')

file_2.write('Сумма элементов:' )
file_2.write(str(sum(soder_int)) + '\n')

file_2.write('Элементы до n-1 умножены на элемент n:' + '\n')
for i in range(1, 10):
    spisok_elem = []
    for n in range(i):
        spisok_elem.append(soder_int[i] * soder_int[n])
    file_2.write(str(spisok_elem) + '\n')

file_2.close()




