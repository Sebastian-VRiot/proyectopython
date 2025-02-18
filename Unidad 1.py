# Code to ask user for their name, contiene variable, igual, función y pregunta que el usuario verá
name = input ("What's your name? ")

# Code to say hello to user, contiene función print, sintaxis y variable que almacena el nombre del user
print ("Hello,",name)

# Otra manera para que los argumentos puedan mostrarse en una sola línea usando el parametro "end"
# Ahora pregunta por el apellido
lastname = input ("What's your last name? ")

# Code to say hello to user using their last name
print ("Nice to meet you ", end="")
print (lastname,"welcome!")
# Basicamente "end" coge la siguiente linea y la encadena para juntarse con la linea anterior y al finalizar agrega una linea nueva

# Otra manera de separar usando el parametro "sep"
# Ahora pregunta por nacionalidad
nacionality = input ("What's your nationality? ")

# Code to ask nationality to users
print ("Hell yeah,", nacionality, "Viva!", sep=" ")
# "sep" supone un espacio entre los argumentos, las comillas deben estar separadas

# Escaping character \ permite agregar comillas dentro de las comillas, ej. print ("hello \"Friend\"") 

# Una manera más eficaz de solucionar problemas como separaciones o letras solo en minuscula para nombres, es con F-Strings
artista_favorito = input ("What's your favorite artist? ")
print (f"Let's go, {artista_favorito}")
# poner una f antes de las comillas dobles permite a python reconocer una variable dentro de unos corchetes como otro argumento diferente

# Metodos de cadena, son funciones de cadena que permiten manipular la info de una entrada (espacios inncesarios, mayusculas)
completename = input ("What's your complete name? ").strip( ).title( )
print (f"Gusto en conocerte nuevamente, {completename}")
# .strip elimina espacios innecesarios a la izqu y a la derec, .title pone en mayus la 1era letra de cada palabra

# La función de cadena .split, permite dividir una cadena en multiplies subcadenas y con otras variable mostrar una u otra info
personaje_favorito = input ("What's your favorite character? ").strip().title()
first, last = personaje_favorito. split(" ")
print (f"El goat, {first}")
# Basicamente esta función permitirá coger un dato para una variable (first) y el otro dato para otra variable (last)