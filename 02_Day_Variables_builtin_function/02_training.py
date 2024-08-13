# Día 2: 30 días de programación en python

# EJERCICIOS - ENTRENAMIENTO !! 💪🏻

#💻 Ejercicios - Día 2

"""
Ejercicios: Nivel 1

1. Dentro de 30DaysOfPython, cree una carpeta llamada day_2. Dentro de esta carpeta, cree un archivo llamado variables.py ✔️
2. Escribe un comentario en python que diga 'Día 2: 30 días de programación en python' ✔️
3. Declarar una variable de nombre de pila y asignarle un valor ✔️ 
4. Declarar una variable last name y asignarle un valor ✔️
5. Declarar una variable de nombre completo y asignarle un valor ✔️
6. Declarar una variable de país y asignarle un valor ✔️
7. Declarar una variable de ciudad y asignarle un valor ✔️
8. Declarar una variable de edad y asignarle un valor ✔️
9. Declarar una variable de año y asignarle un valor ✔️
10. Declarar una variable is_married y asignarle un valor ✔️
11. Declarar una variable is_true y asignarle un valor ✔️
12. Declarar una variable is_light_on y asignarle un valor ✔️
13. Declarar varias variables en una línea ✔️
"""

# SOLUCION NIVEL 1 😁✌️

# 3. Declarar una variable de nombre de pila y asignarle un valor ✔️ 
firs_name = "Brayan"

# 4. Declarar una variable last name y asignarle un valor ✔️
last_name = "Velez"

# 5. Declarar una variable de nombre completo y asignarle un valor ✔️
full_name = "Brayan Fernando Velez Velasco"

# 6. Declarar una variable de país y asignarle un valor ✔️
country = "Colombia"

# 7. Declarar una variable de ciudad y asignarle un valor ✔️
city = "Bogota"

# 8. Declarar una variable de edad y asignarle un valor ✔️
age = 26

# 9. Declarar una variable de año y asignarle un valor ✔️
year = 2024

# 10. Declarar una variable is_married y asignarle un valor ✔️
is_married = "No"

# 11. Declarar una variable is_true y asignarle un valor ✔️
is_true = True

# 12. Declarar una variable is_light_on y asignarle un valor ✔️
is_ligth_on = True

# 13. Declarar varias variables en una línea ✔️
nombre, apellido, nombre_completo, edad, pais, ciudad, año = "Erika", "Urrea", "Erika Ginneth Urrea Lopez", 24, "Colombia", "Bogota", 2024

"""
Ejercicios: Nivel 2

1. Verifique el tipo de datos de todas sus variables usando la función incorporada type() ✔️
2. Usando la función incorporada len(), encuentra la longitud de tu nombre ✔️
3. Compara la longitud de tu nombre y tu apellido ✔️
4. Declare 5 como num_one y 4 como num_two ✔️
    4.1. Agregue num_one y num_two y asigne el valor a un total variable ✔️
    4.2. Reste num_two de num_one y asigne el valor a una variable diff ✔️
    4.3. Multiplique num_two y num_one y asigne el valor a un producto variable ✔️
    4.5. Divida num_one por num_two y asigne el valor a una división variable ✔️
    4.6. Utilice la división de módulos para encontrar num_two dividido por num_one y asigne el valor a un resto variable ✔️
    4.7. Calcule num_one a la potencia de num_two y asigne el valor a una variable exp ✔️
    4.8. Encuentre la división de num_one por num_two y asigne el valor a una variable floor_division ✔️
5. El radio de un círculo es de 30 metros. ✔️ 
    5.1. Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle ✔️
    5.2. Calcule la circunferencia de un círculo y asigne el valor a un nombre de variable de circum_of_circle ✔️
    5.3. Tome el radio como entrada del usuario y calcule el área. ✔️
6. Utilice la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario y almacenar el valor en sus nombres de variable correspondientes ✔️
7. Ejecute help('keywords') en el shell de Python o en su archivo para verificar las palabras reservadas o palabras clave de Python ✔️
"""

