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
