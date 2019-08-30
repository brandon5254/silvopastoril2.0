from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_moment import Moment
from flask_mail import Mail, Message
from pago_servicio import procesar
from generador_token import generarToken
from pagopar_traer import TraerPedido
from models import listData, insertData1, sortData, insertData2, listjoindata, listData2, insertData3, insertData4, listData3, listData4, cantidadIncripto, cantMaxInscripto
from send_mail import mailer
from flask_weasyprint import HTML, render_pdf
import json
import requests
import datetime


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.secret_key = "SECRET"

app.config['MAIL_SERVER'] = 'correo.silvopastoril2019.org.py'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'organizacion@silvopastoril2019.org.py'
app.config['MAIL_PASSWORD'] = 'organizacion'
mail = Mail(app)
moment = Moment(app)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/normas')
def normas():
   return render_template('normas.html')

@app.route('/becas')
def becas():
   return render_template('becas.html')

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
      f_pago = request.form.get('for_pago')
      participation = request.form['tipo_participacion']
      ponencia = request.form.get('ponencia')
      english = request.form.get('ingles')
      coments = request.form.get('comentarios')
      social = request.form.get('nombre_razon_social')
      ruc = request.form['identificador_tributario'] +": "+ request.form['name_identifi']
      if ponencia == '':
         ponencia = None
      if english == '':
         english = None
      if social == '':
         social = None
      if ruc == '':
         ruc = None
      if request.form['identificador_tributario'] == 'otro':
         ruc = request.form['otro'] +": "+ request.form['name_identifi']
      if f_pago == None:
         mensaje = "Por favor ingrese un metodo de pago!!"
         flash(mensaje)
      if n_document == '':
         mensaje = "El numero de documento o pasaporte debe estar presente!!"
         flash(mensaje)
         return render_template('formulario.html')
      if request.form['ocupacion'] == 'Estudiante Nacional' or request.form['ocupacion'] == 'Estudiante Extranjero':
         precio = 100#precio incripcion e n/e
         #descripcion
         res, f_pago = procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio)
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            #si la respuesta es true me redirecciona a la pagina de pago
            token_recibed = all['resultado'][0]['data']
            
            return render_template("redirect.html", token_recibed=token_recibed, f_pago=f_pago)
         else:# de ser falso me recarga la pagina y me salta un mensaje
            mensaje = "No se realizo el registro. Vuelva a intentarlo."
            flash(mensaje)
            return render_template('formulario.html')

      if request.form['ocupacion'] == 'Profesional Nacional':
         #precio debe ser 150$
         precio = 150
         res, f_pago = procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio)
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            #si la respuesta es true me redirecciona a la pagina de pago
            token_recibed = all['resultado'][0]['data']
            return render_template("redirect.html", token_recibed=token_recibed, f_pago=f_pago)
         else:# de ser falso me recarga la pagina y me salta un mensaje
            mensaje = "No se realizo el registro. Vuelva a intentarlo."
            flash(mensaje)
            return render_template('formulario.html')

      else:
         #profesional internacional 200$
         precio = 200
         res, f_pago = procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio)
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            #si la respuesta es true me redirecciona a la pagina de pago
            token_recibed = all['resultado'][0]['data']
            return render_template("redirect.html", token_recibed=token_recibed, f_pago=f_pago, bandera=True)
         else:# de ser falso me recarga la pagina y me salta un mensaje
            mensaje = "No se realizo el registro. Vuelva a intentarlo."
            flash(mensaje)
            return render_template('formulario.html')

   else:
      return render_template('formulario.html')

@app.route('/homei/register', methods=['POST', 'GET'])
def register():
   if request.method=='POST':
      name = request.form['nombre']
      document = "CI"
      n_document = request.form['numero_documento']
      mail = request.form['email']
      country = request.form['pais']
      city = request.form['ciudad']
      address = request.form['direccion']
      phone = request.form['telefono']
      institute = request.form['institucion']
      ocupation = request.form['ocupacion']
      f_pago = request.form.get('for_pago')
      participation = request.form['tipo_participacion']
      ponencia = request.form.get('ponencia')
      english = request.form.get('ingles')
      coments = request.form.get('comentarios')
      social = request.form.get('nombre_razon_social')
      ruc = request.form.get('ruc')
      if ponencia == '':
         ponencia = None
      if english == '':
         english = None
      if social == '':
         social = None
      if ruc == '':
         ruc = None
      if f_pago == None:
         mensaje = "Por favor ingrese un metodo de pago!!"
         flash(mensaje)
         return render_template('form.html')
      if request.form['ocupacion'] == 'Estudiante Nacional' or request.form['ocupacion'] == 'Estudiante Extranjero':
         precio = 100#precio incripcion e n/e
         #descripcion
         res, f_pago = procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio)
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            #si la respuesta es true me redirecciona a la pagina de pago
            token_recibed = all['resultado'][0]['data']
            return render_template("redirect.html", token_recibed=token_recibed, f_pago=f_pago)
         else:# de ser falso me recarga la pagina y me salta un mensaje
            mensaje = "No se realizo el registro. Vuelva a intentarlo."
            print(all['respuesta'])
            flash(mensaje)
            return render_template('form.html')

      if request.form['ocupacion'] == 'Profesional Nacional':
         #precio debe ser 150$
         precio = 150
         res, f_pago = procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio)
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            #si la respuesta es true me redirecciona a la pagina de pago
            token_recibed = all['resultado'][0]['data']
            return render_template("redirect.html", token_recibed=token_recibed, f_pago=f_pago)
         else:# de ser falso me recarga la pagina y me salta un mensaje
            mensaje = "No se realizo el registro. Vuelva a intentarlo."
            print(all['respuesta'])
            flash(mensaje)
            return render_template('form.html')

      else:
         #profesional internacional 200$
         precio = 200
         res, f_pago = procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio)
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            #si la respuesta es true me redirecciona a la pagina de pago
            token_recibed = all['resultado'][0]['data']
            return render_template("redirect.html", token_recibed=token_recibed, f_pago=f_pago)
         else:# de ser falso me recarga la pagina y me salta un mensaje
            mensaje = "No se realizo el registro. Vuelva a intentarlo."
            print(all['respuesta'])
            flash(mensaje)
            return render_template('form.html')

   else:
      return render_template('form.html')

@app.route('/resultado/<string:hash>')
def result(hash):
   
   datos = sortData(hash)
   
   if datos[0][19] == '9' or datos[0][19] == '1':
      
      private_key = "520281c5bbc1e8910ab1a9c5c840512c"
      public_key = "1b85c4c48b70160f3b0ec66e46f4ade2"
   
   else:
      
      private_key = "1d98c69bb9c71a9529ca1e13e228040a"
      public_key = "c8928436431b6c6de669edb2ad199b3f"
   
   token = generarToken(private_key)
   #recibo los estados de los pedidos
   res = TraerPedido(hash, token, public_key)
   ped = json.loads(res)
   #guardo la cadena en mi bd
   pagado = ped['resultado'][0]['pagado']
   forma_pago = ped['resultado'][0]['forma_pago']
   fecha_pago = ped['resultado'][0]['fecha_pago']
   monto = ped['resultado'][0]['monto']
   fecha_maxima_pago = ped['resultado'][0]['fecha_maxima_pago']
   hash_pedido = ped['resultado'][0]['hash_pedido']
   numero_pedido = ped['resultado'][0]['numero_pedido']
   cancelado = ped['resultado'][0]['cancelado']
   forma_pago_identificador = ped['resultado'][0]['forma_pago_identificador']
   token = ped['resultado'][0]['token']
   insertData2(pagado, forma_pago, fecha_pago, monto, fecha_maxima_pago, hash_pedido, numero_pedido, cancelado, forma_pago_identificador, token)

   if pagado == True: # devuelve este mensaje si esta pagado
      mensaje = "¡Su Inscripcion ha sido pagada con exito!!!"
      return render_template('resultado.html', mensaje=mensaje, ped=ped)
      
   else: # si no se encuentra pagado devuelve los sgtes mensajes
         
      if forma_pago_identificador == '1' or forma_pago_identificador == '9':#credito/debito bancard, procard
         mensaje = 'No se realizo correctamente el pago'
         return render_template('resultado_tarjeta.html', mensaje=mensaje)
      
      elif forma_pago_identificador == '10' or forma_pago_identificador == '12':#billetera personal, tigo money 
         mensaje = 'No se realizo correctamente el pago'
         return render_template('resultado_billetera.html', mensaje=mensaje)
      
   if forma_pago_identificador == '7': #cuenta bancaria
      return render_template('resultado_bancario.html', datos=numero_pedido)
      
   if forma_pago_identificador == '2' or forma_pago_identificador == '3' or forma_pago_identificador == '4':
      return render_template('resultado_ventanilla.html', ped=ped ) 

@app.route('/respuesta', methods=['GET', 'POST'])
def reply():
   data = request.get_json()
   #recibo los pedidos pagados
   pagado = data['resultado'][0]['pagado']
   forma_pago = data['resultado'][0]['forma_pago']
   fecha_pago = data['resultado'][0]['fecha_pago']
   monto = data['resultado'][0]['monto']
   fecha_maxima_pago = data['resultado'][0]['fecha_maxima_pago']
   hash_pedido = data['resultado'][0]['hash_pedido']
   numero_pedido = data['resultado'][0]['numero_pedido']
   cancelado = data['resultado'][0]['cancelado']
   forma_pago_identificador = data['resultado'][0]['forma_pago_identificador']
   token = data['resultado'][0]['token']
   insertData1(pagado, forma_pago, fecha_pago, monto, fecha_maxima_pago, hash_pedido, numero_pedido, cancelado, forma_pago_identificador, token)
   email = listData2(hash_pedido)
   mail = mailer(email)
   print("Correo enviado a",mail)
   return json.dumps(data['resultado'])