# SOLUCION NIVEL 2 😁✌️

# 1. Verifique el tipo de datos de todas sus variables usando la función incorporada type() ✔️
print(type(firs_name))
print(type(last_name))
print(type(full_name))
print(type(age))
print(type(country))
print(type(city))
print(type(year))
print(type(is_true))
print(type(is_ligth_on))
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(edad))
print(type(pais))
print(type(ciudad))
print(type(año))

firs_name = "Brayan"
last_name = "Velez"

# 2. Usando la función incorporada len(), encuentra la longitud de tu nombre ✔️
print(len(firs_name))
print(len(last_name))

# 3. Compara la longitud de tu nombre y tu apellido ✔️
longitud_1 = len(firs_name)
longitud_2 = len(last_name)

if longitud_1 > longitud_2:
    print(f"La longitud de caracteres de tu nombre: {firs_name} es mayor a la de tu apellido: {last_name}")
elif longitud_1 < longitud_2:
    print(f"La longitud de caracteres de tu nombre: {firs_name} es menor a la de tu apellido: {last_name}")
else:
    print(f"La longitud de caracteres de tu nombre: {firs_name} es igual a la de tu apellido: {last_name}")

# 4. Declare 5 como num_one y 4 como num_two ✔️
num_one = 5
num_two = 4

print(f"Num one: {num_one}")
print(f"Nuem two: {num_two}")

# 4.1. Agregue num_one y num_two y asigne el valor a un total variable ✔️
total = num_one + num_two
print(f"Total: {total}")

# 4.2. Reste num_two de num_one y asigne el valor a una variable diff ✔️
diff = num_one - num_two
print(f"Diff: {diff}")

# 4.3. Multiplique num_two y num_one y asigne el valor a un producto variable ✔️
producto = num_one * num_two
print(f"Producto: {producto}")

# 4.5. Divida num_one por num_two y asigne el valor a una división variable ✔️
division = num_one / num_two
print(f"Division: {division}")

# 4.6. Utilice la división de módulos para encontrar num_two dividido por num_one y asigne el valor a un resto variable ✔️
resto = num_two % num_one
print(f"Resto: {resto}")

# 4.7. Calcule num_one a la potencia de num_two y asigne el valor a una variable exp ✔️
exp = num_one ** num_two
print(f"Exp: {exp}")

# 4.8. Encuentre la división de num_one por num_two y asigne el valor a una variable floor_division ✔️
floor_division = num_one // num_two
print(f"Florr_division: {floor_division}")

# 5. El radio de un círculo es de 30 metros. ✔️
radio_circulo = 30
print(f"Radio circulo: {radio_circulo}")

# 5.1. Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle ✔️
PI = 3.14
area_of_circle = PI * (radio_circulo ** 2)
print(F"Area circulo: {area_of_circle}")

# 5.2. Calcule la circunferencia de un círculo y asigne el valor a un nombre de variable de circum_of_circle ✔️
circum_of_circle = 2 * PI * radio_circulo
print(f"Circunferencia de circulo: {circum_of_circle}")

# 5.3. Tome el radio como entrada del usuario y calcule el área. ✔️
radio_circulo = input("Ingrese el radio del circulo: ")
radio_circulo = int(radio_circulo)
area_of_circle = PI * (radio_circulo ** 2)
print(f"El area del circulo es: {area_of_circle}")

# 6. Utilice la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario y almacenar el valor en sus nombres de variable correspondientes ✔️
nombre = input("Ingese su nombre: ")
apellido = input("Ingese su apellido: ")
pais = input("Ingese el nombre de su pais: ")
edad = input("Ingrese su edad: ")

print(f"Nombre: {nombre}, Apellido: {apellido}, Pais: {pais}, Edad: {edad}")



# 7. Ejecute help('keywords') en el shell de Python o en su archivo para verificar las palabras reservadas o palabras clave de Python ✔️

""" 
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
"""
