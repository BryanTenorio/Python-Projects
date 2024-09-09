# Limpieza de Datos y Análisis Exploratorio de Datos (EDA) con Python

Este repositorio contiene proyectos realizados en Python, enfocados en la limpieza de datos y el análisis exploratorio de datos (EDA). Utilizando diferentes datasets, se abordan diversos aspectos del análisis y manipulación de datos, empleando librerías como Pandas, Seaborn y Matplotlib.

## Tabla de Contenidos
1. [Resumen de los Datasets](#resumen-de-los-datasets)
2. [Limpieza de Datos](#limpieza-de-datos)
3. [Análisis Exploratorio de Datos (EDA)](#análisis-exploratorio-de-datos-eda)

## Resumen de los Datasets

Este repositorio incluye dos datasets que se utilizan tanto para la limpieza de datos como para el análisis exploratorio de datos (EDA).

### Datasets Utilizados
- **Customer Call List**: Información de clientes, incluyendo nombres, números de teléfono, direcciones, y estatus de contacto.
- **World Population**: Datos de la población mundial desde 1970 hasta 2022, agrupados por países y continentes.

### Columnas Principales del Dataset Customer Call List

- **First_Name**: Nombre del cliente.
- **Last_Name**: Apellido del cliente.
- **Phone_Number**: Número de teléfono del cliente.
- **Address**: Dirección del cliente, incluyendo calle, estado y código postal.
- **Paying Customer**: Indica si el cliente es un cliente que paga (Yes/No).
- **Do_Not_Contact**: Indica si el cliente no debe ser contactado (Yes/No).

[Ver archivo completo](Customer_Call_List.xlsx)

### Columnas Principales del Dataset World Population

- **Country**: País de la población registrada.
- **Continent**: Continente donde se encuentra el país.
- **1970 Population**: Población del país en 1970.
- **2022 Population**: Población del país en 2022.
- **World Population Percentage**: Porcentaje de la población mundial que representa el país en un año específico.

[Ver archivo completo](world_population.csv)

## 1. Limpieza de Datos

En este proyecto se realiza la limpieza de los datasets mencionados utilizando Pandas. Los pasos incluyen la remoción de duplicados, estandarización de datos, manejo de valores nulos y blancos, y la eliminación de columnas innecesarias.

### Pasos Realizados

- **Remover Duplicados**: Identificación y eliminación de filas duplicadas en el dataset.
- **Estandarizar los Datos**: Formateo y limpieza de las columnas `Last_Name` y `Phone_Number`.
- **Manejo de Valores Nulos**: Reemplazo de valores faltantes o nulos en campos clave.
- **Remover Columnas Innecesarias**: Eliminación de columnas que no aportan al análisis.

### Ejemplo: Remover Duplicados en Pandas
```python
df = df.drop_duplicates()
```
### Ejemplo: Estandarización de Números de Teléfono
```python
df["Phone_Number"] = df["Phone_Number"].str.replace('[^0-9]', '', regex=True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[:3] + '-' + x[3:6] + '-' + x[6:])
```
[Ver archivo completo](data_Cleaning_in_pandas.ipynb)

## 2. Análisis Exploratorio de Datos (EDA)
El análisis exploratorio de datos (EDA) se realiza para obtener insights importantes del dataset `World Population`. Se utilizan técnicas estadísticas y visualizaciones para explorar la distribución de la población a nivel mundial.

### Pasos Realizados

- **Visualización General de los Datos**: Exploración de las principales columnas y estadísticas descriptivas.
- **Mapa de Calor de Correlaciones**: Análisis de la correlación entre las diferentes columnas del dataset.
- **Gráficos de Caja**: Representación de los valores de la población a través de los años.
- **Agrupación por Continentes**: Promedio de la población de cada continente por año.
- **Gráficas de Evolución**: Visualización de la evolución de la población en diferentes continentes desde 1970.

### Ejemplo: Mapa de Calor de Correlaciones
```python
sns.heatmap(df.corr(), annot=True)
plt.show()
```
### Ejemplo: Gráfica de la Evolución de la Población por Continente
```python
df2 = df.groupby('Continent')[['1970 Population', '2022 Population']].mean()
df2.transpose().plot()
plt.show()
```
[Ver archivo completo](exploratory_data_analysis.ipynb)

## Conclusiones
A través de estos proyectos se logró limpiar y estandarizar los datos de los clientes, eliminando información duplicada y corrigiendo valores inconsistentes. En el análisis exploratorio de la población mundial, se identificaron tendencias significativas y patrones de crecimiento poblacional a lo largo de los años.

## Herramientas Utilizadas
- **Pandas**: Para la manipulación y limpieza de los datos.
- **Seaborn y Matplotlib**: Para la visualización de datos.
- **Python**: Lenguaje de programación utilizado en ambos proyectos.

## Sobre el Autor

Mi nombre es Jhon Tenorio y este repositorio es parte de mi portafolio como Analista de Datos. Se encontrara con secciones para la limpieza de datos y el análisis exploratorio de datos, en Python visita mi [perfil de GitHub](https://github.com/BryanTenorio).




















