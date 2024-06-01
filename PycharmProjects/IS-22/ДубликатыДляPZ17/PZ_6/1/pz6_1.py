#Дан список размера N и целые числa K и L (1 < K < L < N). Найти сумму элементов списка с номерами от K до L включительно

N = int(input('Введите размер списка N = '))
A = list(range(1, N+1))

K, L = input('Введите K = '), input('Введите L = ')
def prov(n):
  while type(n) != int:
    try:
      n = int(n)
    except ValueError:
      print(f'Ошибка ввода, введите целое число, а не "{n}": ')
      n = input()
  return n

K = prov(K)
L = prov(L)

if 1 < K < L < N:
  sum_elements = sum(A[K-1:L])
  print('Сумма элементов от K до L равна ', sum_elements)
else:
  print('Ошибка ввода, значения не соответствуют условию')