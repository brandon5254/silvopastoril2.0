from flask import Flask, render_template, request, redirect, url_for, flash
from pago_servicio import procesar
from models import listData
import json

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
         return render_template('formulario.html')
      if request.form['ocupacion'] == 'Estudiante Nacional' or 'Estudiante Extranjero':
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
            print(all['respuesta'])
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
            return render_template("redirect.html", token_recibed=token_recibed, f_pago=f_pago)
         else:# de ser falso me recarga la pagina y me salta un mensaje
            mensaje = "No se realizo el registro. Vuelva a intentarlo."
            print(all['respuesta'])
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
      if request.form['ocupacion'] == 'Estudiante Nacional' or 'Estudiante Extranjero':
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

"""@app.route('/reject')
def reject():
   return render_template('redirect.html')"""

@app.route('/board')
def board():
   data = listData()
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
