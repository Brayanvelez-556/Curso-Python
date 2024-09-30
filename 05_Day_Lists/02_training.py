# Día 5: 30 días de programación en python

# EJERCICIOS - ENTRENAMIENTO !! 💪🏻

#💻 Ejercicios - Día 5

'''

Ejercicios: Nivel 1

1. Declarar una lista vacía ✔️
2. Declarar una lista con más de 5 elementos ✔️
3. Encuentra la longitud de tu lista ✔️
4. Obtenga el primer elemento, el elemento del medio y el último elemento de la lista ✔️
5. Declara una lista llamada mixed_data_types, pon tu (nombre, edad, altura, estado civil, dirección) ✔️
6. Declare una variable de lista denominada it_companies y asigne valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon. ✔️
7. Imprime la lista usando print() ✔️ 
8. Imprime el número de empresas de la lista ✔️
9. Imprime la primera, la intermedia y la última empresa ✔️
10. Imprima la lista después de modificar una de las empresas ✔️
11. Agregar una empresa de TI a it_companies ✔️
12. Inserte una empresa de TI en el centro de la lista de empresas ✔️
13. Cambie uno de los nombres de la it_companies a mayúsculas (¡excluido IBM!) ✔️
14. Une el it_companies con una cadena '#; ' ✔️
15. Compruebe si existe una determinada empresa en la lista de it_companies. ✔️
16. Ordene la lista usando el método sort() ✔️
17. Invierta la lista en orden descendente usando el método reverse() ✔️
18. Corta las 3 primeras empresas de la lista ✔️
19. Corta las últimas 3 empresas de la lista ✔️
20. Elimine la empresa o empresas de TI intermedias de la lista ✔️
21. Eliminar la primera empresa de TI de la lista ✔️
22. Eliminar la empresa o empresas de TI intermedias de la lista ✔️
23. Eliminar la última empresa de TI de la lista ✔️
24. Eliminar todas las empresas de TI de la lista ✔️
25. Destruir la lista de empresas de TI ✔️
26. Únete a las siguientes listas:✔️
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
27. Después de unirse a las listas de la pregunta 26. Copie la lista unida y asígnela a una variable full_stack. A continuación, inserte Python y SQL después de Redux. ✔️

'''

# SOLUCION NIVEL 1 😁✌️

# 1. Declarar una lista vacía
my_list = []

# 2. Declarar una lista con más de 5 elementos
my_fruits_list = ['Manzana', 'Naranja', 'Sandia', 'Mandarina', 'Fresa', 'Limon', 'Pera']

# 3. Encuentra la longitud de tu lista
print(f'Longitud de mi lista: {len(my_fruits_list)}\n')

# 4. Obtenga el primer elemento, el elemento del medio y el último elemento de la lista
print(f'Primer elemento: {my_fruits_list[0]}')
print(f'Elemento del medio: {my_fruits_list[3]}')
print(f'Ultimo elemento: {my_fruits_list[-1]}\n')

# 5. Declara una lista llamada mixed_data_types, pon tu (nombre, edad, altura, estado civil, dirección)
mixed_data_types = ['Brayan', 26, 1.65, 'Union Libre', 'Cra 17 P # 70 B26']

# 6. Declare una variable de lista denominada it_companies y asigne valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprime la lista usando print()
print(f'Compañias: {it_companies}')

# 8. Imprime el número de empresas de la lista
print(f'Longitud de la lista compañias: {len(it_companies)}\n')

# 9. Imprime la primera, la intermedia y la última empresa
print(f'Primera empresa: {it_companies[0]}')
print(f'Empresa del medio: {it_companies[3]}')
print(f'Ultima empresa: {it_companies[-1]}\n')

# 10. Imprima la lista después de modificar una de las empresas
it_companies[0] = 'Meta'
print(f'Compañias: {it_companies}')

# 11. Agregar una empresa de TI a it_companies
it_companies.append('Azure')
print(f'Compañias: {it_companies}')

# 12. Inserte una empresa de TI en el centro de la lista de empresas
it_companies.insert(3, 'Intel') 
print(f'Compañias: {it_companies}')

# 13. Cambie uno de los nombres de la it_companies a mayúsculas (¡excluido IBM!)
it_companies[0] = it_companies[0].upper()
print(f'Compañias: {it_companies}')

# 14. Une el it_companies con una cadena '#; '
it_companies_str = '#; '.join(it_companies)
print(f'Compañias: {it_companies_str}\n')

# 15. Compruebe si existe una determinada empresa en la lista de it_companies.
does_exist = 'Apple' in it_companies
print(f'Existe la empresa Apple dentro de la cadena?: {does_exist}\n')

# 16. Ordene la lista usando el método sort()
it_companies.sort()
print(f'Compañias: {it_companies}\n')

# 17. Invierta la lista en orden descendente usando el método reverse()
it_companies.reverse()
print(f'Compañias: {it_companies}\n')

# 18. Corta las 3 primeras empresas de la lista
sub_list = it_companies[0:3]
print(f'Primeras 3 compañias: {sub_list}\n')

# 19. Corta las últimas 3 empresas de la lista
sub_list = it_companies[-3:]
print(f'Ultimas 3 compañias: {sub_list}\n')

# 20. Elimine la empresa o empresas de TI intermedias de la lista
del it_companies[3:-3]
print(f'Empresas intermedias eliminadas: {it_companies}\n')

