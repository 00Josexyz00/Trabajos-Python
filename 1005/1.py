# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:15:07 2018

@author: José Cortez
Ejercicio 1 numero binario a decimal
"""
acumulador=0
def crearBina():
    archivo = open('binario.txt','w')
    archivo.close()
    
def crearDec():
    archivo = open('decimal.txt','w')
    archivo.close()
    
def guardarBina():
    dec = input("Ingrese un numero binario para calcular su decimal\n")
    archivo = open('binario.txt','a')
    archivo.write(dec)
    archivo.close()
    
      
def leerBina():
    archivo=open('binario.txt','r')
    linea=archivo.read()
    i=len(linea)-1
    j=0
    acumulador=0
    while i>=0:
        x=int(linea[j])
        acumulador=acumulador+x*(2**(i))
        print(str(acumulador))
        i=i-1
        j=j+1
    archivo.close()
    archivo=open('decimal.txt','a')
    archivo.write(str(acumulador))
    archivo.close()
    archivo=open('binario.txt','r')
    linea=archivo.read()
    print("El decimal es = "+str(acumulador))
    archivo.close()
        
crearBina()
crearDec()
guardarBina()
leerBina()


