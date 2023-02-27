from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio_ver (*variable,**variableid):
    return HttpResponse ("<h1>Pagina de inicio</h1>")

#logica de negocios#
    
def semana9y10 (request,*variable,**variableid):
    return render (request,'Semana 9.html',{'resultado1':pr, 'resultado2':Bandas, 'resultado3':Países, 'resultado4': Tabla, 'resultado5':Num,
    'resultado6': num,'resultado7': suma,'resultado8':acum_num,'resultado9':Potencia,'resultado10': inversa,'head':head})


head=["INICIO","NOSOTROS","ASESORÍA","MARKETING DIGITAL","CONTACTO"]


#Semana 9 y 10 (For)#

#Ejercicio 1: Suma de los 15 primeros números primos#
pr=0
primos = []
for i in [1,2,3,5,7,11,13,17,19,23,27,31,37,41,43,47]:
    pr=pr+i

#Ejercicio 2: 5 bandas del movimiento musical "Invasión británica"#
Bandas = ["The Beatles", "The Rolling Stones", "The Dave Clark Five", "The Animals", "The Who"]
for i in Bandas:
    print(i)

#Ejercicio 3: Todos los países de Sudamérica#
Países = [ "Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Perú", "Surinam", 
"Trinidad y Tobago", "Uruguay", "Venezuela"]
for i in Países:
    print(i)

#Ejercicio 4: Tabla de multiplicar del 10#
Tabla = []
for i in range (0,13):
    n=i*10
    Tabla.append(n)
    
#Ejercicio 5: Los 10 primeros números pares#
Num = []
for i in range(2,22,2):
    Num.append(i)



#Semana 11 (While)#

#Ejercicio 1: Factorial de los 10 primeros números naturales#
resultado=1
num=[]
contador=1
while contador <=10:
    resultado=resultado*contador
    contador=contador+1
    num.append(resultado)

#Ejercicio 2: Suma de los 50 primeros números naturales#
suma = 0
i = 1
while i <= 50:
    suma += i
    i += 1

#Ejercicio 3: Los 15 primeros números naturales#
acum_num = []
i = 1
while i <=15: 
    acum_num.append(i)
    i += 1 

#Ejercicio 4: Potencia#
Potencia=[]
i=1
while i <=10:
    Pot=i*i
    Esc= str(i) + "*" + str(i) + "=" + str(Pot)
    Potencia.append(Esc)
    i+=1

#Ejercicio 5: #
numero = 753
inversa = 0
while numero != 0:
    residuo = numero % 10
    inversa = (inversa * 10) + residuo
    numero //= 10
