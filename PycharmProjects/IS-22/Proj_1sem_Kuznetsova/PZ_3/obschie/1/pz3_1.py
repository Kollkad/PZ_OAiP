#задание для всех №1
#Ввести 2 числа. Если их произведение отрицательно, умножить его на 8,
#в противном случае увеличить его в 1.5 раза

a, b = input('Введите число 1: '), input('Введите число 2: ')
while type(a) != int:
  try:
    a = int(a)
  except ValueError:
    print('Ошибка, введите число 1 еще раз: ')
    a = input('Введите число 1: ')
while type(b) != int:
  try:
    b = int(b)
  except ValueError:
    print('Ошибка, введите число 2 еще раз: ')
    b = input('Введите число 2: ')

c = a * b
if c < 0 :
  c = c * 8
  print(c)
else:
  c = c * 1.5
  print(c)