#Составить генератор (yield), который преобразует все буквенные символы в заглавные.

def upp_generator(old_string):
    for char in old_string:
        if char.isalpha():
            yield char.upper()
        else:
            yield char

old_string = str(input('Введите текст: '))
result = ''.join(upp_generator(old_string))
print('Преобразованный текст: ', result)

