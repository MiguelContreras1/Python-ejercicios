# MÉTODOS Y MÓDULOS

# MÉTODOS EN CADENAS DE TEXTO

print('Hola Mundo')

# Todos los caracteres alfabéticos en mayúsculas:
'Hola Mundo'.upper()

# Todos los caracteres alfabéticos a minúsculas:
'Hola Mundo'.lower()

# Primera letra del texto en mayúscula:
'hola mundo'.capitalize()

# Primera letra de cada palabra en mayúscula:
'hola mundo'.title()

# Contabilizar el número de veces que aparece una subcadena o carácter dentro de una cadena:
'Hola mundo'.count('o')

# Buscar los índices de aparición de una subcadena, es decir, el lugar en el que aparecen:
'Hola mundo'.find('mundo')

# Buscar el índice de la última aparición de una subcadena:
'Hola mundo mundo mundo'.rfind('mundo')

# Comprobar si una cadena de texto está compuesta únicamente por números:
c = '100'
c.isdigit()

# Comprobar si una cadena de texto está compuesta por carácteres alfanuméricos:
c = 'abcd1234'
c.isalnum()

# Comprobar si una cadena de texto está compuesta únicamente por letras:
c = 'abcd'
c.isalpha()

# Aquí podemos ver cómo devuelve un valor False porque el carácter “espacio” que hay entre la palabra Hola y mundo no
# es una letra:
c = 'Hola mundo'
c.isalpha()

# Comprobar si todos los caracteres son letras minúsculas:
c = 'hola mundo'
c.islower()

# Comprobar si todos los carácteres son letras mayúsculas:
c = 'HOLA MUNDO'
c.isupper()

# Comprobar si la primera letra de cada palabra es mayúscula:
c = 'Hola Mundo'
c.istitle()

# Comprobar si una cadena está compuesta por espacios o tabulaciones:
c = ' '
c.isspace()

# Comprobar si una cadena comienza por un carácter o subcadena concreta:
c = 'Hola mundo'
c.startswith('H')
c.startswith('Hola')

# Comprobar si una cadena termina con un carácter o subcadena concreta:
c.endswith('o')
c.endswith('mundo')

# Separar una cadena en una lista de subcadenas a partir un caracter que haga de delimitador, por ejemplo el espacio:
c = 'Hola mundo mundo'
c.split()

# El mismo ejemplo pero con el caracter ';' como delimitador:
c = 'aaa;bbb;ccc'
c.split(';')

# Añadir un carácter o subcadena entre cada carácter de una cadena, por ejemplo una coma o un guion bajo:
c = 'Hola mundo'
','.join(c)
'_'.join(c)

# Eliminar todos los carácteres o subcadenas que aparezcan al inicio y al final de una cadena, por ejemplo espacios:
c = ' Hola mundo '
c.strip()

# O el mismo ejemplo con guiones medios:
c = '--------Hola mundo---'
c.strip('-')

# Reemplazar un carácter o una subcadena de una cadena, por ejemplo, cambiar la letra o por ceros, o la palabra mundo
# por Miguel:
c = 'Hola mundo'
c.replace('o', '0')
c.replace('mundo', 'Miguel')

# Eliminar un caracter o una subcadena un número de veces:
c = 'Hola mundo mundo mundo mundo mundo'
c.replace(' mundo', '', 3)

# MÉTODOS EN LISTAS

# Añadir elementos a una lista:
l = [1, 2, 3]
l.append(4)
print(l)

# Eliminar todos los elementos de una lista:
l = [1, 2, 3]
l.clear()
print(l)

# Unir los elementos de dos listas en una:
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)

# Contar cuántas veces aparece un elemento en una lista:
l = ['Hola', 'mundo', 'mundo']
l.count('mundo')

# Mostrar la posición del índice en la que aparece por primera vez un elemento en una lista:
l = ['Hola', 'mundo', 'mundo']
l.index('Hola')
l.index('mundo')

# Insertar un elemento dentro de una lista en una posición indicada:
l = [5, 10, 15, 25]
l.insert(3, 20)
print(l)

