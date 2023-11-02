# identación 
if 5 > 2:
  print ("Cinco es mayor que dos") 
  # el bloque de código dentro del if está identado con dos espacios, indicando que pertenece al if.

# variables 
x = 5 # entero
y = "Hola, mundo" # cadena o string

# tipo de datos 
x = 5 # Entero
y = 5.5 # Flotante
z = "Hola" # Cadena
w = True # Booleano


# casting process para cambiar el tipo de una variable
x = 5.5
x = int(x)
print(x) # Salida: 5


# operadores aritmeticos 
print(x + y) # Suma
print(x - y) # Resta
print(x * y) # Multiplicación
print(x / y) # División

# operadores de comparacion
print(x == y) # Igual a
print(x != y) # Diferente de
print(x > y) # Mayor que

# listas 
mylist = ["manzana", "banana", "cherry"]
print(mylist)

# acceder a un item de la lista 
mylist = ["manzana", "banana", "cherry"]
print(mylist[1]) # Salida: banana

# tuplas 
mytuple = ("manzana", "banana", "cherry")
print(mytuple)

#acceder a la tupla
mytuple = ("manzana", "banana", "cherry")
print(mytuple[1]) # Salida: banana

# crear nueva tupla 
mytuple = ("manzana", "banana", "cherry")
mynewtuple = mytuple[:1] + ("arándano",) + mytuple[2:]
print(mynewtuple) # Salida: (’manzana’, ’arándano’, ’cherry’)

# diccionario 
mydict = {
"nombre": "Juan",
"edad": 30
}
print(mydict)

# acceder al diccionario
mydict = {
"nombre": "Juan",
"edad": 30
}
print(mydict["nombre"]) # Salida: Juan

# modificar el diccionario 
mydict = {
"nombre": "Juan",
"edad": 30
}
mydict["edad"] = 31
print(mydict) # Salida: {’nombre’: ’Juan’, ’edad’: 31}

# conjuntos
myset = {"manzana", "banana", "cherry"}
print(myset)

# agregar y remover elementos del conjunto 
myset = {"manzana", "banana", "cherry"}
myset.add("arándano")
myset.remove("banana")
print(myset) # Salida: {’manzana’, ’cherry’, ’arándano’}

# operaciones de conjuntos tradicionales 
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f", "a"}

print(set1.union(set2)) # Unión de conjuntos

print(set1.intersection(set2)) # Intersección de conjuntos

print(set1.difference(set2)) # Diferencia de conjuntos

# condicionales if , elif, else
edad = 18
if edad >= 18:
     print("Mayor de edad")
else:
    print("Menor de edad")

#Elif
# El ”elif” es una abreviatura de ”else if” y permite verificar múltiples expresiones para determinar si son verdaderas.

edad = 18
if edad > 18:
    print("Mayor de edad")
elif edad == 18:
    print("Justo 18 años")
else:
    print("Menor de edad")


# Bucle for y while 

# for 
frutas = ["manzana", "banana", "cherry"]
for fruta in frutas:
  print(fruta)

#while 
i = 1
while i < 6:
  print(i)
i += 1


# funciones 
def saludo(nombre):
 print(f"Hola, {nombre}")
saludo("Javier")


# parametros y argumentos en la funcion
def suma(a, b):
    return a + b
resultado = suma(5, 3)
print(resultado) # Salida: 8


# funciones lambda 
potencia = lambda x, y: x ** y
print(potencia(2, 3)) # Salida: 8

# modulos 
import math

print(math.sqrt(16)) # Salida: 4.0

# importacion selectiva
from math import sqrt

print(sqrt(16)) # Salida: 4.0

# alias al modulo 
import math as m

print(m.sqrt(16)) # Salida: 4.0

#  funciones built-in open(), read(), write(), y close()
# with open(’miarchivo.txt’, ’w’) as f:
#      f.write(’Hola Mundo’)

# with open(’miarchivo.txt’, ’r’) as f:
#     contenido = f.read()
# print(contenido) # Salida: Hola Mundo