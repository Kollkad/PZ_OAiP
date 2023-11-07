#задание для всех №3 попытка 2
#Ввести двузначное число. Если сумма цифр числа четная, то увеличить его на 2, в противном случае уменьшить его на 2
a = input('Введите число а: ')

while type(a) != int:
  try:
    a = int(a)
  except ValueError:
    print("Ошибка, а != int")
    a = input("Введите а еще раз: ")

sum = 0
c = a
if c < 0:
  c *= -1
while (c != 0):
    sum = sum + c % 10
    c = c // 10

if (a > 9 and a < 100) or (a > -100 and a < -9):
  if sum % 2 == 0:
    a = a + 2
    print(a)
  else:
    a = a - 2
    print(a)
else:
  print("Ошибка, а в недопустимом диапазоне")