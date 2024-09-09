# Importar las librerías necesarias para el análisis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset desde un archivo CSV
df = pd.read_csv('world_population.csv')

# Mostrar las primeras filas del dataframe para inspeccionar los datos
print(df.head())

# Establecer el formato de visualización para números flotantes, limitando a 2 decimales
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Mostrar información general sobre el dataset (tipo de datos, valores no nulos, etc.)
df.info()

# Generar estadísticas descriptivas sobre las columnas numéricas del dataset
print(df.describe())

# Verificar la cantidad de valores nulos por columna
print(df.isnull().sum())

# Calcular el número de valores únicos en cada columna
print(df.nunique())

# Ordenar los datos por la columna "World Population Percentage" y mostrar las 10 primeras filas
print(df.sort_values(by="World Population Percentage", ascending=False).head(10))

# Calcular la correlación entre las columnas numéricas del dataframe
correlation_matrix = df.corr()
print(correlation_matrix)

# Visualizar la matriz de correlación usando un heatmap
plt.figure(figsize=(20, 7))
sns.heatmap(correlation_matrix, annot=True)
plt.show()

# Agrupar los datos por continente y calcular la media de las columnas numéricas, luego ordenarlas por la población en 2022
df_by_continent = df.groupby('Continent').mean().sort_values(by="2022 Population", ascending=False)
print(df_by_continent)

# Filtrar las filas que contienen 'Oceania' en la columna 'Continent'
df_oceania = df[df['Continent'].str.contains('Oceania')]
print(df_oceania)

# Agrupar por continente y calcular la media para las poblaciones desde 1970 a 2022
df_population_by_continent = df.groupby('Continent')[
    ['1970 Population', '1980 Population', '1990 Population', '2000 Population', 
     '2010 Population', '2015 Population', '2020 Population', '2022 Population']
].mean().sort_values(by="2022 Population", ascending=False)
print(df_population_by_continent)

# Verificar los nombres de las columnas del dataframe
print(df.columns)

# Transponer el dataframe de continentes y poblaciones para hacer más fácil su visualización
df_transposed = df_population_by_continent.transpose()
print(df_transposed)

# Graficar la población promedio de los continentes a lo largo del tiempo
df_transposed.plot(figsize=(10,6))
plt.title("Evolución de la Población Promedio por Continente")
plt.ylabel("Población Promedio")
plt.xlabel("Años")
plt.show()

# Crear un diagrama de caja (boxplot) para visualizar la distribución de las columnas numéricas
plt.figure(figsize=(20, 10))
df.boxplot()
plt.title("Distribución de los datos numéricos del dataset")
plt.show()

# Seleccionar solo las columnas con tipo de datos float
df_float_columns = df.select_dtypes(include='float')
print(df_float_columns)
