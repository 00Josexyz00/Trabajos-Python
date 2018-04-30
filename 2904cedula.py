# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:36:00 2018

@author: ESFOT
"""

def creartxt():
    archivo=open('cedula.txt','w')
    archivo.close()

print("José Cortez")

creartxt()
cedula=input("Ingresa tu numero de cedula: \n")

    
def guardartxt(cedula):
    archivo=open('cedula.txt','a')
    archivo.write(cedula)
    archivo.close()
    
i=0
def leertxt():
    archivo=open('cedula.txt','r')
    archivo1=archivo.read()
    print("El numero de cedula es = "+archivo1)
    archivo.close()
    
guardartxt(cedula)
leertxt()