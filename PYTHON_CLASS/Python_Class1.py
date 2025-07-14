# Este documento es un registro de aprendizaje de Python.
# Aquí se documentan las lecciones aprendidas y los conceptos clave.

                                                        # Clase 1: Introducción a Python
# En esta clase, aprendimos sobre los tipos de datos en Python
# y cómo se pueden utilizar en diferentes contextos.

# Comentarios: 
# Python permite comentarios de una sola línea con el símbolo #. igual como se hace en esta linea colocando el símbolo # al inicio de la línea.
# Comentarios de varias líneas: se pueden hacer con comillas triples """ o '''. 
#Ejemplo de comentarios:
"""
Este es un comentario de varias líneas.
Puedes escribir aquí lo que quieras sin que Python lo ejecute.
"""
'''Este es otro tipo de comentario de varias líneas.
También puedes usar comillas simples o triples para comentarios
de varias líneas.'''

#Empecemos con un Hola Mundo
print("¡Hola, Mundo!"," *print()* es una *función*. Se utiliza para mostrar mensajes en consola.") # Dentro del () se coloca lo que se quiere mostrar, a esto se le llama argumento.
print("¡Hola, Mundo!",40 ,4.5 ,True) # También se pueden mostrar varios tipos de argumentos separados por comas.

print(type("¡Hola, Mundo!")) # *type()* es una función que muestra el tipo de dato del argumento que recibe. En este caso, muestra que es un string (cadena de texto).
print(type(40)) # Muestra que 40 es un entero (int)(integer).
print(type(4.5)) # Muestra que 4.5 es un número de punto flotante (float).
print(type(True)) # Muestra que True es un booleano (bool).
print(type(False)) # Muestra que False también es un booleano (bool).
print(type(None)) # None es un tipo especial que representa la ausencia de valor, y su tipo es NoneType.
print(type("Hola, Mundo!"), type(40), type(4.5), type(True), type(False), type(None)) # Muestra los tipos de datos de varios valores.
# Tipos de datos en Python
# Python tiene varios tipos de datos, entre ellos:
# - Cadenas de texto (str): Se utilizan para representar texto.
# - Enteros (int): Números enteros sin decimales.
# - Números de punto flotante (float): Números que tienen una parte decimal.
# - Booleanos (bool): Representan valores de verdad, como True o False.
# - NoneType: Representa la ausencia de valor.
 
 # Los Operadores en Python
# Los operadores son símbolos que realizan operaciones sobre variables y valores.
# Existen varios tipos de operadores en Python, entre ellos:
# - Aritméticos: +, -, *, /, // (división entera), % (módulo), ** (exponente).
# - Comparación: ==, !=, <, >, <=, >=. 
# - Lógicos: and, or, not.
# - Asignación: =, +=, -=, *=, /=, //=, %=, **=.
# - Identidad: is, is not.
# - Pertenencia: in, not in.
# - Bit a bit: &, |, ^, ~, <<, >>.
# - Identidad: is, is not.

