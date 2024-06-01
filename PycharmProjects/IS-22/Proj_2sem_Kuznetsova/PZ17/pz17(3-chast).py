import os
import os.path
#перейти в папку с PZ11 и найти там файл с самым коротким именем. Имяя
#вывести в консоль. Использовать basename()(os.path.basename(path))
print('текущий каталог', os.getcwd())
os.chdir('../PZ11')
print('текущий каталог сменился на', os.getcwd())
def get_files_in_folder(path_to_folder: str) -> list[str]:
    return [file for file in os.listdir(path_to_folder) if os.path.isfile(os.path.join(path_to_folder, file))]

files = get_files_in_folder(".")
test = min([f"./{file}" for file in files], key=lambda x: len(x))
print(f"\nФайл с самым коротким именем в PZ_11:\n{os.path.basename(test)} - {os.stat(test).st_size} байт")

#перейти в любую папку, где есть отчет в формате Pdf
#и запустить файл в привязанной к нему программе, использовать функцию os.startfile()
import random
os.chdir('../../OtchetyPoPZ/pz11')
print('текущий каталог сменился на', os.getcwd())
pdf_files = [file for file in os.listdir(".") if file.endswith(".pdf")]
os.startfile(f"{os.path.join('.', random.choice(pdf_files))}")

#удалить файл text.txt
#os.remove('../../test/test1/text.txt')




