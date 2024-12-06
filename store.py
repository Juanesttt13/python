import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("django.csv",encoding="unicode_escape")
print(
df.info()
)

# Configurar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear un histograma de la columna "Discount"
plt.figure(figsize=(8, 6))
sns.histplot(df['Discount'], bins=20, kde=False, color='blue')

# Agregar título y etiquetas
plt.title('Distribución de Descuentos', fontsize=16)
plt.xlabel('Descuento', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)

# Mostrar el gráfico
plt.show()