# Sacar un elemento en una posición indicada de una lista. Si no se indica ninguna posición sacará el último elemento:
l = [10, 20, 30, 40, 50]
l.pop()
print(l)
l = [10, 20, 30, 40]
l.pop(1)
print(l)

# Borrar un elemento de la lista indicando el propio elemento. Si hay varios solo borra el primero:
l = ['uno', 'dos', 'tres']
print(l)
l.remove('dos')
print(l)

# Invertir el orden de los elementos de una lista:
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)
l = ['uno', 'dos', 'tres']
l.reverse()
print(l)

# Ordenar elementos de una lista:
l = [3, -15, 27, -9, 0]
l.sort()
print(l)
l = ['bbb', 'eee', 'ttt', 'ccc']
l.sort()
print(l)

# MÉTODOS EN CONJUNTOS

# Añadir elementos a un conjunto:
c = set()
c.add(1)
c.add(2)
c.add(3)
print(c)

# Descartar o borrar un elemento específico de un conjunto:
c = {1, 2, 3}
print(c)
c.discard(2)
print(c)
c = {'uno', 'dos', 'tres'}
print(c)
c.discard('dos')
print(c)

# Hacer una copia de un conjunto existente.
c1 = {1, 2, 3}
c2 = c1.copy()
c2.discard(2)
print(c1)
print(c2)

# Vaciar o eliminar por completo todos los elementos de un conjunto:
c = {1, 2, 3}
c.clear()
print(c)

# Comprobar que un conjunto es disjunto de otro, es decir, que no hay ningún elemento en común con otro conjunto:
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c3 = {-1, 99}
c1.isdisjoint(c2)
c1.isdisjoint(c3)

# Comprobar si un conjunto es un subconjunto de otro:
c1 = {1, 2, 3}
c2 = {1, 2, 3, 4}
c1.issubset(c2)

# Comprobar si un conjunto es un superconjunto de un subconjunto:
c1 = {1, 2, 3}
c2 = {1, 2, 3, 4}
c2.issuperset(c1)

# Unión de dos conjuntos. Si hay elementos repetidos estos no se añaden varias veces:
c1 = {1, 2, 3, 4, 5}
c2 = {3, 4, 5, 6, 7}
c1.union(c2)

# Pero esto no actualiza el valor de ningún conjunto, solo muestra por pantalla el resultado de la unión.
# Si vemos lo que contienen los conjuntos c1 y c2 veremos que no han mutado:
print(c1)
print(c2)

# Para que se actualice el valor del primer conjunto con la unión de ambos conjuntos como valor se ha de usar el
# método update() de la siguiente manera:
c1 = {1, 2, 3, 4, 5}
c2 = {3, 4, 5, 6, 7}
c1.update(c2)
print(c1)

# Encontrar elementos que no son comunes o que son distintos entre dos conjuntos:
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c1.difference(c2)
c2.difference(c1)

# Actualizar los elementos de un conjunto con los no comunes de un segundo conjunto:
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c1.difference_update(c2)
print(c1)

# Encontrar los elementos comunes entre dos conjuntos:
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c1.intersection(c2)

# Al igual que antes con el método difference() este solo devuelve un resultado, pero no actualiza el valor
# de ningún conjunto:
print(c1)
print(c2)

# Actualizar los elementos de un conjunto con los elementos comunes de un segundo conjunto:
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c1.intersection_update(c2)
print(c1)

# MÉTODOS EN DICCIONARIOS

# Obtener un valor por defecto cuando queremos acceder a una clave que no existe en un diccionario:
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
colores.get('amarillo', 'No se encuentra')
colores.get('negro', 'No se encuentra')

# Obtener una lista con las claves de un diccionario:
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
colores.keys()

# Obtener una lista con los valores de las claves de un diccionario:
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
colores.values()

# Obtener una lista de tuplas con la clave y valor de cada elemento de un # diccionario:
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
colores.items()

# Sustraer o eliminar una clave y su valor de un diccionario:
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
colores.pop('amarillo')
print(colores)

