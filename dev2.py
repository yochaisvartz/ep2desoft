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

# exercicio 5
def calcula_pontos_soma(listadados):
    soma = 0
    for dado in listadados:
        soma += dado
    return soma

# exercicio 6
def calcula_pontos_sequencia_baixa(listadados):
    for dado in listadados:
        if dado == 1:
            for dado in listadados:
                if dado == 2:
                    for dado in listadados:
                        if dado == 3:
                            for dado in listadados:
                                if dado == 4:
                                    return 15
        if dado == 2:
            for dado in listadados:
                if dado == 3:
                    for dado in listadados:
                        if dado == 4:
                            for dado in listadados:
                                if dado == 5:
                                    return 15
        if dado == 3:
            for dado in listadados:
                if dado == 4:
                    for dado in listadados:
                        if dado == 5:
                            for dado in listadados:
                                if dado == 6:
                                    return 15
    else:
        return 0

# exercicio 7
def calcula_pontos_sequencia_alta(listadados):
    for dado in listadados:
        if dado == 1:
            for dado in listadados:
                if dado == 2:
                    for dado in listadados:
                        if dado == 3:
                            for dado in listadados:
                                if dado == 4:
                                    for dado in listadados:
                                        if dado == 5:
                                            return 30
        if dado == 2:
            for dado in listadados:
                if dado == 3:
                    for dado in listadados:
                        if dado == 4:
                            for dado in listadados:
                                if dado == 5:
                                    for dado in listadados:
                                        if dado == 6:
                                            return 30
    return 0
def calcula_pontos_full_house (listados):
    for i in range(len(listados)):
        cont1=0
        cont2=0
        for j in range(len(listados)):
            if listados[j] == listados[l]:
                cont+=1
            if cont1==3:
                for t in range(len(listados)):
                    if listados[t] != listados[l]:
                        for k in range(len(listados)):
                            if listados[k] == listados[t]
                            cont2+=1
            if cont2 == 2:
                soma=0
                for dado in listados:
                    soma += dado
                return soma
    return 0

    

                        

                                    


        
        

        