# Ejemplo de operadores aritméticos
print("Operadores aritméticos:")  # Aquí se muestran ejemplos de operaciones aritméticas básicas.
# Los operadores aritméticos se utilizan para realizar cálculos matemáticos básicos.
print("Suma:", 5 + 3)  # Suma
print("Resta:", 10 - 2)  # Resta
print("Multiplicación:", 4 * 2)  # Multiplicación
print("División:", 8 / 2)  # División
print("División entera:", 8 // 3)  # División entera
print("Módulo:", 5 % 2)  # Módulo
print("Exponente:", 2 ** 3)  # Exponente o Potencia

#Ejemplo 2 de operadores aritméticos con variables
print("Operaciones con variables:")  # Las *variables* son contenedores que almacenan valores y pueden ser utilizadas en operaciones.
# Definimos dos variables a y b. aunque puedes definirlas con cualquier nombre, es una buena práctica usar nombres descriptivos.

a = 10 # asignamos el valor 10 (entero o integer) a la variable a
b = 5 # asignamos el valor 5 (entero o integer) a la variable b
print("Suma:", a + b)  # Suma
print("Resta:", a - b)  # Resta
print("Multiplicación:", a * b)  # Multiplicación
print("División:", a / b)  # División
print("División entera:", a // b)  # División entera
print("Módulo:", a % b)  # Módulo
print("Exponente:", a ** b)  # Exponente o Potencia

print( 10 + 5 * 2 - 3 / 1) # Operaciones combinadas, Se puede usar mas de un operador en conjunto en una misma expresión, pero se respetara la regla matematica de jerarquia de operaciones.
print( (10 + 5) * ((2 - 3) / 1)) # se puede hacer uso de paréntesis para cambiar el orden de las operaciones 

# Ejemplo de operadores lógicos
print("Operadores lógicos:") # Los operadores lógicos se utilizan para combinar expresiones booleanas, osea que tienen de resultado True o False.
print("AND:", True and False)  # AND lógico, Conjunción
print("OR:", True or False)  # OR lógico, Disyunción
print("NOT:", not True)  # NOT lógico, Negación

# Ejemplo de operadores de comparación o relacionales
print("Operadores de comparación:")  # Los operadores de comparación se utilizan para comparar valores y devuelven un valor booleano (True o False).
print("Igual a:", 5 == 5)  # Igual a
print("Distinto de:", 5 != 3)  # Distinto de
print("Mayor que:", 5 > 3)  # Mayor que
print("Menor que:", 5 < 3)  # Menor que
print("Mayor o igual que:", 5 >= 5)  # Mayor o igual que
print("Menor o igual que:", 5 <= 3)  # Menor o igual que

# Ejemplo de operadores de identidad
print("Operadores de identidad:")  # Los operadores de identidad se utilizan para comparar objetos
print("Es:", a is b)  # Es
print("No es:", a is not b)  # No es

# Ejemplo de operadores de pertenencia
print("Operadores de pertenencia:")  # Los operadores de pertenencia se utilizan para       
# verificar si un valor está presente en una secuencia (como una lista o una cadena).
lista = [1, 2, 3, 4, 5]
print("Está en la lista:", 3 in lista)  # Está en la lista
print("No está en la lista:", 6 not in lista)  # No está en la lista    

# Ejemplo de operadores bit a bit
print("Operadores bit a bit:")  # Los operadores bit a bit se utilizan para realizar operaciones a nivel de bits.
# Estos operadores trabajan con los bits individuales de los números y realizan operaciones a nivel binario, como AND, OR, XOR y NOT 
# del mismo modo que se hace en matemáticas con los números binarios en algebra booleana.
print("AND bit a bit:", 5 & 3)  # AND bit a bit
print("OR bit a bit:", 5 | 3)  # OR bit a bit  
print("XOR bit a bit:", 5 ^ 3)  # XOR bit a bit
print("NOT bit a bit:", ~5)  # NOT bit a bit  
print("Desplazamiento a la izquierda:", 5 << 1)  # Desplazamiento a la izquierda
print("Desplazamiento a la derecha:", 5 >> 1)  # Desplazamiento a la derecha 

# Ejemplo de operadores de asignación
print("Operadores de asignación:")  # Los operadores de asignación se utilizan para asignar valores a variables.
x = 10  # Asignación simple         
y = 5  # Asignación simple
print("x =", x)  # Imprime el valor de x
print("y =", y)  # Imprime el valor de y    
# Asignación compuesta
x += 5  # Equivalente a x = x + 5
y *= 2  # Equivalente a y = y * 2
print("x después de la asignación compuesta:", x)
print("y después de la asignación compuesta:", y)   

"""La regla de jerarquía de operaciones se aplica a cada tipo de operación presentada hasta ahora en Python"""
''' recuerda que si quieres cambiar el orden de las operaciones, puedes usar paréntesis para agrupar las operaciones que quieras que se realicen primero.'''
# Ejemplo de jerarquía de operaciones
print("Jerarquía de operaciones:")  # La jerarquía de operaciones se refiere al orden en que se realizan las operaciones en una expresión.
# En Python, la jerarquía de operaciones sigue las reglas matemáticas estándar:
print("1. Paréntesis") #primer nivel de jerarquía
print("2. Exponentes") #segundo nivel de jerarquía
print("3. Multiplicación y división") #tercer nivel de jerarquía
print("4. Suma y resta") #cuarto nivel de jerarquía
print("5. Operadores de comparación") #quinto nivel de jerarquía
print("6. Operadores lógicos") #sexto nivel con una subjerarquía (Not, And, Or)

print("Resultado de la jerarquía de operaciones:", 2 + 3 * 4 - 5 / 2 ** 2)  # Resultado de la jerarquía de operaciones
# La jerarquía de operaciones se aplica a cada tipo de operación presentada hasta ahora en Python.





