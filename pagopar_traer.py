import json
import requests

url = "https://api.pagopar.com/api/pedidos/1.1/traer"

def TraerPedido(hash_pedido, token, token_publico):
    payload = {
        "hash_pedido": hash_pedido,
        "token": token,
        "token_publico": token_publico
    }   

    response = requests.request("POST", url, data=json.dumps(payload))

    return response.text