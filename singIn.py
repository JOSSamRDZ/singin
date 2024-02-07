
serverUsersName= "fulanito"
trialsOfUserName=0
#While para el numero de intentos de ingresar al usuario correcto
while trialsOfUserName <=4:
    #Modulo 1 comprovacion de nombre de usuario
    userName = input("User name:\n")
    if userName == serverUsersName:
        trialsOfPass = 0
        serverUsersPass = "Valhalla123"
        while trialsOfPass <=3:
            #Modulo 2 Comprovacion de la contrasenia del usuario
            userPass = input("Ingrese contrasenia:\n")
            if userPass==serverUsersPass:
                print("Inicio del modulo 3")
                break
            else:
                if trialsOfPass <3:
                    print("Nombre de usuario incorrecto, vuelva a intenrarlo de nuevo")
                    print(f"intentos restantes: {3-trialsOfPass}")
                    trialsOfPass+=1
                else:
                    print("Numero de intentos superados, por favor espere 15 minutos")
                    break
        break
    else:
        if trialsOfUserName < 4:
           print("Nombre de usuario incorrecto, vuelva a intenrarlo de nuevo")
           print(f"intentos restantes: {4-trialsOfUserName}")
           trialsOfUserName+=1;
        else:
            print("Numero de intentos superados, por favor espere 15 minutos")
            break