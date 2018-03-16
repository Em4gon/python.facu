#-*-coding: utf-8-*-
blank="                                            "
print(blank)
def xx(): #funcion de linea en blanco
    print(blank)


#Operaciones con Cadenas de Texto
x = 8
print(x)
y=x*x
print(y)
lenguaje="Python"
print("estoy programando en ", lenguaje)
"""
abs(10)
abs(-10)
max(5,9,-3)
min(5,9)
len ("PYTHON")
n = 17
print(n)
lenguaje = 'Python'
print(lenguaje)
"""
#Funciones Standart

def hola_marta():
    return "Hola Marta! estoy programando en Phyton!!"
print(hola_marta())


def hola_pablo():
    return"Hola Pablo! estoy programando"
    
print(hola_pablo())



def hola(alguien):
    return "Hola " + alguien + "estoy programando en python!"

print(hola("pedro"))


def cuadrado(n):
    return n*n

print(cuadrado(9))
xx()

#Problema: Pensar un numero, duplicarlo, sumarle seis, y dividirlo por dos, y restarle el numero
#elegido al comienzo. El numero que queda es siempre tres.

#soludcion1
def f1(numero):
    return ((numero*2)+6)/2-numero

print("El numero elegido da ", f1(9))

#solucion2
def f2 (elegido):
    n = elegido * 2
    n = n + 6
    n = n / 2
    n = n - elegido
    return n

print("El numero elegido da ", f2(5))

#Supongamos que queremos calcular la suma de los primeros cinco numeros cuadrados.
def suma_5_cuadrados():
    suma=0
    suma=suma+(1*1)
    suma=suma+(2*2)
    suma=suma+(3*3)
    suma=suma+(4*4)
    suma=suma+(5*5)
    return suma
    
print("La suma de los 5 primeros cuadrados", suma_5_cuadrados())

xx()

#: Usando un Ciclo Definido
def suma_5_cuadrados_for():
    suma=0
    for i in range (1,6):
        suma=suma+(i*i)
        
    return suma
 
def suma_5_cuadrados_for2(n): #usando una variable n
    suma=0
    for i in range (1,n+1): # cuerpo de la repeticion
        suma=suma+(i*i)     # 
        
    return suma
       
#print(suma_5_cuadrados_for())
xx()
#print("La suma de los primers 10 cuadrados es ", suma_5_cuadrados_for2(10))

"""

Variantes del ciclo definido, utilizando "range"
#1)range(n1, n2)
# [n1, n+1.... n2-2, n2-1]
#2) range (n1)
# [0,1,2....n1-1]
#3) Especificar valores particulares
# [1,3,9,27]
#for i in [1,3,9,27]:
#   print (i, i*i)        fin

    


coment

"""

"""Problema
: Pensar un numero, duplicarlo, sumarle seis, y dividirlo por dos, y restarle el numero
elegido al comienzo. El numero que queda es siempre tres"""

xx()

#el nopmbre debe estar entre comillas
def hola(nombre):
	return "hola " + nombre + "!"
	
def saludar():
	nombre= input("Por favor ingrese su nombre: ")
	saludo = hola (nombre)
	print (saludo)

#saludar()



#-----------------------------------------------------------ejercicio4c
	
def suma_coord():
	x1= input("Coloque un la coordenada X")
	x2= input("Coloque la otra coordenada X")
	y1= input("Coloque la coordenada Y")	
	y2= input("Coloque la otra coordenada Y")
	numero = abs(x2-x1)*2+abs(y2-y1)*2 
	print("El perimetro del rectangulo es", numero)
	
	
#suma_coord()

#---------------------------------------------------------ejercicio1/2
def imprimir_cuadrados():
	print("Se calcularán cuadrados entre dos numeros ingresados")
	n1= int (input ("Ingrese un numero entero: "))
	n2 = int (input ("Ingrese otro numero entero: "))
	
	for x in range (n1, n2):
		print (x, (x*x))
		
	print("Es todo por ahora")
	
#imprimir_cuadrados()

#--------------------------------------------------ejercicio3
def saludo_producto():
	nombre=input("¿Cual es tu nombre? ") 
	print("Buen dia " + nombre + ", indtroducí dos numeros y los multiplico ")
	num1=int(input("Coloque el primer numero "))
	num2=int(input("Coloque el segundo numero "))
	producto = num1*num2
	print ("El producto de sus numeros es ", producto) #cuando hay que agregar un numero se usa una coma, para concatenar strings, se usa el mas
	
#saludo_producto()

#---------------------------------ejercicio4a
def calcular_rectangulo_perimetro():
	base = int(input("Poné la base del rectangulo"))
	altura = int(input("Poné la altura del rectangulo"))
	perimetro = 2*base+2*altura
	print("El perimetro del rectangulo es ", perimetro)
	
#calcular_rectangulo_perimetro()

#--------------------ejercicio4g

def cuadrado(x):
	return x*x
	
def raiz_cuadrada(m):
	return m**(1/2)
	
def hipotenusa (a,b):
	suma=cuadrado(a)+cuadrado(b)
	return  raiz_cuadrada(suma)
	
#print(hipotenusa(5, 7))

#------------------------ejercicio4b
def area_rectangulo(a,b):
	return (a*b)
	
#print("el area del rectangulo", area_rectangulo(2,8))

#-----------------------ejercicio4d
pi=3,141592
print(pi)
def perimetro_circulo(r):
	

#---------------ej6

def factorial(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	return fact
	
#print(factorial(4))
