import hashlib

def generar(private_key, id_pedido, monto_total):
    concat = private_key+str(id_pedido)+str(monto_total)
    m = hashlib.sha1(concat.encode())
    result = m.hexdigest()
    return result

def generarToken(private_key):
    concat = private_key+"CONSULTA"
    m = hashlib.sha1(concat.encode())
    result = m.hexdigest()
    return result
