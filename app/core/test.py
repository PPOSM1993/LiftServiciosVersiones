import smtplib
from email.mime.text import MIMEText

from config import settings

def send_email():
    try:
        # Establecemos conexion con el servidor smtp de gmail
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        mailServer.ehlo()
        #mailServer.starttls(settings.EMAIL_USE_TLS)
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        
        email_to = "po5905507@gmail.com"
        # Construimos el mensaje simple
        mensaje = MIMEText("""Este es el mensaje
        de las narices""")
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Tienes un correo"
        

        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                    email_to,
                    mensaje.as_string())
    except Exception as e:
        print(e)
        
