
import numpy as np

def menu (*args) :
    while True:
        i=1
        for arg in args:
            print(i,'.-',arg)
            i+=1
        
        try:
            opc=int(input('\nIngrese Opción: '))
            if opc>0 and opc<i:
                return(opc)
            else:
                print('Opcion Incorrecta - Intente nuevamente')    

        except:
            print ('Opcion Invalida - Intente Nuevamente')

##print(menu('Ingreso','Modificacion','Eliminacion','Consultar','Salir'))

asientos = np.array(list(range(1,43)))
NombrePasajero = np.empty(shape=43)
RutPasajero = np.empty(shape=43)
telefonoPasajero = np.empty(shape=43)
BancoPasajero = np.empty(shape=43)

flag = True

while flag :
    opcion=int(input(menu('Ver asientos disponibles','Comprar asiento','Anular vuelo','Modificar datos de pasajero','Salir')))
    
    if opcion==1:
        for i in range(1,43):
            print(asientos[i])
    if opcion==2:
        print("opcion 2")
    if opcion==3:
        print("opcion 3")
    if opcion==4:
        flag = False
        print("Mensaje de salida")
        break           


