#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из результата вновь
#вычли сумму его цифр и т.д. Через сколько таких действий получится нуль?

def konetz():
  def countInt(k):
    t = 0
    while k != 0:
      t = t + (k  % 10)
      k //=10
    return t

  Int_Number = input('Введите число: ')

  while type(Int_Number) != int:
    try:
      Int_Number = int(Int_Number)
    except ValueError:
      print('Ошибка ввода, введите число еще раз: ')
      Int_Number = input()

  kolvo = 0

  while Int_Number != 0:
    Int_Number = Int_Number - countInt(Int_Number)
    kolvo += 1
  print(f'Нужно {kolvo} шагов, чтоб придти к нулю')

konetz()