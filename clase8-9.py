### condicionales pai 
#paso 1: Escribir un if basico

"""""
x = 1 #puedes cambiar este valor y ver como cambia el resultado.
x = int(input("ingrese un numero mani: "))
if x > 5:
    print("Hellodwa marrano")
elif x < 5:
    print("Salio negativo")
"""
"""""
############# Otro lado de la clase ######################
#Como usar el if en listas:
# Paso 1: usar for con if para filtrar elementos
numbers = [1, 4, 6, 7, 2, 8, 3]
#complete el codigo, para que se haga lo siguiente:
#1 Sume los numeros mayores que 5 y muestre el resultado
#2. Multiplique los numeros menores que 5 y muestre el resultado
#3 Cuente y muestre la cantidad de datos del arreglo
#4 Modifique el programa para que analice cualquier numero
suma = 0
multiplicacion = 1
condicion = int(input("Ingrese el numero: "))

for number in numbers:
    if number > condicion:
     suma += number

    elif number <5:
       multiplicacion *= number

print("La suma de los menores a,", condicion, "es", suma )
print("La multiplicacion de los numeros menores que ", condicion, ",", multiplicacion)

## Usamos un for para rrecorer la lista y un iof para filtrar
for number in numbers:
    if number >5:
        print(number)

"""""

############## segundo lado de la clase ##############
"""""
i = 1
tabla = []
while i < 10:
    tabla.append(i*3)
    i = i+1
    print(tabla) 
"""
"""""
frutas = ["manzana", "naranja", "pera", "papaya"]

x = ""
i = len(frutas)
while i <= 4:
    x = frutas.pop()
    print(x)
"""
diccionario = {"nombre": "Carlos", "cedula": 75002424, "edad": "35"}
lista_menores = []
lista_mayores =[]
valor_nombre_nuevo = ""
valor_cedula_nuevo = ""
valor_Edad_nuevo = ""
usuario = []
subir_usuario = [" ", " ", " "]
def f():
    print("Seleccione 1 para ingresar a un usuario")
    print("Seleccione 2 para ver la lista de menores de edad")
    print("Seleccion 3 para ver la lista de mayores de edad")
    print("Seleccione 0 para salir del programa")
f()
i = int(input("Seleccione su opcion: "))

while i<=3:
    if i == 1:
    
        valor_nombre_nuevo = input("Ingrese el nombre del usuario: ")
        valor_cedula_nuevo = input("ingrese el numero de cedula: ")
        valor_Edad_nuevo = int(input("Ingrese la edad: "))
        usuario_lista = [valor_Edad_nuevo]
        usuario =[ ("nombre", valor_nombre_nuevo), ("cedula", valor_cedula_nuevo), ("edad", valor_Edad_nuevo)]
        subir_usuario = dict(usuario)
        if valor_Edad_nuevo < 18:
          lista_menores.append(usuario_lista)
          pass
        else:
          lista_mayores.append(usuario_lista)
          pass
        diccionario = {
            "Usuario": subir_usuario,
            "Usuario0": diccionario
        }
        print("Datos ingresados exitosamente.")
        usuario_lista.clear(), usuario.clear(), subir_usuario.clear()
        print("Saliendo del programa.....")
    
    elif i == 2:
        print("La lista de menores de edad es: ", lista_menores)
        print("Saliendo del programa.....")
        f()
    elif i == 3:
        print("La lista de mayores de edad es: ", lista_mayores)
        print("Saliendo del programa.....")
        f()
    elif i ==0:
        print("Saliendo del programa......")
        f()
else:
    print("Ninguna de las opciones elegidas")        