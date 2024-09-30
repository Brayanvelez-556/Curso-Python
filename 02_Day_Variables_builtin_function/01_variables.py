# Día 2: 30 días de programación en python

# Variables
my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

# Convertir una variable de tipo INT a tipo STR
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable) 

# Concatenacion de variables en un print
print(my_string_variable, ',', my_int_variable, ',', type(my_int_to_str_variable), ',', my_bool_variable)

# Algunas Funciones del sistema
print(len(my_string_variable)) # Len imprime la cantidad de caracteres que hay en el STR

# Variables en una sola linea
name, surname, alias, edad = "Brayan", "Velez", "Nando", 26
print(" Mi nombre es:", name, "\n", "Mi apellido es:", surname, "\n", "Mi alias es:", alias, "\n", "Mi edad es:", edad)

# Inputs
print("Holaaa, por favor ingresa tus datos:")
first_name = input("Cual es tu nombre: ")
age = int(input("Cual es tu edad: "))
print(f"Hola {first_name} bienvenido, tu edad es: {age} años.")

