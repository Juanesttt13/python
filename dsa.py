import matplotlib.pyplot as plt


categorias = ["Categoría A", "Categoría B", "Categoría C"]
tamaños = [40, 35, 25]

# Crear gráfico circular
plt.pie(tamaños, labels=categorias, autopct="%1.1f%%", startangle=140)
plt.title("Gráfico Circular")
plt.show()
            