# num = 10
# while num > 0:
#     print(f"{num}")
#     num-=1
# print("termino el conteo")

# num = int(input("dame un numero de la tabla de multiplicar"))
# i = 1
# print(f"\inicia el contador en 1 {num}")
# while i <= 10:
#     print(f"{num} * {i} = {num * i}")
#     i+= 1

#ejercicios while
# 1
# total = 0
# while True:
#     numero= int(input("dame un numero"))
#     if numero == 0:
#         break
#     total += numero
# print(f"la suma total es {total}")

# 2
# contraseña=""
# while contraseña!="python123":
#      contraseña=input("ingrese la contraseña : ")
# print("error contraseña invalida ")
# print("correcto contraseña valida")

3
# product=""
# producto=[]
# while product!="fin":
#      product=input("deme un producto para su lista (fin) si quiere finalizar : ")
#      producto.append(product)
# print(f"su lista de productos  es {producto}")

#4
# pares = 0
# impares = 0
# n = 0
# while n < 10:
#     numero = int(input("ingrese un numero"))
#     if numero % 2 ==0:
#         pares += 1
#     else:
#         impares += 1
#     n += 0
#     print(f" numeros: {pares} son pares ") 
#     print(f" numeros_ {impares} son impares")   

# 5
# notas = []
# while True:
#     nota=input("ingrese una nota entre 0 y 5 (para salir digite 'salir' : ")
#     if nota == "salir":
#         break
#     nota=float(nota)
#     if 0 <= nota and nota <=5:
#         notas.append(nota)
# promedio=sum(notas )/ len(notas)
# print(f"las notas son {notas} y su promedio es {promedio}")

# 6
# numero=int(input("ingrese un numero para multiplicar : "))
# num=1
# print(f"\n inicando proceso para tabla de multiplicar : ")
# while num<=10:
#     print(f"{numero} por {num} = {numero*num}")
#     num+=1
#     print("fin de la tabla ")

#7
# premio=13
# while True:
#      prm=int(input("adivina el numero entre el 0 y 50 : "))
#      if prm > premio:
#          print("no tan alto ")
#      elif prm< premio:
#         print("no tan bajo")
#      else:
#          break
# print(f"correcto el numero era {premio}")

# 8
# tupla=("manzana","pera","uva","papaya","sandia")
# correcto= False
# while not correcto:
#     fruta=input("ingresa una fruta para si adiivinas la correcta: ")
#     if fruta in tupla:
#         print(F"correcto la fruta: {fruta} si esta en la tupla")
#         correcto=True
#     else:
#         print("incorrecto la fruta no esta en la tupla")

#9
# diccionario={"demonio":"demon", "piña":"pineapple", "sol":"sun","estrella":"Star", "luz":"light"}
# while True:
#     palabra=input("Ingresa una palabra a traducir: ")
#     if palabra in diccionario:
#         print(diccionario[palabra])
#         break
#     else:
#         print("tu palabra no esta en este diccionario: ")

# 10
# while True:
#     print("""----MENU----
#     1. Sumar
#     2. Restar
#     3. Multiplicar
#     4. Dividir
#     5. Salir""")
#     operacion=int(input("Elige una opción: "))
#     if operacion==5:
#         break
#     numero1=int(input("Ingresa el primer numero para comenzar la operacion: "))
#     numero2=int(input("Ingresa el segundo numero para comenzar la operacion: "))
#     if operacion==1:
#         print(f"->{numero1}+{numero2}={numero1+numero2}")
#     elif operacion==2:
#         print(f"->{numero1}-{numero2}={numero1-numero2}")
#     elif operacion==3:
#         print(f"->{numero1}*{numero2}={numero1*numero2}")
#     elif operacion==4:
#         print(f"->{numero1}/{numero2}={numero1/numero2}")
#     print("")


# 11
# personas={}
# print("Ingresa 'salir' como nombre para finalizar")
# while True:
#      dato=input(("dame un nombre: "))
#      if dato=="salir":
#          break
#      valor=int(input((f"dame la edad de {dato}: ")))
#      personas[dato]=valor
# print(personas)

# #12
# colores=["blanco","amarillo","negro","rojo","morado"]
# color=input("Adivina un color de la lista: ")
# while color not in colores:
#      color=input("el color que ingresaste no esta: ")
# print("Correcto")


# 13
# numero=int(input("dame un número para mostrar sus potencias del 1 al 5: "))
# i=1
# print(f"\npotecias del {numero}")
# while i<=5:
#     print(f"{numero}^{i}={numero**i}")
#     i+=1

# # 14
# numeros=[]
# print("Este programa solo permite ingresar 5 numeros para al final mostrar el resultado de elevar cada uno al cuadrado")
# w=1
# while w<=5:
#     numeros.append(int(input("Ingrese un numero: "))**2)
#     w+=1
# print(numeros)

# # 15
# estudiantes={}
# print("Ingresa 'fin' como nombre para finalizar")
# while True:
#     dato=input(("Ingrese el nombre de su estudiante: "))
#     if dato=="fin":
#         break
#     valor=int(input((f"cual es la nota {dato}: ")))
#     estudiantes[dato]=valor
# print(estudiantes)