# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:06:09 2018

@author: ESFOT
"""
def crear():
    archivo = open('cadena.txt','w')
    archivo.close()
    
crear()

cadena="Cadena1 de prueba"
i=0
j=len(cadena)-1    
def guardar(cad):
    archivo = open('cadena.txt','a')
    archivo.write(cad)
    archivo.close()
    return 0

def leer():
    archivo = open('cadena.txt','r')
    texto=archivo.read()
    print("La cadena normal es = "+cadena)
    print("La cadena invertida es = "+texto)
    archivo.close() 
    
while i<len(cadena):
    cad=cadena[j]
    guardar(cad)
    i=i+1
    j=j-1
leer()