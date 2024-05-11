print('----------------')

class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self):
        self.resolution = input('Введите новое разрешение')
    def title_upper(self, title):
        self.title = title.upper()



img1 = Image('1000*1000', 'Train', '.png')
img2 = Image('1920*1080', 'Airplane', '.jpeg')
print(img1.__dict__)
print(img1.resize(), img1.__dict__)
print('--')
print(img2.__dict__)
print(img2.resize(), img2.__dict__)
print(img1.title_upper(), img1.__dict__)

#Пара10 мая вот, 16 пз. превый блок до ---- работает. второй нет
class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks
    def srednee(self):
        vse = 0
        for i in self.marks:
            vse += i
        sred = vse / len(self.marks)
        return sred
    def otlichnik(self, sred):
        if sred == 5:
            return('Отличник')
        else:
            return('Не отличник')

student1 = Student('Stasy', 'Bread', [2, 2, 3, 4, 4])

print(student1.__dict__)
print('Среднее по оценкам', student1.srednee())
print('Отличник?', student1.otlichnik(student1.srednee()))
print('---------------------------')

class Tier:#дышать, есть, слышать, бегать
    def __init__(self, name, atmen, essen):
        self.name = name
        self.atmen = atmen
        self.essen = essen
    def atmen(self):
        self.atmen = True
    def essen(self):
        self.essen = True
    #def horen(self):
        #self.horen = True
    #def laufen(self):
        #self.laufen = True

class Katze(Tier):
    def mur(self):
        print('mur mur mur')

class Hund(Tier):
    def gav(self):
        print('gav gav gav')

animal_none = Tier('Not found', False, False)
print(animal_none.__dict__, animal_none.essen)
cat = Katze('Lola', False, False)
print(cat.__dict__, cat.essen, cat.mur)

#РАЗНОГО ВСЯКОГО С ДВУХ ФАЙЛОВ ДА

class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks
    def srednee(self):
        vse = 0
        for i in self.marks:
            vse += i
        sred = vse / len(self.marks)
        return sred
    def otlichnik(self, sred):
        if sred == 5:
            return('Отличник')
        else:
            return('Не отличник')

student1 = Student('Stasy', 'Bread', [2, 2, 3, 4, 4])

print(student1.__dict__)
print('Среднее по оценкам', student1.srednee())
print('Отличник?', student1.otlichnik(student1.srednee()))
print('---------------------------')

class Tier:#дышать, есть, слышать, бегать
    def __init__(self, name, atmen, essen):
        self.name = name
        self.atmen = atmen
        self.essen = essen
    def atmen(self):
        return self.atmen
    def essen(self):
        return self.essen
    #def horen(self):
        #self.horen = True
    #def laufen(self):
        #self.laufen = True

class Katze(Tier):
    def mur(self):
        return('mur mur mur')

class Hund(Tier):
    def gav(self):
        return('gav gav gav')

animal_none = Tier('Not found', False, False)
print(animal_none.__dict__, animal_none.essen)

cat = Katze('Lola', True, False)
print(cat.__dict__, cat.atmen, cat.mur())

print('-----------------------')
import pickle as p
class Student2:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks
    def srednee(self):
        vse = 0
        for i in self.marks:
            vse += i
        sred = vse / len(self.marks)
        return sred
    def otlichnik(self, sred):
        if sred == 5:
            return('Отличник')
        else:
            return('Не отличник')
    def save_def(self):
        with open('f1.bin', 'wb') as f:
            p.dump(self, f)
        return('сохранено')
    def load_def(self):
        with open('f1.bin', 'rb') as f:
            fld = p.load(f)
        return fld


student01 = Student2('Klo', 'Stu', [2, 4, 5, 3, 4, 4, 3])
student02 = Student2('Bro', 'Bin', [2, 3, 3, 3, 2])
student03 = Student2('Tru', 'Sam', [4, 5, 3, 5, 5, 4])
exempl = []#попытка обьеденить все три обьекта
exempl.append(student01 and student02 and student03)
print('ex =', exempl)
print(student01.save_def(), student01.load_def())




# [htym krwbz
#try:
#    file = open('z3.bin', 'wb')
#    try:
#        p.dump(student01, file)
#        p.dump(student02, file)
#        p.dump(student03, file)
#    finally:
#        file.close()

#except FileNotFoundError:
#    print('Невозможно открыть файл')

#file = open('z3.bin', 'rb')
#s1 = p.load(file)
#s2 = p.load(file)
#s3 = p.load(file)
#print(s1, s2, s3, sep='\n')

#Дальше лекция. до этого из лекции по пикл кусок

import os
print('текущий каталог', os.getcwd())
#os.mkdir('folder')
if not os.path.isdir('folder'):
    os.mkdir('folder')

os.chdir('folder')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())

#вложенные папки
#os.makedirs('n1/n2/n3')

#cоздать файл и записать туда что-то
#text_file = open('text.txt', 'w')
#text_file.write('text file das is')
#text_file.close()

#переименовать и переместить
#os.rename('text.txt', 'rt.txt')
#os.replace('rt.txt', 'folder/rt.txt')

#все папки и файлы в тек каталоге
print(os.listdir())
#папки и файлы со вложеными
print('----------------------------------')
for dirpath, dirnames, filenames in os.walk('.'):
    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))
    for filename in filenames:
        print(os.path.join(dirpath, filename))

#удалить файл и папку, папки
#os.remove('folder/rt.txt')
#os.rmdir('folder')
#os.removedirs('n1/n2/n3')
print('----------------------------------')
#данные о файле
text_file = open('rt.txt', 'w')
text_file.write('text file das is')
text_file.close()
print(os.stat('rt.txt'))#после скобок с файлом ставят различные дополнения
print(os.stat('rt.txt').st_size)
print('----------------------------------')
#выводит содержимое папки особым образом фото есть лень
def pr_d(directory):
    all = os.walk(directory)
    for catalog in all:
        print(f'папка {catalog[0]} содержит:')
    print(f'dirs {",".join([folder for folder in catalog[1]])}')
    print(f'files {",".join([file for file in catalog[2]])}')
    print('-' * 40)

pr_d('/home/student/Документы/22new/')







