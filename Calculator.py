#Code "int" para convertir valores que en la entrada de la cadena se parezca a un numero entero y se pueda usar para calculos matemáticos
X = int(input ("Cuanto es X? "))
Y = int(input ("Cuanto es Y? "))
print (X + Y)
#Python leerá los valores que hayan dentro del parentesis mas interno y de ahi retornará los valores a la función externa

#Code "float" se entenderá como un número con punto decimal, llamado valor de punto flotante
x = float (input("What's X? "))
y = float (input("What's Y? "))
print (x + y)
# float tomará los valores en la entrada de la cadena que parexca un numero decimal separado con punto (.) sistema de EEUU

#Code "round" nos permitirá redondear esos decimales al número entero más próximo. el codigo es round (number [, n digits])
x = float (input ("What's x? "))
y = float (input ("What's y? "))
z = round (x + y)
print (z)
# El resultado será el numero entero más proximo, 1.2 + 3.4 = 5
# En el caso de querer dividir numero grandes con un punto o una coma (1000) se podría hacer de la siguiente manera
numero1 = float (input ("Cual es el 1er número grande? "))
numero2 = float (input ("Cual es el 2do número grande? "))
resultado = round (numero1 + numero2)
print (f"{resultado:,}")
#El resultado de un numero que sea una milesima como 999+1, será 1,000 separado por una coma, esto es debido a que en la... 
#...función print agregamos el argumento para el formato especial "f" donde le decimos que al resultado lo formatee con la separación de una coma

#Code para que la calculadora divida
n1 = float (input("What's n1 dividido? "))
n2 = float (input ("What's n2 dividido? "))
r = n1 / n2
print (r)
#Notamos que el resultado de 2/3 es un numero decimal muy largo, podriamos reducirlo de 2 manera, una a travez de "round" y otra a travez de "f-string"
#Con round:
nu1 = float (input ("Cual es el numero a dividir con round? "))
nu2 = float (input ("Cual es el otro numero a dividir con round? "))
result = round (nu1 / nu2, 2)
print (result)
#El resultado de 2/3 pasará de 0.66666 a 0.67 en donde 1) se reducen los decimales y 2) se redondea el ultimo decimal al numero entero más cercano

#Con f-string
nu1 = float (input("1er número dividido con resultado reducido f? "))
nu2 = float (input ("2do número dividido con resultado reducido f? "))
result = nu1 / nu2 
print (f"{result:.2f}")
#Usar :.2f es la forma de especificar cuantos digitos quieres imprimir usando una cadena f. dará como resultado 0.67 a una division de 2/3
