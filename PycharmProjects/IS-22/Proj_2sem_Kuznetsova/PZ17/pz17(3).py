# перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
#вложенных подкаталогов выводить не нужно.

# перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в PZ_7(1).py. Вывести в консоль информацию о размере
#файлов в папке test.

# перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#консоль. Использовать функцию basename () (os.path.basename()).

# перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
#привязанной к нему программе. Использовать функцию os.startfile().

# удалить файл text.txt
import os
#ПОСЛЕ КАЖДОГО ЗАПУСКА !!!!! проверить папку дубликаты
print('текущий каталог', os.getcwd())
os.chdir('../PZ11')
print('текущий каталог сменился на', os.getcwd())
# перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.
print('______________________________________________')
print('№1 Папки и каталоги без подкаталогов в PZ11', os.listdir())
print('______________________________________________')

# перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в PZ_7(1).py. Вывести в консоль информацию о размере
#файлов в папке test.
os.chdir('../..')
print('текущий каталог сменился на', os.getcwd())
#Папка test
if not os.path.isdir('test/test1'):
    os.mkdir('test/test1')
    print('Создание паки test и test1')

if not os.path.isfile("C:/Документы/PycharmProjects/IS-22/test/pz6_2(2).py"):
    os.replace("C:/Документы/PycharmProjects/IS-22/Proj_1sem_Kuznetsova/PZ_6/2/pz6_2(2).py", "C:/Документы/PycharmProjects/IS-22/test/pz6_2(2).py")

if not os.path.isfile("C:/Документы/PycharmProjects/IS-22/test/pz6_2.py"):
    os.replace("C:/Документы/PycharmProjects/IS-22/Proj_1sem_Kuznetsova/PZ_6/2/pz6_2.py", "C:/Документы/PycharmProjects/IS-22/test/pz6_2.py")

if not os.path.isfile("C:/Документы/PycharmProjects/IS-22/test/test1/pz7_1.py") and not os.path.isfile("C:/Документы/PycharmProjects/IS-22/test/test1/text.txt"):
    os.replace("C:/Документы/PycharmProjects/IS-22/Proj_1sem_Kuznetsova/PZ_7/1/pz7_1.py", "C:/Документы/PycharmProjects/IS-22/test/test1/pz7_1.py")

if not os.path.isfile("C:/Документы/PycharmProjects/IS-22/test/test1/text.txt"):
    os.rename("test/test1/pz7_1.py", "test/test1/text.txt")

#Размер файлов в папке text
print('______________________________________________')
file_size1 = os.path.getsize("C:/Документы/PycharmProjects/IS-22/test/pz6_2(2).py")
print('Размер файла1:', file_size1, 'байт')
file_size1 = os.path.getsize("C:/Документы/PycharmProjects/IS-22/test/pz6_2.py")
print('Размер файла2:', file_size1, 'байт')
print('______________________________________________')

#Пути до файлов-исходников для перемещения
#"C:\Документы\PycharmProjects\IS-22\Proj_1sem_Kuznetsova\PZ_6\2\pz6_2(2).py"
#"C:\Документы\PycharmProjects\IS-22\Proj_1sem_Kuznetsova\PZ_6\2\pz6_2.py"
#"C:\Документы\PycharmProjects\IS-22\Proj_1sem_Kuznetsova\PZ_7\1\pz7_1.py"

#Обратная команда, чтобы вернуть файл: дубликаты хранятся на "C:\Документы\PycharmProjects\IS-22\ДубликатыДляPZ17"
print('Служебный чек. Возвращаем файлы в каталоги пз')
if not os.path.isfile("C:/Документы/PycharmProjects/IS-22/Proj_1sem_Kuznetsova/PZ_6/2/pz6_2(2).py"):
    os.replace("C:/Документы/PycharmProjects/IS-22/ДубликатыДляPZ17/PZ_6/2/pz6_2(2).py", "C:/Документы/PycharmProjects/IS-22/Proj_1sem_Kuznetsova/PZ_6/2/pz6_2(2).py")
if not os.path.isfile("C:/Документы/PycharmProjects/IS-22/Proj_1sem_Kuznetsova/PZ_6/2/pz6_2.py"):
    os.replace("C:/Документы/PycharmProjects/IS-22/ДубликатыДляPZ17/PZ_6/2/pz6_2.py", "C:/Документы/PycharmProjects/IS-22/Proj_1sem_Kuznetsova/PZ_6/2/pz6_2.py")
if not os.path.isfile("C:/Документы/PycharmProjects/IS-22/Proj_1sem_Kuznetsova/PZ_7/1/pz7_1.py"):
    os.replace("C:/Документы/PycharmProjects/IS-22/ДубликатыДляPZ17/PZ_7/1/pz7_1.py", "C:/Документы/PycharmProjects/IS-22/Proj_1sem_Kuznetsova/PZ_7/1/pz7_1.py")


#перейти в папку с PZ11 и найти там файл с самым коротким именем. Имя
#вывести в консоль. Использовать basename()(os.path.basename(path))
os.chdir('Proj_2sem_Kuznetsova/PZ11')
print('текущий каталог сменился на', os.getcwd())
def get_files_in_folder(path_to_folder: str) -> list[str]:
    return [file for file in os.listdir(path_to_folder) if os.path.isfile(os.path.join(path_to_folder, file))]

files = get_files_in_folder(".")
test = min([f"./{file}" for file in files], key=lambda x: len(x))
print('______________________________________________')
print(f"Файл с самым коротким именем в PZ_11:\n{os.path.basename(test)} - {os.stat(test).st_size} байт")
print('______________________________________________')
#перейти в любую папку, где есть отчет в формате Pdf
#и запустить файл в привязанной к нему программе, использовать функцию os.startfile()
import random
os.chdir('../../OtchetyPoPZ/pz11')
print('текущий каталог сменился на', os.getcwd())
pdf_files = [file for file in os.listdir(".") if file.endswith(".pdf")]
os.startfile(f"{os.path.join('.', random.choice(pdf_files))}")
print('Файл открыт')

#удалить файл text.txt
#os.remove('../../test/test1/text.txt')







