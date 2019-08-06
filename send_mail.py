
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mailer(email_to):

    email_from = "organizacion@silvopastoril2019.org.py"
    password = "organizacion"

    message = MIMEMultipart()
    message["Subject"] = "Gracias por su inscripción"
    message["To"] = email_to
    message["From"] = email_from

    html_body="""
    
        <html>

            <body>
                <center>
                    <h3>Gracias por Inscribirse al X CONGRESO INTERNACIONAL
                        DE SISTEMAS SILVOPASTORILES!</h1>
                    <br>
                    <p>
                        Hemos recibido el pago correspondiente a su inscripción para participar del evento a llevarse a cabo los
                        días 24 al 26 de septiembre de 2019, en la ciudad de Mariano Roque Alonso, Paraguay.<br><br>
                        Si usted solicito la emisión de Factura Legal por el pago de la inscripción, puede pasar a retirar de la oficina del Dpto. de Tesorería del INFONA, Ruta 2 Mcal. Estigarribia km 10 1/2 - San Lorenzo de 7 a 15 hs de lunes a viernes. 
                        En el caso de ser participante extranjero el día del congreso haremos entrega de la correspondiente Factura Legal por el pago de la presente inscripción.

                    </p>
                    
                    <p>Si desea participar de la visita técnica a la ciudad de San Pedro de la Región Oriental, el día 27 de septiembre del corriente, registrese a traves del siguiente <a href="http://silvopastoril2019.org.py/visita-registro" target="_blank" rel="noopener">link</a></p>

                    <p>CUPOS LIMITADOS</p>

                    <p>
                        ¡Les esperamos!
                    </p>

                    <img style="width: 40%;" src="https://i.ibb.co/LrxPVPm/Logo-Congreso-Silvopastoril-COLOR-Horizontal-04.png" alt="Logo-Congreso-Silvopastoril-COLOR-Horizontal-04" border="0">

                </center>
            </body>

            </html>
    
    """

    message.attach(MIMEText(html_body, 'html'))

    try:
        smOb = smtplib.SMTP('168.90.176.111', 25)
        smOb.starttls()
        smOb.login('admin', 'geav261112')
        email_message = message.as_string().encode("utf-8")
        smOb.sendmail(message["From"], message["To"], email_message)
        smOb.quit()
        print("Email sent")
    except Exception as e:
        print(e)

    return email_to