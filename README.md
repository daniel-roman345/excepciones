Descripción

Este proyecto corresponde a la evidencia GA1-220501096-01-AA1-EV05 y tiene como objetivo aplicar el manejo de excepciones en Python para controlar errores durante la ejecución de un programa.

Se trabajaron los bloques try, except, else y finally, además de excepciones específicas, raise, validación de datos y excepciones personalizadas. Estos temas hacen parte del material de formación.

Estructura
excepciones/
│
├── ejemplos/
├── reto/
│   └── dividir_numeros.py
└── README.md
Manejo de excepciones
try: contiene el código que puede generar un error.
except: captura y maneja el error.
else: se ejecuta cuando no ocurre ninguna excepción.
finally: se ejecuta siempre.

También se utilizaron excepciones como ValueError y ZeroDivisionError, junto con raise para generar errores de forma intencional.

Reto: dividir_numeros()

El reto consiste en crear la función dividir_numeros() para:

Solicitar dos números mediante input().
Convertirlos a enteros.
Realizar la división.
Controlar ValueError.
Controlar ZeroDivisionError.
Mostrar mensajes personalizados.
Ejecutar finally con el mensaje:
Operación finalizada
Pruebas realizadas
Operación correcta
15 / 4
Resultado: 3.75
Operación finalizada
División entre cero
16 / 0
Error: no se puede dividir entre cero.
Operación finalizada
Dato inválido
hola
Error: debe ingresar números enteros válidos.
Operación finalizada

Las capturas de estas pruebas se encuentran en la carpeta capturas/.



Autor

Daniel Salas Roman