# Si quisiéramos extraer de un diccionario un elemento o registro que no existe, por ejemplo negro, podríamos añadir
# al método pop() un texto a mostrar en este caso:
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
colores.pop('negro', 'No se encuentra')

# Vaciar o eliminar todos los elementos de un diccionario:
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
print(colores)
colores.clear()
print(colores)

# MÓDULOS

# COLLECTIONS

# la colección Counter nos devolverá un diccionario con el número de veces que se repite cada uno de los elementos
# de una lista:
from collections import Counter

l = [1, 2, 4, 3, 3, 5, 1, 3, 1, 1, 6]
print(Counter(l))

# Otro ejemplo en el uso de la colección Counter es contar las veces que aparece un carácter en una cadena de
# caracteres o string:
p = 'Hola mundo!'
print(Counter(p))

# Saber cuántas veces aparece cada palabra, pero hay # que precisar que esto no es una lista de palabras, sino una
# cadena de carácteres
s = 'rojo verde azul rojo morado rojo blanco blanco'
print(s.split())

# Ya podemos utilizar la colección Counter del mismo modo que antes:
print(Counter(s.split()))

# Función integrada llamada most_common(), a la que le hemos de pasar como argumento el número de elementos que
# queremos que nos diga que son los más comunes:
n = [10, 20, 30, 40, 10, 20, 30, 10, 20, 10]
c = Counter(n)
print(c.most_common(1))

# Si a la función integrada most_common() le pasamos como argumento el # número 2 nos devolverá los dos elementos
# más comunes:
print(c.most_common(2))

# Con la colección OrderedDict podremos mostrar los índices ordenados # por la posición en la que se van añadiendo.
from collections import OrderedDict

d = {'perro': 'dog', 'gato': 'cat', 'loro': 'parrot'}
print(OrderedDict(d))

# Una manera de comprobar esta ordenación es la siguiente:
d1 = {'perro': 'dog', 'gato': 'cat'}
d2 = {'gato': 'cat', 'perro': 'dog'}
print(d1 == d2)
print(OrderedDict(d1) == OrderedDict(d2))

# DATETIME

# crear un objeto de tipo datetime en el que haremos uso del sub paquete datetime y su método now():
import datetime

dt = datetime.datetime.now()
print(dt)

# Acceder a cada uno de los atributos del objeto dt, como solo el año, # el mes, día, hora, minuto,
# segundo o microsegundos, de la siguiente manera:
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

# Podremos darle el formato que se # prefiera, por ejemplo:
print(f'{dt.year}/{dt.month}/{dt.day}')
print(f'{dt.hour}:{dt.minute}:{dt.second}.{dt.microsecond}')

# Podemos crear una fecha manualmente tal y como se muestra en el # siguiente ejemplo:
dt = datetime.datetime(2000, 1, 1, 0, 0)
print(dt)

# El módulo datetime dispone de un método propio llamado replace() para realizar este cambio, se haría lo siguiente:
dt = dt.replace(year=3000)
print(dt)

# En el módulo datetime existe un método llamado isoformat() que convierte el # dato de tipo fecha a un standard ISO:
dt = datetime.datetime.now()
print(dt.isoformat())

# Método para darle formato personalizado a la fecha y hora es el método strftime(). %A es el día de la semana
# escrito en inglés, %d es el número de día del mes, %B es el nombre del mes en inglés, %Y es el año con 4 cifras,
# %I es la hora (en formato 12h, para formato 24h es %H) y %M son los minutos.
print(dt.strftime('%A %d %B %Y %I:%M'))

# Cambiar a formato de español con librería locate:
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')
print(dt.strftime('%A %d %B %Y %I:%M'))

# MATH

# Módulo math integra una serie de funciones y métodos que nos servirán para realizar algunas operaciones matemáticas.
import math

# El método round() redondeará a la baja todos aquellos números decimales que sus decimales sean menores de 5:
print(round(1.4))

