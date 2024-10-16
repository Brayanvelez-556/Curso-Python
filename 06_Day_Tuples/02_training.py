# Día 6: 30 días de programación en python

# EJERCICIOS - ENTRENAMIENTO !! 💪🏻

#💻 Ejercicios - Día 6

'''
Ejercicios: Nivel 1

1. Crear una tupla vacía ✔️
2. Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien) ✔️
3. Unir tuplas de hermanos y hermanas y asignarlas a hermanos ✔️
4. ¿Cuántos hermanos tienes? ✔️
5. Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a family_members ✔️

'''

# SOLUCION NIVEL 1 😁✌️

# 1. Crear una tupla vacía 
my_tuple = ()

# 2. Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
my_brothers = ('Santiago', 'Cristian', 'Yerson', 'Nicolas')
my_sisters = ('Erika', 'Ginneth', 'Laura', 'Valentina')

print(f'Mis hermanos: {my_brothers}')
print(f'Mis hermanas: {my_sisters}\n')

# 3. Unir tuplas de hermanos y hermanas y asignarlas a hermanos
brothers = my_brothers + my_sisters
print(f'Mis hermanos: {brothers}\n')

# 4. ¿Cuántos hermanos tienes?
print(f'Yo tengo {len(brothers)} hermanos\n')

# 5. Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a family_members
parents = ('Fernando', 'Yamile')
family_members = parents + brothers
print(f'Miembros de mi familia {family_members}\n')


'''
Ejercicios: Nivel 2

1. Desempaca a los hermanos y padres de family_members ✔️
2. Crea tuplas de frutas, verduras y productos de origen animal. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp. ✔️
3. Cambiar la tupla acerca de food_stuff_tp a una lista food_stuff_lt ✔️
4. Divida el elemento o elementos del medio de la food_stuff_tp tupla o lista de food_stuff_lt. ✔️
5. Corta los tres primeros elementos y los tres últimos de food_staff_lt lista ✔️
6. Elimine la tupla food_staff_tp por completo ✔️
7. Compruebe si un elemento existe en tupla: ✔️

    7.1 Comprueba si 'Estonia' es un país nórdico ✔️
    7.2 Comprueba si 'Islandia' es un país nórdico ✔️
    
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

'''

# SOLUCION NIVEL 2 😁✌️

# 1. Desempaca a los hermanos y padres de family_members
my_father, my_mother, *my_siblings = family_members
print(f'Mi padre: {my_father}\nMi madre: {my_mother}\nMis hermanos: {my_siblings}\n')

# 2. Crea tuplas de frutas, verduras y productos de origen animal. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
fruits = ('Naranja', 'Manzana', 'Durazno', 'Pera')
vegetables = ('Brocoli', 'Espinaca', 'Zanahoria', 'Tomate')
products_animal_origin = ('Leche', 'Huevo', 'Carne', 'Pollo')
food_stuff_tp = fruits + vegetables + products_animal_origin

print(f'Alimentos tupla: {food_stuff_tp}')

# 3. Cambiar la tupla acerca de food_stuff_tp a una lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print(f'Alimentos lista: {food_stuff_lt}')

# 4. Divida el elemento o elementos del medio de la food_stuff_tp tupla o lista de food_stuff_lt.
middle_food_stuff_lt = len(food_stuff_lt) // 2
print(f'Indice del alimento del medio: {middle_food_stuff_lt}')
print(f'Alimento del medio lista: {food_stuff_lt[middle_food_stuff_lt]}')

# 5. Corta los tres primeros elementos y los tres últimos de food_staff_lt lista
first_foods = food_stuff_lt[:3]
lasted_foods = food_stuff_lt[-3:]

print(f'Primeros alimentos: {first_foods}')
print(f'Ultimos alimentos: {lasted_foods}')

# 6. Elimine la tupla food_staff_tp por completo
del food_stuff_tp
# print(f'Alimentos tupla: {food_stuff_tp}') NameError: name 'food_stuff_tp' is not defined. Did you mean: 'food_stuff_lt'?

# 7. Compruebe si un elemento existe en tupla:
#   7.1. Comprueba si 'Estonia' es un país nórdico
#   7.1. Comprueba si 'Islandia' es un país nórdico    
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print(f'Estonia es un pais nordico: {'Estonia' in nordic_countries}')
print(f'Estonia es un pais Islandia: {'Iceland' in nordic_countries}')


