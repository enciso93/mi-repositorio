# talller condiconales
# 1
# numero = float(input(f"ingrese un numero:"))
# if numero > 0:
#     print(f"el numero {numero}es positivo")
# elif numero < 0:
#     print(f"el numero {numero} es negativo")
# else:
#     print(f"el numero es 0")

# 2
# numero1 = float(input("ingrese el primer numero"))
# numero2 = float(input("ingrese el segundo numero"))

# if numero1 > numero2:
#      print(f"el numero {numero1} es mayor que {numero2}")

# elif numero2 > numero1:
#      print(f"el numero {numero2} es mayor que {numero1}")

# 3
# numero = float(input("ingrese un numero entero "))
# if numero % 2 == 0:
#     print(f"el numero {numero} es par")
# else:
#     print(f"el numero {numero} es impar")

# 4
# numero = float(input(f"ingresa un numero: "))
# if 10<= numero <= 20:
#     print(f"el numero {numero} esta entre 10 y 20")
# else:
#     print(f"el numero {numero} no esta entre 10 y 20")    

# 5
# numero = [float(input(f"ingrese el primer numero: ")) , float(input(f"ingrese el segundo numero: ")) , float(input(f"ingresa el tercer numero: "))] 
# if numero [0] > numero[1] and numero[0] > numero[2]:
#     print(f"el numero {numero[0]} es mayor que {numero[1]} y {numero[2]}")
# elif numero [1] > numero [0] and numero [2]:
#     print(f"el numero {numero[1]} es mayor que {numero[0]} y {numero[2]}")
# else:
#     print(f"el numero {numero[2]} es mayor que{numero[0]} y {numero[1]}")

# 6 
# precio = float(input(f"Ingresa el precio de un producto: "))
# precios = precio - (precio * 0.1)
# if precio > 100: 
#      print(f"El precio final del producto con 10% de descuento es {precios}")
# else:
#      print(f"El precio final sin el 10% de descuento es: {precio}")

# 7 
# edad = int(input(f"Ingresa tu edad: "))
# if edad >= 18:
#     print(f"El ciudadano puede votar")
# else:
#     print(f"El ciudadano no puede votar")

# 8
# precio = (float(input(f"Ingrese del precio de producto: ")) , input(f"Eres cliente VIP? (Si/No): "))
# precios = precio[0] - (precio[0] * 0.2)
# if precio[1] == "Si":
#     print(f"El precio total con el descuento VIP del 20% es {precios}")
# else:
#     print (f"El precio total sin el descuento VIP es de {precio[0]}")

#9 
# numero = float(input(f"Ingresa un numero: "))
# if numero % 3 == 0 and numero % 5 == 0:
#     print(f"El numero {numero} es multiplo de 3 y 5")
# else:
#     print(f"El numero {numero} no es múltiplo de 3 y 5")

# 10
# numero1 = float(input(f"Ingresa un numero: "))
# numero2 = float(input(f"Ingresa un numero para dividirlo: "))
# numero3 = float(input(f"Ingresa otro numero para dividirlo: "))
# if numero1 % numero2 == 0 and numero1 %numero3 == 0:
#     print(f"{numero1} es divisible entre {numero2} y {numero3}")
# else:
#     print(f"{numero1} no es divisible entre {numero2} y {numero3}")






#------------------ segundo taller de condicionales-----------------------
# 1
# edad = int(input(f"dime cual es tu edad"))
# if edad <= 17:
#     print(f"Eres menor de edad")
# elif edad >=18 and edad < 65:
#     print("Eres mayor de edad")
# else:
#     print("Eres un adulto mayor")

# 2
# estatura = (float(input(f"dime tu estatura")))
# if estatura <= 1.5:
#     print(f"eres una persona baja de estatura")
# elif estatura >= 1.5 and estatura < 1.8 :
#     print(f"eres una persona de mediana estatura")   
# else:
#     print("eres una persona alta")

#3
# numero = float(input(f"dame un numero: "))
# if numero % 3 == 0 and numero % 2 == 0:
#      print(f"el numero ({numero}) es multiplo de 2 y 3")
# elif numero % 3 == 0 or numero % 2 == 0:
#      print(f"el numero ({numero}) es multiplo de 2 o de 3")
# else:
#      print(f"el numero ({numero} no es multiplo ni de 2 ni de 3)")

