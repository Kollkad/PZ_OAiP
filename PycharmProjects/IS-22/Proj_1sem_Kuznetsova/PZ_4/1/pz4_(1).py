# Дано вещественное число Х и целое число N (>0). Найти значение выражения Х - Х^3/(3!) + X^5/(5!) - ....
# ... +((-1)^N)-X^(2N+1))/((2N+1)!) (N! = 1 *2*3...N). Полученное число является приближенным значением функции sin
# В точке Х

n = input('введите n:')
while type(n)!=int:
  try:
    n = int(n)
  except:
    print('Неверный ввод')
    n = input('Заново введите n:')

x = input('Введите x:')
while type(x)!=float:
  try:
    x = float(x)
  except:
    print('Неверный ввод')
    x = input('Заново введите x:')

s = x
xx = x
nn = 1
znak = 1

for i in range(2, n+1):
  xx *= x**2
  nn *= (2*i-1)*(2*i-2)
  znak *= -1
  s += znak * xx / nn

print(s)