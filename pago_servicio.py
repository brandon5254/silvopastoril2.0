from generador_token import generar
from pagopar import CrearPedido
from datetime import datetime, time, timedelta
import models as dbHandler
import dolarpy
import json

dict = {'bancard':9, 'procard': 1, 'aqui_pago': 2, 'pago_exp': 3, 'pract_pag':4, 'cuent_ban':7, 'tigo':10 }

def procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio):
    
    if f_pago == 'bancard' or 'procard':
        if ocupation == 'Estudiante Nacional' or 'Estudiante Extranjero':
            descripcion = "Inscripción Estudiante Nacional/Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 100 USD (Tipo de cambio del día)"
            descripcion_resumen = "Inscripción Estudiante Nacional/Internacional"
        elif ocupation == 'Profesional Nacional':
            descripcion = "Inscripción Profesional Nacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 150 USD (Tipo de cambio del día)"
            descripcion_resumen = "Inscripción Profesional Nacional"
        else:
            descripcion = "Inscripción Profesional Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 200 USD (Tipo de cambio del día)"
            descripcion_resumen = "Inscripción Profesional Internacional"
        #-----------------Se utiliza token api INFONA credito----------------------
        cotizacion = dolarpy.get_venta(provider='cambioschaco')#obtiene la cotizacion del dia
        monto = int(cotizacion)*precio#el monto entero de la inscripcion en guaranies
        monto_total = int((monto*100)/(100-6.82))
        #inserta los datos en la BD
        dbHandler.insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
        id_pedido = dbHandler.findByID(name, n_document)#obtiene el id en base al ultimo pedido del nombre la persona
        private_key = "520281c5bbc1e8910ab1a9c5c840512c"
        public_key = "1b85c4c48b70160f3b0ec66e46f4ade2"
        print(private_key, public_key)
        print(monto_total)
        token = generar(private_key, id_pedido, monto_total)#genera el token para pagopar
        print(token)
        dates = datetime.today()#obtengo la fecha de hoy
        max = dates+timedelta(days=1)#le sumo 1 dia=24hrs
        fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")#la fecha maxima de pago
        #devuelve true+token o false
        print(token, ruc, mail, name, phone, n_document, social, public_key, monto_total, descripcion, "Inscripción X CONGRESO SILVOPASTORIL", public_key, monto_total, fecha_maxima_pago, id_pedido, descripcion_resumen)
        response = CrearPedido(token, ruc, mail, name, phone, n_document, social, public_key, monto_total, descripcion, "Inscripción X CONGRESO SILVOPASTORIL", public_key, monto_total, fecha_maxima_pago, id_pedido, descripcion_resumen)#crea el pedido
        print(response)
        all = json.loads(response)
        
        if all['respuesta'] == False:
            print(all['resultado'])
            
        else:

            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)

        num = dict.get(f_pago)

    else:

        #-----------------Se utiliza token api Instituto Forestal Nacional----------------------
        if ocupation == 'Estudiante Nacional' or 'Estudiante Extranjero':
            descripcion = "Inscripción Estudiante Nacional/Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 100 USD (Tipo de cambio del día)"
            descripcion_resumen = "Inscripción Estudiante Nacional/Internacional"
        elif ocupation == 'Profesional Nacional':
            descripcion = "Inscripción Profesional Nacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 150 USD (Tipo de cambio del día)"
            descripcion_resumen = "Inscripción Profesional Nacional"
        else:
            descripcion = "Inscripción Profesional Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 200 USD (Tipo de cambio del día)"
            descripcion_resumen = "Inscripción Profesional Internacional"
        #-----------------Se utiliza token api INFONA credito----------------------
        cotizacion = dolarpy.get_venta(provider='cambioschaco')#obtiene la cotizacion del dia
        monto = int(cotizacion)*precio#el monto total entero de la inscripcion en guaranies
        monto_total = int((monto*100)/(100-5.39))
        #inserta los datos en la BD
        dbHandler.insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
        id_pedido = dbHandler.findByID(name, n_document)#obtiene el id en base al ultimo pedido del nombre la persona
        private_key1 = "1d98c69bb9c71a9529ca1e13e228040a"
        public_key1 = "c8928436431b6c6de669edb2ad199b3f"
        print(private_key1, public_key1)
        token1 = generar(private_key1, id_pedido, monto_total)#genera el token para pagopar
        print(token1)
        dates = datetime.today()#obtengo la fecha de hoy
        max = dates+timedelta(days=2)#le sumo 2 dias=48hrs
        fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")#la fecha maxima de pago
        #devuelve true+token o false
        response = CrearPedido(token1, ruc, mail, name, phone, n_document, social, public_key1 ,monto_total, "Inscripción X CONGRESO SILVOPASTORIL", public_key1, descripcion, monto_total, fecha_maxima_pago, id_pedido, descripcion_resumen)#crea el pedido
        print(response)
        all = json.loads(response)
        
        if all['respuesta'] == False:
            print(all['resultado'])
            
        else:

            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)

        num = dict.get(f_pago)

    return response, num;
