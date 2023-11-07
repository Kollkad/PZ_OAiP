#задание для всех №5
#Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2
a = input("Введите число a: ")
b = input("Введите число b: ")

while type(a) != int:
  try:
    a = int(a)
  except ValueError:
    print("Ошибка, а != int")
    a = input("Введите а еще раз: ")

while type(b) != int:
  try:
    b = int(b)
  except ValueError:
    print("Ошибка, b != int")
    b = input("Введите b еще раз: ")

c = a + b

if c % 5:
  print("С не кратно 5 и равно ", c)
  c = c - 2
  print("c = ", c)
else:
  print("С кратно 5 и равно ", c)
  c = c + 1
  print("c = ", c)