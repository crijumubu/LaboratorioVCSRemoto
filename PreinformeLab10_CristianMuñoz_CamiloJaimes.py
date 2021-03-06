<<<<<<< HEAD
# -*- coding: utf-8 -*-
"Created on Thu Apr  2 16:10:55 2020"

import numpy as np

Utilidad = np.array ([27834*10**6,23789*10**6,30189*10**6,30967*10**6,32501*10**6,32701*10**6,31665*10**6,17155*10**6,4614*10**6,834*10**6])

#%% PUNTO 1

def diferencia1(Utilidad):
    
#Media de la utilidad operacional de los dos primeros años de registro

    suma1=0
    cont1=0
    for i1 in range(0,2):
        suma1 += Utilidad[i1]
        cont1 += 1
    media1 = suma1/cont1
   
#Media de la utilidad operacional de los dos últimos años de registro

    suma2=0
    cont2=0
    for i2 in range(8,10):
        suma2 += Utilidad[i2]
        cont2 += 1
    media2 = suma2/cont2
    
#Diferencia de la media de utilidad operacional entre los dos ultimos años y los dos primeros años de registro

    diferencia2 = int(media1-media2)
    return diferencia2

print("La diferencia de la media en la utilidad operacional de Kellog's en los últimos dos años comparada con la de los primeros dos años de registro es " + str(diferencia1(Utilidad)) + " COP")

#%% PUNTO 2

def diferencia3(Utilidad):
    
#Año con mayor utilidad operacional

    long = len(Utilidad)
    mayor = Utilidad[0]
    for i3 in range(1,long):
        if mayor<Utilidad[i3]:
            mayor = Utilidad[i3]

#Año con menor utilidad operacional

    menor = Utilidad[0]
    for i4 in range(1,long):
        if menor>Utilidad[i4]:
            menor = Utilidad[i4]
        
#Diferencia entre las utilidades operacionales del año con mayor utilidad y el año con menor utilidad

    diferencia4 =int(mayor-menor)
    return diferencia4

print("La diferencia entre las utilidades operacionales del año con mayor utilidad y el año con menor utilidad es " + str(diferencia3(Utilidad)) + " COP")

#%% PUNTO 3

def mediana(Utilidad):
    
    utilidad = sorted(Utilidad)
    mediana = int((utilidad[4] + utilidad[5]) / 2)
    
    print("La mediana es: " + str(mediana) + " COP")
    
mediana(Utilidad)

#%% PUNTO 4

def media_mediana(Utilidad):
    
#Media
    
    long = len(Utilidad)
    suma3 = 0
    cont5 = 0
    for i5 in range(0,long):
        suma3 += Utilidad[i5]
        cont5 += 1
    media = int(suma3 / cont5)

#Mediana
    
    utilidad = sorted(Utilidad)
    mediana = int((utilidad[4] + utilidad[5]) / 2)
    
    print("La media es: " + str(media) + " COP")
    print("La mediana es: " + str(mediana) + " COP")

media_mediana(Utilidad)

#%% PUNTO 5

def porcentaje_utilidad(Utilidad):
    
#Utilidad operacional acumulado
    
    long = len(Utilidad)
    suma4 = 0
    año = 2008
    for i6 in range(0,long):
        suma4 += Utilidad[i6]
        
#Utilidad operacional de cada año y porcentaje que aporta

    for i7 in range(0, long):
        porcentaje_que_aporta = round((Utilidad[i7] / suma4)*100 , 2)
        print("El porcentaje que le aporta la utilidad operacional del año " +str(año) + " es: " + str(porcentaje_que_aporta) + "%")
        año += 1
        
porcentaje_utilidad(Utilidad)

#%% PUNTO 6

def deficit(Utilidad):
    
    deficit=0
    for i7 in range(8, 10):
        deficit = Utilidad[i7]-deficit
    return deficit
        
print("El déficit operacional del año 2017 con respecto al año anterior es: " + str(abs(deficit(Utilidad))) + " COP")

#%% PUNTO 7

def deficit_cada_año(Utilidad):
    
#Hallamos la media
    
    long= len(Utilidad)
    suma6 = 0
    cont7 = 0
    for i9 in range(0,long):
        suma6 += Utilidad[i9]
        cont7 += 1
    media4 = int(suma6/cont7)
    
#Hallamos el déficit operecaional de cada año con respecto a la media
    
    año = 2008
    for i10 in range(0,long):
        deficit1 = round((((media4 - Utilidad[i10]) / media4) * 100), 2)
        if deficit1<0:
            print("El año " +str(año) + " no tuvo un déficit operacional ya que está por éncima de la media")
        else:
            print("El déficit operacional del año " + str(año) + " es: " + str(deficit1) + "%")
        año +=1
        
deficit_cada_año(Utilidad)
        
