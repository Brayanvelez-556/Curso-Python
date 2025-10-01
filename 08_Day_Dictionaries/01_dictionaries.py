# Día 8: 30 días de programación en python

# DICTIONARIES

# Creacion de un diccionario
my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {
    'Nombre': 'Brayan',
    'Apellido': 'Velez',
    'Edad': 26,
    1: 'Python'
    }

my_dict = {
    'Nombre': 'Brayan',
    'Apellido': 'Velez',
    'Edad': 26,
    'Lenguajes': ['Python', 'Swift', 'Kotlin'],
    'Estatura': 1.65
    }

print(my_other_dict) # {'Nombre': 'Brayan', 'Apellido': 'Velez', 'Edad': 26, 1: 'Python'}
print(my_dict) # {'Nombre': 'Brayan', 'Apellido': 'Velez', 'Edad': 26, 'Lenguajes': {'Kotlin', 'Python', 'Swift'}}

# Se accede a los elementos por medio de la (Clave)
print(my_dict['Nombre']) # Brayan
print(my_dict['Lenguajes']) # {'Kotlin', 'Swift', 'Python'}
print(my_dict['Lenguajes'][0]) # Python

# Agregar nuevos pares
my_other_dict['Calle'] = 'Cra 17 P 70'
print(my_other_dict) # {'Nombre': 'Brayan', 'Apellido': 'Velez', 'Edad': 26, 1: 'Python', 'Calle': 'Cra 17 P 70'}

# Comprobar si una clave existe dentro del diccionario
print('Nombre' in my_other_dict) # True

# Comprobacion si un valor existe dentro del diccionario
print('Brayan' in my_other_dict.values())

# Comprobacion si un valor existe dentro de una clave del diccionario
print('Python' in my_dict['Lenguajes']) # True

# Retorna los items del diccionario
print(my_dict.items()) # dict_items([('Nombre', 'Brayan'), ('Apellido', 'Velez'), ('Edad', 26), ('Lenguajes', ['Python', 'Swift', 'Kotlin']), ('Estatura', 1.65)])

# Retorna las keys del diccionario
print(my_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 'Estatura'])

# Retorna los valores del diccionario
print(my_dict.values()) # dict_values(['Brayan', 'Velez', 26, ['Python', 'Swift', 'Kotlin'], 1.65])


# El método fromkeys() en Python se utiliza para crear un nuevo diccionario a partir de una secuencia de claves o un diccionario ya creado y un valor predeterminado.
claves = ['Nombre', 'Apellido', 'E-mail']
my_new_dict = dict.fromkeys(claves)

# Como no se especifica el valor de las claves se retorna en None para despues ingresar los valores
print(my_new_dict) # {'Nombre': None, 'Apellido': None, 'E-mail': None}


