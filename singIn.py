
serverUsersName= "fulanito"
trialsOfUserName=0
#While para el numero de intentos de ingresar al usuario correcto
while trialsOfUserName <=4:
    userName = input("User name:\n")
    if userName == serverUsersName:
        print("Aqui comienza el modulo 2")
        break
    else:
        if trialsOfUserName < 4:
            print("Nombre de usuario incorrecto, vuelva a intenrarlo de nuevo")
            print(f"intentos restantes: {4-trialsOfUserName}")
            trialsOfUserName+=1
        else:
            print("Numero de intentos superados, por favor espere 15 minutos")
            break