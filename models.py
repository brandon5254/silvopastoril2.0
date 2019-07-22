import sqlite3 as sql

def insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO silvopastoril VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (None, name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto, None, None))
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

def updateByID(token_respuesta, id, num):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("UPDATE silvopastoril SET token_api = ?, forma_pago = ? WHERE id = ?;", (token_respuesta, num, id))
    con.commit()
    con.close()

def insertData1(pagado, forma_pago, fecha_pago, monto, fecha_maxima_pago, hash_pedido, numero_pedido, cancelado, forma_pago_identificador, token):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO transactions_pagopar VALUES (?,?,?,?,?,?,?,?,?,?,?)", (None, pagado, forma_pago, fecha_pago, monto, fecha_maxima_pago, hash_pedido, numero_pedido, cancelado, forma_pago_identificador, token))
    con.commit()
    con.close()

def sortData(hash_pedido):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM silvopastoril where token_api = ? ORDER BY id DESC LIMIT 1",(hash_pedido, ))
    data = cur.fetchall()
    con.close()
    return data

def insertData2(pagado, forma_pago, fecha_pago, monto, fecha_maxima_pago, hash_pedido, numero_pedido, cancelado, forma_pago_identificador, token):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO pedido_traer VALUES (?,?,?,?,?,?,?,?,?,?,?)", (None, pagado, forma_pago, fecha_pago, monto, fecha_maxima_pago, hash_pedido, numero_pedido, cancelado, forma_pago_identificador, token))
    con.commit()
    con.close()

def listjoindata():
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("select s.nombre_completo, s.tipo_identificacion, s.nro_documento, s.email, s.pais, s.ciudad, s.telefono, s.institucion, s.ocupacion, s.area_ponencia, s.ingles, s.comentarios, s.nombre_razon_social, s.ruc, s.monto, tp.forma_pago, tp.fecha_pago, tp.numero_pedido from silvopastoril s INNER JOIN transactions_pagopar tp ON s.token_api=tp.hash_pedido;")
    data = cur.fetchall()
    con.close()
    return data

def listData2(hasher):
    con = sql.connect("datos.db")
    cur = con.cursor()
    cur.execute("select email from silvopastoril where token_api = '%s'" % hasher)
    data = cur.fetchall()
    for dato in data:
        r = ' '.join(dato)
    con.close()
    return r


    