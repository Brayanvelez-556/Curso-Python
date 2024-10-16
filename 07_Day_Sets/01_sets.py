# Día 7: 30 días de programación en python

# SETS

# Definir un set syntax
my_set = set()
print(type(my_set)) #<class 'set'>


# Definir un set {}
my_other_set = {'Brayan', 'Velez', 26}
print(my_other_set) # {'Brayan', 26, 'Velez'}
print(type(my_other_set)) # <class 'set'>

# Validar la longitud del set
print(len(my_other_set)) # 3

# No se puede acceder a los elementos por medio de indices [0] dado a que es una estructura que no tiene orden
# print(my_other_set[0])  TypeError: 'set' object is not subscriptable

# Agregar nuevos elementos (.add) "No se aceptan elementos duplicados en los conjuntos!"
my_other_set.add('Samuel')
print(my_other_set) # {'Samuel', 'Brayan', 26, 'Velez'}

# Verificar si un elemento esta dentro del set (in)
print('Samuel' in my_other_set) # True

# Remover elementos de un set (remove)
my_other_set.remove('Velez')
print(my_other_set) # {'Brayan', 26, 'Samuel'}
print(my_other_set) # {'Brayan', 26, 'Samuel'}

# Vaciar los elementos del set (clear)
my_other_set.clear()
print(my_other_set) # set()

# Eliminar en su totalidad el set (set)
del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined()

# Convertir un set en una lista (list())
my_set = {'Erika', 'Ginneth', 'Urrea', 'Lopez', 24}
my_list = list(my_set)
print(type(my_list)) # <class 'list'>

# Unir sets (union)
my_other_set = {'Kotlin', 'Swift', 'Python'}
my_new_set = my_set.union(my_other_set)
print(my_new_set) # {'Python', 'Lopez', 'Erika', 'Ginneth', 'Swift', 'Kotlin', 24, 'Urrea'}

# Forma de mostrar la union de elementos creados dentro del metodo (union) // No modifica el set original
print(my_new_set.union({'JavaScript', 'C#'})) # {'JavaScript', 'Urrea', 'Swift', 'Python', 'Lopez', 'Kotlin', 'Ginneth', 'Erika', 24, 'C#'}

# Diferencia en los sets (difference)
print(my_new_set.difference(my_set)) # {'Swift', 'Kotlin', 'Python'}
