from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Дано 3х значное число. В нем зачеркунли первую справа цифру и приписали ее слева. Вывести полученное число
def calculate_ch():
    chislo_z = int(chislo_v.get())
    if chislo_z > 99 and chislo_z < 1000:
        chislo2 = chislo_z % 10
        chislo_z //= 10
        chislo_z = chislo2 * 100 + chislo_z
        messagebox.showinfo('Результат перестановки', f'{chislo_z} - новый вид числа')
    else:
        messagebox.showinfo('Результат перестановки', f'Число в неверном диапазоне')

window = Tk()
window.title('Перестановка последней цифры 3х значного числа')
window.geometry('600x130')

frame1 = Frame(window, height=20)
frame1.pack(expand=True)

zadacha= Label(frame1, text="Дано 3х значное число. В нем зачеркунли первую справа цифру и приписали ее слева.")
zadacha.grid(row=0, column=0)
zadacha2= Label(frame1, text="Вывести полученное число")
zadacha2.grid(row=1, column=0)

frame = Frame(window)
frame.pack(expand=True)
chislo_t= Label(frame, text="Введите число")
chislo_t.grid(row=0, column=0)
chislo_v = Entry(frame)
chislo_v.grid(row=0, column=1, pady=5)

cal_ch = Button(frame, text='Совершить перестановку', command=calculate_ch)
cal_ch.grid(row=3, column=1)

window.mainloop()