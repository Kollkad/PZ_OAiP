# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохрянять информацию из
# экзэмпляров класса(3шт) в файл и загружать ее обратно. Использовать модуль picle для
# сеарилизации и десериализации обьектов Python в бинарном формате

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

def save_def(obj):
    with open('f1.bin', 'wb') as f:
        p.dump(obj, f)
    return('сохранено')
def load_def():
    with open('f1.bin', 'rb') as f:
        obj = p.load(f)
    return obj

student01 = Student2('Klo', 'Stu', [2, 4, 5, 3, 4, 4, 3])
student02 = Student2('Bro', 'Bin', [2, 3, 3, 3, 2])
student03 = Student2('Tru', 'Sam', [4, 5, 3, 5, 5, 4])

exempl = [student01, student02, student03]#попытка обьеденить все три обьекта
print('exempl =', exempl)
save_def(exempl)
retrieve = load_def()
for x in retrieve:
    print(x.__dict__)
