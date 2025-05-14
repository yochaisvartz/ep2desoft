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
#exercicio 8
def calcula_pontos_full_house(lista_dados):
    for dado_principal in lista_dados:
        quantidade_principal = lista_dados.count(dado_principal)
        
        if quantidade_principal == 3:
            for outro_dado in lista_dados:
                if outro_dado != dado_principal and lista_dados.count(outro_dado) == 2:
                    soma = 0
                    for dado in lista_dados:
                        soma += dado
                    return soma
                    
        elif quantidade_principal == 2:
            for outro_dado in lista_dados:
                if outro_dado != dado_principal and lista_dados.count(outro_dado) == 3:
                    soma = 0
                    for dado in lista_dados:
                        soma += dado
                    return soma
                    
    return 0

#exercicio 9
def calcula_pontos_quadra(lista_dados):
    for dado in lista_dados:
        quantidade = lista_dados.count(dado)
        if quantidade >= 4:
            soma = 0
            for valor in lista_dados:
                soma += valor
            return soma
    return 0

    #exercicio 10
def calcula_pontos_quina(listadados):
    dicsoma = {}
    for i in range(len(listadados)):
        if listadados[i] in dicsoma:
            dicsoma[listadados[i]] += 1
        else:
            dicsoma[listadados[i]] = 1  
    for numero in dicsoma:    
        if dicsoma[numero] >= 5:
            return 50
    return 0
    #exercicio 11
def calcula_pontos_regra_avancada(listadados):
    newdic = {}
    newdic['cinco_iguais'] = calcula_pontos_quina(listadados)
    newdic['full_house'] = calcula_pontos_full_house(listadados)
    newdic['quadra'] = calcula_pontos_quadra(listadados)
    newdic['sem_combinacao'] = calcula_pontos_soma(listadados)
    newdic['sequencia_alta'] = calcula_pontos_sequencia_alta(listadados)
    newdic['sequencia_baixa'] = calcula_pontos_sequencia_baixa(listadados)
    return newdic
    #exercicio 12
def faz_jogada(dados, categoria, cartela_de_pontos):
    if str(categoria) in ['1', '2', '3', '4', '5', '6']:
        categoria_num = int(categoria)
        pontos = calcula_pontos_regra_simples(dados)[categoria_num]
        cartela_de_pontos['regra_simples'][categoria_num] = pontos
    else:
        pontos = calcula_pontos_regra_avancada(dados)[categoria]
        cartela_de_pontos['regra_avancada'][categoria] = pontos
    return cartela_de_pontos

# Exercicio 13
from funcoes import imprime_cartela
from funcoes import rolar_dados
from funcoes import guardar_dado
from funcoes import remover_dado
from funcoes import calcula_pontos_regra_simples
from funcoes import calcula_pontos_soma
from funcoes import calcula_pontos_sequencia_baixa
from funcoes import calcula_pontos_sequencia_alta
from funcoes import calcula_pontos_full_house
from funcoes import calcula_pontos_quadra
from funcoes import calcula_pontos_quina
from funcoes import calcula_pontos_regra_avancada
from funcoes import faz_jogada

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
imprime_cartela(cartela)

todas_categorias = ['1', '2', '3', '4', '5', '6', 'sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']
categorias_utilizadas = []
contador = 0

while contador < 12:
    numero_dados = 5
    dados_rolados = rolar_dados(numero_dados)
    dados_guardados = []

    print('Dados rolados:', dados_rolados)
    print('Dados guardados:', dados_guardados)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    escolha = input(">")

    numero_rerrolagens = 0
    while escolha != '0':
        if escolha == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice_guardar = int(input(">"))
            while indice_guardar >= len(dados_rolados):
                print("Índice inválido. Digite o índice do dado a ser guardado (0 a 4):")
                indice_guardar = int(input(">"))
            guardar_dado(dados_rolados, dados_guardados, indice_guardar)
            print('Dados rolados:', dados_rolados)
            print('Dados guardados:', dados_guardados)

        elif escolha == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice_remover = int(input(">"))
            while indice_remover >= len(dados_guardados):
                print("Índice inválido. Digite o índice do dado a ser removido (0 a 4):")
                indice_remover = int(input(">"))
            remover_dado(dados_rolados, dados_guardados, indice_remover)
            print('Dados rolados:', dados_rolados)
            print('Dados guardados:', dados_guardados)

        elif escolha == '3':
            if numero_rerrolagens == 2:
                print("Você já usou todas as rerrolagens.")
            else:
                numero_rerrolagens += 1
                numero_dados = len(dados_rolados)
                dados_rolados = rolar_dados(numero_dados)
            print('Dados rolados:', dados_rolados)
            print('Dados guardados:', dados_guardados)

        elif escolha == '4':
            imprime_cartela(cartela)

        else:
            print("Opção inválida. Tente novamente.")

        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        escolha = input(">")

    print("Digite a combinação desejada:")
    categoria_escolhida = input(">")

    while categoria_escolhida in categorias_utilizadas or categoria_escolhida not in todas_categorias:
        if categoria_escolhida in categorias_utilizadas:
            print("Essa combinação já foi utilizada.")
        else:
            print("Combinação inválida. Tente novamente.")
        categoria_escolhida = input(">")

    categorias_utilizadas.append(categoria_escolhida)

    todos_dados = dados_rolados + dados_guardados
    cartela = faz_jogada(todos_dados, categoria_escolhida, cartela)

    contador += 1

imprime_cartela(cartela)

pontuacao_total = 0
for tipo, pontuacoes in cartela.items():
    for valor in pontuacoes.values():
        pontuacao_total += int(valor)

if sum(cartela['regra_simples'].values()) >= 63:
    pontuacao_total += 35

print("Pontuação total:", str(pontuacao_total))

    

                        

                                    

        
        

        