# 4
# numero = input("Ingresa un número decimal: ")
# opcion = numero.split(".")

# if len(opcion) == 2:
#     decimales = opcion[1]
# if len(decimales) == 1:
#          print(f"El número {numero} tiene 1 decimal.")
# elif len(decimales) == 2:
#          print(f"El número {numero} tiene 2 decimales.")
# else:
#          print(f"El número {numero} tiene más de 2 decimales.")

#5
# pais = ("Colombia", "Peru", "Argentina", "Mexico")
# pais2 = input("Ingresa un país: ")
# if pais2 in pais:
#     print(f"El pais ({pais2}) está en la tupla de países (Colombia, Peru, Argentina, Mexico).")
# else:
#     print(f"El pais ({pais2}) NO está en la tupla de países (Colombia, Peru, Argentina, Mexico).")

#6
# sangre = {"A": "A, O",
#      "B": "B, O",
#      "AB": "A, B, AB, O",
#      "O": "O"}

# tipodesangre = input("Ingresa tu tipo de sangre (A, B, AB, O): ")
# if tipodesangre == "A":
#      print("Tu sangre es compatible con:", sangre["A"])
# elif tipodesangre == "B":
#      print("Tu sangre es compatible con:", sangre["B"])
# elif tipodesangre == "AB":
#      print("Tu sangre es compatible con:", sangre["AB"])
# elif tipodesangre == "O":
#      print("Tu sangre es compatible con:", sangre["O"])
# else:
#      print("Tipo de sangre no reconocido")

# 7
# temperatura = float(input(f"Ingresa una temperatura (°C): "))
# if temperatura < 10:
#     print(f"esta haciendo frio")
# elif temperatura >= 10 and temperatura < 25:
#     print(f"el clima esta templado")
# else:
#     print(f"esta haciendo calor")

# 8
# numero1 = float(input(f"Ingresa un número: "))
# numero2 = float(input(f"Ingresa otro numero: "))
# operacion = {"1": (numero1 + numero2) , "2" : (numero1 - numero2) , "3": (numero1 * numero2)}
# pregunta = int(input(f"cual es la operacion que quieres realizar?:\n1- Suma\n2- Resta\n3- Multiplicacion\n"))
# if pregunta == 1:
#     print(f"El resultado de la suma es: {operacion['1']}")
# elif pregunta == 2:
#     print(f"El resultado de la resta es: {operacion['2']}")
# else:
#      print(f"El resultado de la multiplciacion es: {operacion['3']}")


# 9
# numero = int(input("escriba un numero del 1 al 12: "))
# if numero == 1:
#     print(f"El numero {numero} corresponde al mes Enero")
# elif numero ==2:
#     print(f"El numero {numero} corresponde al mes Febrero")
# elif numero ==3: 
#     print(f"El numero {numero} corresponde al mes Marzo ")
# elif numero ==4: 
#     print(f"El numero {numero} corresponde al mes Abril")
# elif numero ==5: 
#     print(f"El numero {numero} corresponde al mes Mayo ")
# elif numero ==6: 
#     print(f"El numero {numero} corresponde al mes Junio ")
# elif numero ==7: 
#     print(f"El numero {numero} corresponde al mes Julio ")
# elif numero ==8: 
#     print(f"El numero {numero} corresponde al mes Agosto")
# elif numero ==9: 
#     print(f"El numero {numero} corresponde al mes Septiembre")
# elif numero ==10: 
#     print(f"El numero {numero} corresponde al mes Octubre")
# elif numero ==11: 
#     print(f"El numero {numero} corresponde al mes Noviembre ")
# elif numero ==12: 
#     print(f"El numero {numero} corresponde al mes Diciembre")
# else:
#     print(f"El numero {numero} no corresponde a ningun mes,solo tenemos 12 meses")


# 10
# numero = (input("escriba un numero de 4 digitos "))
# if numero[0] ==  "1":
#     print(f"El numero de 4 digitos: {numero} empieza por el numero uno")
# elif numero[0] == "2":
#     print(f"El numero de 4 digitos: {numero} empieza por el numero dos")
# else:
#     print(f"El numero de 4 digitos: {numero} no empieza ni por el numero 2 ni por el numero 1")


# 11
# palabra= input("Ingresa una palabra: ")
# tipo = {"vocales": ["a", "e", "i", "o", "u"],
# "consonantes": ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"],
# "numeros": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]}
 
