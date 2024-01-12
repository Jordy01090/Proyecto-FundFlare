import smtplib
from email.mime.text import MIMEText

class Correo():

    def enviar_correo_confirmacion(self,destinatario):
        # Configuración del servidor SMTP de Gmail
        servidor_smtp = 'smtp.gmail.com'
        puerto_smtp = 587
        remitente = 'fundflare28@gmail.com'
        contraseña = 'xdij znow qing mjka'

        # Mensaje de correo electrónico
        asunto = 'Confirmación de Registro'
        mensaje = f'Hola,\nGracias por registrarte. Tu registro ha sido confirmado.'

        # Configuración del mensaje MIME
        mensaje_mime = MIMEText(mensaje)
        mensaje_mime['Subject'] = asunto
        mensaje_mime['From'] = remitente
        mensaje_mime['To'] = destinatario

        # Inicio de la conexión con el servidor SMTP
        server = smtplib.SMTP(servidor_smtp, puerto_smtp)
        server.starttls()

        # Inicio de sesión en la cuenta de correo electrónico
        server.login(remitente, contraseña)

        # Envío del correo electrónico
        server.sendmail(remitente, [destinatario], mensaje_mime.as_string())

        # Cierre de la conexión
        server.quit()

