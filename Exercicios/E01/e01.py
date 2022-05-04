#Questao 1) Escreva um programa em Python que receba o salario de um funcionario e calcule
#seu imposto de renda. O imposto de renda e calculado da seguinte forma: o salario e multiplicado
#por uma porcentagem (aliquota) de acordo com faixas pre-estabelecidas. Desse valor e deduzido
#um valor fixo, tambem de acordo com faixas pre-estabelecidas.
#Sal´ario base Al´ıquota Dedu¸c˜ao
#Ate 1903,98 | Isento -
#De 1903,99 a 2826,65 | 7,5 | 142,80
#De 2826,66 a 3751,05 | 15,0 | 354,80
#De 3751,06 a 4664,68 | 22,5 | 636,13
#Acima de 4664,69 | 27,5 | 869,36
#
#salario = float(input("Informe o salario: "))
#if salario <= 1903.98:
#    print("Isento")
#elif salario >= 1903.99 and salario <= 2826.65:
#    print("Imposto de Renda = %.2f" % (abs(((salario * 0.075) - 142.80))))
#elif salario >= 2826.66 and salario <= 3751.05:
#    print("Imposto de Renda = %.2f" % ((salario * 0.15) - 354.80))
#elif salario >= 3751.06 and salario <= 4664.68:
#    print("Imposto de Renda = %.2f" % ((salario * 0.225) - 636.13))
#else: #salario > 4664.69:
#    print("Imposto de Renda = %.2f" % ((salario * 0.275) - 869.36))

#Questao 2) Escreva um programa em Python que leio um tamanho n e imprima o seguinte quadrado
#formado por asteriscos (para n = 4)
#* * * *
#*     *
#*     *
#* * * *
#tam = int(input("Informe o tamanho: "))
#topo_base = (("*" + " ") * tam) #topo e base do quadrado a ser desenhado = asterisco + um espaco, tamanho vezes
#topo_base = topo_base[:-1] #remove o ultimo caractere, obtido "indevidamente"
#desenhando o quadrado
#print(topo_base) #imprime a primeira linha (topo) do quadrado
#for i in range(2, tam): #for para desenhar o meio do quadrado. comeca em 2, pois, imprimimos a primeira linha antes do for e a ultima depois
#    print("*" + (" " * (len(topo_base)-2) + "*")) #o meio possuira um asterisco no comeco + (quantidade de espacos em braco no topo_base - 2) + um asterisco no final
#print(topo_base) #imprime a ultima linha (base) do quadrado

#Questao 3) Escreva uma funcao Python que calcule e retorne a media dos elementos de uma lista de
#numeros passada por parametro sem usar a funcoes avg e sum
#def media(lista):
#    soma = 0
#    cont = 0
#    for i in range (len(lista)):
#        soma = soma + lista[i]
#        cont += 1
#    return (soma/cont)
#lista = [2, 3, 3, 5, 7, 10]
#print(media(lista))

#Questao 4) Escreva uma funcao em Python que receba uma lista de inteiros e um valor e retorne a posicao
#do elemento caso ele tenha sido encontrado na lista ou -1 caso contrario. Nao e permitido o uso da funcao index()
#VERSAO ITERATIVA
#def indice(lista, valor):
#    for i in range(len(lista)):
#        if lista[i] == valor:
#            return i
#    return -1
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 6]
#print(indice(lista, 6))
#VERSAO RECUSIVA - permite lista com valores repetidos, retornando os indices de todos os valores ao inves de somente o primeiro
#ocorrencias = ["" for i in range (0, 10)]
#def indice_rec(lista, valor, ind):
#    print(ind)
#    if ind == len(lista):
#        if lista[ind-1] == valor:
#            ocorrencias[ind-1] = ind
#        return ocorrencias
#    elif lista[ind] == valor:
#        ocorrencias[ind] = ind
#        return indice_rec(lista, valor, ind=ind+1)
#    else:
#        return indice_rec(lista, valor, ind=ind+1)
#print(indice_rec(lista, 6, 0))

#Questao 5) Implemente uma classe Bomba em Python com os seguintes atributos:
# - tipo de combustivel
# - valor por litro
# - quantidade de combustivel
#e dois metodos:
# - abastecer_valor(valor) que recebe um valor em reais, exiba a quantidade de combustivel que foi colocada
#no veiculo e atualiza a quantidade de combustivel na bomba
# - abastecer_qtde(qtde) que recebe a quantidade (em litros) a ser abastecida, exibe o valor do abastecimento
#e atualiza a quantidade de combustivel na bomba
#class Bomba:
#    def __init__(self, tipo_combustivel, valor_litro, qntd_combustivel):
#        self.tipo_combustivel = tipo_combustivel
#        self.valor_litro = valor_litro
#        self.qntd_combustivel = qntd_combustivel
#    
#    def abastecer_valor(self, valor): #recebe um valor em reais, exibe a quantidade de combustivel que foi colocada no veiculo e atualiza qntd_combustivel na bomba
#        qntd_abastecida = valor / self.valor_litro
#        self.qntd_combustivel = self.qntd_combustivel - qntd_abastecida
#        print("Foram abastecidos: ", qntd_abastecida, "L")
#
#    def abastecer_qntd(self, qntd): #recebe a quantidade (em litros) a ser abastecida, exibe o valor do abastecimento e atualiza a quantidade de combustivel na bomba
#        valor_abastecido = self.valor_litro * qntd
#        self.qntd_combustivel = self.qntd_combustivel - qntd
#        print("Serao abastecidos: R$", valor_abastecido)
#
#bomba = Bomba("Gasolina", 5.00, 100)
#bomba.abastecer_valor(10)
#print(bomba.qntd_combustivel)
#bomba.abastecer_qntd(10)
#print(bomba.qntd_combustivel)