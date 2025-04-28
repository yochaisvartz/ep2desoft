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

# exercicio 3
def remover_dado (listadados, dadosguardados, n):
    newguardados = []
    for i in range(len(dadosguardados)):
        if i != n:
            newguardados.append(dadosguardados[i])
        else:
            listadados.append(dadosguardados[i])
    listastatus = [listadados, newguardados]
    return listastatus

# exercicio 4
def calcula_pontos_regra_simples(listadados):
    dicpontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in listadados:
        if dado in listadados:
            n = dado
            dicpontos[n] += dado
        else:
            dicpontos[n] = dado
    return dicpontos
        