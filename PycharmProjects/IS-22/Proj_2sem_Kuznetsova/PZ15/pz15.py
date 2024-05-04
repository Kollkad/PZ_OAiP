#Приложение грузовые перевозки для некоторой организации БД должна содержать таблицу ПЕРЕВОЗКИ
# со следующей структурой записи: маршрут, фамилия водителя, дата отправки и прибытия, масса груза
import sqlite3 as sq
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute('DROP TABLE IF EXISTS perev')
  cur.execute('''CREATE TABLE IF NOT EXISTS perev (
    id_perev INTEGER PRIMARY KEY AUTOINCREMENT,
    marshrut INTEGER NOT NULL,
    fam TEXT NOT NULL,
    data_otpr DATA,
    data_prib DATA,
    massa INTEGER NOT NULL
  )''')
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute('''INSERT INTO perev VALUES(1, 15, 'Limonchello', '1989-02-14', '1989-02-15', 89 )''')#1
  cur.execute('''INSERT INTO perev VALUES(2, 83, 'Peskov', '1989-02-15', '1989-02-16', 12 )''')#2
  cur.execute('''INSERT INTO perev VALUES(3, 65, 'Ruvalov', '1989-02-07', '1989-02-25', 45 )''')#3
  cur.execute('''INSERT INTO perev VALUES(4, 81, 'Petrov', '1989-02-16', '1989-02-25', 12 )''')#4
  cur.execute('''INSERT INTO perev VALUES(5, 83, 'Peskov', '1989-02-17', '1989-03-01', 3 )''')#5
  cur.execute('''INSERT INTO perev VALUES(6, 23, 'Lavrov', '1989-04-23', '1989-05-03', 8 )''')#6
  cur.execute('''INSERT INTO perev VALUES(7, 6, 'Sidorov', '1989-04-23', '1989-04-26', 56 )''')#7
  cur.execute('''INSERT INTO perev VALUES(8, 23, 'Valuev', '1989-05-09', '1989-06-09', 140 )''')#8
  cur.execute('''INSERT INTO perev VALUES(9, 67, 'Brovin', '1989-06-01', '1989-06-03', 12 )''')#9
  cur.execute('''INSERT INTO perev VALUES(10, 23, 'Lavrov', '1989-04-23', '1989-07-29', 11 )''')#10
#Поиск
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute("SELECT * FROM perev")#1
  result0 = cur.fetchall()
print('База данных perev', result0)

with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute("SELECT * FROM perev WHERE id_perev = 2")#2
  result1 = cur.fetchall()
print('Перевозка с id_perev = 2: ', result1)

with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute("SELECT data_otpr, data_prib FROM perev WHERE data_prib <= '1989-03-01' AND data_otpr >= '1989-02-01' ")#3
  result2 = cur.fetchall()
print('Дата отправки и прибытия перевозки с 1 февраля по 1 марта включительно: ', result2)
print('============================================')
#Редактирование
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute("UPDATE perev SET data_prib = '1989-08-01' WHERE id_perev = 10")#1
  cur.execute("SELECT * FROM perev WHERE id_perev = 10")
  result3 = cur.fetchall()
print('Первый update с заменой даты прибытия:', result3)
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute("UPDATE perev SET massa = 130 WHERE massa > 130")#2
  cur.execute("SELECT * FROM perev WHERE massa = 130")
  result4 = cur.fetchall()
print('Второй update с заменой массы груза > 130:', result4)
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute("UPDATE perev SET fam = 'Aliev' WHERE id_perev = 9")#3
  cur.execute("SELECT * FROM perev WHERE id_perev = 9")
  result5 = cur.fetchall()
print('Третий update с заменой водителя: ', result5)
print('============================================')
#Удаление
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute("DELETE FROM perev WHERE id_perev = 10")#1
  cur.execute("SELECT * FROM perev")
  result6 = cur.fetchall()
print('Удаление перевозки с id_perev = 10: ', result6)
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute("DELETE FROM perev WHERE fam = 'Valuev'")#2
  cur.execute("SELECT * FROM perev")
  result7 = cur.fetchall()
print('Удаление перевозки с водителем Valuev: ', result7)
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute("DELETE FROM perev WHERE marshrut = 83 OR massa = 12")#3
  cur.execute("SELECT * FROM perev")
  result8 = cur.fetchall()
print('Удаление перевозки с маршрутом 83 или массой 12: ', result8)


