



def saludo():
    print ("Saludando")

saludo()    

def suma():
    num1 = 3
    num2 = 5
    return(num1+num2)

print("La suma es:", suma())    

def sumar(a,b):
    suma = a + b
    print(f"La suma de los argumentos es {suma}")

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
sumar(num1,num2)   

def sumar2(a,b):
    suma = a + b
    return(suma)

     

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
print(f"El resultado de la suma es: ", sumar2 (num1,num2))   