# primeral = palabra[0]
# if primeral in tipo["vocales"]:
#      print("La primera letra es una vocal.")
# elif primeral in tipo["consonantes"]:
#      print("La primera letra es una consonante.")
# elif primeral in tipo["numeros"]:
#      print("La primera letra es un número.")
# else:
#      print("La primera letra no es una vocal, consonante ni número.")

# 12
# frutas = ["manzana", "pera", "piña"]
# precios = [3300, 2800, 5700]
# fruta = input("que fruta quieres: ")
# if fruta == frutas[0]:
#      print("Precio: $", precios[0])
# elif fruta == frutas[1]:
#      print("Precio: $", precios[1])
# elif fruta == frutas[2]:
#      print("Precio: $", precios[2])
# else:
#      print(" la Fruta que quiere no esta disponible.")


# 13
# calificacion = int(input(f"Ingresa tu calificación (0 a 5): "))
# if calificacion < 3:
#      print(f"Tu calificacion fue {calificacion} reprobaste")
# elif calificacion >= 3 and calificacion < 4:
#      print(f"Tu calificacion fue {calificacion}  aprobaste felicidades")
# else:
#      print(f"Tu calificacion fue {calificacion}, excelente felicidades")

# 14
# numero = float(input(f"Ingresa un numero: "))
# if numero % 4 == 0 and numero % 6 == 0 :
#      print(f"El numero {numero} es divisible entre 4 y 6")
# else:
#      print(f"El numero no es divisible entre 4 ni 6")

# 15
# datos = {"usuario": input("escribe tu nombre de usuario: "),
# "clave": int(input("Crea tu clave numérica: "))}
# print("Tus datos fueron guardados correctamente.\n")
# tuusuario = input("Ingresa tu usuario: ")
# tuclave = int(input("Ingresa tu clave: "))
# if tuusuario == datos["usuario"] and tuclave == datos["clave"]:
#      print("Acceso concedido.")
# else:
#      print("Acceso denegado.")

# 16
# edad = int(input(f"cual es tu edad: "))
# if edad <= 12:
#      print(f"Tu edad es {edad} y eres un niño")
# elif edad >= 13 and edad <= 17:
#      print(f"Tu edad es {edad} y eres un adolescente")
# elif edad >= 18 and edad <= 64:
#      print(f"Tu edad es {edad} y eres un adulto")
# else:
#      print(f"Tu edad es {edad} y eres un adulto mayor")

# 17
# ciudad = input(f"Ingresa el nombre de una ciudad de Colombia (Primera letra en mayúscula): ")
# cap = ("Leticia", "Medellín","Arauca","Barranquilla","Cartagena","Tunja","Manizales","Florencia","Yopal","Popayán","Valledupar","Quibdó" "Montería","Bogotá","Inírida","San José del Guaviare","Neiva","Riohacha","Santa Marta","Villavicencio","Pasto","San Andrés","Cúcuta","Mocoa","Armenia","Pereira","Sincelejo","Ibagué","Cali","Mitú","Puerto Carreño")
# if ciudad in cap:
#      print(f"{ciudad} es una ciduad capital")
# else:
#      print(f"{ciudad} es una ciudad secundaria")

# 18
# producto = float(input("Ingresa el valor de la producto: "))
# precio1 = producto - (producto * 0.15)
# precio2 = producto - (producto * 0.10) 
# if producto > 200000:
#      print(f"El total a pagar con 15% de descuento es: ${precio1}")
# elif producto >= 100000 and producto <= 200000:
#      print(f"El total a pagar con 15% de descuento es: ${precio2}")
# else:
#      print(f"Tu producto fue de ${producto} y no tiene descuento")

# 19
# nombre = input("Ingresa tu nombre: ")
# horas = int(input("Ingresa el número de horas trabajadas: "))
# pago = horas * 10000
# extra = pago + (pago * 0.20)
# if horas > 40:
#     print(f"El pago de {nombre} es: ${extra}")
# else:
#     print(f"El pago de {nombre} es: ${pago}")

# 20 
calificacion = int(input(f"Ingresa tu nota (0-100): "))
if calificacion < 50:
    print(f"Tu calificacion es {calificacion} y es insuficente")
elif calificacion >= 50 and calificacion <= 79:
    print(f"Tu calificacion es {calificacion} y es aceptable")
else:
    print(f"Tu calificación es {calificacion} y es sobresaliente")