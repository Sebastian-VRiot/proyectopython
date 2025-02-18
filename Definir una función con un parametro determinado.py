#Se puede personalizar una función creada para que esta, en este caso, tome el nombre de usuario como entrada a traves de un parametro que llamaremos to
#def hola(to):
#    print ("Bienvenido,",to)
#En este caso usaremos "to" simplemente por obras del ejercicio. De modo que el codigo pueda no solo saludar si no tambien mostrar el nombre de la persona


#Ahora, la funcion creada fue diseñada para tomar el parametro "to" como entrada. Se usará el valor de ese parametro para introducirlo en "print".
#Tambien podemos poner un valor determinado para que, de esta manera no solo se verá "Bienvenido" si no que tambien se verá "animate a responder" 
#ESto es en caso de que el programador no haya llamado la función con el nombre de la persona. es decir que solo haya puesto Bienvenida ()
 
def bienvenida (to="animate a responder"):
    print("Bienvenido,", to)
#"to" (puede ser cualquier cosa) que la computadora detectará como la variable (user_name) que usaremos más adelante

#Aqui usamos nuestra nueva función sin argumentos, lo que nos mostrará (bienvenido, animate a responder)
bienvenida ()

user_name = input("Cómo te gustaria que te llamemos? ").strip().title()

#Aquí usaremos el codigo esta vez con el parametro o variable "user_name" 
bienvenida (user_name)
#A pesar de que la variable se llama "user_name", cuando la función en sí es llamada, la computadora asume que el mismo valor de la variable "user_name" se llama "to."
#Así entonces "user_name" es esencialmente copiado a otra variable, en este caso "to". Que en el contexto de "print ("Bienvenido,",to) pueda decir "Bienvenido" a esa variable "to"
