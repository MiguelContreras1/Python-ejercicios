# NUMPY

import numpy as np

# Crear dos listas a y b:
a = [1, 2, 3]
b = [4, 5, 6]

# Sumar las dos listas
print(a + b)

# Sumar en arrays:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a + b

# Ejemplo Índice de Masa Corporal (IMC):
altura = [1.7, 1.65, 1.82]
peso = [67, 55, 72]

# Cálculo para obtener el IMC:
print([p / a ** 2 for p, a in zip(peso, altura)])

# Realizar el mismo cálculo de manera más eficiente usando los arrays de NumPy:
np_altura = np.array([1.7, 1.65, 1.82])
np_peso = np.array([67, 55, 72])
imc = np_peso / np_altura ** 2
print(imc)

# Para saber qué valores son mayores que 21:
print(imc > 21)

# Obtener solo los elementos del array que cumplen la condición anterior:
print(imc[imc > 21])

# Ejemplo cálculo áreas de triángulos:
bases_tri = np.array([2, 2.37, 3.05, 1.75, 4, 2.81])
alturas_tri = np.array([1.21, 2.6, 4.4, 7.03, 4.01, 5.25])
areas_tri = bases_tri * alturas_tri / 2
print(areas_tri)

# Obtener solo los de área mayor a 6.5:
print(areas_tri[areas_tri > 6.5])

# Obtener solo los de área mayor a 6.5 y menores que 8:
print(areas_tri[(areas_tri > 6.5) & (areas_tri < 8)])

# Arrays de dos dimensiones en NumPy:
a = np.array([[2, 7, 8], [4, 8, 10]])
print(a)

# Mostrar el valor 10 del array:
print(a[1, 2])

# Obtener todas las filas, pero solo los valores de las columnas primera y segunda:
print(a[:, 0:2])

# Cálculo estadístico con NumPy:
temperaturas = np.array([12, 13.5, 13, 14, 13.2, 14.8, 15, 15.16, 16, 16.2,
                         15.7, 17, 17.2, 16.8, 14, 14.2, 14.7, 16, 17.5])

# Calcular media, mediana, mínimo, máximo, varianza, desviación estándar, y el percentil 90:
print(np.mean(temperaturas))
print(np.median(temperaturas))
print(np.min(temperaturas))
print(np.max(temperaturas))
print(np.var(temperaturas))
print(np.std(temperaturas))
print(np.percentile(temperaturas, 90))

# Generación de datos random con NumPy:
# Crear un array de 1000 elementos cuya media sea 2 y su desviación estándar sea 0,5:
array_gauss = np.random.normal(2, 0.5, 1000)
print(array_gauss)

# Comprobar la media y desviación estándar para ver que se aproximan a los valores dados:
media = np.mean(array_gauss)
print(media)
desviacion = np.std(array_gauss)
print(desviacion)

# Crear gráfico de puntos y da una campana:
import matplotlib.pyplot as plt
import scipy.stats as stats
plt.scatter(
    array_gauss,
    stats.norm.pdf(array_gauss, media, desviacion)
)

# Indexación booleana:
# Generar un array de Numpy de 5 filas y 3 columnas de números random:
numbers = np.random.randn(5, 3)
print(numbers)

# Generar otro array de Numpy en el que se establece manualmente 5 valores:
chars = np.array(['a', 'b', 'c', 'a', 'b'])

# Ver cuales valores son a:
print(chars == 'a')

# Ver los valores del array que corresponden a los lugares donde salió True (el primero y el cuarto):
print(numbers[chars == 'a'])

# Ver los valores del array que correspondan a los valores donde salió distinto a True (donde salió False, segundo,
# y quinto)
print(numbers[chars != 'a'])

# Con la disyunción "OR" (|) se evalúan dos condiciones (de numbers muestra los elementos de chars que sean b o c):
print(numbers[(chars == 'b') | (chars == 'c')])

# Usar conjunción "AND" (&) en la que también, imprimir los números que sean mayor que 0 y menor que 1:
print(numbers[(numbers > 0) & (numbers < 1)])

# Redimensionar de un array:
# Generar un array de una fila y 20 columnas, por ejemplo todos los números del 0 al 19:
a = np.arange(0, 20)
print(a)

# Convertir en un array de 4 filas y 5 columnas (debe tener la misma cantidad de elementos, en este caso 20):
a45 = a.reshape(4, 5)
print(a45)

# Seleccionar las filas 2 0 y 1 en ese orden y almacenar en array b:
b = a45[[2, 0, 1]]
print(b)

# Hacer la matriz transpuesta con '.T':
print(b.T)

# Concatenar dos arrays:
# Generar un array de 12 números enteros (arange), se redimensiona (reshape) en 3 filas y 4 columnas y se llama arr1:
arr1 = np.arange(12).reshape(3, 4)
print(arr1)

# Generar otro array de 3 filas y 4 columnas, de números flotantes random (random.randn)  y se llama arr2:
arr2 = np.random.randn(3, 4)
print(arr2)

# Concatenar con el método 'concatenate', de modo que el array arr2 se añada a continuación del array arr1:
np.concatenate([arr1, arr2], axis=1)
