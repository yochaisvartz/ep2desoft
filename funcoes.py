# exercicio 1
import random
def rolar_dados(n):
    listadados = []
    for i in range(n):
        numero = random.randint(1,6)
        listadados.append(numero)
    return listadados

# exercicio 2
def guardar_dado (listadados, dadosguardados, n):
    dadosrolados = []
    for i in range(len(listadados)):
        if i != n:
            dadosrolados.append(listadados[i])
    dadoarmazenado = listadados[n]
    dadosguardados.append(dadoarmazenado)
    listastatus = [dadosrolados, dadosguardados]
    return listastatus