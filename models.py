import sqlite3 as sql

def insertdata(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO silvopastoril VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (None, name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto, token_api))
    con.commit()
    con.close()

def listdata():
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("SELECT id FROM silvopastoril")
    data = cur.fetchall()
    con.close()
    return data

def lastID():
    con = sql.connect("datos.db")
    cur = con.cursor()
    for row in cur.execute("select id from silvopastoril order by id DESC limit 1;"):
        data = row[0]
    #cur.execute
    #data = cur.fetchall()
    con.close()
    return data