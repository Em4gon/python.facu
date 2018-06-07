import random

def clear(n):
	for i in range(n):
		print("\n")
	
#muestra el menu
def menu():
	print("Bienvenido al juego del ahorcado")
	print("a. Partida nueva")
	print("b. Partida contra la maquina")
	print("c. Salir")
	

listaDificultadHell=["adaptacion","agudo","antibiotico","artritis","ataxia","atrofia","otorrinolaringologo","abreviatura","electroencefalografista","esternocleidomastoideo","desoxirribonucleico","electrocardiograma","fotosinteticamente","electrodomestico","caleidoscopio","pneumonoultramicroscopicsilicovolcanoconiosis","hipopotomonstrosesquipedaliofobia","supercalifragilisticoespialidoso"]

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
	for letra in palabra:
			palabraLista+=[letra]
	return [palabra,palabraLista]

	
def pidePalabraMOD(palabra):
	palabraLista=[]
	for letra in palabra:
			palabraLista+=[letra]
	return [palabra,palabraLista]


#lista,lista-> boolean
def chequeo(lis1,lis2):
	contador=0
	for elemento in lis1:
		for i in range(len(lis2)):
			if elemento == lis2[i]:
				contador+=1
	#print("holaolaoaloal", contador)
	if contador==len(lis1):
		print("todos los elementos de la primer lista (",lis1,"se encuentran dentro de la segunda (",lis2,")")
		return True
	#	print("mierdaa", contador)
	else:
		print("la lista1 ", lis1, "no esta contenida en la segunda", lis2)
		return False


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

"""
def listXCompletar(x):
#recibe una lista x y devuelve una lista de guiones bajos _
	papel=["_"]
#	for i in range(len(x)):
#		papel+="_"
	papel*= len(x)
	return papel
	
	"""
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

basico= ["perro", "Patricio", "maíz", "nuez", "Dory"]
superior=["La casa de papel", "Titanic", "Los Redonditos de Ricota", "Los Palmeras", "Buscando a Nemo", "paralelepípedo"]

def menuSinglePlayer(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada):
	subOpcion=int(input("Ingrese una dificultad, 1=facil, 2=dificil"))
	if subOpcion==1:
		palabra,palabraLista=pidePalabraMOD((basico[random.randint(0,len(basico)-1)]).lower())
		palabraMostrada=listXCompletar(palabra)
		while vidas!=0 and (letrasTotales2(letrasCorrectas,palabraLista)+cantidadEspacios(palabraLista))!= len(palabraLista):
			letra=pideLetra(letrasUsadas)
			if hayLetra(letra,palabra):
				letrasUsadas+=letra
				letrasCorrectas+=letra
				palabraMostrada=permutaLista(palabraMostrada,devuelveIndice(letra,palabra))
				print("La letra es correcta! ")
				print(palabraMostrada)
				mletrasUsadas(letrasUsadas)
				clear(2)
			else:
				print("La letra es incorrecta")
				print(palabraMostrada)
				letrasUsadas+=letra
				mletrasUsadas(letrasUsadas)
				clear(1)
				vidas-=1
				print("Te quedan ", vidas, "vidas")
				clear(4)
		if vidas !=0:
			print("Felicidades, la palabra era: ", palabra)
		elif vidas==0:
			clear(4)
			print("Perdiste ameo...")	
	elif subOpcion==2:
		
		palabra,palabraLista=pidePalabraMOD((superior[random.randint(0,len(basico)-1)]).lower())
		palabraMostrada=listXCompletar(palabra)
		
		while vidas!=0 and (letrasTotales2(letrasCorrectas,palabraLista)+cantidadEspacios(palabraLista))!= len(palabraLista):
			letra=pideLetra(letrasUsadas)
			if hayLetra(letra,palabra):
				letrasUsadas+=letra
				letrasCorrectas+=letra
				palabraMostrada=permutaLista(palabraMostrada,devuelveIndice(letra,palabra))
				print("La letra es correcta! ")
				print(palabraMostrada)
				mletrasUsadas(letrasUsadas)
				clear(2)
			else:
				print("La letra '",letra, "' es incorrecta.")
				print(palabraMostrada)
				letrasUsadas+=letra
				mletrasUsadas(letrasUsadas)
				clear(1)
				vidas-=1
				print("Te quedan ", vidas, "vidas")
				clear(4)
		if vidas !=0:
			print("Felicidades, la palabra era: ", palabra)
			opcion=pideOpcion()
		elif vidas==0:
			clear(4)
			print("Perdiste ameo...")				
	opcion=pideOpcion()
	return opcion
					
def funcionJuego():
	opcion=pideOpcion()
	palabra=""
	palabraLista=[]
	letrasUsadas=[]
	letrasCorrectas=[]
	palabraMostrada=[]
	vidas=6
	if opcion=="a":
		palabra,palabraLista=pidePalabra()
		clear(20)
		palabraMostrada=listXCompletar(palabra)
		while vidas!=0 and (letrasTotales2(letrasCorrectas,palabraLista)+cantidadEspacios(palabraLista))!= len(palabraLista):
			letra=pideLetra(letrasUsadas)
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
		if vidas !=0:
			print("Felicidades, la palabra era: ", palabra)
			opcion=pideOpcion()
		elif vidas==0:
			clear(4)
			print("Perdiste ameo...")
	elif opcion=="b":
		menuSinglePlayer(opcion,vidas, letrasCorrectas,palabraLista,letrasUsadas,palabraMostrada)
	elif opcion!="b" or opcion!="a":
		print("Gracias, vuelvas prontos")
		#return opcion
		
def main():
	opcion=""
	while opcion!="a" and opcion!="b" and opcion!="c":
		menu()
		funcionJuego()
		break
	if opcion=="c":
		print("Gracias por haber jugado!!!!!!!!!!!!!!!!!!#!")
main()


#funcion que toma una letra y una lista de letras (la palabra descomprimida)
#arma una lista que tiene la longitud de la palabra

#shit
