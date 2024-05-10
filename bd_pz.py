import sqlite3 as sq
with sq.connect('pere.db') as con:
  cur = con.cursor()
  cur.execute('DROP TABLE IF EXISTS perev')
  cur.execute('''CREATE TABLE IF NOT EXISTS perev (
    id_perev INTEGER PRIMARY KEY AUTOINCREMENT,
    marshrut INTEGER NOT NULL,
    fam TEXT NOT NULL,
    data_otpr DATATIME,
    data_prib DATATIME,
    massa INTEGER NOT NULL
  )''')
  print('done')
