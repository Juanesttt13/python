import csv
import pandas as pd




df = pd.read_csv("poblacion.csv")
print("\nContenido del DataFrame leído desde el archivo CSV:")
print(df)

print("\nEstadísticas descriptivas:")
print(df.describe())

print(df.head())

df["COL"].mean()
print(df["COL"].mean())