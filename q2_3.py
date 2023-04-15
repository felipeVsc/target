'''
Esse código utiliza a biblioteca Pandas para realizar as operações. Necessário instalação dela por meio do seguinte comando:

pip3 install pandas
'''

import pandas as pd

df = pd.read_json('dados.json')

def calcularMinIncluindoZeros(df):
    return min(df.valor)

def calcularMinSemIncluirZeros(df):
    dfLimpo = df[df.valor>0]
    return min(dfLimpo.valor)

def calcularMax(df):
    return max(df.valor)

def calcularMedia(df):
    dfLimpo = df[df.valor>0]
    media = sum(dfLimpo.valor)/len(dfLimpo.valor)
    return media

def calcularQntDiasSuperiorMedia(df):
    media = calcularMedia(df)
    dfNovo = df[df.valor>media]
    return len(dfNovo.valor)

print(f'Menor Faturamento incluindo zeros: {calcularMinIncluindoZeros(df)}')
print(f'Menor Faturamento excluindo zeros: {calcularMinSemIncluirZeros(df)}')
print(f'Maior valor de faturamento: {calcularMax(df)}')
print(f'Quantidade de dias em que o valor do faturamento superou a média: {calcularQntDiasSuperiorMedia(df)}')
