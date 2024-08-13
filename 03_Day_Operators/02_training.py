# Día 3: 30 días de programación en python

# EJERCICIOS - ENTRENAMIENTO !! 💪🏻

#💻 Ejercicios - Día 3

'''
Ejercicios:

1. Declara tu edad como variable entera ✔️
2. Declara tu altura como una variable float ✔️
3. Declarar una variable que almacena un número complejo ✔️
4. Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule un área de este triángulo (área = 0,5 x b x h). ✔️
5. Escriba un script que pida al usuario que escriba el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c). ✔️
6. Obtenga la longitud y el ancho de un rectángulo usando el símbolo del sistema. Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho)) ✔️
7. Obtenga el radio de un círculo usando el mensaje. Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3.14. ✔️
8. Calcula la pendiente, la intersección con el eje x y la intersección con el eje y de y = 2x -2 ✔️
9. La pendiente es (m = y2-y1/x2-x1). Halla la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10) ✖️
10. Compara las pendientes de las tareas 8 y 9. ✖️
11. Calcula el valor de y (y = x^2 + 6x + 9). Intenta usar diferentes valores de x y averigua en qué valor de x y va a ser 0. ✖️
12. Encuentra la longitud de 'pitón' y 'dragón' y haz una afirmación de comparación falsa. ✔️
13. Use el operador y para verificar si 'on' se encuentra tanto en 'python' como en 'dragon' ✔️
14. Espero que este curso no esté lleno de jerga. Úselo en para verificar si hay jerga en la oración. ✔️
15. No hay 'encendido' tanto en dragón como en pitón ✔️
16. Encuentre la longitud del texto python y convierta el valor en float y conviértalo en string ✔️
17. Los números pares son divisibles por 2 y el resto es cero. ¿Cómo se comprueba si un número es par o no usando python? ✔️
18. Compruebe si la división del suelo de 7 por 3 es igual al valor int convertido de 2,7. ✔️ 
19. Compruebe si el tipo '10' es igual al tipo 10 ✔️
20. Comprueba si int('9.8') es igual a 10 ✔️
21. Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el pago de la persona? ✔️
22. Escriba un script que solicite al usuario que introduzca el número de años. Calcula el número de segundos que una persona puede vivir. Supongamos que una persona puede vivir cien años ✔️
23. Escriba un script de Python que muestre la siguiente tabla ✔️
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
'''

# SOLUCION NIVEL 1 😁✌️

# 1. Declara tu edad como variable entera ✔️
age = 26

# 2. Declara tu altura como una variable float ✔️
altura = 1.65

# 3. Declarar una variable que almacena un número complejo ✔️
number_complex = 1 + 3j

# 4. Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule un área de este triángulo (área = 0,5 x b x h). ✔️
base = float(input("Por favor ingrese la base del triangulo: "))
heigth = float(input("Por favor ingrese la altura del triangulo: "))

area = 0.5 * base * heigth

print(f"El area del triangulo es: {area}")

# 5. Escriba un script que pida al usuario que escriba el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c). ✔️
lado_a = float(input("Por favor ingresa el valor del lado A del triangulo: "))
lado_b = float(input("Por favor ingresa el valor del lado B del triangulo: "))
lado_c = float(input("Por favor ingresa el valor del lado C del triangulo: "))

perimetro = lado_a + lado_b + lado_c

print(f"El perimetro del triangulo es: {perimetro}")

# 6. Obtenga la longitud y el ancho de un rectángulo usando prompt. Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho)) ✔️
length = float(input("Por favor ingrese el largo del rectangulo: "))
width = float(input("Por favor ingrese el ancho del rectangulo: "))

area = length * width
perimetro = 2 * (length + width)

print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")

#7. Obtenga el radio de un círculo usando prompt. Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3.14. ✔️
PI = 3.14

radio = float(input("Ingrese por favor el radio del circulo: "))

area = PI * radio ** 2
circunferencia = 2 * PI * radio

