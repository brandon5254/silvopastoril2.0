import json
import requests

url = "https://api.pagopar.com/api/forma-pago/1.1/traer/"

def TraerPedido(token, token_publico):
    payload= {
        "token": token,
        "token_publico": token_publico
    }   

    response = requests.request("POST", url, data=json.dumps(payload))

    return response.text