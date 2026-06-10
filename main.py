user1 = "matias"
user2 = "barbara"
password = "1234"

def login(usuario, contrasena):
    if usuario == user1 and password == contrasena or usuario == user2 and password == contrasena:
        print("Login exitoso")
        return True
    else:
        print("Credenciales incorrectas")
        return False


def menu_opciones():
    print("1. Bancos")
    print("2. Brokers (Inversiones)")
    print("3. Criptos")
    print("4. Correos")
    print("5. Redes Sociales")
    print("6. Notas")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        menu_bancos()
    elif opcion == "2":        
        menu_brokers()
    elif opcion == "3":
        menu_criptos()
    elif opcion == "4":
        menu_correos()
    elif opcion == "5":
        menu_redes_sociales()
    elif opcion == "6":
        menu_notas()
    elif opcion == "7":
        print("Saliendo...")
    else:
        print("Opción no válida")

def menu_bancos():
    print("1. Banorte")
    print("2. Klar")
    print("3. Plata")
    print("4. Mercado Pago")
    print("5. Nubank")
    print("6. uala")
    print("7. Galicia (Argentina)")
    print("8. Santander (Argentina)")
    print("9. Rebank (Argentina)")
    print("10. Brubank (Argentina)")
    print("11. Volver al menú principal")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Has seleccionado Banorte")
    elif opcion == "2":        
        print("Has seleccionado Klar")  
    elif opcion == "3":
        print("Has seleccionado Plata")
    elif opcion == "4":
        print("Has seleccionado Mercado Pago")
    elif opcion == "5":
        print("Has seleccionado Nubank")
    elif opcion == "6":
        print("Has seleccionado uala")
    elif opcion == "7":
        print("Has seleccionado Galicia (Argentina)")
    elif opcion == "8":
        print("Has seleccionado Santander (Argentina)")
    elif opcion == "9":
        print("Has seleccionado Rebank (Argentina)")
    elif opcion == "10":
        print("Has seleccionado Brubank (Argentina)")
    elif opcion == "11":
        menu_opciones()
    else:
        print("Opción no válida")

def menu_criptos():
    print("1. Binance")
    print("2. Bitso")
    print("3. Coinbase")
    print("4. Volver al menú principal")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Has seleccionado Binance")
    elif opcion == "2":        
        print("Has seleccionado Bitso")  
    elif opcion == "3":
        print("Has seleccionado Coinbase")
    elif opcion == "4":
        menu_opciones()
    else:
        print("Opción no válida")  

def menu_brokers():
    print("1. Balanz")
    print("2. Cocos capital")
    print("3. GBM")
    print("4. Volver al menú principal")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Has seleccionado Balanz")
    elif opcion == "2":        
        print("Has seleccionado Cocos capital")  
    elif opcion == "3":
        print("Has seleccionado GBM")
    elif opcion == "4":
        menu_opciones()
    else:
        print("Opción no válida")     

def menu_correos():
    print("1. Gmail")
    print("2. Outlook")
    print("3. Yahoo")
    print("4. Volver al menú principal")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Has seleccionado Gmail")
    elif opcion == "2":        
        print("Has seleccionado Outlook")  
    elif opcion == "3":
        print("Has seleccionado Yahoo")
    elif opcion == "4":
        menu_opciones()
    else:
        print("Opción no válida")         

def menu_redes_sociales():
    print("1. Facebook")
    print("2. Twitter")
    print("3. Instagram")
    print("4. LinkedIn")
    print("5. TikTok")
    print("6. YouTube")
    print("7. Pinterest")
    print("8. telegram")
    print("9. discord")
    print("10. Volver al menú principal")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Has seleccionado Facebook")
    elif opcion == "2":        
        print("Has seleccionado Twitter")  
    elif opcion == "3":
        print("Has seleccionado Instagram")
    elif opcion == "4":
        print("Has seleccionado LinkedIn")
    elif opcion == "5":
        print("Has seleccionado TikTok")
    elif opcion == "6":
        print("Has seleccionado YouTube")
    elif opcion == "7":
        print("Has seleccionado Pinterest")
    elif opcion == "8":
        print("Has seleccionado telegram")
    elif opcion == "9":
        print("Has seleccionado discord")
    elif opcion == "10":
        menu_opciones()
    else:
        print("Opción no válida")

usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")
login_exitoso = login(usuario, contrasena)
if login_exitoso:
    menu_opciones()