print(f"El area del circulo es: {area}")
print(f"La circunferencia del circulo es: {circunferencia}")

# 8. Calcula la pendiente, la intersección con el eje x y la intersección con el eje y de y = 2x -2 ✔️
pendiente = 2
interseccion = -2

x_interseccion = -(interseccion) / pendiente

print(f"Pendiente: {pendiente}")
print(f"Intersección en el eje y: {interseccion}")
print(f"Intersección en el eje x: {x_interseccion}")

# 9. La pendiente es (m = y2-y1/x2-x1). Halla la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10) ✖️
# 10. Compara las pendientes de las tareas 8 y 9. ✖️
# 11. Calcula el valor de y (y = x^2 + 6x + 9). Intenta usar diferentes valores de x y averigua en qué valor de x y va a ser 0. ✖️

# 12. Encuentra la longitud de 'pitón' y 'dragón' y haz una afirmación de comparación falsa. ✔️
print(len("piton"))
print(len("dragon"))

print(len("piton") == len("dragon"))

# 13. Use el operador y para verificar si 'on' se encuentra tanto en 'python' como en 'dragon' ✔️
print("on" in ("piton" and "dragon"))

# 14. Espero que este curso no esté lleno de jerga. Úse in para verificar si hay jerga en la oración. ✔️
print("jerga" in "Espero que este curso no esté lleno de jerga")

# 15. No hay 'on' tanto en dragón como en pitón ✔️
print("on" not in ("piton" and "dragon"))

# 16. Encuentre la longitud del texto python y convierta el valor en float y conviértalo en string ✔️
text = "python"
print(len(text))

float_text = float(len(text))
print(float_text)

string_text = str(float_text)
print(type(string_text))

# 17. Los números pares son divisibles por 2 y el resto es cero. ¿Cómo se comprueba si un número es par o no usando python? ✔️
num = int(input("Ingese por favor un numero: "))

if (num % 2) == 0:
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")
    
# 18. Compruebe si la división floor de 7 por 3 es igual al valor int convertido de 2,7. ✔️
num_1 = 7
num_2 = 3

division = num_1 / num_2
floor_division = num_1 // num_2

print(f"Division: {division}")
print(f"Floor division: {floor_division}")

# 19. Compruebe si el tipo '10' es igual al tipo 10 ✔️
num_a = "10"
num_b = 10

print(type(num_a))
print(type(num_b))
print(num_a == num_b)

#20. Comprueba si int('9.8') es igual a 10 ✔️
num_int = int(9.8)

print(num_int == 10)

# 21. Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el pago de la persona? ✔️
horas = int(input("Por favor ingrese las horas: "))
tarifa_hora = int(input("Por favor ingrese la tarifa por hora: "))
pago_persona = horas * tarifa_hora

print(f"El pago por persona es {pago_persona}")

# 22. Escriba un script que solicite al usuario que introduzca el número de años. Calcula el número de segundos que una persona puede vivir. Supongamos que una persona puede vivir cien años ✔️
dias_por_año = 365
horas_por_dia = 24
minutos_por_hora = 60
segundos_por_minutos = 60
segundos_por_año = dias_por_año * horas_por_dia * minutos_por_hora * segundos_por_minutos

años = int(input("Por favor ingrese el numero de años: "))

segundos_vividos = años * segundos_por_año

if años == 100:
    print("Una persona de cien años ha vivido", segundos_vividos * años, "segundos.")
elif años < 100:
    print(f"Usted ha vivido {segundos_vividos} segundos.")
else:
    print(f"Es muy poco probable que una persona viva mas de cien años :( ... Sin embargo habria vivido {segundos_vividos} segundos.")

# 23. Escriba un script de Python que muestre la siguiente tabla ✔️
#    1 1 1 1 1
#    2 1 2 4 8
#    3 1 3 9 27
#    4 1 4 16 64
#    5 1 5 25 125
for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")





