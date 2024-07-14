'''
Tentar prever possíveis incosistências durante a execução deste código
por parte do usuário
'''

nome = input('Digite seu nome: ')
if nome.isnumeric() == True:
    print('Você digitou um número. Escreva seu nome corretamente!')
    exit()
elif nome.isspace() == True:
    print('Você digitou um espaço em branco. Escreva seu nome corretamente!')
    exit()
elif len(nome) == 0:
    print('Você digitou nada. Escreva seu nome corretamente!')


salario = int(input('Digite seu salário: '))
if salario.isnumeric() == False:
    print('Você digitou um texto. Escreva seu salario corretamente!')
    exit()
elif salario.isspace() == True:
    print('Você digitou um espaço em branco. Escreva seu salario corretamente!')
    exit()
elif len(salario) == 0:
    print('Você digitou nada. Escreva seu salario corretamente!')




# bonus_inicial = float(input('Digite o bônus: '))
# bonus_inicial = bonus_inicial * 100
# bonus_final = 1 + bonus_inicial
# novo_salario = salario * bonus_final
# acrescimo = novo_salario - salario
# print(f'Neste ano tivemos um bônus de {bonus_inicial}%!\nParabéns, {nome}! Você irá receber {novo_salario} reais neste mês.\nUm acréscimo de {acrescimo} reais!')
