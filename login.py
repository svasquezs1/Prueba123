print("hola mundo")

def login():
    print("Iniciando sesión...")
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")     
    if username == "admin" and password == "password123":
        print("¡Inicio de sesión exitoso!")
    else:        print("Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.")