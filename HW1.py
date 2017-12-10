#!/usr/bin/env python
#  -*- coding: utf-8 -*-


import numpy as np
from operator import mul

#######ESERCIZIO 1###########
#A = [1,1,1,3,1,1,1]
#A = [1,2,1,3,4,2,1,1]
#A = [1,2,1,4,1,1]

################################

def max_subarray(A):
     max_ending_here = max_so_far = A[0]
     for x in A[1:]:
         max_ending_here = max(x, max_ending_here * x)
         max_so_far = max(max_so_far, max_ending_here)
     return max_so_far

A=[-2,3,2,0.1]

#print max_subarray(A)

#https://www.youtube.com/watch?v=86CQq3pKSUw



###### ESERCIZIO 2 #######

G = {"F": ["B","G"],
     "B": ["A","D"],
     "A": [],
     "D": ["C","E"],
     "C": [],
     "E": [],
     "G": ["I"],
     "I": ["H"],
     "H": []}

def generaArchi(grafo):
    listaArchi = []
    for nodo in grafo:
        for adiacente in grafo[nodo]:
            listaArchi.append((nodo,adiacente))
    return listaArchi

#print generaArchi(G)

def contaFigli(nodo,grafo):
    somma = 0
    if  len(grafo[nodo]) == 0:
        return 0
    else :
        for figlio in grafo[nodo]:
            #print figlio
            somma += contaFigli(figlio,grafo)+1
        return somma

#print contaFigli("F",G) #conta tutti i figli discendenti

def subComp(grafo):
    dict={}
    for nodo in grafo :
        dict[nodo] = contaFigli(nodo,grafo)+1 #conta anche il nodo stesso
    return dict

#print subComp(G)

def trovaComponentiRimuovendoArco(arco,grafo):
    dict = subComp(grafo)
    return dict[arco[1]] , len(grafo)-dict[arco[1]]

#print trovaComponentiRimuovendoArco(("F","B"),G)

listaNodi = G.keys()
#print listaNodi

def listaHub(grafo):
    listaNodi = grafo.keys()
    for arco in generaArchi(grafo):
        C1,C2 = trovaComponentiRimuovendoArco(arco,grafo)
        #print "sto valutando l'arco"+str(arco)
        #print C1
        #print C2
        if C1 >= len(grafo)*0.5:
            #print C1
            listaNodi.remove(arco[0])
        if C2 >= len(grafo)*0.5:
            #print C2
            listaNodi.remove(arco[1])
        #print listaNodi
    return listaNodi[0]      #primo elemento hub di quelli che  trovi

#print listaHub(G)

################ ESERCIZIO 4 #####################


jobs = [(1,1) , (2,11) , (3,7) , (4,7)]

numeroMacchine = 2



def secondoElemento(tupla) :
    return tupla[1]

jobs = sorted(jobs,key=secondoElemento)

#[(1, 1), (3, 7), (4, 7), (2, 11)]

#print jobs.pop()
#print jobs


#macchinaGrande.append(maxItem)

while len(jobs) > 0:

    macchinaGrande = []
    jobs = sorted(jobs, key=secondoElemento)
    cmax = jobs[-1][1]
    ctotal = cmax*numeroMacchine

    while ctotal>0:
        maxItem = jobs.pop()
        if ctotal >= maxItem[1]:
            macchinaGrande.append(maxItem)
            ctotal = ctotal - maxItem[1]
            #print ctotal
        else:
            processoResiduo = (maxItem[0],ctotal)
            macchinaGrande.append(processoResiduo)
            ctotal = ctotal - processoResiduo[1]
            jobs.append((maxItem[0],maxItem[1]-processoResiduo[1])) #inserisco il job col valore rimanente
            #print ctotal
        #print ctotal
        if len(jobs) == 0:
            break


    #print "i jobs nella mia macchina sono : "
    #print macchinaGrande

    #print "i jobs ancora da schedulare sono : "
    #print jobs



 ###############ESERCIZIO 5#################


class Processo:
    i=0
    def __init__(self,waiting):
        Processo.i +=1
        self.i = Processo.i
        self.executing = 0
        self.waiting = waiting
        self.next = None
    def __str__(self):
        return "executing : "+str(self.executing)+", waiting : " +str(self.waiting)


class Macchina:
    i = 0
    def __init__(self, remaining):
        Macchina.i += 1
        self.i = Macchina.i
        self.processing = 0
        self.remaining = remaining
        self.next = None
    def __str__(self):
        return "processing : " + str(self.processing) + ", remaining : " + str(self.remaining)

def linkList(lista):
    prossimo = None
    for elem in reversed(lista):
        elem.next = prossimo
        prossimo = elem

def approximation(numeratore , denominatore):
    if numeratore%denominatore == 0:
        return numeratore/denominatore
    else: return numeratore/denominatore+1

def add(m , p):
    if m.remaining != 0: print "aggiunto processo "+str(p.i) + " di durata " + str(min([p.waiting,m.remaining]))+ " a macchina "+str(m.i)
    if  m.remaining >= p.waiting:
        m.remaining = m.remaining - p.waiting
        m.processing = m.processing + p.waiting
        p.executing = p.executing + p.waiting
        p.waiting = 0
    else:
         m.processing = m.processing + m.remaining
         p.executing = p.executing + m.remaining
         p.waiting = p.waiting-m.remaining
         m.remaining = 0

def funcRic(p,m):
    add(m,p)
    if p.waiting != 0:
        funcRic(p, m.next)



m = 3

durate = [10 , 8 , 7 , 5]

totalDuration = sum(durate)

processi = [Processo(durata) for durata in durate]

rapporto = approximation(totalDuration , m)

M = [Macchina(rapporto) for _ in range(m)]

linkList(processi)
linkList(M)

x = processi[0]
while x!= None:
    y = M[0]
    funcRic(x,y)
    x = x.next
for processo in processi:
    print processo
for macchina in M:
    print macchina










