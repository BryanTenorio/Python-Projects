def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Peso Bajo o Delgado"
    elif imc <= 24.9:
        return "Adecuado o Aceptable"
    elif imc <= 29.9:
        return "Sobrepeso"
    elif imc <= 34.9:
        return "Obesidad grado 1"
    elif imc <= 39.9:
        return "Obesidad grado 2"
    else:
        return "Obesidad grado 3"

def main():
    name = input("Ingresa tú nombre: ")

    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))

        if peso <= 0 or altura <= 0:
            print("El peso y la altura deben ser valores positivos.")
            return

        imc = calcular_imc(peso, altura)
        categoria = clasificar_imc(imc)

        print(f"{name}, tu peso es: {peso} kg, tu altura es: {altura} m, por lo tanto tu IMC es: {imc:.2f}.")
        print(f"{name}, estás en el rango de: {categoria}.")

    except ValueError:
        print("Por favor, ingresa valores numéricos válidos para el peso y la altura.")

if __name__ == "__main__":
    main()
