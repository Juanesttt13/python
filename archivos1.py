import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("poblacion.csv")

# Verificar los nombres de las columnas
print("\nColumnas en el DataFrame:")
print(df.columns)

# Limpiar nombres de columnas (opcional)
df.columns = df.columns.str.strip()

año = 2000  # Año deseado
pais_codigo = "ARG"

# try:
#     poblacion = df[df["Date"] == año][pais_codigo].values[0]
#     print(f"La población de {pais_codigo} en el año {año} fue: {poblacion}")
# except KeyError:
#     print("El nombre de la columna no es correcto. Verifica las columnas disponibles.")
# except IndexError:
#     print(f"No se encontró información para el año {año} y el país {pais_codigo}.")

df1 = pd.DataFrame({"A": [1, 2, 3]})
df2 = pd.DataFrame({"A": [4, 5, 6]})
df_concat = pd.concat([df1, df2])

df_merge = pd.merge(df1, df2, on="A", how="inner")

df.sort_values(by="Edad", ascending=False)