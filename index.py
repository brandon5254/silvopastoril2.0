from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "SECRET"

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
      document = "CI"
      n_document = request.form['numero_documento']
      mail = request.form['email']
      country = request.form['pais']
      city = request.form['ciudad']
      address = request.form['direccion']
      phone = request.form['telefono']
      institute = request.form['institucion']
      ocupation = request.form['ocupacion']
      f_pago = request.form['for_pago']
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
      
      if request.form['ocupacion'] == 'Estudiante Nacional' or request.form['ocupacion'] == 'Estudiante Extranjero':
         precio = 100#precio incripcion e n/e
         res = procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio)
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            #si la respuesta es true me redirecciona a la pagina de pago
            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)
            return render_template("redirect.html", token_recibed=token_recibed)
         else:# de ser falso me recarga la pagina y me salta un mensaje
            mensaje = "No se realizo el registro. Vuelva a intentarlo."
            print(all['respuesta'])
            flash(mensaje)
            return render_template('formulario.html')

      if request.form['ocupacion'] == 'Profesional Nacional':
         #precio debe ser 150$
         precio = 150
         res = procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio)
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)
            return render_template("redirect.html", token_recibed=token_recibed)
         else:
            mensaje = "No se realizo el registro. Vuelva a intentarlo."
            flash(mensaje)
            return render_template('formulario.html')

      else:
         #profesional internacional 200$
         precio = 200
         res = procesar(name, document, n_document, mail, country, city, address, phone, institute, ocupation, f_pago, participation, ponencia, english, coments, social, ruc, precio)
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)
            return render_template("redirect.html", token_recibed=token_recibed)
         else:
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
      
      if request.form['ocupacion'] == 'Estudiante Nacional' or request.form['ocupacion'] == 'Estudiante Extranjero':
         precio = 100
         cotizacion = dolarpy.get_venta()
         monto_total = int(cotizacion)*precio
         dbHandler.insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
         id_pedido = dbHandler.findByID(name, n_document)
         private_key = "1d98c69bb9c71a9529ca1e13e228040a"
         public_key = "c8928436431b6c6de669edb2ad199b3f"
         token = generar(private_key, id_pedido, monto_total)
         dates = datetime.today()
         max = dates+timedelta(days=1)
         fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")
         res = CrearPedido(token, ruc, mail, name, phone, n_document, social, public_key ,monto_total, "Inscripción X CONGRESO SILVOPASTORIL", public_key, 
         "Inscripción Estudiante Nacional/Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 100 USD (Tipo de cambio del día)", 
         monto_total, fecha_maxima_pago, id_pedido, "Inscripción Estudiante Nacional/Internacional")
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)
            return render_template("redirect.html", token_recibed=token_recibed)
         else:
            mensaje = "Registration was not performed. Try again."
            flash(mensaje)
            return render_template('form.html')

      if request.form['ocupacion'] == 'Profesional Nacional':
         precio = 150
         cotizacion = dolarpy.get_venta()
         monto_total = int(cotizacion)*precio
         dbHandler.insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
         id_pedido = dbHandler.findByID(name, n_document)
         private_key = "1d98c69bb9c71a9529ca1e13e228040a"
         public_key = "c8928436431b6c6de669edb2ad199b3f"
         token = generar(private_key, id_pedido, monto_total)
         dates = datetime.today()
         max = dates+timedelta(days=1)
         fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")
         res = CrearPedido(token, ruc, mail, name, phone, n_document, social, public_key ,monto_total, "Inscripción X CONGRESO SILVOPASTORIL", public_key, 
         "Inscripción Profesional Nacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 150 USD (Tipo de cambio del día)", 
         monto_total, fecha_maxima_pago, id_pedido, "Inscripción Profesional Nacional")
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)
            return render_template("redirect.html", token_recibed=token_recibed)
         else:
            mensaje = "Registration was not performed. Try again."
            flash(mensaje)
            return render_template('form.html')

      else:
         precio = 200
         cotizacion = dolarpy.get_venta()
         monto_total = int(cotizacion)*precio
         dbHandler.insertData(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc, monto_total)
         id_pedido = dbHandler.findByID(name, n_document)
         private_key = "1d98c69bb9c71a9529ca1e13e228040a"
         public_key = "c8928436431b6c6de669edb2ad199b3f"
         token = generar(private_key, id_pedido, monto_total)
         dates = datetime.today()
         max = dates+timedelta(days=1)
         fecha_maxima_pago = max.strftime("%Y-%m-%d %H:%M:%S")
         res = CrearPedido(token, ruc, mail, name, phone, n_document, social, public_key ,monto_total, "Inscripción X CONGRESO SILVOPASTORIL", public_key, 
         "Inscripción Profesional Internacional, el monto que figura corresponde a la moneda local (Guaraníes) lo cual equivale al monto total de 200 USD (Tipo de cambio del día)", 
         monto_total, fecha_maxima_pago, id_pedido, "Inscripción Profesional Internacional")
         all = json.loads(res)
         if all['respuesta'] == True or all['respuesta'] == "true":
            token_recibed = all['resultado'][0]['data']
            dbHandler.updateByID(token_recibed, id_pedido)
            return render_template("redirect.html", token_recibed=token_recibed)
         else:
            mensaje = "Registration was not performed. Try again."
            flash(mensaje)
            return render_template('form.html')

   else:
      return render_template('form.html')

"""@app.route('/reject')
def reject():
   return render_template('redirect.html')"""

@app.route('/board')
def board():
   data = dbHandler.listData()
   return render_template('board.html', data=data)

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
