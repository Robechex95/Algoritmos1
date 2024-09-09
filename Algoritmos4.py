def third_angle(angle1, angle2):
    return 180 - (angle1 + angle2)

# Solicita los dos ángulos interiores del triángulo
angle1 = int(input("Introduce el primer ángulo: "))
angle2 = int(input("Introduce el segundo ángulo: "))

# Calcula el tercer ángulo
result = third_angle(angle1, angle2)
print(f"El tercer ángulo es: {result} grados")