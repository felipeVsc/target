listaEstados = ["SP","RJ","MG","ES","OUTROS"]
lista = [67836.43,36678.66,29229.88,27165.48,19849.53]

def calcularMax(lista):
    return sum(lista)

def calcularPercentual(lista,listaEstados):
    total = calcularMax(lista)
    for index,estado in enumerate(listaEstados):
        formula = (lista[index]/total)*100
        print(f"Estado: {estado}, Contribuição: {formula}")

calcularPercentual(lista,listaEstados)
