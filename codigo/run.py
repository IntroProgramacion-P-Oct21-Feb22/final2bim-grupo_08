"""
    Proyecto Bimestral
    Segundo Bimestre

    Problemática:
"""


def main():
    contador = 1
    condicionString = "seguir"
    while condicionString:
        print ("Ingrese un número para ingresar una cuenta\n[1] Facebook\n[2] Twitter\n[3] WhatsApp\n[4] Telegram\n[5] Signal\n[6] Instagram\n[7] Flickr")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print(crearFacebook())
        elif opcion == 2:
            crearTwitter()
        elif opcion == 3:
            print(crearWhatsapp())
        elif opcion == 4:
            crearTelegram()
        elif opcion == 5:
            print(crearSignal())
        elif opcion == 6:
            crearInstagram()
        elif opcion == 7:
            print(crearFlickr())
        else:
            print("No existe la opción ingresada")
        print("Ingrese 'seguir' para introducir otra cuenta")
        condicionString = input()
        if condicionString == "seguir":
            contador += 1
        else:
            print("Ha finalizado la creación de cuentas de redes sociales")
            break
    mensajeFinal = obtenerMensaje(contador)
    print(mensajeFinal)
        
    


def crearFacebook():
    """
        explicación de método
    """
    usuario = input("Ingrese su nombre de usuario: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese su ciudad: ")
    pais = input("Ingrese su país: ")
    correo = input("Ingrese su correo: ")
    
    cadena = ("Datos de la cuenta Facebook:\nUsuario: %s\nEdad: %d\nCiudad: %s\nPais: %s\nCorreo: %s" % (usuario, edad, ciudad, pais, correo))
    return cadena

def crearTwitter():
    """
        explicación de método
    """
    usuario = input("Ingrese su nombre de usuario: ")
    nombres = input("Ingrese su nombre: ")
    apellidos = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    ciudad  = input("Ingrese su ciudad: ")
    pais = input("Ingrese su país: ")
    idioma = input("Ingrese su idioma: ")
    correo = input("Ingrese su correo: ")
    print("Datos de la cuenta Twitter:\nUsuario: %s\nNombres: %s\nApellidos: %s\nEdad: %d\nCiudad: %s\nPais: %s\nIdioma: %s\nCorreo: %s" % (usuario, nombres, apellidos, edad, ciudad, pais, idioma, correo))

def crearWhatsapp():
    """
        explicación de método
    """
    usuario = input("Ingrese su nombre de usuario: ")
    telefono = input("Ingrese su número de teléfono: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese su ciudad: ")
    pais = input("Ingrese su país: ")
    cadena = ("Datos de la cuenta Whatsapp:\nUsuario: %s\nTeléfono: %s\nEdad: %d\nCiudad: %s\nPais: %s" % (usuario, telefono, edad, ciudad, pais))
    return cadena

def crearTelegram():
    """
        explicación de método
    """
    usuario = input("Ingrese su nombre de usuario: ")
    telefono = input("Ingrese su número de teléfono: ")
    ciudad = input("Ingrese su ciudad: ")
    pais = input("Ingrese su país: ")
    area = input("Ingrese su área: ")
    print("Datos de la cuenta Telegram:\nUsuario: %s\nTeléfono: %s\nCiudad: %s\nPais: %s\nÁrea: %s" % (usuario, telefono, ciudad, pais, area))

def crearSignal():
    """
        explicación de método
    """
    usuario = input("Ingrese su nombre de usuario: ")
    telefono = input("Ingrese su número de teléfono: ")
    ciudad = input("Ingrese su ciudad: ")
    pais = input("Ingrese su país: ")
    hobby = input("Ingrese su hobby: ")
    cadena = ("Datos de la cuenta Signal:\nUsuario: %s\nTeléfono: %s\nCiudad: %s\nPais: %s\nHobby: %s" % (usuario, telefono, ciudad, pais, hobby))
    return cadena

def crearInstagram():
    """
        explicación de método
    """
    usuario = input("Ingrese su nombre de usuario: ")
    ciudad = input("Ingrese su ciudad: ")
    edad = int(input("Ingrese su edad: "))
    correo = input("Ingrese su correo: ")
    print ("Datos de la cuenta Instagram:\nUsuario: %s\nCiudad: %s\nEdad: %d\nCorreo: %s" % (usuario, ciudad, edad, correo))
    

def crearFlickr():
    """
        explicación de método
    """
    usuario = input("Ingrese su nombre de usuario: ")
    correo = input("Ingrese su correo: ")
    cadena = ("Datos de la cuenta Flickr:\nUsuario: %s\nCorreo: %s" % (usuario, correo))
    return cadena

def obtenerMensaje(contador):
    mensajeFinal = ["campaña con poca afluencia", "campaña moderada siga adelante", "Excelente campaña"]
    if contador >= 1 and contador <= 5:
        cadena = mensajeFinal[0]
    elif contador > 5 and contador <= 15:
        cadena = mensajeFinal[1]
    else:
        cadena = mensajeFinal[2]
    return cadena

    

# agregar los métodos faltantes

# Aquí empieza el proceso cuando se ejecuta por consola
# el archivo
# python run.py
# if name == "main":
#     """
#     Leer las indicaciones para que el proceso cumpla
#     lo solicitado.
#     """

#     print("proceso inicial")
#     crearFacebook()
#     cuenta_twitter = crearTwitter()
#     print(cuenta_twitter)
main()