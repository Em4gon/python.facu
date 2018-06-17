import random


basico= ["perro", "Patricio", "maíz", "nuez", "Dory"]
superior=["La casa de papel", "Titanic", "Los Redonditos de Ricota", "Los Palmeras", "Buscando a Nemo", "paralelepípedo"]
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
listaAcentos=["á","é","í","ó","ú","Á","É","Í","Ó","Ú"]
listaSAcentos=["a","e","i","o","u","A","E","I","O","U"]

def replaceAcentos(lista):
	#toma una lista.... no, string..... y si una de las vocales esta dentro de la lista de vocales con acento la reemplalza
	#devuelve la misma lista sin letras acentuadas
	resul=""
	for i in range(len(lista)):
		letra = lista[i]
		if letra in listaAcentos:
			resul+=listaSAcentos[listaAcentos.index(letra)]
		else:
			resul+=letra
	return resul

#test sacar acentos
#listatest=["m","í","é","r","d","á"]
#print(replaceAcentos(listatest))
#print("esta es la lista pre funcion", listatest)
#listatest=replaceAcentos(listatest)
#print("esta es la lista post funcion", listatest)

def clear(n):
	for i in range(n):
		print("\n")
	
#muestra el menu
def menu():
	print("Bienvenido al juego del ahorcado")
	print("a. Partida nueva")
	print("b. Partida contra la maquina")
	print("c. Salir")
	

#recibe una lista de letras, cuenta la cantidad de veces que aparece cada letra dentro de la palabra
#lista lista -> number
def letrasTotales2(lis1,lis2):
	contador=0
	for elemento in lis1:
		for i in range(len(lis2)):
			if elemento == lis2[i]:
				contador+=1
	return contador

def cantidadEspacios(lis):
	contador=0
	for elem in lis:
		if elem == " ":
			contador+=1
	return contador


#None->list(string,list)
def pidePalabra():
	palabraLista=[]
	palabra=(input("Ingrese una palabra... ")).lower()
	palabra= replaceAcentos(palabra)
	for letra in palabra:
			palabraLista+=[letra]
	#palabraLista= replaceAcentos(palabraLista)
	return [palabra,palabraLista]


def pidePalabraMOD(palabra):
	palabraLista=[]
	palabra= replaceAcentos(palabra)
	for letra in palabra:
			palabraLista+=[letra]
	return [palabra,palabraLista]



#funcion ahorcado: verifica si una letra esta en una palabra y devuelve un boolano
def hayLetra(letra,palabra):
	#if letra.lower() in palabra.lower():
	if letra in palabra:
		return True
	else:
		return False

def pideOpcion():
	opcion=input("Ingrese una opcion: ")
	while opcion!= "a" and opcion!= "b" and opcion!= "c":
		opcion=input("Ingrese una opcion valida (a/b/c) : ")
	else:
		return opcion


def pideLetra(lista):
	letra=input("Ingrese una letra... ")
	#while  (True != letra.isdigit())
	if letra in lista:
		print("La letra ya se cuentra ingresada...")
		while letra in lista:
			letra=input("Ingrese una letra no ingresada previamente... ")
	while len(letra)!=1:
		if letra in lista:
			letra=input("Ingrese UNA sola letra... ")
		else:
			letra=input("Ingrese UNA sola letra... ")
	else:
		return letra

		
def devuelveIndice(letra,palabra):
#toma una letra y una lista de letras, para cada posicion que se repita la letra agrega
#un numemero correspondiente al indice en la lista de letras en donde se repia
#ej: A,alabama ->(a,[0,2,4,6])
	indices=[]
	for i in range(len(palabra)):
		if letra == palabra[i]:
			indices+=[i]
	return (letra,indices)



def listXCompletar(x):
#recibe una lista x y devuelve una lista de guiones bajos _
	papel=[]
	for char in x:
		if char!=" ":
			papel+=["_"]
		else:
			papel+=[char]
	return papel


def permutaLista(lcompletando,tuplaIndice):
#recibe la lcompletando, que toma los elementos de la tuplaIndice y devuelva la lcompletando	
	letra=tuplaIndice[0]
	indic=tuplaIndice[1]
	for numerito in indic:
		lcompletando= lcompletando[:numerito]+[letra]+lcompletando[(numerito+1):]
	return lcompletando

#lista->none
def mletrasUsadas(lista):
	comp=len(lista)
	if comp>=1:
		print("Las letras que ha usado son: ", end="\n")
		for char in lista:
			print(char,end=", ")

def fcond(letrasCorrectas,palabraLista):
	if (letrasTotales2(letrasCorrectas,palabraLista)+cantidadEspacios(palabraLista))!= len(palabraLista):
		return True
	else:
		return False

def engine(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada,cosoinput):
	palabra,palabraLista=cosoinput
	#palabraLista=replaceAcentos(palabraLista)
	condicion = fcond(letrasCorrectas,palabraLista)
	clear(20)
	palabraMostrada=listXCompletar(palabra)
	while vidas!=0 and condicion:
		letra=pideLetra(letrasUsadas)
		if letra!="*":
			if hayLetra(letra,palabra):
				letrasUsadas+=letra
				letrasCorrectas+=letra
				palabraMostrada=permutaLista(palabraMostrada,devuelveIndice(letra,palabra))
				print("La letra '",letra,"' es correcta! ")
				print(palabraMostrada)
				mletrasUsadas(letrasUsadas)
				clear(7)
			else:
				print("La letra '",letra,"' es incorrecta")
				print(palabraMostrada)
				letrasUsadas+=letra
				mletrasUsadas(letrasUsadas)
				clear(1)
				vidas-=1
				print("Te quedan ", vidas, "vidas")
				clear(7)
		else:
			letrasUsadas=[]
			letrasCorrectas=[]
			letra=input("Ingrese una palabra completa\t")
			if letra == palabra:
				condicion = False
				print("La palabra era correcta")
			else:
				vidas = 0
	if vidas !=0:
		print("Felicidades, la palabra era: ", palabra)
		clear(5)
		#opcion=pideOpcion()
	elif vidas==0:
		clear(4)
		print("Perdiste ameo...")
		print("La palabra era incorrecta, la palabra correcta era: ", palabra)
		clear(4)

def menuSinglePlayer(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada):
	subOpcion=int(input("Ingrese una dificultad, 1=facil, 2=dificil"))
	if subOpcion==1:
		engine(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada,pidePalabraMOD((basico[random.randint(0,len(basico)-1)]).lower()))
	elif subOpcion==2:
		engine(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada,pidePalabraMOD((superior[random.randint(0,len(basico)-1)]).lower()))

					
def funcionJuego(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada):
	engine(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada,pidePalabra()) 															#COMIENZA BLOQUE ENGINE 
		
def main():
	menu()
	opcion=pideOpcion()
	while opcion=="a" or opcion=="b":
		palabra=""
		palabraLista=[]
		letrasUsadas=[]
		letrasCorrectas=[]
		palabraMostrada=[]
		vidas=6
		if opcion == "a":
			funcionJuego(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada)
		elif opcion=="b":
			menuSinglePlayer(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada)
		menu()
		opcion=pideOpcion()
	if opcion=="c":
		clear(5)
		print("Gracias por haber jugado!!!!!!!!!!!!!!!!!!#!")
main()

#shit
