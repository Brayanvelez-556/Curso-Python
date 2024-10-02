# Día 6: 30 días de programación en python

# TUPLES

# Definir una tupla
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (26, 1.65, 'Brayan', 'Brayan', 'Velez')
print(f'Mi tupla: {my_tuple}')

my_other_tuple = (35, 26, 24, 5, 16, 14)

print(type(my_tuple))

# Se puede acceder a los valores de las tuplas igual que en las listas por sus indices
print(my_tuple[0])
print(my_tuple[-1]) 

# Metodos de las tuplas // Las tuplas tienen pocos metodos dado a que es inmutable
print(my_tuple.count('Brayan'))

print(my_tuple.index('Brayan'))

# my_tuple[0] = 35 TypeError: 'tuple' object does not support item assignment)

print(my_tuple + my_other_tuple)

my_sum_tuples = my_tuple + my_other_tuple # Las tuplas se pueden sumar
print(f'Mis tuplas unidas: {my_sum_tuples}\n') 

# Se puede convertir una tupla en lista y viceversa
my_tuple = list(my_tuple)
print(f'Mi tupla convertida en lista: {my_tuple}\nTipo: {type(my_tuple)}') 

# Borrar Tupla
del my_tuple
print(f'Mi tupla: {type(my_tuple)}') 
