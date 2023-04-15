"""
Essa versão não utiliza a biblioteca Pandas nem outras funções prontas. Apenas a lib json para ler o arquivo Json.

"""
import json

dados = open('dados.json')
json_dados = json.load(dados)

listaValores = [json_dados[x]['valor'] for x in range(30)]
listaValoresSemZero = [listaValores[x] for x in range(30) if listaValores[x]>0]

def calcularMin(lista):
    valorMin = 9999999
    for x in lista:
        if x<valorMin:
            valorMin = x
        
    return valorMin

def calcularMax(lista):
    valorMax = 0
    for x in lista:
        if x>valorMax:
            valorMax = x
        
    return valorMax

def calcularSoma(lista):
    soma = 0
    for x in lista:
        soma+=x
    return soma

def calcularMedia(lista):
    media = calcularSoma(lista)/len(lista)
    return media

def calcularQntDiasSuperiorMedia(lista):
    media = calcularMedia(lista)
    
    qntDias = 0
    for x in lista:
        if x>media:
            qntDias+=1

    return qntDias

print(f'Menor Faturamento incluindo zeros: {calcularMin(listaValores)}')
print(f'Menor Faturamento excluindo zeros: {calcularMin(listaValoresSemZero)}')
print(f'Maior valor de faturamento: {calcularMax(listaValores)}')
print(f'Quantidade de dias em que o valor do faturamento superou a média: {calcularQntDiasSuperiorMedia(listaValoresSemZero)}')