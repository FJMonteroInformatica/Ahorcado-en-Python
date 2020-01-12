#!/usr/bin/python3

from random import randint

dibujo=['''
      +---+
      |   |
          |
          |
          |
          |
    ==========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    ==========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    ==========''', '''
      +---+
      |   |
     _O   |
      |   |
          |
          |
    ==========''', '''
      +---+
      |   |
     _O_  |
      |   |
          |
          |
    ==========''', '''
      +---+
      |   |
     _O_  |
      |   |
     /    |
          |
    ==========''', '''
      +---+
      |   |
     _O_  |
      |   |
     / \  |
          |
    ==========''']

lista = ["PANTALLA", "VERDE", "TECLADO", "MANZANA"]


#Devuelve el nombre del autor
def autor():
    return "Francisco Jesús Montero Martínez"


#Devuelve una palabra aleatoria de la lista
def damePalabra():    
    aleatorio = randint(0, len(lista) -1)

    return lista[aleatorio]


#Escribe un texto
def recuadro(texto, h_char, v_char):
    print("{} {} {}".format(h_char, texto, v_char))


#Dibuja el juego en cada vuelta, comprobando las letras de la palabra que ya han sido adivinadas.
#Devuelve la palabra que se muestra en el juego, en la que solo se ven las letras adivinadas.
def escena(pal, usadas, intentos):
    print(dibujo[intentos])
    print("")
    print("<{}> Intentos: {}".format(usadas, intentos))
    palabraAMostrar = pal

    contador = 0
    for var in range(0,len(pal)):    	

    	if pal[contador] not in usadas:    		
    		palabraAMostrar = palabraAMostrar.replace(pal[contador], "_")

    	contador += 1    		    		

    print("")
    print(palabraAMostrar)  
    print("")  

    return palabraAMostrar


#Pide una letra por teclado y la devuelve, junto con un boolean de si se ha introducido una letra correcta o no
def pideLetra(usadas):
	incorrecta = False

	print("Introduzca una letra:", end=" ")    
	letra = input() 
	letra = letra.upper()
	
	if len(letra) != 1:
		print("El número de letras tiene que ser uno")
		incorrecta = True
	elif not letra.isalpha():
		incorrecta = True
		print("No es una letra")
	elif letra in usadas:
		incorrecta = True
		print("Ya has dicho esa letra")
	else:
		usadas.append(letra)

	return letra, incorrecta


#Comprueba si se ha ganado o perdido. En uno de los dos casos, devuelve que el juego ha acabado.
def comprueba(palabra, intentos):
	continuar = True
	gana = True

	if palabra.count("_") == 0:
		continuar=False
		gana=True

	if intentos==len(dibujo)-1:
		continuar=False
		gana=False

	return continuar, gana


#Obtener una palabra a adivinar
palabra = damePalabra()

#Letras que ya se han usado
usadas = []

#Intentos realizados
intentos = 0

#Mensaje de inicio
recuadro("Juego del Ahorcado - creado por " + autor(), "#", "#")
recuadro("Comienza el juego", "=", "=")

continuar = True

while continuar:
    palabraModificada = escena(palabra, usadas, intentos)
    continuar, gana = comprueba(palabraModificada, intentos)

    if continuar:
    	letra, incorrecta = pideLetra(usadas)

    	#Suma un intento si la letra era incorrecta o no está en la palabra
    	if incorrecta:
    		intentos += 1
    	elif palabra.find(letra) == -1:
    		intentos += 1 

    
if gana:
  	recuadro("Has ganado en {} {}".format(intentos, "intento" if intentos == 1 else "intentos"),"*", "*")
else:
   	recuadro("Has perdido. La palabra era {}".format(palabra), "-", "-")
           
