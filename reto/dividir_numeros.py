def dividir_numeros():
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))

        resultado = numero1 / numero2

        print(f"Resultado: {resultado}")

        return resultado

    except ValueError:
        print("Error: debe ingresar números enteros válidos.")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")

    finally:
        print("Operación finalizada")


dividir_numeros()