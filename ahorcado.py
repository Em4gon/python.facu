def clear(n):
	for i in range(n):
		print("\n")

#muestra el menu
def menu():
	print("Bienvenido al juego del ahorcado")
	print("a. Partida nueva")
	print("b. Salir")
	


#recibe una lista de letras, cuenta la cantidad de veces que aparece cada letra dentro de la palabra
#lista lista -> number
def letrasTotales2(lis1,lis2):
	contador=0
	for elemento in lis1:
		for i in range(len(lis2)):
			if elemento == lis2[i]:
				contador+=1
	return contador




#None->list(string,list)
def pidePalabra():
	palabraLista=[]
	palabra=input("Ingrese una palabra... ")
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
	if letra in palabra:
		return True
	else:
		return False

def pideOpcion():
	opcion=input("Ingrese una opcion: ")
	while opcion!= "a" and opcion!= "b":
		opcion=input("Ingrese una opcion valida (a/b) : ")
	else:
		return opcion
	

def pideLetra():
	letra=input("Ingrese una letra... ")
	#while  (True != letra.isdigit())
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
	for i in range(len(x)):
		papel+="_"
	return papel
	


def permutaLista(lcompletando,tuplaIndice):
#recibe la lcompletando, que toma los elementos de la tuplaIndice y devuelva la lcompletando	
	letra=tuplaIndice[0]
	indic=tuplaIndice[1]
	for numerito in indic:
		lcompletando= lcompletando[:numerito]+[letra]+lcompletando[(numerito+1):]
	return lcompletando

print(permutaLista(listXCompletar("mierda"),devuelveIndice("a","mierda")))		

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
		while vidas!=0 and letrasTotales2(letrasCorrectas,palabraLista)!= len(palabraLista):
			letra=pideLetra()
			if hayLetra(letra,palabra):
				letrasUsadas+=letra
				letrasCorrectas+=letra
				palabraMostrada=permutaLista(palabraMostrada,devuelveIndice(letra,palabra))
				print("La letra es correcta! ")
				print(palabraMostrada)
				clear(2)
			else:
				print("La letra es incorrecta")
				vidas-=1
				print("Te quedan ", vidas, "vidas")
				
		if vidas !=0:
			print("Felicidades, la palabra era: ", palabra)
		elif vidas==0:
			clear(4)
			print("Perdiste ameo...")
	elif opcion=="b" or opcion!="a":
		print("Gracias, vuelvas prontos")
		
def main():
	menu()
	funcionJuego()
	
main()


""" no modularizado-----
def main():
	menu()
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
		#while vidas!=0 and not(chequeo(letrasCorrectas,palabraLista)):
		#while ((vidas!=0) and (len(letrasCorrectas) != len(palabraLista))):
		while vidas!=0 and letrasTotales2(letrasCorrectas,palabraLista)!= len(palabraLista):
			letra=pideLetra()
			if hayLetra(letra,palabra):
				letrasUsadas+=letra
				letrasCorrectas+=letra
				palabraMostrada=permutaLista(palabraMostrada,devuelveIndice(letra,palabra))
				print("La letra es correcta! ")
				print(palabraMostrada)
				clear(2)
			else:
				print("La letra es incorrecta")
				vidas-=1
				print("Te quedan ", vidas, "vidas")
				
		if vidas !=0:
			print("Felicidades, la palabra era: ", palabra)
		elif vidas==0:
			clear(4)
			print("Perdiste ameo...")
	elif opcion=="b" or opcion!="a":
		print("Gracias, vuelvas prontos")
	

main()
"""


