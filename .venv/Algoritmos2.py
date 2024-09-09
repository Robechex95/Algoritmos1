import math

def convert_to_16_9(y_resolution):
    # La proporción 16:9 implica que X = (16/9) * Y
    x_resolution = math.ceil((16 / 9) * y_resolution)
    return x_resolution, y_resolution

# Solicita las resoluciones X e Y originales
y_resolution = int(input("Introduce la resolución en Y: "))

# Convierte y muestra la resolución con la relación 16:9 manteniendo la altura
x_resolution, y_resolution = convert_to_16_9(y_resolution)
print(f"Resolución convertida a 16:9: {x_resolution} × {y_resolution}")