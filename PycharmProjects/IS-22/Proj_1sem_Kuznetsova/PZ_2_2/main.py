chislo = input("Введите число: ")
proverka = len(chislo)
if proverka == 3 and chislo.isdigit():
    chislo = chislo[-1] + chislo[:-1]
    print(chislo)
else:
    print("Нарушено условие задачи")
