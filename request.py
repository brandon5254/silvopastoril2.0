import json
import requests
from generador_token import generar

url = "https://api.pagopar.com/api/comercios/1.1/iniciar-transaccion"

def CrearPedido(token, ruc, email, ciudad, nombre, telefono, direccion, documento, coordenadas, razon_social, tipo_documento, direccion_referencia, monto_total,
tipo_pedido, ciudad_item, nombre_ticket, cantidad, categoria, url_imagen, descripcion, id_producto, precio_total, vendedor_telefono, vendedor_direccion, vendedor_direccion_referencia,
vendedor_direccion_coordenadas, fecha_maxima_pago, id_pedido, descripcion_resumen):

    payload = {
    "token": token,
    "comprador": {
    "ruc": ruc,
    "email": email,
    "ciudad": ciudad,
    "nombre": nombre,
    "telefono": telefono,
    "direccion": direccion,
    "documento": documento,
    "coordenadas": coordenadas,
    "razon_social": razon_social,
    "tipo_documento": tipo_documento,
    "direccion_referencia": direccion_referencia
    },
    "public_key": "c8928436431b6c6de669edb2ad199b3f",
    "monto_total": monto_total,
    "tipo_pedido": tipo_pedido,
    "compras_items": [
    {
    "ciudad": ciudad_item,
    "nombre": nombre_ticket,
    "cantidad": cantidad,
    "categoria": categoria,
    "public_key": "c8928436431b6c6de669edb2ad199b3f",
    "url_imagen": "",
    "descripcion": descripcion,
    "id_producto": id_producto,
    "precio_total": precio_total,
    "vendedor_telefono": vendedor_telefono,
    "vendedor_direccion": vendedor_direccion,
    "vendedor_direccion_referencia": vendedor_direccion_referencia,
    "vendedor_direccion_coordenadas": vendedor_direccion_coordenadas
    }
    ],
    "fecha_maxima_pago": fecha_maxima_pago,
    "id_pedido_comercio": id_pedido,
    "descripcion_resumen": descripcion_resumen
    }

    #print(json.dumps(payload))

    response = requests.request("POST", url, data=json.dumps(payload))

    #print(response.text)

    return response.text