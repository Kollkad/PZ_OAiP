#Дана строка. Если она представляет собой записть целого числа, то вывести 1, если вещественного (с дробной частью) - вывести 2,
#если строку нельзя преобразовать в число, то вывести 0. Считать, что дробная часть вещественного числа
#отделяется от его целой части десятичной точкой "."

def check_number_type(s):
  try:
    int_num = int(s)
    return 1
  except ValueError:
    try:
      float_num = float(s)
      return 2
    except ValueError:
      return 0


A = input('Введите необходимое значение на проверку: ')
Atype = check_number_type(A)
print(Atype)