"@author: user"
=======
# -*- coding: utf-8 -*-
"Created on Thu Apr  2 16:10:55 2020"

import numpy as np

Utilidad = np.array ([27834*10**6,23789*10**6,30189*10**6,30967*10**6,32501*10**6,32701*10**6,31665*10**6,17155*10**6,4614*10**6,834*10**6])

#%% PUNTO 1

def diferencia1(Utilidad):
    
#Media de la utilidad operacional de los dos primeros años de registro

    suma1=0
    cont1=0
    for i1 in range(0,2):
        suma1 += Utilidad[i1]
        cont1 += 1
    media1 = suma1/cont1
   
#Media de la utilidad operacional de los dos últimos años de registro

    suma2=0
    cont2=0
    for i2 in range(8,10):
        suma2 += Utilidad[i2]
        cont2 += 1
    media2 = suma2/cont2
    
#Diferencia de la media de utilidad operacional entre los dos ultimos años y los dos primeros años de registro

    diferencia2 = int(media1-media2)
    return diferencia2

print("La diferencia de la media en la utilidad operacional de Kellog's en los últimos dos años comparada con la de los primeros dos años de registro es " + str(diferencia1(Utilidad)) + " COP")

#%% PUNTO 2

def diferencia3(Utilidad):
    
#Año con mayor utilidad operacional

    long = len(Utilidad)
    mayor = Utilidad[0]
    cont3 = 0
    for i3 in range(1,long):
        if Utilidad[cont3]<Utilidad[i3]:
            mayor = Utilidad[i3]
        cont3 += 1

#Año con menor utilidad operacional

    menor = Utilidad[0]
    cont4 = 0
    for i4 in range(1,long):
        if Utilidad[cont4]>Utilidad[i4]:
            menor = Utilidad[i4]
        cont4 += 1
        
#Diferencia entre las utilidades operacionales del año con mayor utilidad y el año con menor utilidad

    diferencia4 =int(mayor-menor)
    return diferencia4

print("La diferencia entre las utilidades operacionales del año con mayor utilidad y el año con menor utilidad es " + str(diferencia3(Utilidad)) + " COP")

#%% PUNTO 3

def mediana(Utilidad):
    
    utilidad = sorted(Utilidad)
    mediana = int((utilidad[4] + utilidad[5]) / 2)
    
    print("La mediana es: " + str(mediana) + " COP")
    
mediana(Utilidad)

#%% PUNTO 4

def media_mediana(Utilidad):
    
#Media
    
    long = len(Utilidad)
    suma3 = 0
    cont5 = 0
    for i5 in range(0,long):
        suma3 += Utilidad[i5]
        cont5 += 1
    media = int(suma3 / cont5)

#Mediana
    
    utilidad = sorted(Utilidad)
    mediana = int((utilidad[4] + utilidad[5]) / 2)
    
    print("La media es: " + str(media) + " COP")
    print("La mediana es: " + str(mediana) + " COP")

media_mediana(Utilidad)

#%% PUNTO 5

def porcentaje_utilidad(Utilidad):
    
#Utilidad operacional acumulado
    
    long = len(Utilidad)
    suma4 = 0
    año = 2008
    for i6 in range(0,long):
        suma4 += Utilidad[i6]
        
#Utilidad operacional de cada año y porcentaje que aporta

    for i7 in range(0, long):
        porcentaje_que_aporta = round((Utilidad[i7] / suma4)*100 , 2)
        print("El porcentaje que le aporta la utilidad operacional del año " +str(año) + " es: " + str(porcentaje_que_aporta) + "%")
        año += 1
        
porcentaje_utilidad(Utilidad)

#%% PUNTO 6

def deficit(Utilidad):
    
    deficit=0
    for i7 in range(0, 10):
        deficit -= Utilidad[i7]
    return deficit
        
print("El déficit operacional del año 2017 con respecto al año anterior es: " + str(abs(deficit(Utilidad))) + " COP")

#%% PUNTO 7

def deficit_cada_año(Utilidad):
    
#Hallamos la media
    
    long= len(Utilidad)
    suma6 = 0
    cont7 = 0
    for i9 in range(0,long):
        suma6 += Utilidad[i9]
        cont7 += 1
    media4 = int(suma6/cont7)
    
#Hallamos el déficit operecaional de cada año con respecto a la media
    
    año = 2008
    for i10 in range(0,long):
        deficit1 = round((((media4 - Utilidad[i10]) / media4) * 100), 2)
        if deficit1<0:
            print("El año " +str(año) + " no tuvo un déficit operacional ya que está por éncima de la media")
        else:
            print("El déficit operacional del año " + str(año) + " es: " + str(deficit1) + "%")
        año +=1
        
deficit_cada_año(Utilidad)
        
"@author: user"
