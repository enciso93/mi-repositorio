# 1
# # numeros = float(input(f"dame un numero"))
# # if numeros > 0:
# #     print(f"el numero es positivo")
# # elif numeros < 0:
# #     print(f"el numero es negativo")
# # else:
# #    print(f"tu numero es 0")   

# # 2
# # numero = [float(input(f"dame un numero: ")) , float(input(f"dame un numero: "))]
# # if numero[0] > numero[1]:
# #     print(f"El numero mayor es {numero[0]}")
# # elif numero[1] > numero[0]:
# #      print(f"El numero mayor es {numero[1]}")
# # else:
# #     print(f"Los numeros que diste son iguales")


# # 3
# # numero = float(input(f"dame un numero para saber si es par o impar"))
# # if numero % 2 == 0:
# #     print(f"el numero es par")
# # else:
# #     print(f"el numero es impar")

# # 4
# # numero = float(input(f"Ingrese un numero: "))
# # if numero >= 10 and numero <= 20:
# #      print(f"El numero si se encuentra entre 10 y 20")
# # else:
# #      print(f"El numero  no se encuentra entre 10 y 20")

# # 5
# # numero = [float(input(f"Ingrese el 1 numero: ")) , float(input(f"Ingrese un 2 numero: ")) , float(input(f"Ingrese un 3 numero: "))]
# # if numero[0] > numero[1] and numero[0] > numero[2]:
# #      print(f"El mayor de {numero} es {numero[0]}")
# # elif numero[1] > numero[0] and numero[1] > numero[2]:
# #      print(f"El mayor de {numero} es {numero[1]}")
# # elif numero[2] > numero[0] and numero[2] > numero[1]:
# #      print(f"El mayor de {numero} es {numero[2]}")
# # else:
# #      print(f"Todos los numeros son iguales")

# # 6
# # costo = int(input(f"Ingrese el costo de su producto: $"))
# # if costo > 100:
# #     print(f"El costo total a pagar es de: ${costo - (costo * 0.1)}\nTu compra tiene un 10% de descuento por ser mayor a $100!")
# # else:
# #      print(f"El costo total de su compra es de ${costo}")


# # 7
# # edad = int(input(f"cual es tu edad: "))
# # if edad >= 18:
# #      print(f"si puedes votar")
# # else:
# #      print(f"no puedes votar")

# # 8
# precio = float(input(f"Ingrese el precio del producto: $"))
# tipo_decliente = input(f"Selecciona tu tipo de cliente:\nSi eres cliente VIP, ingrese: 1\nSi eres cliente normal, ingrese: 0\n")
# if tipo_decliente == "1":
#      print(f"Al ser cliente VIP, tienes un 20% de descuento.\no total a pagar es de ${precio - (precio * 0.2)}")
# else:
#      print(f"Al ser cliente normal, no tienes descuento.\no total a pagar es ${precio}")

# 9
# numero = float(input(f"Ingrese un número: "))
# if numero % 3 == 0 and numero % 5 == 0:
#      print(f"El numero es multiplo de 3 y 5 al mismo tiempo!")
# else:
#      print(f"El numero  no es multiplo de 3 y 5 al mismo tiempo")

# 10
# numero = [float(input(f"Ingrese un numero: ")) , float(input(f"Ingrese un numero para dividir el primero: ")) , float(input(f"Ingrese otro numero para dividir el primero: "))]
# if numero[0] % numero[1] == 0 and numero[0] % numero[2] == 0:
#      print(f"El numero {numero[0]} si es divisible entre {numero[1]} y {numero[2]}")
# else:
#      print(f"El numero {numero[0]} no es divisible entre {numero[1]} y {numero[2]}")


# 11
# dato = [float(input(f"Ingrese un primer numero: ")) , float(input(f"Ingrese un segundo numero: ")) , float(input(f"Ingrese un tercer numero: ")) , float(input(f"Ingrese un cuarto numero: ")) , float(input(f"Ingrese un quinto numero: "))]
# if dato[2] > 10:
#     print(f"Mayor que 10")
# else:
#     print(f"Menor que 10")

# 12
# numero = [float(input(f"Ingrese un primer numero: ")) , float(input(f"Ingrese un segundo numero: ")) , float(input(f"Ingrese un tercer numero: ")) , float(input(f"Ingrese un cuarto numero: "))]
# if numero[0] == 7 or numero[1] == 7 or numero[2] == 7 or numero[3] == 7:
#      print(f"El numero 7 si se encuentra en la lista! {numero}")
# else:
#      print(f"El numero 7 no se encuentra en la lista! {numero}")

