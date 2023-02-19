from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tarea(request,*cadena,**cadenaID):
    #semana 9 y 10: for
    #ejercicio 1
    #Contar la cantidad de vocales en la palabra computadora
    texto = "computadora"
    vocales = "aeiouAEIOU"
    a=0
    for i in texto:
        if i in vocales:
            a=a+1
    
    
    #Ejercicio 2
    #separa la palabra computadora en comas 
    b=[]
    word="computadora"
    for letter in word:
        b.append(letter)
    #Ejercicio 3
    #halla Suma de los 30 primeros numeros impares
    
    c=0
    for i in range (1,31,1):
        if i % 2 == 1 :
            print(i)
            c=c+i
    #ejercicio 4
    #halla la suma de los 100 primeros numeros pares
    d=0
    for i in range (1,101):
         if i% 2 == 0:
            print(i)
            d=d+i
    #ejercicio 5
    #hacer la tabla de multiplicar del 7 hasta el 10
    tabla = 7
    e= [ ]
    for i in range (1,11):
        e.append(i*tabla)
    #semana 11 :while
    #ejercicio 6
    #hacer la suma de los 50 primeros numeros
    f=0
    i=0
    while i<50:
        i=i+1
        f=f+i
    #ejercicio 7
    #Determinar que hora es   si pasara 3 segundo de la hora actual 
    import time 
    segundos=0
    g=[ ]
    while True:
        segundos= segundos + 1
        current_time = time.strftime ('%H:%M:%S') 

        g.append(current_time)
        time.sleep(1)
        if segundos == 3:
            break
    #ejercicio 8
    #Mostrar un aviso  cuando un  balde llegue a 5 litros y advierta que derramara el agua
    caño="abierto"
    litros = 0
    h=[ ]
    while caño =="abierto":
        litros +=1
        h.append(f"balde lleno con {litros} litros ")
        if litros >=5:
            break
        advertencia="¡Se derramara el agua del balde!"
    #ejercicio 9 
    #hacer la suma de los 100 primeros numeros
    k=0
    i=0
    while i<100:
        i=i+1
        k=k+i
    #ejercicio 10 
    #Promedios de los primeros 80 numeros
    suma = 0
    contador = 0
    numero = 1
    while numero <= 80:
     suma += numero
     contador += 1
     numero += 1
     promedio1 = suma / contador
     print("el promedio de los 80 primeros numeros es:", promedio1)
     #semana12 do while
    #ejercicio11
    #mostrar los 20 primeros numeros
    number=0
    n=[ ]
    while number < 20:
        number= number+1
        n.append(number)
    #ejercicio12
    #cuantos de los 20 primeros numeros son divisibles entre 3
    ñ=20
    o=0
    while o<ñ:
        o=o+1
    if ñ%3 ==0:
        ñ=ñ-1
    if ñ%3 ==0:
        ñ=ñ-2
    if ñ%3 ==0:
        ñ=ñ-3
    else:
        ñ=ñ+0
        ejercicio12 =((ñ+1)/3)
    #ejercicio13
    #mostrar la suma de los numeros multiplos de 3 , menores que 100
    contador2=0
    p=0
    numero_maximo=100
    while contador2 < numero_maximo:
        p=p+contador2
        contador2=contador2+3
    #ejercico14
     #mostrar los 50 primeros numeros
    number1=0
    q=[ ]
    while number1 < 50:
        number1= number1+1
        q.append(number1)
    #ejercicio15
    #Factorial de 10 usando do while
    fact=1
    i=1
    while True:
        fact=fact*i
        i=i+1
        if i>10:
            break
    print(fact)
    



    return render(request,'tarea.html',{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'k':k,
    'advertencia':advertencia,'promedio1':promedio1,'n':n,'ejercicio12':ejercicio12,
    'p':p,'q':q,'fact':fact})


