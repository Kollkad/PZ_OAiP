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