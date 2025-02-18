#def nos permite crear una función, en este caso lleva por nombre "haz_lo_tuyo():", esta función muestra en pantalla "Eres un hombre de cultura?"
def haz_lo_tuyo():
    print("Eres un hombre de cultura?")
#Es importante, debajo de la linea de la función, dejar el espacio con TAB o 4 espacios de la barra
#Todo lo que esté debajo en la sangria de "def" será lo que hará la función creada

#Aquí llamamos a nuestra función creada
haz_lo_tuyo()

#Luego creamos una variable con un dato de entrada que el usuario responderá, la variable va acompañada por unos parametros de .strip y .tittle
dubstep_artist = input ("Cómo se llama el artista que la esta partiendo en Dubstep? ").strip().title()

#Por ultimo, imprimiremos en la pantalla un texto que acompañe a la info que ingresó el usuario en la pestaña anterior
print("Eso es correcto,", dubstep_artist, ", The Goat!")

