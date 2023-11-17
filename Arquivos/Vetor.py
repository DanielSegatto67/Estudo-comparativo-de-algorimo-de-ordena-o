import numpy as n
def preencheVetor(tam):
    arr = []
    for x in range(0, tam):
        arr.append(x)
    return arr

def randomizaVetor(arr):
    n.random.shuffle(arr)

def preencheVetorDesc(tam):
    arr = []
    c = tam-1
    while c>=0:
        arr.append(c)
        c-=1
    return arr