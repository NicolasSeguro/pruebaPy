import matplotlib.pyplot as plt
import numpy as np

# Definir las dos funciones
def f1(x):
    return x + 10

def f2(x):
    return -x + 3

# Crear un rango de valores de x
x = np.linspace(-10, 10, 400)

# Calcular los valores correspondientes de y
y1 = f1(x)
y2 = f2(x)

# Encontrar el punto de intersección
intersection_x = -7/2
intersection_y = 13/2

# Graficar las dos funciones
plt.plot(x, y1, label='y = x + 10')
plt.plot(x, y2, label='y = -x + 3')

# Marcar el punto de intersección
plt.scatter(intersection_x, intersection_y, color='red', label='Intersección')

# Etiquetas de ejes y leyenda
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
