#задание для всех №2
#Ввести число. Если оно четное, разделить его на 4, если не четное - умножить на 5

a = input('Введите число 1: ')
while type(a) != int:
  try:
    a = int(a)
  except ValueError:
    print('Ошибка, введите число 1 еще раз: ')
    a = input('Введите число 1: ')

if a % 2 == 0:
  a = a / 4
else:
  a = a * 5

print(a)