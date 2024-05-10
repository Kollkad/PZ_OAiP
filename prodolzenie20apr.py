class Note:
    def __init__(self, text):
        self.text = text
        self.count = 8

    def upcount(self):
        self.count +=1

note1 = Note('Задача1')
print(note1.__dict__)
print(dir(note1))#доступные
print(note1.text) #выводит то че в скобках
note2 = Note('Задача2')
#до уже было 20 апреля, после 24.04
#Начали с теста уже написанного
print('---------------------')
print(note2.__dict__)
print(dir(note2))

note1.upcount()#изменит именно каунт 1 задачи
print(note1.count)
print('--------')
print(note1.upcount)
print(Note.upcount)

print('Изменения по заданию1')
class NoteEx1:
    def __init__(self, text, iscompleted):
        self.text = text
        self.count = 0
        self.iscompleted = iscompleted

    def upcount(self):
        self.count += int(input('Введите величину увеличения Count: '))

    def reset_count(self):
        self.count = 0

ex = NoteEx1('задача1', False)
print(ex.__dict__)
ex.upcount()
print(ex.__dict__)



print('----------------')
class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self):
        self.resolution = input('Введите новое разрешение')

img = Image('1920*1080', 'Airplane', '.jpeg')



