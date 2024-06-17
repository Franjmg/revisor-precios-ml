import src.scraper.scraper as scraper
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config


def comparar_productos():
    ruta_archivo = 'backend/productos.json'
    productos_previos = scraper.leer_productos_json(ruta_archivo)
    productos_actuales = scraper.get_productos()

    # Convertir la lista previa en un diccionario para facilitar la comparación
    dicc_productos_previos = {p['titulo']: p for p in productos_previos}

    for producto in productos_actuales:
        titulo = producto['titulo']
        if titulo in dicc_productos_previos:
            precio_previo = dicc_productos_previos[titulo]['precio']
            if producto['precio'] != precio_previo:
                return(f"El precio de '{titulo}' cambió de {precio_previo} a {producto['precio']}")
        else:
            return(f"Nuevo producto encontrado: {titulo}")



def enviar_cambios_email(cambios):
    # Configuración del servidor SMTP y credenciales
    servidor_smtp = "smtp.gmail.com"
    puerto_smtp = 587
    correo_remitente = config('EMAIL')
    contraseña_remitente = config('PASSWORD')
    
    # Crear el mensaje de correo electrónico
    mensaje = MIMEMultipart()
    mensaje['From'] = correo_remitente
    mensaje['To'] = "42227624@fi.unju.edu.ar"
    mensaje['Subject'] = "Cambios de Precios"
    
    # El cuerpo del correo con los cambios
    cuerpo = "Cambios detectados:\n\n" + "".join(cambios)
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    
    # Iniciar conexión con el servidor SMTP y enviar el correo
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()  # Iniciar TLS
    servidor.login(correo_remitente, contraseña_remitente)
    servidor.send_message(mensaje)
    servidor.quit()
    
    print("Correo enviado exitosamente.")
    