# PANDAS Y MATPLOTLIB

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

# Series

# Crear una serie de Pandas a partir de una lista de números:
numeros = [1, 2, 3, 4, 5]
serie = pd.Series(numeros)
print(serie)

# Crear una serie de Pandas a partir de cadenas de texto:
palabras = ['gato', 'perro', 'pájaro', 'pez']
serie = pd.Series(palabras)
print(serie)

# Crear una serie de Pandas a partir de una tupla:
alturas = (1.75, 1.65, 1.60, 1.85, 1.90)
alturas_series = pd.Series(alturas)
print(alturas_series)

# Crear una serie de Pandas a partir de un diccionario:
poblaciones = {
    "China": 1433783686,
    "India": 1380004385,
    "Estados Unidos": 331002651,
    "Indonesia": 273523615,
    "Brasil": 210867954
}
poblaciones_series = pd.Series(poblaciones)
print(poblaciones_series)

# Acceder a los elementos de la serie utilizando el nombre del campo:
print(poblaciones_series['Indonesia'])

# Acceder a los elementos de la serie utilizando el nombre del índice:
print(poblaciones_series[0])

# Seleccionar elementos específicos proporcionando el índice en la lista:
print(poblaciones_series[['India', 'Estados Unidos']])

# Dataframes

# CrearDataFrame que contenga información sobre varios libros, como el título, el autor y el número de páginas:
libros_df = pd.DataFrame([
    {'título': 'El principito', 'autor': 'Antoine de Saint-Exupéry', 'páginas': 91},
    {'título': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes', 'páginas': 992},
    {'título': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'páginas': 417},
    {'título': 'Matar a un ruiseñor', 'autor': 'Harper Lee', 'páginas': 281},
    {'título': 'El gran Gatsby', 'autor': 'F. Scott Fitzgerald', 'páginas': 180},
])
print(libros_df)

# Añadir nueva columna “ISBN” con un valor por defecto “Unknow”:
libros_df['ISBN'] = 'Unknown'
print(libros_df)

# Cambiar el índice de cada fila usando el atributo index:
libros_df.index = ['zero', 'one', 'two', 'three', 'four']
print(libros_df)

# Configurar cualquier columna del DataFrame como índice usando el atributo set_index():
libros_df = libros_df.set_index(['título'])
print(libros_df)

# Acceder a los datos usando el índice de una columna:
print(libros_df['páginas'])

# Acceder a los datos usando el índice de una fila:
print(libros_df.loc['Cien años de soledad'])

# Acceder a todas las filas de una columna.
print(libros_df.loc[:, 'autor'])

# Acceder a un elemento específico del DataFrame:
print(libros_df.loc['Matar a un ruiseñor', 'páginas'])

# Eliminar columnas mediante el comando del:
del libros_df['autor']
print(libros_df)

# Eliminar columnas mediante el comando drop() con axis = 1 para indicar que queremos eliminar columnas:
libros_df.drop('ISBN', axis=1)

# Lectura de ficheros

# Leer cast:
casts = pd.read_csv('C:/Users/Usuario/Documents/CIENCIA DE DATOS/REPOSITORIO GITHUB/PYTHON ejercicios/'
                    r'Pandas y Matplotlib/Pandas y Matplotlib/cast.csv',
                    index_col=None,
                    encoding='ISO-8859-1')
casts.head()

# Leer titles:
titles: DataFrame = pd.read_csv('C:/Users/Usuario/Documents/CIENCIA DE DATOS/REPOSITORIO GITHUB/PYTHON ejercicios/'
                     r'Pandas y Matplotlib/Pandas y Matplotlib/titles.csv',
                     index_col=None,
                     encoding='ISO-8859-1')
titles.tail()
print(titles)
len(titles)

# Operaciones con los datos

# Selección

# Ver los primeros y últimos títulos:
t = titles['title']
type(t)
t.head()
t.tail()

# Ver el título de la posición 0:
f = titles.loc[0]
type(f)
print(f)

# Filtrado

# Ver los títulos de las películas después de 1985:
after85 = titles[titles['year'] > 1985]
after85.head()

# Ver títulos de las películas de los 90s:
t = titles
movies90 = t[(t['year'] >= 1990) & (t['year'] < 2000)]
movies90.head()

# Ordenación

# Filtrar todas las películas cuyo título sea “Macbeth”:
t = titles
macbeth = t[t['title'] == 'Macbeth']
macbeth.head()

# Asegurarse que los datos se ordenan por índice:
macbeth = t[t['title'] == 'Macbeth'].sort_index()
macbeth.head()

# Ordenar los datos por los valores de la columna year:
macbeth = t[t['title'] == 'Macbeth'].sort_values('year')
macbeth.head()

# Tratamiento de valores nulos

# Método isnull() devuelve True si alguna fila tiene valores nulos:
print(casts.loc[3:4])
c = casts
c['n'].isnull().head()

# Método notnull() hace lo contrario que isnull():
c['n'].notnull().head()

# Mostrar las filas completas que contengan algún valor nulo:
c[c['n'].isnull()].head()

# Reemplazar los valores NaN por N/A:
c_fill = c[c['n'].isnull()].fillna('N/A')
c_fill.head()

# Operaciones con strings

# Buscar la película cuyo título es 'Maa':
t = titles
print(t[t['title'] == 'Maa'])

# Buscar todas las películas que comienzan con 'Maa':
t[t['title'].str.startswith("Maa ")].head()

# Contar valores

# Contar el número total de películas que hay por cada año:
t['year'].value_counts()

# Generación de gráficos

# Filtrar número total de películas por año y guardar estos valores en un nuevo DataFrame llamado p y trazar los datos
# en un gráfico usando pandas y la utilidad plt de matplotlib.pyplot:
t = titles
p = t['year'].value_counts()
p.plot()
plt.show()

# Ordenar primero los años (es decir, el índice) y luego trazar los datos:
p.sort_index().plot()
plt.show()

# Agrupación de datos

# Método groupby() devuelve un objeto, al que luego se le concatena el método size() para contar el número total de
# filas en cada año:
cg = c.groupby(['year']).size()
cg.plot()
plt.show()

# Agrupar las películas del actor 'Aaron Abrams' según el año:
c = casts
cf = c[c['name'] == 'Aaron Abrams']
cf.groupby(['year']).size().head()

# Para ver la lista de películas con los títulos agrupadas por años se debe pasar las columnas year y title en forma
# de lista:
cf.groupby(['year', 'title']).size().head(10)

# Agrupar los artículos por año y ver la calificación máxima, mínima y media en esos años:
cf.groupby(['year']).n.max().head()
cf.groupby(['year']).n.min().head()
cf.groupby(['year']).n.mean().head()

# Agrupación número total de películas en cada década (Para obtener la década de un año: 1985//10 = 198, 198*10 = 1980):
decade = c['year'] // 10 * 10
c_dec = c.groupby(decade).size()
c_dec.head()

# Stack/Unstack para cambiar estructura de Dataframe

# Crear DataFrame con el número de ventas de distintos productos en diferentes tiendas:
ventas_df = pd.DataFrame([
    {'Tienda 1': 100, 'Tienda 2': 150, 'Tienda 3': 200, 'Tienda 4': 250},
    {'Tienda 1': 50, 'Tienda 2': 100, 'Tienda 3': 150, 'Tienda 4': 200}
])
ventas_df.index = ['Producto 1', 'Producto 2']
print(ventas_df)

# Analizar ventas por tienda en lugar de por producto utilizando método stack() para convertir columnas en filas:
ventas_por_tienda = ventas_df.stack()
print(ventas_por_tienda)

# Analizar ventas por producto en lugar de por tienda utilizando método unstack() para convertir filas en columnas:
ventas_por_producto = ventas_df.unstack()
print(ventas_por_producto)

# Agrupar datos de DataFrame casts por década y tipo, es decir, actor y actriz:
c = casts
c.groupby([c['year'] // 10 * 10, 'type']).size().head(8)

# Agrupar los datos según el tipo:
c = casts
c_decade = c.groupby(['type', c['year'] // 10 * 10]).size()
print(c_decade)

# Crear nuevo DataFrame usando comando unstack(). Creará un nuevo marco de datos basado en el índice:
c_decade.unstack()

# Generar el gráfico mediante el método plot(), como parámetro kind el valor 'bar' para que sea un gráfico de barras:
c_decade.unstack().plot(kind='bar')
plt.show()

# MERGE

# Merge de datos de diferentes archivos:

# Cargar archivo release_dates.csv que contiene las fechas de # lanzamiento de algunas de las películas
# enumeradas en cast.csv.:
release = pd.read_csv('C:/Users/Usuario/Documents/CIENCIA DE DATOS/REPOSITORIO GITHUB/PYTHON ejercicios/'
                      r'Pandas y Matplotlib/Pandas y Matplotlib/release_dates.csv',
                      index_col=None,
                      encoding='ISO-8859-1')
release.head()
casts = pd.read_csv('C:/Users/Usuario/Documents/CIENCIA DE DATOS/REPOSITORIO GITHUB/PYTHON ejercicios/'
                    r'Pandas y Matplotlib/Pandas y Matplotlib/cast.csv',
                    index_col=None,
                    encoding='ISO-8859-1')
casts.head()

# Ver fecha de estreno de la película 'Amelia'. Filtrar Amelia en el DataFrame casts.csv:
c_amelia = casts[casts['title']=='Amelia']
c_amelia.head()

# Ver entradas de la película 'Amelia' en fechas de lanzamiento:
release[release['title'] == 'Amelia'].head()

# No hay ninguna entrada para Amelia en el año 1966 en el DataFrame c_amelia y el método merge() no combinará las
# fechas de lanzamiento de Amelia-1966:
c_amelia.merge(release).head()

# Merge de datos de un mismo archivo:

# Ver la lista de co-actores en las películas. Se fusiona la tabla consigo misma según los campos title y year:
# Ver películas cuyo protagonista es el actor 'Aaron Abrams':
c = casts[casts['name']=='Aaron Abrams']
c.head()

# Fusionar el DataFrame c con el dataframe casts completo según los campos title y year (para ser coprotagonista, el
# nombre de la película y el año deben ser iguales en ambos DataFrames):
c.merge(casts, on=['title', 'year']).head()

# Para evitar el problema de que también muestra las películas en las # que 'Aaron Abrams' es co-actor, por lo que
# aparecerá dos veces (en el campo # name_x y name_y), se hace:
c_costar = c.merge(casts, on=['title', 'year'])
c_costar = c_costar[c_costar['name_y'] != 'Aaron Abrams']
c_costar.head()

# Indexación de los datos:

# Cargar los datos de DataFrame casts sin indexación:
cast = pd.read_csv('C:/Users/Usuario/Documents/CIENCIA DE DATOS/REPOSITORIO GITHUB/PYTHON ejercicios/'
                    r'Pandas y Matplotlib/Pandas y Matplotlib/cast.csv', index_col=None)
cast.head()

# '%%timeit' ejecutará el código que viene a continuación varias veces y mostrará tiempo promedio (solo en jupiter):
# %%timeit -r 5 -n 1000

# Acceso a los datos sin indexación:
print(cast[cast['title']=='Macbeth'])

# Usar set_index para crear un índice para todos los datos. Se establece el índice con base al campo title, los números
# de índice se reemplazan por el título de las películas:
c = cast.set_index(['title'])
c.head(4)

# %%timeit -r 5 -n 1000

# Acceso a los datos con indexación sin ordenar:
print(c.loc['Macbeth'])

# Ordenar el índice y realizar la operación de filtro otra vez para ver la gran diferencia en cuanto a performance
# y tiempos se refiere:
cs = cast.set_index(['title']).sort_index()
print(cs)

# %%timeit -r 5 -n 1000

# Acceso a los datos con indexación ordenada:
print(cs.loc['Macbeth'])

# Indexación múltiple:

# Indexar usando varios índices (title y n):
cm = cast.set_index(['title', 'n']).sort_index()
print(cm)

# Buscar por el campo title. En el resultado anterior, el campo title se elimina de la lista de índices:
print(cm.loc['Macbeth'])

# Filtrar las películas # cuyo título es Macbeth y que tengan una puntuación entre 4 y 18:
print(cm.loc['Macbeth'].loc[4:18])

# Películas cuyo título es Macbeth y que tengan una puntuación de 4 en el campo n:
print(cm.loc['Macbeth'].loc[4])

# Resetear los índices:
# Restablecer o resetear los índices usando el comando reset_index:
cm.head()
cm = cm.reset_index('n')
cm.head()

# Implementación usando la librería CSV de Python:

# Lectura de fichero:
import csv
titles = list(csv.DictReader(open('C:/Users/Usuario/Documents/CIENCIA DE DATOS/REPOSITORIO GITHUB/PYTHON ejercicios/Pandas y Matplotlib/Pandas y Matplotlib/titles.csv')))

# Imprimir el título y año de los 5 primeros elementos de la lista de diccionarios:
print(titles[0:5])

# Imprimir el título y año de los últimos 5 elementos de la lista de diccionarios:
print(titles[-5:])

# Tomar primer elemento de lista de diccionarios y mostrar el título y el año en diferentes filas:
for k, v in titles[0].items():
    print(k, ':', v)

# Mostrar películas con base al año (filtrar todas las películas de 1985 y mostrar las 5 primeras):
year85 = [a for a in titles if a['year'] == '1985']
print(year85[:5])

# Filtrar películas cuyo año es entre 1990 y 1999:
movies90 = [m for m in titles if (int(m['year']) < int('2000')) and
            (int(m['year']) > int('1989'))]
print(movies90[:5])

# Mostrando películas con base al título (filtrar todas las películas que tienen un mismo título, por ejemplo Macbeth):
macbeth = [m for m in titles if m['title']=='Macbeth']
print(macbeth)

# Listar todas las películas cuyo título comience por la cadena 'Maa':
maa = [m for m in titles if m['title'].startswith('Maa')]
print(maa)

# Ordenar películas con filtro de título Macbeth por año con sorted y operator e itemgetter:
from operator import itemgetter
sorted(macbeth, key=itemgetter('year'))

# Reemplazo de cadenas vacías con un '0':
casts = list(csv.DictReader(open('C:/Users/Usuario/Documents/CIENCIA DE DATOS/REPOSITORIO GITHUB/PYTHON ejercicios/Pandas y Matplotlib/Pandas y Matplotlib/cast.csv')))
print(casts[:5])
for c in casts:
        if c['n'] == '':
            c['n'] = '0'
print(casts[:5])

# Contar valores (Counter de la librería collections para extraer un conteo de películas por año, en datos title):
from collections import Counter
by_year = Counter(t['year'] for t in titles)
print(by_year.elements)

# Saber en qué años se han estrenado más películas (los tres años):
by_year.most_common(3)

# Generación de gráficos:

# Con plt.plot() se indica qué lista de datos se quiere en cada eje. Años en eje x y número de películas en eje y:
import matplotlib.pyplot as plt
data = by_year.most_common(len(titles))
data = sorted(data)
years = [c[0] for c in data]
num_of_movies = [c[1] for c in data]
plt.plot(years, num_of_movies);

# Hacer el gŕafico un poco más ancho e indicar mediante plt.xticks() que se muestra etiqueta con el año por ejemplo
# solo una vez de cada 8 años:
data = by_year.most_common(len(titles))
data = sorted(data)
years = [c[0] for c in data]
num_of_movies = [c[1] for c in data]
fig = plt.gcf()
fig.set_size_inches(9.5, 4)
plt.xticks(ticks=range(0, len(years), 8))
plt.plot(years, num_of_movies);

# Ejemplo Standard & Poor's 500:

# Crear dataframe llamado df_sp500 en el que se importa el archivo CSV SP500_data.csv:
import matplotlib.pyplot as plt
import pandas as pd
df_sp500 = pd.read_csv(
r'C:/Users/Usuario/Documents/CIENCIA DE DATOS/REPOSITORIO GITHUB/PYTHON ejercicios/Pandas y Matplotlib/Pandas y Matplotlib/SP500_data.csv',
encoding='ISO-8859-1',
delimiter=','
)
df_sp500.head()

# Representar la columna del cierre bursátil de cada día, columna Close:
df_sp500['Close'].plot()

# Representar en el eje x la fecha del dato, hay especificar que índice del dataframe df_sp500 ha de ser columna Date:
df_sp500.index = df_sp500['Date']

# Volver a mostrar la cabecera, se han insertado en el índice los valores del campo Date:
df_sp500.head()

# Representar el gráfico de nuevo con la instrucción de antes:
df_sp500['Close'].plot()

# Ejemplo esperanza de vida frente a renta per cápita por países:

# Importar librerías y CSV Info_pais.csv:
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(
r'C:/Users/Usuario/Documents/CIENCIA DE DATOS/REPOSITORIO GITHUB/PYTHON ejercicios/Pandas y Matplotlib/Pandas y Matplotlib/Info_pais.csv',
encoding='ISO-8859-1',
delimiter=';',
decimal=','
)
df.head()

# Poner datos en orden ascendente según los valores de la columna Poblacion:
df_order = df.sort_values(
'Poblacion',
ascending=False
)
df_order.head()

# Gráfico con scatter(). En eje x los datos de columna Renta per capita y en eje y datos de columna Esperanza de vida:
plt.scatter(df_order['Renta per capita'], df_order['Esperanza de vida']);

# Añadir un título y etiquetas a los ejes x e y:
plt.scatter(
df_order['Renta per capita'],
df_order['Esperanza de vida']
)
plt.title('Renta per cápita vs Esperanza de vida')
plt.xlabel('Renta per cápita')
plt.ylabel('Esperanza de vida');

# Configurar gráfico para que sean proporcionales en tamaño y color para cada país. Crear una nueva columna llamada
# df_order['Poblacion_normalizada'] que normalice frente al máximo de # población, por lo que se asignara como valores
# la columna Población dividida entre el valor máximo de esta columna Población, dejando escalado o normalizado:
df_order['Poblacion_normalizada'] =
df_order['Poblacion']/max(df_order['Poblacion'])
df_order.head()

# Es recomendable que en vez de dividir la población de cada país entre el máximo de población, hacer la división del
# máximo entre 10000:
df_order['Poblacion_normalizada'] =
df_order['Poblacion']/(max(df_order['Poblacion'])/10000)
df_order.head()

# Crear nueva visualización utilizando la nueva columna de datos normalizados generada (utilizado el parámetro s (size)
# y como valor la columna Poblacion_normalizada):
plt.scatter(
df_order['Renta per capita'],
df_order['Esperanza de vida'],
s=df_order['Poblacion_normalizada']
)
plt.title('Renta per cápita vs Esperanza de vida')
plt.xlabel('Renta per capita')
plt.ylabel('Esperanza de vida');

# Aumentar las pulgadas del gráfico:
plt.scatter(
df_order['Renta per capita'],
df_order['Esperanza de vida'],
s=df_order['Poblacion_normalizada']
)
plt.title('Renta per cápita vs Esperanza de vida')
plt.xlabel('Renta per cápita')
plt.ylabel('Esperanza de vida')
fig = plt.gcf()
fig.set_size_inches(14.5, 10);

# Modificar el color. Añadir el atributo c (color) a continuación del atributo s (size) y como valor la columna
# Poblacion_normalizada:
plt.scatter(
df_order['Renta per capita'],
df_order['Esperanza de vida'],
s=df_order['Poblacion_normalizada'],
c=df_order['Poblacion_normalizada']
)
plt.title('Renta per cápita vs Esperanza de vida')
plt.xlabel('Renta per cápita')
plt.ylabel('Esperanza de vida')
fig = plt.gcf()
fig.set_size_inches(14.5, 10);

# Añadir etiqueta del nombre del país dentro de cada burbuja utilizando el método annotate(), para los 10 primeros, y
# arreglar los índices utilizando el método reset_index y pasándole los parámetros drop e inplace con valor True:
plt.scatter(
df_order['Renta per capita'],
df_order['Esperanza de vida'],
s=df_order['Poblacion_normalizada'],
c=df_order['Poblacion_normalizada']
)
plt.title('Renta per cápita vs Esperanza de vida')
plt.xlabel('Renta per cápita')
plt.ylabel('Esperanza de vida')
fig = plt.gcf()
fig.set_size_inches(14.5, 10);
df_order.reset_index(drop=True, inplace=True)
for i in range(0, 10):
plt.annotate(
df_order['País'][i],
(
df_order['Renta per capita'][i],
df_order['Esperanza de vida'][i]
)
)

# Añadir propiedad alpha con valor 0.5 para añadir transparencia a los círculos, y añadir mediante plt.colorbar() una
# barra lateral que indica la # escala de colores y qué valores representa:
plt.scatter(
df_order['Renta per capita'],
df_order['Esperanza de vida'],
s=df_order['Poblacion_normalizada'],
c=df_order['Poblacion_normalizada'],
alpha=0.5
)
plt.title('Renta per cápita vs Esperanza de vida')
plt.xlabel('Renta per cápita')
plt.ylabel('Esperanza de vida')
plt.colorbar()
fig = plt.gcf()
fig.set_size_inches(14.5, 10);
df_order.reset_index(drop=True, inplace=True)
for i in range(0, 10):
    plt.annotate(
df_order['País'][i],
(
df_order['Renta per capita'][i],
df_order['Esperanza de vida'][i]
)
)
