# Día 4: 30 días de programación en python

# EJERCICIOS - ENTRENAMIENTO !! 💪🏻

#💻 Ejercicios - Día 4

'''

Ejercicios:

1. Concatene la cadena 'Thirty', 'Days', 'Of', 'Python' en una sola cadena, 'Thirty Days Of Python'. ✔️
2. Concatene la cadena 'Coding', 'For', 'All' en una sola cadena, 'Coding For All'. ✔️
3. Declare una variable denominada company y asígnela a un valor inicial "Coding For All". ✔️
4. Imprime la variable company usando print(). ✔️
5. Imprima la longitud de la cadena de la empresa utilizando el método len() y print(). ✔️
6. Cambie todos los caracteres a letras mayúsculas usando el método upper(). ✔️
7. Cambie todos los caracteres a letras minúsculas usando el método lower(). ✔️
8. Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All. ✔️
9. Corta la primera palabra de la cadena Coding For All. ✔️
10. Compruebe si la cadena Codificación para todos contiene una palabra Codificación mediante el método index, find u otros métodos. ✔️
11. Reemplace la palabra codificación en la cadena 'Coding For All' a Python. ✔️
12. Cambie Python para todos a Python para todos usando el método replace u otros métodos. ✔️
13. Divida la cadena 'Coding For All' usando el espacio como separador (split()) . ✔️
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" dividió la cadena en la coma. ✔️
15. ¿Cuál es el carácter en el índice 0 en la cadena Coding For All? ✔️
16. ¿Cuál es el último índice de la cadena Coding For All? ✔️
17. Qué carácter está en el índice 10 en la cadena "Coding For All". ✔️
18. Crea un acrónimo o una abreviatura para el nombre 'Python For Everyone'. ✔️
19. Cree un acrónimo o una abreviatura para el nombre 'Coding For All'. ✔️
20. Utilice el índice para determinar la posición de la primera aparición de C en Coding For All. ✔️
21. Utilice index para determinar la posición de la primera aparición de F en Coding For All. ✔️
22. Utilice rfind para determinar la posición de la última aparición de l en Codificación para todas las personas. ✔️
23. Use index o find para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque porque es una conjunción' ✔️
24. Utilice rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 'No puedes terminar una oración con porque porque porque porque es una conjunción' ✔️
25. Corta la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque porque es una conjunción" ✔️
26. Halla la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque porque es una conjunción' ✔️
27. Corta la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque porque es una conjunción" ✔️
28. ¿''Coding For All' comienza con una subcadena Coding? ✔️ 
29. ¿'Coding For All' termina con una codificación de subcadena? ✔️
30. ' Codificación para todos ', elimine los espacios finales izquierdo y derecho en la cadena dada. ✔️
31. ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier(): ✔️
    30DaysOfPython
    thirty_days_of_python
32. La siguiente lista contiene los nombres de algunas de las bibliotecas de python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con cadena de espacio. ✔️
33. Utilice la nueva secuencia de escape de línea para separar las siguientes oraciones. ✔️
    I am enjoying this challenge. 
    I just wonder what is next. 
34. Utilice una secuencia de escape de tabulación para escribir las siguientes líneas. ✔️
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
35. Utilice el método de formato de cadena para mostrar lo siguiente: ✔️
    radius = 10
    area = 3.14 * radius ** 2
    The area of a circle with radius 10 is 314 meters square.
36. Realice lo siguiente utilizando métodos de formato de cadena: ✔️
    8 + 6 = 14
    8 - 6 = 2
    8 * 6 = 48
    8 / 6 = 1.33
    8 % 6 = 2
    8 // 6 = 1
    8 ** 6 = 262144
'''

# SOLUCION 😁✌️

# 1. Concatene la cadena 'Thirty', 'Days', 'Of', 'Python' en una sola cadena, 'Thirty Days Of Python'. ✔️
string_a = "Thirty"
string_b = "Days"
string_c = "Of"
string_d = "Python"

string_concatenated = string_a + " " + string_b + " " + string_c + " " + string_d
print(string_concatenated)

# 2. Concatene la cadena 'Coding', 'For', 'All' en una sola cadena, 'Coding For All'. ✔️
string_e = "Coding"
string_f = "For"
string_g = "All"

string_concatenated = string_e + " " + string_f + " " + string_g
print(string_concatenated)

# 3. Declare una variable denominada company y asígnela a un valor inicial "Coding For All". ✔️
company = "Coding For All"

# 4. Imprime la variable company usando print(). ✔️
print(company)

# 5. Imprima la longitud de la cadena de la empresa utilizando el método len() y print(). ✔️
print(len(company))

# 6. Cambie todos los caracteres a letras mayúsculas usando el método upper(). ✔️
company_upper = company.upper()
print(company_upper)

# 7. Cambie todos los caracteres a letras minúsculas usando el método lower(). ✔️
company_lower = company.lower()
print(company_lower)

# 8. Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All. ✔️
company_capitalize = company.capitalize()
company_title = company.title()
company_swapcase = company.swapcase()

print(company_capitalize)
print(company_title)
print(company_swapcase)

# 9. Corta la primera palabra de la cadena Coding For All. ✔️
cadena_cortada = company[0:6]
print(cadena_cortada)

# 10. Compruebe si la cadena Codificación para todos contiene una palabra Codificación mediante el método index, find u otros métodos. ✔️
sub_string = "Coding"
print(company.index(sub_string))

# 11. Reemplace la palabra codificación en la cadena 'Coding For All' a Python. ✔️
company_modificado = company.replace("Coding", "Pyhon")
print(company_modificado)

# 12. Cambie Python for All  por Python for Everyone usando el método replace u otros métodos. ✔️
company_replace = company_modificado.replace("All", "Everyone")
print(company_replace)

# 13. Divida la cadena 'Coding For All' usando el espacio como separador (split()) . ✔️
print(company_modificado.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divida la cadena en la coma. ✔️
companys_technological = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companys_technological.split(','))

# 15. ¿Cuál es el carácter en el índice 0 en la cadena Coding For All? ✔️
print(company)
print(f"El caracter en el indice 0 es: \"{company[0]}\"")

# 16. ¿Cuál es el último índice de la cadena Coding For All? ✔️
print(f"El caracter en el ultimo indice es: \"{company[-1]}\"")

# 17. Qué carácter está en el índice 10 en la cadena "Coding For All". ✔️
print(f"El caracter en el indice 10 es: \"{company[10]}\"")

# 18. Crea un acrónimo o una abreviatura para el nombre 'Python For Everyone'. ✔️
palabras = company_replace.split() # Separamos las palabras de la cedena de texto
print(palabras)

iniciales = [palabra[0] for palabra in palabras] # Se obtiene la primera letra de cada palabra
resultado = ''.join(iniciales) # Se unen en una sola palabra las iniciales obtenidas anteriormente
print(resultado) # Se imprime el resltado

# 19. Cree un acrónimo o una abreviatura para el nombre 'Coding For All'. ✔️
palabras = company.split()
print(palabras)

iniciales = [palabra[0] for palabra in palabras] # Se obtiene la primera letra de cada palabra 
resultado = ''.join(iniciales) # Se unen en una sola palabra las iniciales obtenidas anteriormente
print(resultado) # Se imprime el resltado

# 20. Utilice el índice para determinar la posición de la primera aparición de C en Coding For All. ✔️
print(f"La primera aparicion de \"C\" en Coding For All es en el indice: {company.find("C")}")

# 21. Utilice index para determinar la posición de la primera aparición de F en Coding For All. ✔️
print(f"La primera aparicion de \"F\" en Coding For All es en el indice: {company.find("F")}")

# 22. Utilice rfind para determinar la posición de la última aparición de l en Coding For All. ✔️
print(f"La ultima aparicion de \"l\" en Coding For All es en el indice: {company.rfind("l")}")

# 23. Use index o find para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque porque es una conjunción' ✔️
oracion = 'No puedes terminar una oración con porque porque porque porque es una conjunción'

print(f"La primera aparicion de la palabra \"porque\" es en: {oracion.find("porque")}")

# 24. Utilice rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 'No puedes terminar una oración con porque porque porque porque es una conjunción' ✔️
print(f"La ultima aparicion de la palabra \"porque\" es en: {oracion.rfind("porque")}")

# 25. Corta la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque porque es una conjunción" ✔️
print(oracion.replace("porque porque porque porque", "porque"))

# 26. Halla la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque porque es una conjunción' ✔️
print(f"La pocicion de la primera aparicion de la palabra \"porque\" es en: {oracion.find("porque")}")

# 27. Corta la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque porque es una conjunción" ✔️
frase_oracion = "porque"
print(oracion.replace("porque porque porque porque", "porque"))

# 28. ¿'Coding For All' comienza con una subcadena Coding? ✔️
print(company.startswith("Coding"))

# 29. ¿'Coding For All' termina con una codificación de subcadena? ✔️
print(company.endswith("Coding"))

# 30. 'Coding for All', elimine los espacios finales izquierdo y derecho en la cadena dada. ✔️
print(company.replace(" ", ""))

# 31. ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier(): ✔️
#    30DaysOfPython
#    thirty_days_of_python
string_a = "30DaysOfPython" # False
string_b = "thirty_days_of_python" # True

print(string_a.isidentifier())
print(string_b.isidentifier())

# 32. La siguiente lista contiene los nombres de algunas de las bibliotecas de python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Úna la lista con un con cadena de espacio. ✔️
bibliotecas_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
bibliotecas_python_unidas = " ".join(bibliotecas_python)

print(bibliotecas_python_unidas)

# 33. Utilice la nueva secuencia de escape de línea para separar las siguientes oraciones. ✔️
#    I am enjoying this challenge.
#    I just wonder what is next.
print("I am enjoying\nhis challenge.")
print("I just wonder\nwhat is next.")

# 34. Utilice una secuencia de escape de tabulación para escribir las siguientes líneas. ✔️
#    Name      Age     Country   City
#    Asabeneh  250     Finland   Helsinki
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. Utilice el método de formato de cadena para mostrar lo siguiente: ✔️
#    radius = 10
#    area = 3.14 * radius ** 2
#    The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 36. Realice lo siguiente utilizando métodos de formato de cadena: ✔️
#    8 + 6 = 14
#    8 - 6 = 2
#    8 * 6 = 48
#    8 / 6 = 1.33
#    8 % 6 = 2
#    8 // 6 = 1
#    8 ** 6 = 262144
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")




