#Создание базового класса 'Животное' и его наследование для создания классов 'Собака' и 'Кошка'
#В классе 'Животное' будут общие методы, такие как 'Дышать' и 'Питаться'
#а классы наследники будут иметь свои уникальные методы и свойства, такие как 'гавкать' и 'мурлыкать'

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

animal_base = Tier('Base-tier', False, False)
print(animal_base.__dict__, animal_base.essen)

cat = Katze('Lola', True, False)
print(cat.__dict__, cat.atmen, cat.mur())

dog = Hund('Lila', True, True)
print(dog.__dict__, dog.atmen, dog.gav())