# Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами(одним или несколькими).
# Преобразовать каждое слово в строке, заменив в нем все предыдущие вхождения его последней буквы на символ "." (точка)
# Например "МИНИМУМ" ---> ".ИНИ.УМ"
phrase = input('Введите фразу ')
phrase = phrase.upper()
phrase_new = ''

slovo = 0
bukva = ''
position = len(phrase) - 1

while position >= 0:
    if slovo:
        if phrase[position] == bukva:
            phrase = phrase[:position] + '.' + phrase[position + 1:]
        if phrase[position] == ' ':
            slovo = 0
    else:
        if phrase[position] != ' ':
            slovo = 1
            bukva = phrase[position]

    position -= 1

print('Преобразованная строка выглядит следующим образом: ', phrase)