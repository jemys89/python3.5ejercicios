#Modifica el programa anterior para que en vez de mostrar un mensaje genérico en el caso de que alguno o los dos números sean negativos, 
#escriba una salida diferenciada para cada una de las situaciones que se puedan producir, utilizando los siguientes mensajes:
#No se calcula la suma porque el primer número es negativo.
#No se calcula la suma porque el segundo número es negativo.
#No se calcula la suma porque los dos números son negativos.

#Jamal
#Ejercicio que suma dos números positivos

numero=float(input("teclee un número:" ))
numeroUno=float(input("teclee el siguiente número:"))
if numero >=0 and numeroUno >=0:
    print(("La suma de los dos números es:"),(numero + numeroUno))
elif numero <=0 and numeroUno <=0:
    print("No se calcula la suma porque los dos números son negativos.")
elif numero <0 and numeroUno >0:
    print("No se calcula la suma porque el primer número es negativo.")
elif numero >0 and numeroUno <0:
    print("No se calcula la suma porque el segundo número es negativo.")
