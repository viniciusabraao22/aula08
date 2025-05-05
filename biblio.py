def imprimirNome(n):
    print(f"ola: {n}")
def piramide(num):
    for x in range(1,num+1,1):
        for y in range(0,x):
            print(x,end=" ")
        print()
def vogais(texto):
    cont=0
    novoTexto=texto
    for x in novoTexto:
        if x in "aeiou,":
            cont+=1
    print(cont)
def estoque(p,q,v):
    total= q * v
    return p,total
def PN(valor):
    if valor>0:
        respota= "p"
    elif valor<0:
        respota= "N"
    else:
        respota="Z"
    return respota
def somar(*a):
    print(a)
def foma(*item):
    soma=0
    for x in item:
        soma+=x
    print(soma)
def textinho(poema):
    cont=0
    for x in range(len(poema)-1,-1,-1):
        if poema [x]!=" ":
            cont+=1
        print(poema[x],end=" ")
    print(cont)
def listas(lista):
    novalista=[]
    for x in lista:
        if x not in novalista:
            novalista.append(x)
    print(novalista)
def listas2(lista):
    novalista=[]
    novalista=set(lista)
    print(novalista)