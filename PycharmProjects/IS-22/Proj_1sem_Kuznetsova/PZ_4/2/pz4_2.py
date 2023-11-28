# Дано целое число N (>0). Найти сумму 1^N + 2^N-1 + ... + N^1


n = input('Введите n: ')
while type(n)!=int:
  try:
    n = int(n)
  except:
    print('Неверный ввод')
    n = input('Заново введите n:')

sum = 0
for i in range (n):
  sum += ((i +1) ** (n -i))
print(sum)