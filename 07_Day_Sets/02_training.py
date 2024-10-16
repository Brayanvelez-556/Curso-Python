# Día 7: 30 días de programación en python

# EJERCICIOS - ENTRENAMIENTO !! 💪🏻

#💻 Ejercicios - Día 7

'''

Ejercicios: Nivel 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

1. Encuentre la longitud del conjunto it_companies ✔️
2. Añade 'Twitter' a it_companies ✔️
3. Inserte varias empresas de TI a la vez en el conjunto it_companies ✔️
4. Eliminar una de las empresas del conjunto it_companies ✔️
5. ¿Cuál es la diferencia entre quitar y desechar? ✔️

'''

# SOLUCION NIVEL 1 😁✌️

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Encuentre la longitud del conjunto it_companies
print(f'Longitud de conjunto it_companies: {len(it_companies)}')

# 2. Añade 'Twitter' a it_companies
it_companies.add('Twitter')
print(f'it_companies: {it_companies}')

# 3. Inserte varias empresas de TI a la vez en el conjunto it_companies
it_companies.update(['Uber', 'Tesla', 'Spotify'])
print(f'it_companies: {it_companies}')

# 4. Eliminar una de las empresas del conjunto it_companies
it_companies.remove('Spotify')
print(f'it_companies: {it_companies}\n')

# 5. ¿Cuál es la diferencia entre Remove y discard?
# La diferencia entre el metodo Remove() y discard() es que si el elemento que se ve a eliminar se realiza
# con Remove y no esta dentro del conjunto se genera un error # KeyError: 'Claro' y si se genera con discard no genera error.
it_companies.discard('Claro')
# it_companies.remove('Claro') # KeyError: 'Claro'

'''

Ejercicios: Nivel 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

1. Unir A y B ✔️
2. Buscar la intersección A B ✔️
3. Es un subconjunto de B ✔️
4. Son conjuntos disjuntos A y B ✔️
5. Unir A con B y B con A ✔️
6. ¿Cuál es la diferencia simétrica entre A y B? ✔️
7. Eliminar los conjuntos por completo ✔️

'''

# SOLUCION NIVEL 2 😁✌️

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Unir A y B
print(f'Union: {A.union(B)}')

# 2. Buscar la intersección A B
print(f'Interseccion: {A.intersection(B)}')

# 3. Es un subconjunto de B
print(f'A es subconjunto de B: {A.issubset(B)}')

# 4. Son conjuntos disjuntos A y B
print(f'Son conjuntos disjuntos: {A.isdisjoint(B)}')

# 5. Unir A con B y B con A
print(f'Union A con B: {A.union(B)}')
print(f'Union B con A: {B.union(A)}')

# 6. ¿Cuál es la diferencia simétrica entre A y B?
print(f'Diferencia simetrica: {A.symmetric_difference(B)}\n')

# 7. Eliminar los conjuntos por completo
del A, B

'''

Ejercicios: Nivel 3

age = [22, 19, 24, 25, 26, 24, 25, 24]

1. Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande? ✔️
2. Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto ✔️
3. Soy profesora y me encanta inspirar y enseñar a la gente. ✔️
¿Cuántas palabras únicas se han utilizado en la oración? Utilice los métodos de división y conjunto para obtener las palabras únicas.

'''

# SOLUCION NIVEL 3 😁✌️

# 1. Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print(type(age_set))

print(f'Longitud lista age: {len(age)}\nLongitud set age_set: {len(age_set)}')

if len(age) > len(age_set):
    print(f'La lista Age es mas grande: {age}') # La lista Age es mas grande: [22, 19, 24, 25, 26, 24, 25, 24]
elif len.age < len.age_set:
    print(f'El conjunto Age_set es mas grande: {age_set}')
else:
    print(f'Ambas estrucuras son igual de grandes: age_set {age_set}, age {age}')

# 2. Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto
# La diferencia entre los tipos de dato: Cadena, lista, tupla y conjunto es la siguiente.
# La cadena es un tipo de dato en el cual se ingresan los elementos como texto y se puede manipular por medio de indice y es ordenado
# La lista es una estructura ordenada a la cual se puede acceder por medio de un indice y acepta valores dublicados y homogeneos
# La tupla no permite modificaciones dado a que es inmutable pero es ordenada y se puede acceder a los elementos por medio de indice
# El conjunto es un elemento el cual no permite valores duplicados y es desordenado por ende no se puede acceder por medio de indice

# 3. Soy profesora y me encanta inspirar y enseñar a la gente. 
# ¿Cuántas palabras únicas se han utilizado en la oración? Utilice los métodos de división y conjunto para obtener las palabras únicas.

cadena = "Soy profesora y me encanta inspirar y enseñar a la gente"
new_cadena = cadena.split()
new_cadena_set = set(new_cadena)

print(f'Palabras unicas: {new_cadena_set}') # {'me', 'Soy', 'profesora', 'gente', 'y', 'a', 'la', 'enseñar', 'inspirar', 'encanta'}