@app.route('/board')
def board():
   data = listData()
   data1 = listjoindata()
   data2 = listData3()
   data3 = listData4()
   list1 = list(range(1, len(data1)+1))
   return render_template('board.html', data=data, list1=list1, data1=data1, data2=data2, data3=data3)

@app.route('/visita-registro', methods=['POST', 'GET'])
def visit():
   if request.method=='POST':
      name = request.form['nombre']
      document = request.form['tipo_documento']
      n_document = request.form['numero_documento']
      mail = request.form['email']
      country = request.form['pais']
     
      if name == None or name == '' or name == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario2.html')

      if n_document == None or n_document == '' or n_document == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario2.html')

      if mail == None or mail == '' or mail == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario2.html')

      if country == None or country == '' or country == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario2.html')

      band = insertData3(name, document, n_document, mail, country)
      if band == False:
         mensaje = "Lo siento ya se ha registrado!!"
      else:
         mensaje = "Registro Exitoso!!!"
      flash(mensaje)
      return render_template('formulario2.html')

   return render_template('formulario2.html')

@app.route('/registro-empresa1', methods=['POST', 'GET'])
def empresa1():
   if request.method=='POST':
      name = request.form['nombre']
      document = request.form['tipo_documento']
      n_document = request.form['numero_documento']
      mail = request.form['email']
      country = request.form['pais']
      city = request.form['ciudad']
      address = None
      phone = request.form['telefono']
      institute = request.form['institucion']
      ocupation = request.form['ocupacion']
     
      if name == None or name == '' or name == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario4.html')

      if n_document == None or n_document == '' or n_document == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario4.html')

      if mail == None or mail == '' or mail == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario4.html')

      if country == None or country == '' or country == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario4.html')

      if city == None or city == '' or city == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario4.html')

      """if address == None or address == '' or address == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario4.html')"""

      if phone == None or phone == '' or phone == ' ':
         mensaje = "No se aceptan campos vacios!!"
         flash(mensaje)
         return render_template('formulario4.html')

      if (ocupation == '22' or ocupation == '23'):
         institute = request.form['ocupacion']
         ocupation = 'ORGANIZADOR'

      cant_max = cantidadIncripto(institute, ocupation)
      
      cant_permitido = cantMaxInscripto(institute, ocupation)

      if not cant_max == cant_permitido:
         
         band = insertData4(name, document, n_document, mail, country, city, address, phone, institute, ocupation)
         
         if band == False:
            
            mensaje = "Lo siento ya se ha registrado!!"

         else:
            
            mensaje = "Registro Exitoso!!!"
         
            flash(mensaje)
         
            return render_template('formulario4.html')
      
      else:
         
         mensaje = "Ha alcanzado su cupo limite!!!"
         
         flash(mensaje)

         return render_template('formulario4.html')

   return render_template('formulario4.html')

@app.route('/programa')
def programa():
   return render_template('programa.html')

@app.route('/exponentes')
def exponentes():
   return render_template('exponentes.html')

@app.route('/reporte/<int:num>')
def report(num):
   data = listjoindata()
   strFecha = data[num][16]
   d_date = datetime.datetime.strptime(strFecha, '%Y-%m-%d %H:%M:%S.%f')
   fecha = d_date.strftime("%d %B %Y %I:%M:%S %p")
   medio_pago = data[num][15]
   nombre = data[num][0]
   descripcion = data[num][8]
   email = data[num][3]
   telefono = data[num][6]
   ci = data[num][2]
   razon = data[num][12]
   ruc = data[num][13]
   monto_total = data[num][14]
   ocupacion = data[num][8]
   direccion = data[num][18]
   
   if medio_pago == 'Procard - Tarjetas de crédito' or medio_pago == 'Bancard - Tarjetas de crédito':
      ms_inter = int((monto_total*93.18)/100)
   else:
      ms_inter =  int((monto_total*94.61)/100)
   
   comision = (monto_total - ms_inter)

   html = render_template('reporte.html', fecha=fecha, medio_pago=medio_pago, nombre=nombre, descripcion=descripcion, email=email, telefono=telefono, ci=ci, razon=razon, ruc=ruc, monto_total=monto_total, ms_inter=ms_inter, comision=comision, ocupacion=ocupacion, direccion=direccion)
   return render_pdf(HTML(string=html))


@app.route('/reportes')
def reports():
   data1 = listjoindata()
   return render_template('reportes.html', data1=data1, len=enumerate(data1,0))

@app.route('/expositores')
def expositores():
   return render_template('expositores.html')

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
