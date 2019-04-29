from flask import Flask, render_template, request, redirect, url_for, flash
from generador_token import generar
from pagopar import CrearPedido
from datetime import datetime, time, timedelta
import models as dbHandler
import dolarpy
import json



app = Flask(__name__)

app.config['MAIL_SERVER'] = 'correo.silvopastoril2019.org.py'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/normas')
def normas():
   return render_template('normas.html')

@app.route('/galeria')
def galeria():
   return render_template('galeria.html')
   
@app.route('/registro', methods=['POST', 'GET'])
def registro():
   if request.method=='POST':
      name = request.form['nombre']
      document = request.form['tipo_documento']
      n_document = request.form['numero_documento']
      mail = request.form['email']
      country = request.form['pais']
      city = request.form['ciudad']
      address = request.form['direccion']
      phone = request.form['telefono']
      institute = request.form['institucion']
      ocupation = request.form['ocupacion']
      participation = request.form['tipo_participacion']
      ponencia = request.form['ponencia']
      english = request.form['ingles']
      coments = request.form['comentarios']
      social = request.form['nombre_razon_social']
      ruc = request.form['ruc']
      if ponencia == '':
         ponencia = None
      if english == '':
         english = None
      if social == '':
         social = None
      if ruc == '':
         ruc = None
      if request.form['ocupacion'] == 'Estudiante Nacional' or request.form['ocupacion'] == 'Estudiante Extranjero':
         #precio debe ser 100$
         precio = 100
         cotizacion = dolarpy.get_venta()
         monto_total = cotizacion*100
         dbHandler.insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
         id_pedido = dbHandler.findByID(name, n_document)
         private_key = "1d98c69bb9c71a9529ca1e13e228040a"
         public_key = "c8928436431b6c6de669edb2ad199b3f"
         token = generar(private_key, id_pedido, monto_total)
         dates = datetime.today()#obtengo la fecha de hoy
         max = dates+timedelta(days=1)#le sumo 1 dia=24hrs
         fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")
         #devuelve true+token o false
         res = CrearPedido(token, ruc, mail, name, phone, n_document, social, public_key ,monto_total, "Inscripción X CONGRESO SILVOPASTORIL", 
         public_key, "Inscripción Estudiante Nacional/Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 100 USD (Tipo de cambio del día)", 
         monto_total, fecha_maxima_pago, id_pedido, "Inscripción Estudiante Nacional/Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 100 USD (Tipo de cambio del día)")
         all = json.loads(res)
         if all['respuesta'] == True:
            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)
            return redirect(url_for('reject'), token_api = token_recibed)
         else:
            return redirect(url_for('home'))
      if request.form['ocupacion'] == 'Profesional Nacional':
         #precio debe ser 150$
         precio = 150
         cotizacion = dolarpy.get_venta()
         monto_total = cotizacion*100
         dbHandler.insertdata(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
         id_pedido = dbHandler.findByID(name, n_document)
         private_key = "1d98c69bb9c71a9529ca1e13e228040a"
         public_key = "c8928436431b6c6de669edb2ad199b3f"
         token = generar(private_key, id_pedido, monto_total)
         dates = datetime.today()#obtengo la fecha de hoy
         max = dates+timedelta(days=1)#le sumo 1 dia=24hrs
         fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")
         #devuelve true+token o false
         res = CrearPedido(token, ruc, mail, name, phone, n_document, social, public_key ,monto_total, "Inscripción X CONGRESO SILVOPASTORIL", 
         public_key, "Inscripción Profesional Nacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 150 USD (Tipo de cambio del día)", 
         monto_total, fecha_maxima_pago, id_pedido, "Inscripción Profesional Nacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 150 USD (Tipo de cambio del día)")
         all = json.loads(res)
         if all['respuesta'] == True:
            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)
            return redirect(url_for('reject'), token_api = token_recibed)
         else:
            return redirect(url_for('home'))
      else:
         #profesional internacional 200$
         precio = 200
         cotizacion = dolarpy.get_venta()
         monto_total = cotizacion*100
         dbHandler.insertdata(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
         id_pedido = dbHandler.findByID(name, n_document)
         private_key = "1d98c69bb9c71a9529ca1e13e228040a"
         public_key = "c8928436431b6c6de669edb2ad199b3f"
         token = generar(private_key, id_pedido, monto_total)
         dates = datetime.today()#obtengo la fecha de hoy
         max = dates+timedelta(days=1)#le sumo 1 dia=24hrs
         fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")
         #devuelve true+token o false
         res = CrearPedido(token, ruc, mail, name, phone, n_document, social, public_key ,monto_total, "Inscripción X CONGRESO SILVOPASTORIL", 
         public_key, "Inscripción Profesional Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 200 USD (Tipo de cambio del día)", 
         monto_total, fecha_maxima_pago, id_pedido, "Inscripción Profesional Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 200 USD (Tipo de cambio del día)")
         all = json.loads(res)
         if all['respuesta'] == True:
            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)
            return redirect(url_for('reject'), token_api = token_recibed)
         else:
            return redirect(url_for('home'))
   else:
      return render_template('formulario.html')

@app.route('/form', methods=['POST', 'GET'])
def register():
   if request.method=='POST':
      name = request.form['nombre']
      document = request.form['tipo_documento']
      n_document = request.form['numero_documento']
      mail = request.form['email']
      country = request.form['pais']
      city = request.form['ciudad']
      address = request.form['direccion']
      phone = request.form['telefono']
      institute = request.form['institucion']
      ocupation = request.form['ocupacion']
      participation = request.form['tipo_participacion']
      ponencia = request.form['ponencia']
      english = request.form['ingles']
      coments = request.form['comentarios']
      social = request.form['nombre_razon_social']
      ruc = request.form['ruc']
      if request.form['ponencia'] == '':
         ponencia = None
      if request.form['ingles'] == '':
         english = None
      if request.form['nombre_razon_social'] == '':
         social = None
      if request.form['ruc'] == '':
         ruc = None
      dbHandler.insertdata(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc)
      if request.form['ocupacion'] == 'Estudiante Nacional' or request.form['ocupacion'] == 'Estudiante Extranjero':
         return render_template('redirect.html')
      if request.form['ocupacion'] == 'Profesional Nacional':
         return render_template('redirect1.html')
      else:
         return render_template('redirect2.html')
   else:
      return render_template('form.html')

@app.route('/reject')
def reject():
   return render_template('redirect.html')

@app.route('/homei')
def homei():
   return render_template('index-e.html')

@app.route('/homei/norms')
def norms():
   return render_template('normas-e.html')

@app.route('/homei/gallery')
def gallery():
   return render_template('galeria-e.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
