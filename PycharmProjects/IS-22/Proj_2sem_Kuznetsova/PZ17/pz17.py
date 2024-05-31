from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Задача1')
root.geometry('960x540')

#Регистрация и настройки
#register = Label(root, text='Регистрация', fg='#56BAF4', font=('Arial', 20))
#register.grid(column=0, row=0)

#Окно "создание нового сайта"
Base = Frame(root, bg='white', bd=5, padx=10, pady=10)
Base.pack(expand=True)

#--------Регистрация----------
#сначала фрейм whit
whit = Frame(Base, bg='white', width=960, height=50)
whit.pack()
#сама надпись
reg = Label(whit, text='Регистрация', bg='white', fg='#56BAF4', font=('Arial', 20))
reg.place(x=0, y=0)

#------НовыЙ фрейм sns для надписи-----------
Sns = Frame(Base, bg='#56BAF4', width=960, height=50)
Sns.pack()
#Надпись Создание нового сайта
sozd = Label(Sns, text='Создание нового сайта', bg='#56BAF4', fg='white', font=('Arial', 18))
sozd.place(x=330, y=8)

#-----------Фрейм для опроса---------------
opr = Frame(Base, bg='white', width=960, height=140)
opr.pack()
#Email
em = Label(opr, text='Email',  bg='white', fg='#56BAF4', font=('Arial', 8))
em.place(x=290, y=10)
emV = Entry(opr, width=40, bd=2)
emV.place(x=340, y=10)
emCB = Checkbutton(opr, bg='white', fg='green', height=1)
emCB.place(x=590, y=8)
#Пароль
prl = Label(opr, text='Пароль',  bg='white', fg='#56BAF4', font=('Arial', 8))
prl.place(x=290, y=35)
prlV = Entry(opr, width=40, bd=2)
prlV.place(x=340, y=35)
prlCB = Checkbutton(opr, bg='white', fg='green', height=1)
prlCB.place(x=590, y=33)
#Имя
name = Label(opr, text='Имя',  bg='white', fg='#56BAF4', font=('Arial', 8))
name.place(x=290, y=60)
nameV = Entry(opr, width=40, bd=2)
nameV.place(x=340, y=60)
nameCB = Checkbutton(opr, bg='white', fg='green', height=1)
nameCB.place(x=590, y=58)
#Фамилия
sname = Label(opr, text='Фамилия',  bg='white', fg='#56BAF4', font=('Arial', 8))
sname.place(x=290, y=85)
snameV = Entry(opr, width=40, bd=2)
snameV.place(x=340, y=85)
snameCB = Checkbutton(opr, bg='white', fg='green', height=1)
snameCB.place(x=590, y=83)
#Никнейм
nname = Label(opr, text='Никнейм',  bg='white', fg='#56BAF4', font=('Arial', 8))
nname.place(x=290, y=110)
nnameV = Entry(opr, width=40, bd=2)
nnameV.place(x=340, y=110)
nnameCB = Checkbutton(opr, bg='white', fg='green', height=1)
nnameCB.place(x=590, y=108)


#-------------Фрейм для даты, пол, город----------------
dat = Frame(Base, bg='white', width=960, height=80)
dat.pack()
#Дата рождения
data = Label(dat, text='Дата',  bg='white', fg='#56BAF4', font=('Arial', 8))
data.place(x=290, y=10)

from tkinter.ttk import Combobox
datad1 = Combobox(dat, width=8)
datad1['values']=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'другое')
datad1.current(0)
datad1.place(x=340, y=10)

datad2 = Combobox(dat, width=10)
datad2['values']=('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
datad2.current(0)
datad2.place(x=415, y=10)

datad3 = Combobox(dat, width=10)
datad3['values']=(2001, 2002, 2000, 1988, 'другое')
datad3.current(0)
datad3.place(x=500, y=10)

dataCB = Checkbutton(dat, bg='white', fg='green', height=1)
dataCB.place(x=590, y=8)
#Пол
pol = Label(dat, text='Пол',  bg='white', fg='#56BAF4', font=('Arial', 8))
pol.place(x=290, y=35)

polCB1 = Checkbutton(dat, bg='white', fg='black', height=1)
polCB1.place(x=340, y=33)
polf = Label(dat, text='Женщина',  bg='white', fg='#56BAF4', font=('Arial', 8))
polf.place(x=360, y=35)

polCB2 = Checkbutton(dat, bg='white', fg='black', height=1)
polCB2.place(x=500, y=33)
polm = Label(dat, text='Мужчина',  bg='white', fg='#56BAF4', font=('Arial', 8))
polm.place(x=520, y=35)
#ГОРОД
city = Label(dat, text='Место проживания',  bg='white', fg='#56BAF4', font=('Arial', 8))
city.place(x=235, y=60)

cityCB = Combobox(dat, width=37)
cityCB['values']=('Другой город', 'Минск', 'Новосибирск', 'Берлин')
cityCB.current(0)
cityCB.place(x=340, y=60)

#------------Код безопасности-----------------
kod = Frame(Base, bg='white', width=960, height=55)
kod.pack()
#
kodb = Label(kod, text='код безопасности',  bg='white', fg='#56BAF4', font=('Arial', 8))
kodb.place(x=235, y=10)

kodbV1 = Entry(kod, width=18, bd=2)
kodbV1.place(x=340, y=10)
kodbK = Combobox(kod, width=15)
kodbK['values']=('Uiu8da', 'uh8YHHD', '*YSBvdy', 'bUDyd8')
kodbK.current(0)
kodbK.place(x=475, y=10)

kodbCB = Checkbutton(kod, bg='white', fg='green', height=1)
kodbCB.place(x=590, y=8)

#Подтверждаю условия пользования
kodbCB2 = Checkbutton(kod, bg='white', fg='green', height=1)
kodbCB2.place(x=340, y=33)
kodb = Label(kod, text='Подтверждаю условия пользования uid сообщества',  bg='white', fg='black', font=('Arial', 8))
kodb.place(x=370, y=35)

#--------Регистрация ФИНАЛ)))--------
fin = Frame(Base, bg='white', width=960, height=100)
fin.pack()

butt = Button(fin, text='Регистрация', command='button_clicked', bg='#56BAF4', fg='white')
butt.place(x=290, y=10)
butt.pack()




#img
#canvas = Canvas(opr, bg='#0000b3', width=30, height=30)
#canvas.place(x=400, y=10)
#canvas.pack()
#img1 = PhotoImage(file="C:\Документы\PycharmProjects\IS-22\Proj_2sem_Kuznetsova\PZ17\gal.png")
#itogIMG = canvas.create_image(10, 10, anchor = NW, image = img1)
#emGal = Label(image=img1)
#emGal.place(x=450, y=10)
#emGal.pack()

def button_clicked():
    print('ПОЗДРАВЛЯЕМ, Вы зарегистрировались!')
def close():
    root.destroy()
    root.quit()
    print('Закрытие главного окна')

root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()