# 13
# numero = [float(input(f"Ingrese un primer numero: ")) , float(input(f"Ingrese un segundo numero: ")) , float(input(f"Ingrese un tercer numero: ")) , float(input(f"Ingrese un cuarto numero: "))]
# if numero[0] + numero[1] > 10:
#     print(f"la Suma es alta")
# else:
#     print("la Suma es baja")

# 14
# nombre = [input(f"Ingresa un primer nombre: ") , input(f"Ingresa un segundo nombre: ") , input(f"Ingresa un tercer nombre: ") , input(f"Ingresa un cuarto nombre: ")]
# if nombre[3] == "Marta" or nombre[3] == "marta":
#      print(f"el nombre correcto! {nombre[3]}")
# else:
#      print(f"el nombre incorrecto! {nombre[3]}")



# 15
# colores = [input(f"Ingresa un color: ") , input(f"Ingresa otro color: ") , input(f"Ingresa un último color: ")]
# if colores[1] == "Azul" or colores[1] == "azul":
#      colores[1]="amarillo"
#      print(f"La lista actualizada es: {colores}")
# else:
#      print(f"La lista permanece igual")


# 16
# numero = (float(input(f"Ingrese un numero (1/5): ")) , float(input(f"Ingrese un numero (2/5): ")) , float(input(f"Ingrese un numero (3/5): ")) , float(input(f"Ingrese un numero (4/5): ")))
# if numero[0] < numero[3]:
#     print(f" es Orden ascendente")
# else:
#     print(f"es Orden descendente")

# 17
# tupla = (int(input(f"Ingresa un numero (1/3): ")) , int(input(f"Ingresa un numero (2/3): ")) , int(input(f"Ingresa un numero (3/3): ")))
# if tupla[1] > 30:
#      print(f"la edad es ({tupla[1]}) mayor a 30")
# else:
#      print(f"la edad es ({tupla[1]}) menor o igual a 30")

# 18 
# tupla = (int(input(f"Ingresa un numero (1/3): ")) , int(input(f"Ingresa un numero (2/3): ")) , int(input(f"Ingres un numero (3/3): ")))
# lista = list(tupla)
# if lista[1] == 2:
#      lista[1] = 10
#      tupla = tuple(lista)
#      print(f"Numeros que ingresaste: {tupla}")
# else:
#      tupla = tuple(lista)
#      print(f"Numeros que ingresaste: {tupla}")

# 19 
# tupla = (int(input(f"Ingresa una coordenada: ")) , int(input(f"Ingresa una coordenada: ")))
# if tupla[1] > 5:
#      print(f"Coordenada alta: {tupla[1]}")
# else:
#      print(f"Coordenada baja: {tupla[1]}")

# 20
# tuplaA = (int(input(f"Ingresa un numero (1/2): ")) , int(input(f"Ingresa un numero (2/2): ")))
# tuplaB = (int(input(f"Ingresa un numero (1/2): ")) , int(input(f"Ingresa in numero (2/2): ")))
# if tuplaA == tuplaB:
#      print(f"las Tuplas son iguales")
# else:
#      print(f"las Tuplas son diferentes")

# 21 
# dato = {"nombre" : input(f"escriba su nombre: ") , "edad" : int(input(f"escriba su edad: "))}
# if dato["edad"] >= 18:
#      print(f"hola {dato['nombre']} tienes {dato['edad']} por lo tanto eres un adulto")
# else:
#      print(f"hola {dato['nombre']} tienes {dato['edad']} por lo tanto eres un menor de edad")

# 22
# dato = {"nombre" : input(f"Ingrese su nombre: ") , "edad" : int(input(f"Ingrese su edad: "))}
# if dato["edad"] > 18:
#      dato["edad"] = 21
#      print(f"Datos ingresados: {dato}")
# else:
#      print(f"Datos ingresados: {dato}")

# 23
# dato = {"nombre" : input(f"Ingresa tu nombre: ")}
# if dato.get("ciudad") == None :
#      dato["ciudad"] = "Bogotá"
#      print(f"{dato}")
# else:
#      print(f"{dato}")

# 24
# producto = {"producto": input("Ingrese el producto: "),"precio": float(input("Ingrese el precio: ")) }

# if "precio" in producto: 
#     print(f"La clave 'precio' si esta en el diccionario: {producto["precio"]}")

# else: 
#     print("No hay precio en el diccionario.")        

# 25
# comida = {"pan": 1200, "leche": 2000 }
# if "pan" in comida: 
#     print(f"El precio del pan es de: {comida["pan"]}")
# else: 
    # print("Producto no disponible por precio no disponible")
