# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:00:12 2023

@author: Nicolas Marr
"""

def cargar():
    archivo = open("g05_60.txt", "r")

    cantidadNodos, cantidadVertices = archivo.readline().split()
    grafo = [[0 for k in range(int(cantidadNodos))] for k in range(int(cantidadNodos))]

    for _ in range(int(cantidadVertices)):
        vertice = archivo.readline().split()
        grafo[int(vertice[0])-1][int(vertice[1])-1] = 1

    archivo.close()
    return grafo

cargar()


#for i in cargar():
        #print(i)