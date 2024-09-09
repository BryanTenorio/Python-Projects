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

df["Phone_Number"] = df["Phone_Number"].str.replace('[^0-9]', '', regex=True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[:3] + '-' + x[3:6] + '-' + x[6:])

