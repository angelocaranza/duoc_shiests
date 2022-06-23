
version = 1.0
nombre = "Luis Pai"

numero_parte = []
nombre_parte = []
precio_parte = []
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
                ingreso_numero = input("Ingrese número de parte (10 Caracteres): ")
                ingreso_nombre = input("Ingrese nombre de producto (minimo 6 caracteres): ")
                ingreso_precio = int(input("Ingrese Precio de producto (Mayor a 0): "))
                if (len(ingreso_numero) >= 10) and (len(ingreso_nombre) >= 6) and (ingreso_precio > 0):
                   numero_parte.append(ingreso_numero)
                   nombre_parte.append(ingreso_nombre)
                   precio_parte.append(ingreso_precio) 
                   flag = False
                else:
                    print('Ingreso incorrecto, Intente nuevamente')               
        if opcion == 2:
            print("opcion 2")
            while flag2:
                numero_buscar = input("Ingrese Número a buscar: ")
                for i in range(len(numero_parte)):
                    if numero_buscar == numero_parte[i]:
                        if precio_parte[i] >= 500 :
                            print("El producto buscado es : ", numero_parte[i]," ", nombre_parte[i]," Valor : $ ", precio_parte[i])
                            i = len(numero_parte)
                            flag2 = False
                        else:
                            print("Producto sin stock")    
                        
        if opcion == 3:
            print("opcion 3")

        if opcion == 4:
            print("opcion 4")
            print(f"Gracias por usar nuestro programa {nombre}, version del programa {version}...")
            break
    except:
        print("Opción ingresada no es valida, favor de ingresar nuevamente")
