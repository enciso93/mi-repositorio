# numero1 = int(input("ingrese un numero"))
# if numero > 0:
#     print(f"positivo porque es {numero1}")
# elif numero1 < 0:
#     print(f"es negativo porque es {numero1}")
# else:
#     print(f"es cero{numero1}")

# calcula el mayor de dos numeros ingresados
# numero1 = float(input("ingrese el primer numero"))
# numero2 = float(input("ingrese el segundo numero"))

# if numero1 > numero2:
#     print(f"el numero {numero1} es mayor que {numero2}")

# elif numero2 > numero1:
#     print(f"el numero {numero2} es mayor que {numero1}")


# 3 nombres y el monto que cada unog asta y promedio

paco = float(input(f"cual fue el monto de paco"))
luis = float(input(f"cual fue el monto de luis"))
gerardo = float(input(f"cual fue el monto de gerardo"))

tupla = ("paco", "luis", "gerardo")
tot = paco + luis + gerardo
promedio = tot /3
print(tot, promedio)