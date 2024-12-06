import pandas as pd

datos = {"Edades": [25, 30, 35, 40, 45]}
df = pd.DataFrame(datos)

# Calcular estadísticas
media = df["Edades"].mean()
mediana = df["Edades"].median()
desviacion = df["Edades"].std()


print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion)