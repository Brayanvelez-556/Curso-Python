'''
salud_bienvenida = "Hola bienvenido a mi codigo, mi nombre es Brayan Velez"

print(list(salud_bienvenida))
print(type(salud_bienvenida))



edad = int(input("Ingrese su edad: "))

print(f"Su edad es: {edad}")

print(type(edad))





nombre = input("Por favor ingrese su nombre: ")
'''


def convertir(nombre):
    nombre_list = list(nombre)
    return print(f'Nombre {nombre_list}')

convertir("Brayan Fernando Velez")


def revertir(cadena):
    return cadena[::-1]


print(revertir("Brayan Fernando Velez Velasco"))    



def numero_par():
    numero = int(input("Ingrese por favor un numero: "))
    if numero % 2 == 0:
        print(f'El numero es par: {numero}')
    else:
        print(f'El numero no es par: {numero}')


numero_par()