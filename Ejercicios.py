import os
os.system("cls")

#1. Contar del 1 al 10
#Usa un for con range para imprimir los números del 1 al 10.
for i in range(1,11):
    print(i)

# 2. Números pares
# Imprime todos los números pares entre 1 y 20 usando for.

for i in range(1,21):
    if i % 2 == 0:
        print(i)

# 3. Tabla de multiplicar
# Pide un número al usuario y muestra su tabla del 1 al 10.

numero = int(input("Ingrese un numero: "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")

# 4. Suma acumulada
# Calcula la suma de los números del 1 al 100 usando un for.
numero1 = int(input("Ingrese un numero: "))
for i in range(1,101):
    print(f"{numero1} + {i} = {numero1+i}")

# 5. Contador con while
# Usa un while para imprimir los números del 10 al 1 (cuenta regresiva).
