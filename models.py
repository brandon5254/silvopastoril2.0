import sqlite3 as sql

def insertdata(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO silvopastoril VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (None, name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments))
    con.commit()
    con.close()

def listdata():
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM silvopastoril")
    data = cur.fetchall()
    con.close()
    return data