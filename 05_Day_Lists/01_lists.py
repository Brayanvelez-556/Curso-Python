# Día 5: 30 días de programación en python

# LISTS

# Dos formas para crear listas vacias
my_list = list()
my_other_list = []

print(type(my_list)) # type sirve para optener el tipo de dato, en este caso es tipo de dato 'list'
print(type(my_other_list))

print(len(my_list)) # len devuelve la longitud de la lista
print(len(my_other_list))

my_list = [35, 26, 62, 52, 30, 30, 17]
print(len(my_list))
print(my_list)
print(my_list[3]) # Devuelve el valor que se encuentra en el indice expecificado en este caso es el indice [3] = 52
print(sorted(my_list)) # Sorted devuelve la lista sin modificar la lista original

# Las listas pueden guardar diferentes tipos de datos
my_other_list = [26, 1.65, "Brayan", "Velez"] 

# Acceder a los indices de la lista
print(f'Primer item de la lista --> {my_other_list[0]}')
print(f'Segundo item de la lista --> {my_other_list[1]}')
print(f'Tercer item de la lista --> {my_other_list[2]}')
print(f'Cuarto item de la lista --> {my_other_list[3]} \n')
# print(f'Cuarto item de la lista --> {my_other_list[4]}') IndexError, Indice de lista fuera de rango

# Funciona tambien con valores negativos empezando a contar de adelante hacia atras
print(f'Primer item de la lista --> {my_other_list[-4]}')
print(f'Segundo item de la lista --> {my_other_list[-3]}')
print(f'Tercer item de la lista --> {my_other_list[-2]}')
print(f'Cuarto item de la lista --> {my_other_list[-1]} ')

# Count es un metodo que funciona para contar el numero de ocurrencias de un elemento dentro de una lista
print(my_list.count(30))

# Desestructurar o desempaquetar una lista en multiples variables
edad, estatura, nombre, apellido = my_other_list

print(f'Edad: {edad}')
print(f'Estatura: {estatura}')
print(f'Nombre: {nombre}')
print(f'Apellido: {apellido}\n')

# Otra manera de desestructurar las listas es indicando el indice
my_second_list = ['Erika', 'Urrea', 1.55, 24]

print(f'Mi segunda lista: {my_second_list}')

height, age, name, lastname = my_second_list[2], my_second_list[3], my_second_list[0], my_second_list[1]

print(f'Estatura: {height}')
print(f'Edad: {age}')
print(f'Nombre: {name}')
print(f'Apellido: {lastname}\n')

# Sumar "Unir" listas
my_united_lists = my_second_list + my_other_list
print(my_united_lists)

# METODOS DE LISTAS

# Nueva lista
my_new_list = []

print(f'\nMi lista: {my_new_list}')

# extend agrega varios elemntos a una lista
my_new_list.extend([5, 7, 8, 26, 42, 35, 8, 9]) 

print(f'Mi lista: {my_new_list}')

# index muestra en que indice se encuentra posicionado el valor a buscar en este caso estamos buscando el numero "7"
print(my_new_list.index(7)) 

# count cuenta cuantas veces esta el item que ingesamos en este caso "8" esta dos veces dentro de la lista
print(my_new_list.count(8)) 

# Append sirve para agregar elementos a la lista uno a uno y se inserta al final
my_new_list.append('Brayan')
print(f'Mi lista: {my_new_list}')

# Insert sirve para insertar elementos en la lista indicando en que indice "Posición" deseamos insertarlo
my_new_list.insert(2, 'Velez')
print(f'Mi lista: {my_new_list}')

# Copy sirve para copiar la lista
my_second_new_list = my_new_list.copy()
print(f'Mi segunda nueva lista: {my_second_new_list}\n')

# Modificar el item de la lista pasandole el indice y asignandole un nuevo valor
my_new_list[0] = 6
print(f'Mi lista: {my_new_list}')

# Remove sirve para eliminar un valor de la lista indicandole el item que deseamos eliminar en este caso es "8" y se elimina el primero que enceuntre en la lista
my_new_list.remove(8)
print(f'Mi lista: {my_new_list}')

# Pop elimina el ultimo item dentro de la lista por default es el ultimo elemento
print(my_new_list.pop()) # Si se imprime el pop muestra cual fue el elemento que se elimino
print(f'Mi lista: {my_new_list}')

# Si se le pasa un indice el pop elimina el item dentro de el indice ingresado
my_new_list.pop(2)
print(f'Mi lista: {my_new_list}')

# Podemos guardar el elemento eliminado con el pop en una variable
my_pop_elemnt = my_new_list.pop(3) 
print(f'Mi elemento pop: {my_pop_elemnt}')

# Del sirve para eliminar elementos de la lista pasandole el indice, similar a remove pero del es por indice y remove elimina ingresandole el nombre del item el primer item encontrado
del my_new_list[0]
print(f'Mi lista: {my_new_list}')

# Reverse sirve para ordenar los valores al reves
my_new_list.reverse()
print(f'Mi lista al reves: {my_new_list}')

# Sort  sirve para ordenar la lista de menor a mayor
my_new_list.sort()
print(f'Mi lista de menor a mayor: {my_new_list}')

# Para divir la lista en sublistas lo realizamos de la siguiente manera
my_sub_list = my_new_list[1:3]
print(f'Sub lista de mi lista: {my_sub_list}')

# Clear sirve para elimnar todos los elementos de la lista
my_new_list.clear()
print(f'Mi lista: {my_new_list}')








