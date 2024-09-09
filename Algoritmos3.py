def usd_to_cny(usd):
    conversion_rate = 6.75
    cny = usd * conversion_rate
    return f"{cny:.2f} Chinese Yuan"

# Solicita la cantidad en USD
usd = int(input("Introduce la cantidad en USD: "))

# Convierte a CNY y muestra el resultado
result = usd_to_cny(usd)
print(result)