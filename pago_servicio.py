from generador_token import generar
from pagopar import CrearPedido
from datetime import datetime, time, timedelta
import models as dbHandler
import dolarpy
import json

def procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio):
    
    if forma_pago == 'Bancard Tarjeta Crédito/Débito' or 'Procard Tarjeta Crédito/Débito':
        #se utiliza token api infona credito
        cotizacion = dolarpy.get_venta()#obtiene la cotizacion del dia
        monto_total = int(cotizacion)*precio#el monto total de la inscripcion en guaranies
        #inserta los datos en la BD
        dbHandler.insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
        id_pedido = dbHandler.findByID(name, n_document)#obtiene el id en base al ultimo pedido del nombre la persona
        private_key = "1d98c69bb9c71a9529ca1e13e228040a"
        public_key = "c8928436431b6c6de669edb2ad199b3f"
        token = generar(private_key, id_pedido, monto_total)#genera el token para pagopar
        dates = datetime.today()#obtengo la fecha de hoy
        max = dates+timedelta(days=1)#le sumo 1 dia=24hrs
        fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")#la fecha maxima de pago
        #devuelve true+token o false
        response = CrearPedido(token, ruc, mail, name, phone, n_document, social, public_key ,monto_total,
        "Inscripción X CONGRESO SILVOPASTORIL", public_key, "Inscripción Estudiante Nacional/Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 100 USD (Tipo de cambio del día)", 
        monto_total, fecha_maxima_pago, id_pedido, "Inscripción Estudiante Nacional/Internacional")#crea el pedido
    
    else:
        #se utiliza token api Instituto Forestal Nacional
        if forma_pago == 'Bancard Tarjeta Crédito/Débito' or 'Procard Tarjeta Crédito/Débito':
        #se utiliza token api infona credito
        cotizacion = dolarpy.get_venta()#obtiene la cotizacion del dia
        monto_total = int(cotizacion)*precio#el monto total de la inscripcion en guaranies
        #inserta los datos en la BD
        dbHandler.insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
        id_pedido = dbHandler.findByID(name, n_document)#obtiene el id en base al ultimo pedido del nombre la persona
        private_key = "1d98c69bb9c71a9529ca1e13e228040a"
        public_key = "c8928436431b6c6de669edb2ad199b3f"
        token = generar(private_key, id_pedido, monto_total)#genera el token para pagopar
        dates = datetime.today()#obtengo la fecha de hoy
        max = dates+timedelta(days=1)#le sumo 1 dia=24hrs
        fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")#la fecha maxima de pago
        #devuelve true+token o false
        response = CrearPedido(token, ruc, mail, name, phone, n_document, social, public_key ,monto_total,
        "Inscripción X CONGRESO SILVOPASTORIL", public_key, "Inscripción Estudiante Nacional/Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 100 USD (Tipo de cambio del día)", 
        monto_total, fecha_maxima_pago, id_pedido, "Inscripción Estudiante Nacional/Internacional")#crea el pedido
    
    return response
