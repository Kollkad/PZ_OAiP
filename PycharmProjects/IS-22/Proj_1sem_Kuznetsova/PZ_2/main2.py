Дано 3х значное число. В нем зачеркунли первую справа цифру и приписали ее слева. Вывести полученное число

chislo = int(input())
if chislo > 99 and chislo < 1000:
    chislo2 = chislo % 10
    chislo //= 10
    chislo = chislo2 * 100 + chislo
    print(chislo)
else:
    print('Нарушено условие задачи')

