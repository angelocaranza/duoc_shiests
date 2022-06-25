import random


version = 1.0
nombre = "Angel Ocaranza"

certificados = [1000,1500]

rut = []
nombre = []
apellido_paterno = []
edad = []
estado_civil = []
genero = []
fecha_afiliacion = []
flag = True
flag2 = True
flag3 = True
def menu (*args) :
    while True:
        i=1
        for arg in args:
            print("Opción ",i,': ',arg)
            i+=1
        
        try:
            opc=int(input('\nIngrese Opción: '))
            if opc>0 and opc<i:
                return opc
            else:
                print('Opcion Incorrecta - Intente nuevamente')    

        except:
            print ('Opcion Invalida - Intente Nuevamente')

while True:

    opcion = menu('Grabar','Buscar','Imprimir','Salir')
    try:    
        if opcion == 1:
            while flag:
                
                rut_v = True
                while rut:
                    ingreso_rut = input("Ingrese rut afiliado sin puntos ni guion: ")
                    if len(ingreso_rut) >= 9 and len(ingreso_rut) <= 10:
                        rut.append(ingreso_rut) 
                        rut_v = False
                    else:
                        print("Rut ingresado no es valido, ingrese nuevamente") 
                              
                
                nombre_v = True
                while nombre_v:
                    ingreso_nombre = input("Ingrese nombre afiliado: ")
                    if len(ingreso_nombre) > 0:
                        nombre.append(ingreso_nombre)
                        nombre_v = False
                    else:
                        print("Nombre ingresado no es valido, ingrese nuevamente")    
                        
                
                apellido_v = True
                while apellido_v:
                    ingreso_apellido = input("Ingrese Apellido de afiliado")
                    if len(ingreso_apellido) > 0:
                        apellido_paterno.append(ingreso_apellido)
                        apellido_v = False
                    else:
                        print("Apellido ingresado no es valido, ingrese nuevamente")
                            
                
                edad_v = True
                while edad_v:
                    ingreso_edad = int(input("Ingrese edad afiliado: "))
                    if ingreso_edad >= 18:
                        edad.append(ingreso_edad)
                        edad_v = False
                    else :
                        print("Edad ingresada no es valida, ingrese nuevamente")    
                        
                estado_v = True
                while estado_v:            
                    ingreso_estado_civil = input("Ingrese estado civil C/casado S/soltero V/viudo: ")
                    if ingreso_estado_civil == "C" or ingreso_estado_civil == "S" or ingreso_estado_civil == "V":
                        estado_civil.append(ingreso_estado_civil)
                        estado_v = False
                    else:
                        print("Estado civil ingresado no es valido, ingrese nuevamente")
                genero_v = True
                while genero_v:            
                    ingreso_genero = input("Ingrese genero M/masculino F/femenino: ")
                    if ingreso_genero == "M" or ingreso_genero == "F":
                      genero.append(ingreso_genero)
                      genero_v = False
                    else:
                        print("Genero ingresado no es valido, ingrese nuevamente")  
                fecha_v = True
                while fecha_v:        
                    ingreso_fecha_afiliacion = input("Ingrese fecha afiliación DD/MM/YYYY")
                    if len(ingreso_fecha_afiliacion) == 10:
                        fecha_afiliacion.append(ingreso_fecha_afiliacion)
                        fecha_v = False
                    else:
                        print("Fecha ingresada no es valida, ingrese nuevamente")    
                           
        if opcion == 2:
            print("opcion 2")
            while flag2:
                rut_buscar = input("Ingrese rut de afiliado a buscar: ")
                for i in range(len(rut)):
                    if rut_buscar == rut[i]:
                        print(f"Afiliado rut {rut[i]} encontrado sus datos son: ")
                        print(f"\n Rut: {rut[i]} \n Nombre: {nombre[i]} {apellido_paterno[i]} \n Edad: {edad[i]} \n Estado civil: {estado_civil[i]} \n Genero: {genero[i]} \n Fecha de afiliación: {fecha_afiliacion[i]}")
                        i = len(rut)
                        flag2 = False
        if opcion == 3:
            while flag3:
                rut_buscar = input("Ingrese rut de afiliado a buscar: ")
                for j in range(len(rut)):
                    if rut_buscar == rut[j]:
                        rancer = random.choice(certificados)
                        if rancer == 1000:
                            cert = "A"
                        else:
                            cert = "B"    
                        print(f"Afiliado rut {rut[i]} encontrado sus datos son: ")
                        print(f"\n Certificado: {cert} Valor {rancer} Rut: {rut[i]} \n Nombre: {nombre[i]} {apellido_paterno[i]} \n Edad: {edad[i]} \n Estado civil: {estado_civil[i]} \n Genero: {genero[i]} \n Fecha de afiliación: {fecha_afiliacion[i]}")
        if opcion == 4:
            print("opcion 4")
            print(f"Gracias por usar nuestro programa {nombre}, version del programa: {version}...")
            break
    except:
        print("Opción ingresada no es valida, favor de ingresar nuevamente")
