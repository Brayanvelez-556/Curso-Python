# Día 4: 30 días de programación en python

# STRINGS

my_string = "Mi strings"
my_other_string = "Mi otro strings"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tap_string = "\tEste es un string con tabulacion"
print(my_tap_string)

my_escape_string = "\tEste es un string\nescapado"
print(my_escape_string)

# Formateo

first_name = "Brayan"
last_name = "Velez"
age = 26

# Formato de cadena de estilo antiguo (operador %)
formated_string = 'Hola, mi nombre es %s %s y tengo %d años' %(first_name, last_name, age)
print(formated_string)

# Nuevo formato de cadena de estilo (str.format)
formated_new_string = 'Hola, mi nombre es {} {} y tengo {} años'.format(first_name, last_name, age)
print(formated_new_string)

# Interpolación de cadenas / f-Strings (Python 3.6+)
print(f'Hola, mi nombre es {first_name} {last_name} y tengo {age} años')

# Desempaquetado de caracteres
lenguage = "Python"
a,b,c,d,e,f = lenguage
print(a) #P
print(b) #y
print(c) #t
print(d) #h
print(e) #o
print(f) #n

# Division

lenguage_slice = lenguage[1:3]
print(lenguage_slice)

lenguage_slice = lenguage[0:6:2] # Cadena[inicio:fin:paso]
print(lenguage_slice) 

lenguage_slice = lenguage[1:]
print(lenguage_slice)

lenguage_slice = lenguage[-3]
print(lenguage_slice)


# Reverse

reversed_lenguage = lenguage[::-1]
print(reversed_lenguage)

# Funciones

print(lenguage.capitalize()) # Primera letra en mayuscula
print(lenguage.upper()) # Convierte la cadena en MAYUSCULA
print(lenguage.count("o")) # Cuenta cuantas veces esta el caracter en la cadena
print(lenguage.isnumeric()) # Verifica si el contenido de la cadena es un numero
print(lenguage.lower()) # Convierte la cadena en minuscula
print(lenguage.upper().isupper()) # Convierte la cadena en MAYUSCULA y despues verifica con isupper si es Mayuscula
print(lenguage.startswith("Py")) # Verifica si la cadena empieza con los carecteres introducidos, tiene en cuenta mayusculas!