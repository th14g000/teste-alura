#! python3
# -*- coding: utf-8 -*-
# Obs: Teste com titulo
# Calculando numeros primos
# Código abaixo - Alteração 3


print('Descubra se um número é primo ou não')
print('Numeros de 1 a 100')
numeros = list(range(0, 101))

try:
    n1 = int(input('Digite o número: '))
    if (n1 >= 1):
        if (n1 == 1):
            print('Não é um número primo!')
        elif (n1 == 2 or n1 == 3 or n1 == 5):
            print('É um número primo!')
        elif (numeros[::2]):
            print('Não é um número primo!')
        elif (numeros[::3]):
            print('Não é um número primo!')
        elif (numeros[::5]):
            print('Não e um número primo!')
        else:
            print('É um número primo')

except ValueError:
    print('Favor, entrar somente com números!')




