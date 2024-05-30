#Создайте класс 'студент', который имеет атрибуты имя, фамилия
#и оценки. Добавьте методы для вычисления среднего балла и определения
#является ли студент отличником

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
print('----------')
student2 = Student('Prohor', 'Patrikeev', [5, 5, 5, 5, 5])
print('Среднее по оценкам', student2.srednee())
print('Отличник?', student2.otlichnik(student2.srednee()))