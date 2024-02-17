text = open('text18-19.txt', 'r', encoding='utf-16 LE')

read_file = text.readlines()
if read_file[0][0] == '\ufeff':
    read_file[0] = read_file[0][1:]
print(read_file)

count_letters = 0
for i in read_file:
    count_letters += sum([1 for letter in i if letter.isalpha()])
print("Количество символов, принадлежащих к группе букв:", count_letters)

new_text = open('nizniy.txt', 'w')
text_lower = [i.lower() for i in read_file]

print("Содержимое файла с символами верхнего регистра замененными на нижний:", text_lower)

for i in text_lower:
    new_text.write(i)

text.close()
new_text.close()
