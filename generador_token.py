import hashlib

#private_key = "1d98c69bb9c71a9529ca1e13e228040a"
#public_key = "c8928436431b6c6de669edb2ad199b3f"

def generar(private_key, id_pedido, monto_total):
    concat = private_key+str(id_pedido)+str(monto_total)
    m = hashlib.sha1(concat.encode())
    result = m.hexdigest()
    return result