# Se redondeará todos aquellos números decimales que sus decimales sean igual o mayor que 5:
print(round(1.5))

# Con método floor() del módulo math podremos forzar que el redondeo sea siempre a la baja:
print(math.floor(1.3))
print(math.floor(1.5))
print(math.floor(1.9))

# Para forzar un redondeo al alza debemos utilizar el método ceil() del módulo math:
print(math.ceil(1.00001))
print(math.ceil(1.3))
print(math.ceil(1.8))

# Del módulo math el método fsum() es un sumatorio de una lista de números y que devuelve el resultado en formato float:
numeros = [1, 2, 3, 4, 5]
print(math.fsum(numeros))

# Diferencia con método sum:
numeros = [0.9999999, 1, 2, 3]
print(sum(numeros))
print(math.fsum(numeros))

# El método trunc() trunca un número decimal y devuelve la parte entera:
print(math.trunc(3.14159265359))

# Potencias con método llamado pow() al que se le han de pasar dos argumentos, el primero es la base y el segundo el
# exponente:
print(math.pow(2, 3))
print(math.pow(5, 4))

# Método sqrt() permitirá realizar raíces cuadradas:
print(math.sqrt(9))

# algunos atributos como las constantes del número pi o el número e:
print(math.pi)
print(math.e)

# RANDOM

# Módulo random que contiene varias herramientas o funcionalidades para trabajar y generar números aleatorios:
import random

# Genera números flotantes aleatorios menores o iguales que uno y mayores de cero.:
print(random.random())
print(random.random())
print(random.random())

# Genera números random entre un rango de dos números podríamos usar el método uniform():
print(random.uniform(1, 10))
print(random.uniform(1, 10))
print(random.uniform(1, 10))

# Generar números enteros random entre cero y un número es utilizando el método randrange():
print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))

# Podemos pasarle dos números como argumentos para que devuelva un número aleatorio entre esos números:
print(random.randrange(0, 100))
print(random.randrange(0, 100))
print(random.randrange(0, 100))

# Si añadimos un número 2 como tercer argumento solo nos sacará números random pares entre cero y cien:
print(random.randrange(0, 100, 2))
print(random.randrange(0, 100, 2))
print(random.randrange(0, 100, 2))

# Usar módulo random con algunas colecciones como las cadenas de texto, en la que podremos escoger una letra de forma
# aleatoria. Esto se consigue con el método choice():
cadena = 'Hola mundo!'
print(random.choice(cadena))
print(random.choice(cadena))
print(random.choice(cadena))

# Método choice() para obtener de forma aleatoria cualquiera de los elementos de la lista:
lista = [1, 2, 3, 4, 5]
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))

# Método shuffle() para desordenar los elementos de una lista:
lista = [1, 2, 3, 4, 5]
print(lista)
random.shuffle(lista)
print(lista)

# Método sample() le pasamos una lista como argumento, y también un número de elementos que queremos que nos devuelva
# de forma aleatoria:
lista = [1, 2, 3, 4, 5]
print(random.sample(lista, 3))
print(random.sample(lista, 3))
print(random.sample(lista, 3))

# MANEJO DE FICHEROS

# Creación de ficheros
texto = 'Esta es una línea de texto.\nY esta es otra línea de texto.\n'
fichero = open('fichero.txt', 'w', encoding='utf-8')
fichero.write(texto)
fichero.close()

# Apertura o lectura
fichero = open('fichero.txt', 'r', encoding='utf-8')
texto = fichero.read()
fichero.close()
print(texto)

# Leer un archivo línea a línea almacenando cada línea en una lista con método readlines() que tienen los objetos de
# tipo archivo:
fichero = open('fichero.txt', 'r', encoding='utf-8')
lineas = fichero.readlines()
print(lineas)
fichero.close()

# Modificación
fichero = open('fichero.txt', 'a', encoding='utf-8')
fichero.write('Esta es una línea nueva.\n')
fichero.close()

with open('fichero.txt', 'r', encoding='utf-8') as fichero:
    for linea in fichero:
        print(linea.rstrip('\n'))