# 21. Eliminar la primera empresa de TI de la lista
it_companies.pop(0)
print(f'Primera empresa eliminada: {it_companies}\n')

# 22. Eliminar la empresa o empresas de TI intermedias de la lista
del it_companies[2:-2]
print(f'Empresa intermedia eliminada: {it_companies}\n')

# 23. Eliminar la última empresa de TI de la lista
it_companies.pop()
print(f'Ultima empresa eliminada: {it_companies}\n')

# 24. Eliminar todas las empresas de TI de la lista
it_companies.clear()
print(f'Todas las empresas eliminadas: {it_companies}\n')

# 25. Destruir la lista de empresas de TI
del it_companies
#print(f'Se elimina la lista en su totalidad: {it_companies}\n') # NameError: it_companies no esta definida

# 26. Únete a las siguientes listas:
#   front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#   back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
print(f'Lista front_end: {front_end}')

back_end = ['Node','Express', 'MongoDB']
print(f'Lista back_end: {back_end}\n')

# 27. Después de unirse a las listas de la pregunta 26. Copie la lista unida y asígnela a una variable full_stack. A continuación, inserte Python y SQL después de Redux.
full_stack = front_end + back_end
print(f'Lista full_stack: {full_stack}\n')

full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

print(f'Lista full_stack: {full_stack}\n')

'''

Ejercicios: Nivel 2

1. La siguiente es una lista de 10 edades de estudiantes: ✔️
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
2. Ordene la lista y encuentre la edad mínima y máxima ✔️
3. Agregue la edad mínima y la edad máxima nuevamente a la lista ✔️
4. Encuentre la edad media (un elemento del medio o dos elementos del medio divididos por dos) ✔️
5. Encuentre la edad promedio (suma de todos los artículos dividida por su número) ✔️
6. Encuentre el rango de las edades (máx. menos mín.) ✔️
7. Compare el valor de (min - promedio) y (max - promedio), use el método abs() ✔️
8. Encuentre el (los) país (s) del medio en la lista de países ✔️
9. Divida la lista de países en dos listas iguales si es incluso si no hay un país más para la primera mitad. ✔️
10. ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']. Desempaqueta los tres primeros países y el resto como países escandinavos. ✔️

'''  

# SOLUCION NIVEL 2 😁✌️

# 1. La siguiente es una lista de 10 edades de estudiantes:
#   ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f'Lista edades: {ages}')

# 2. Ordene la lista y encuentre la edad mínima y máxima
ages.sort()
print(f'Lista edades ordenada: {ages}\n')

age_min = min(ages)
print(f'Edad minima: {age_min}')

age_max = max(ages)
print(f'Edad maxima: {age_max}\n')

# 4. Encuentre la edad media (un elemento del medio o dos elementos del medio divididos por dos)
longitud_list = len(ages)
print(f'Longitud lista: {longitud_list}\n')

if longitud_list % 2 != 0:
    middle_age = ages[longitud_list // 2]
else:
    medio1 = ages[longitud_list // 2 -1]
    medio2 = ages[longitud_list // 2]
    middle_age = (medio1 + medio2) // 2
    
print(f'Edad media: {middle_age}\n')

# 5. Encuentre la edad promedio (suma de todos los artículos dividida por su número)
total_ages = sum(ages)
print(f'Suma de todas las edades: {total_ages}')

average_age = total_ages / len(ages)
print(f'Promedio de todas las edades: {average_age}')

# 6. Encuentre el rango de las edades (máx. menos mín.)
rank_ages = age_max - age_min
print(f'Rango de las edades: {rank_ages}\n')

# 7. Compare el valor de (min - promedio) y (max - promedio), use el método abs()
valor_min_promedio = abs(age_min - average_age)
valor_max_promedio = abs(age_max - average_age)
print(f'Comparacion min - promedio, valor absoluto: {valor_min_promedio}\nComparacion max - promedio, valor absoluto: {valor_max_promedio}\n')

# 8. Encuentre el (los) país (s) del medio en la lista de países
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein', # 100
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
];

print(f'Total paises: {len(countries)}')
print(f'Pais del medio: {len(countries) // 2}')

if len(countries) % 2 == 0:
    middle_countrie1 = countries[len(countries) // 2]
    middle_countrie2 = countries[len(countries) // 2 - 1]
    print(f'Paises del medio: {middle_countrie1} y {middle_countrie2}')
else:
    middle_countrie = countries[len(countries) // 2] 
    print(f'Pais del medio: {middle_countrie}')

print(countries.index('Lesotho'))

# 9. Divida la lista de países en dos listas iguales si es incluso si no hay un país más para la primera mitad.
middle_index = len(countries) // 2
print(middle_index)

first_half = countries[:middle_index]
second_half = countries[middle_index:]

print(f'Primera mitad: {first_half}\n')
print(f'Segunda mitad: {second_half}\n')

print(len(first_half), len(second_half))

# 10. ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']. Desempaqueta los tres primeros países y el resto como países escandinavos.
others_countries = ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
first_countrie, second_countrie, three_countrie, *scandic_countries = others_countries

print(f'Primer pais: {first_countrie}')
print(f'Segundo pais: {second_countrie}')
print(f'Tercer pais: {three_countrie}')
print(f'Paises escandinavos: {scandic_countries}')
