import string


while True:
    rut=[]
    nombre = []
    direccion = []
    comuna = []
    correo = []
    edad = []
    genero = []
    celular = []
    tipo_suscripcion = []
    verificador = 0
    while True:
        print("Juan Maestro App: ")
        print("1. Registrar Cliente")
        print("2. Suscripcion")
        print("3. Consultar Datos Cliente")
        print("4. Salir")
        opcion = int(input())
        try:
            if(opcion == 1):
                while (verificador == 0):
                    rut_nuevo = int(input("Ingrese su rut sin digito verificador ni guiones:\n"))
                    if(rut_nuevo<4000000 or rut_nuevo>99999999):
                        print("El rut ingresado no es valido, por favor intentelo nuevamente.")
                    else:
                        rut.append(rut_nuevo)
                        verificador = 1
                verificador = 0
                nombre_nuevo = input("Por favor ingrese su nombre:\n")
                nombre.append(nombre_nuevo)
                direccion_nueva=input("Ingrese su direccion por favor:\n")
                direccion.append(direccion_nueva)
                comuna_nueva=input("Ingrese su comuna:\n")
                comuna.append(comuna_nueva)
                while (verificador==0):
                    correo_nuevo= input("Ingrese su correo:\n")
                    if (len(correo_nuevo) > 1):
                        correo.append(correo_nuevo)
                        verificador=1
                    else:
                        print("El correo ingresado no es valido, por favor intentelo nuevamente")
                verificador = 0
                while (verificador == 0):
                    try:
                        edad_nueva=int(input("Ingrese su edad:\n"))
                        if(edad_nueva<0 or edad_nueva>110):
                            print("La edad ingresada no es correcta, por favor ingrese su edad nuevamente.")
                        else:
                            verificador = 1
                            edad.append(edad_nueva)
                    except:
                        print("La edad ingresada no es correcta, ingrese nuevamente")
                verificador = 0
                while(verificador==0):
                    genero_nuevo = input("Ingrese su genero:\nM para masculino y F para femenino\n")
                    genero_nuevo = genero_nuevo.upper()
                    if (genero_nuevo == "M" or genero_nuevo == "F"):
                        genero.append(genero_nuevo)
                        verificador = 1
                    else:
                        print("El genero ingresado no es correcto, intentelo nuevamente.")
                verificador = 0
                while (verificador == 0):
                    try:
                        celular_nuevo=int(input("Ingrese su numero de celular despues de 9:\n"))
                        if(celular_nuevo<11111111 or celular_nuevo>99999999):
                            print("El celular ingresado no es correcto, por favor ingrese su celular nuevamente.")
                        else:
                            verificador = 1
                            celular.append(celular_nuevo)
                    except:
                        print("El celular ingresado no es correcto, por favor ingrese su celular nuevamente.") 
                verificador = 0                  
                while(verificador==0):
                    tipo_suscripcon_nuevo = input("Ingrese su tipo de suscripcion:\nS para Silver, P para Premium y G para gold\n")
                    tipo_suscripcon_nuevo = tipo_suscripcon_nuevo.upper()
                    if (tipo_suscripcon_nuevo == "S" or tipo_suscripcon_nuevo == "P" or tipo_suscripcon_nuevo == "G"):
                        tipo_suscripcion.append(tipo_suscripcon_nuevo)
                        verificador = 1
                    else:
                        print("El tipo de suscripcion ingresado no es correcto, por favor ingrese nuevamente.")               
                print("Ususario ingresado correctamente!:)\n")
                verificador = 0
                opcion = 0
            print(rut)
            print(len(rut))
            if (opcion == 2):
                while (verificador==0):
                    cnt = 0
                    try: 
                        buscar_rut = int(input("Ingrese rut a buscar, sin puntos ni digito verificador:\n"))
                        while (cnt < len(rut)):
                            if (rut(cnt)==buscar_rut):
                                indice = rut.index(buscar_rut) 
                                verificador=1
                            else:
                                print("El rut solicitado no ha sido ingresado en el sistema\n")
                            cnt = cnt+1
                    except:
                        ("Datos ingresados no validos, por favor intente nuevamente\n")
                verificador=0                          
        except:
            print("La opcion ingresada no es valida, por favor intente nuevamente")
