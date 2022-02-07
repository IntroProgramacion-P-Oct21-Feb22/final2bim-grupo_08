"""
    Proyecto Bimestral
    Segundo Bimestre

    Problemática: Crear un programa que sirva para ingresar distintas cuentas, para después mostrar un mensaje en 
    pantalla en funcón al número de cuentas creadas.
"""


def main():
    """
    En esta función se presenta un ciclo repetitivo en el cual se pueden crear cuentas de distinto tipo, dependiendo
    de el número que el usuario ingrese por teclado, además existe un contador que aumenta en 1 por cada cuenta creada;
    el usuario decide cuando quiere dejar de ingresar datos.
    Después se presenta un mensaje en función de la cantidad de las cuentas creadas.
    """
    condicionString = "seguir"  """"Cadena que sirve para determinar las veces que se ingresará una cuenta"""
    contador = 0
    while condicionString:
        print ("Ingrese un número para ingresar una cuenta\n[1] Facebook\n[2] Twitter\n[3] WhatsApp\n[4] Telegram\n[5] Signal\n[6] Instagram\n[7] Flickr")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            contador = contador + 1
            print(crearFacebook())
        elif opcion == 2:
            contador = contador + 1
            crearTwitter()
        elif opcion == 3:
            contador = contador + 1
            print(crearWhatsapp())
        elif opcion == 4:
            contador = contador + 1
            crearTelegram()
        elif opcion == 5:
            contador = contador + 1
            print(crearSignal())
        elif opcion == 6:
            contador = contador + 1
            crearInstagram()
        elif opcion == 7:
            contador = contador + 1
            print(crearFlickr())
        else:
            print("No existe la opción ingresada")
        print("Ingrese 'seguir' para introducir otra cuenta")
        condicionString = input()
        if condicionString != "seguir":
            print("Ha finalizado la creación de cuentas de redes sociales")
            break
    mensajeFinal = obtenerMensaje(contador)
    print(mensajeFinal)
        
    


def crearFacebook():
    """
        explicación de método.
        Se empieza pidiendo los datos del usuario para la creación de cuenta
        todas son de tipo string a excepción de la edad, que es tipo entero
        al final se reune todos los datos que el usuario ingresó y hace un retorno
        a la función principal para que pueda imprimirlo
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
        Se empieza pidiendo los datos del usuario para la creación de cuenta (usuario, nombres, apellidos, edad, ciudad, país e idioma)
        todas son de tipo string a excepción de la edad, que es tipo entero
        al final se reune todos los datos que el usuario ingresó y en este caso no hace un retorno a
        a la función principal, si no que imprime directamente los datos
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
        explicación de método.
        Se empieza pidiendo los datos del usuario para la creación de cuenta (usuario, teléfono, edad, ciudad, país)
        al final se reune todos los datos que el usuario ingresó y hace un retorno
        a la función principal para que pueda imprimirlo
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
        Se empieza pidiendo los datos del usuario para la creación de cuenta (usuario, teléfono, ciudad, país y área)
        todas son de tipo string a excepción de la edad, que es tipo entero
        al final se reune todos los datos que el usuario ingresó y en este caso no hace un retorno a
        a la función principal, si no que imprime directamente los datos
    """
    usuario = input("Ingrese su nombre de usuario: ")
    telefono = input("Ingrese su número de teléfono: ")
    ciudad = input("Ingrese su ciudad: ")
    pais = input("Ingrese su país: ")
    area = input("Ingrese su área: ")
    print("Datos de la cuenta Telegram:\nUsuario: %s\nTeléfono: %s\nCiudad: %s\nPais: %s\nÁrea: %s" % (usuario, telefono, ciudad, pais, area))

def crearSignal():
    """
        explicación de método.
        Se empieza pidiendo los datos del usuario para la creación de cuenta (usuario, teléfono, ciudad, país, hobby)
        al final se reune todos los datos que el usuario ingresó y hace un retorno
        a la función principal para que pueda imprimirlo
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
        Se empieza pidiendo los datos del usuario para la creación de cuenta (usuario, ciudad, edad, correo)
        todas son de tipo string a excepción de la edad, que es tipo entero
        al final se reune todos los datos que el usuario ingresó y en este caso no hace un retorno a
        a la función principal, si no que imprime directamente los datos
    """
    usuario = input("Ingrese su nombre de usuario: ")
    ciudad = input("Ingrese su ciudad: ")
    edad = int(input("Ingrese su edad: "))
    correo = input("Ingrese su correo: ")
    print ("Datos de la cuenta Instagram:\nUsuario: %s\nCiudad: %s\nEdad: %d\nCorreo: %s" % (usuario, ciudad, edad, correo))
    

def crearFlickr():
    """
        explicación de método.
        Se empieza pidiendo los datos del usuario para la creación de cuenta (usuario, correo)
        al final se reune todos los datos que el usuario ingresó y hace un retorno
        a la función principal para que pueda imprimirlo
    """
    usuario = input("Ingrese su nombre de usuario: ")
    correo = input("Ingrese su correo: ")
    cadena = ("Datos de la cuenta Flickr:\nUsuario: %s\nCorreo: %s" % (usuario, correo))
    return cadena

def obtenerMensaje(contador):
    """
        explicación de método.
        Este método es una función que recibe como parametro el contador, el cual es el  registro de 
        el número de cuentas creadas. En base a este dato, se presentará un mensaje en pantalla
        dependiendo de las distintas condiciones impuestas para este contador. Al final se retorna la cadena
        que contiene el mensaje
    """
    mensajeFinal = ["campaña con poca afluencia", "campaña moderada siga adelante", "Excelente campaña"]
    cadena = ""
    if contador >= 1 and contador <= 5:
        cadena = mensajeFinal[0]
    elif contador > 5 and contador <= 15:
        cadena = mensajeFinal[1]
    elif contador > 15:
        cadena = mensajeFinal[2]
    else:
        print("No se han registrado cuentas")
    return cadena
main()
    

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
