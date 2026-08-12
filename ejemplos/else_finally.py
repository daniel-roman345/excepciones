try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero

except ValueError:
    print("Debes introducir un número válido.")

except ZeroDivisionError:
    print("No puedes dividir entre cero.")

else:
    print(f"El resultado es: {resultado}")

finally:
    print("Proceso finalizado")