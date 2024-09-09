def calculate_pet_ages(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

# Solicita la cantidad de años humanos
human_years = int(input("Introduce la cantidad de años humanos: "))

# Calcula y muestra el resultado
result = calculate_pet_ages(human_years)
print(f"Human years: {result[0]}, Cat years: {result[1]}, Dog years: {result[2]}")