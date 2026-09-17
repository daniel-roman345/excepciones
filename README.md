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

Captura de la ejecución

![Captura de pantalla de la ejecución del reto](Captura%20de%20pantalla%202026-08-11%20200844.png)

Reflexión personal

Durante el desarrollo de esta evidencia aprendí la importancia de anticipar los errores que pueden ocurrir cuando un programa recibe datos del usuario. El manejo de excepciones con try, except, else y finally me permitió escribir un código más seguro y confiable, evitando que la aplicación se detenga de forma inesperada. Al trabajar con ValueError y ZeroDivisionError comprendí que cada error tiene un contexto específico y que mostrar mensajes claros ayuda a que el usuario entienda qué debe corregir. Además, incluir un return en la función dividir_numeros() me hizo notar que una función no solo debe imprimir, sino también devolver el resultado para que pueda ser reutilizado en otras partes del programa. Esta práctica fortaleció mi comprensión sobre la programación defensiva y la calidad del software.

Autor

Daniel Salas Roman