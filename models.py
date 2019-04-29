import sqlite3 as sql

def insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO silvopastoril VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (None, name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto, None))
    con.commit()
    con.close()

def listData():
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM silvopastoril")
    data = cur.fetchall()
    con.close()
    return data

def findByID(name, n_document):
    con = sql.connect("datos.db")
    cur = con.cursor()
    for row in cur.execute("SELECT id FROM silvopastoril WHERE nombre_completo = ? AND nro_documento = ? ORDER BY id DESC LIMIT 1;", (name, n_document)):
        data = row[0]
    con.close()
    return data

def updateByID(token_respuesta, id):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("UPDATE silvopastoril SET token_api = ? WHERE id = ?;", (token_respuesta, id))
    con.commit()
    con.close()