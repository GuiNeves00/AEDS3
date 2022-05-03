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
tam = int(input("Informe o tamanho: "))

topo_base = (("*" + " ") * tam) #topo e base do quadrado a ser desenhado = asterisco + um espaco, tamanho vezes
topo_base = topo_base[:-1] #remove o ultimo caractere, obtido "indevidamente"

#desenhando o quadrado
print(topo_base) #imprime a primeira linha (topo) do quadrado
for i in range(2, tam): #for para desenhar o meio do quadrado. comeca em 2, pois, teremos um asterisco no comeco e outro no final
    print("*" + (" " * (len(topo_base)-2) + "*")) #o meio possuira um asterisco no comeco + (quantidade de espacos em braco no topo_base - 2) + um asterisco no final
print(topo_base) #imprime a ultima linha (base) do quadrado