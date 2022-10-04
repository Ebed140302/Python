"""num1 = int(input("Escribe un numero"))
num2 = int(input("Escribe un numero"))

resultado = num1 + num2

print("El resultado es: ", resultado)"""

"""diacalf = int(input("Califica tu dia del 1 al 10: "))
print ("Tu dia estuvo: " , diacalf, "de 10")"""

"""titulo = input("Proporciona el nombre del libro: ")
autor = input("Proporciona el autor del libro: ")

print(titulo, "fue escrito por ", autor)"""

"""miVariable = 10
print(miVariable)

#para modificar una variable se tiene que hacer esto:
miVariable = miVariable + 1

print(miVariable)

#Incremento con reasignaci[on]
miVariable += 1
print(miVariable)
#miVariable = mivariable - 2
miVariable -= 2
print(miVariable)
#mivariable = mivariable * 3
miVariable *= 3
print(miVariable)
#miVariable  = mivariable / 2
miVariable /= 2
print(miVariable)"""

#Operadores de comparacion#
'''
a = 4
b = 2
resultado = (a == b) #parentesis opcionales
print(f'Resultado == : {resultado}')

resultado = a != b

print(f'Resultado != : {resultado}')

resultado = a > b
print(f'Resultado > : {resultado}')

resultado = a >= b
print(f'Resultado >= : {resultado}')


resultado = a < b
print(f'Resultado < : {resultado}')

resultado = a <= b
print(f'Resultado <= : {resultado}') '''


'''#Numero impar o par#
numero = int(input("Ingrese un numero:"))

if numero % 2 == 0:
    print("Es un numero par")
else:
    print("No es numero par")
    
    
##determinnar si eres mayor de edad
edad = int(input("Ingresa tu edad"))
if edad >= 18:
    print ("Eres mayor de edad")
else:
    print("No eres mayor de edad")
'''
"""
a = True
b = True

resultado = a and b
#print(resultado)

resultado = a or b
#print(resultado)

resultado = not a
print(resultado)
"""

### Ejercicio con operador and
'''
valor = int(input("Escribe el valor: "))
valormin = 0
valormax = 5

dentroRango = (valor >= valormin) and (valor <= valormax)

if dentroRango:
    print(f'El valor {valor} esta dentro de rango')
else:
    print(f'El valor {valor} esta dentro del rango')
'''

###Ejercico con operador or###
'''
vacaciones = True
diaDescanso = False

if vacaciones or diaDescanso:
    print('Puede asistir')
else:
    print('Tienes deberes por hacer')'''

###Ejercicio con operador not (Invierte el resultado)
'''
vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso):
    print('Tienes deberes por hacer')
else:
    print('Puede asistir')
    '''
    
    ####Ejercico para edad con if anidados
    '''
edad = int(input("Proporciona tu edad: "))

veintes = edad >= 20 and edad < 30

treintas = edad >= 30 and edad < 40

#edadRango = veintes or treintas
if veintes or treintas:
    
    if veintes:
        print("Dentro de los 20's")
    elif treintas:
        print("Dentro de los 30's")
    else:
        print("Fuera del rango")
else:
    print("No se encuentra dentro de los 20's y 30's")
    '''
