# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# numero_01 = int(input('Digite um número inteiro: '))
# numero_02 = int(input('Digite outro número inteiro: '))
# resultado = numero_01 + numero_02
# print(f'O resultado da soma é {resultado}')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero_01 = int(input('Digite um número inteiro: '))
# resultado = numero_01 % 5
# print(f'O resto da divisão do número digitado por 5 é {resultado}')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# numero_01 = int(input('Digite um número inteiro: '))
# numero_02 = int(input('Digite outro número inteiro: '))
# resultado = numero_01 * numero_02
# print(f'O resultado da multiplicação é {resultado}')

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numero_01 = int(input('Digite um número inteiro: '))
# numero_02 = int(input('Digite outro número inteiro: '))
# resultado = numero_01 // numero_02
# print(f'O resultado inteiro da divisão é {resultado}')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero_01 = int(input('Digite um número inteiro: '))
# resultado = numero_01 ** 2
# print(f'O quadrado do número é {resultado}')

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_01 = float(input('Digite um número decimal: '))
# numero_02 = float(input('Digite outro número decimal: '))
# resultado = numero_01 + numero_02
# print(f'O resultado da soma é {resultado}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero_01 = float(input('Digite um número decimal: '))
# numero_02 = float(input('Digite outro número decimal: '))
# DIVISAO_METADE = 2
# resultado = (numero_01 + numero_02) / DIVISAO_METADE
# print(f'O resultado da média é {resultado}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# numero_01 = float(input('Digite um número que irá servir como base: '))
# numero_02 = float(input('Digite um número que irá servir como expoente: ')    )
# resultado = numero_01 ** numero_02
# print(f'O resultado da potência é {resultado}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# grau_celcius = float(input('Digite um a temperatura em graus Celcius: '))
# grau_fahrenheit = (grau_celcius * 9/5) + 32
# print(f'O temperatura em graus Fahrenheit é {grau_fahrenheit}')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# numero_01 = int(input('Digite um número inteiro: '))
# numero_02 = int(input('Digite outro número inteiro: '))
# if numero_01 == numero_02:
#     print('Os números digitados são iguais!')

# else:
#     print('Os números digitados são diferentes!')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# numero_01 = int(input('Digite um número inteiro: '))
# numero_02 = int(input('Digite outro número inteiro: '))
# resultado_diferenca = (numero_01 != numero_02)

# if numero_01 != numero_02:
#     print(f'Os números digitados são diferentes!\n{resultado_diferenca}')

# else:
#     print(f'Os números digitados são iguais!\n{resultado_diferenca}')


# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     grau_celcius = float(input('Digite um a temperatura em graus Celcius: '))
#     grau_fahrenheit = (grau_celcius * 9/5) + 32
#     print(f'O temperatura em graus Fahrenheit é {grau_fahrenheit}')
# except ValueError:
#     print('Por favor, digite um número válido!')

# 22: Verificador de Palíndromo
try:
    entrada = input('Digite uma frase ou palavra: ')
    if isinstance(entrada, str):
        entrada_formatada = entrada.replace(' ', '').lower()
        if entrada_formatada == entrada_formatada[:: -1]:
            print('É um palíndromo')
        else:
            print('Não é um palíndromo')
except:
    print('Entrada inválida. Digite uma frase ou palavra!')

# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
