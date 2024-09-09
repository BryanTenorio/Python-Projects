import pandas as pd

# Cargar el dataset desde un archivo Excel
df = pd.read_excel("Customer Call List.xlsx")

# Eliminar duplicados
df = df.drop_duplicates()

# Eliminar columnas innecesarias
df = df.drop(columns="Not_Useful_Column")

# Limpiar la columna "Last_Name"
df["Last_Name"] = df["Last_Name"].str.strip("123._/")

# Limpiar la columna "Phone_Number"
df["Phone_Number"] = df["Phone_Number"].str.replace('[^0-9]', '', regex=True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

# Corregir valores en la columna "Phone_Number"
df["Phone_Number"] = df["Phone_Number"].str.replace('nan--', '')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--', '')

# Dividir la columna "Address" en varias columnas
df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',', 2, expand=True)

# Establecer valores consistentes en "Paying Customer"
df["Paying Customer"] = df["Paying Customer"].replace({'N': 'No', 'Y': 'Yes'})

# Establecer valores consistentes en "Do_Not_Contact"
df["Do_Not_Contact"] = df["Do_Not_Contact"].replace({'N': 'No', 'Y': 'Yes'})

# Reemplazar valores NaN con cadenas vacías
df = df.fillna('')

# Reemplazar "N/a" con cadenas vacías
df = df.replace('N/a', '')

# Eliminar filas donde "Do_Not_Contact" es "Yes"
df = df[df["Do_Not_Contact"] != 'Yes']

# Eliminar filas con números de teléfono vacíos
df = df[df["Phone_Number"] != '']

# Reiniciar los índices del DataFrame
df = df.reset_index(drop=True)

# Guardar el DataFrame limpio en un archivo CSV
df.to_csv("Cleaned_Customer_Call_List.csv", index=False)