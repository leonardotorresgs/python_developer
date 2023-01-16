from time import sleep
import os
menu = '''
======== BANCO ========
[0] - Saque
[1] - Depósito
[2] - Extrato
[3] - Sair
=======================
'''
saldo = 0
limite = 500
extrato = ''
num_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    print(menu)
    op = int(input('Digite a operação desejada: '))

    if op == 0:
        excedeu_saque = num_saques >= LIMITE_DE_SAQUES
        if excedeu_saque:
            print('Limite de saques diários atingido')
        else:
            valor = float(input('Informe o valor do saque: '))

            excedeu_limite = valor > limite
            excedeu_saldo = valor > saldo
            
            if excedeu_limite:
                print('Operação falhou! Valor acima do limite')
            elif excedeu_saldo:
                print('Operação falhou! Saldo insuficiente')
            
            elif valor > 0:
                saldo -= valor
                num_saques += 1
                extrato += f'Saque: R${valor:.2f}\n'
                print(f'\nSaque de R${valor:.2f} efetuado com sucesso!')
            else:
                print('Operação falhou! Valor informado é inválido')
            print(f'Redirecionando em ', end='')
            for i in range(5, 0, -1):
                print(f'{i}...')
                sleep(0.8)
            os.system("cls")

    elif op == 1:
        valor = float(input('Informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
            print(f'\nDepósito de R${valor:.2f} efetuado com sucesso!')
        else:
            print('Operação falhou! Valor informado é inválido')

        print(f'Redirecionando em ', end='')
        for i in range(5, 0, -1):
           print(f'{i}...')
           sleep(0.8)
        os.system("cls")

    elif op == 2:
        if not extrato:
            print('\nNão foram realizadas movimentações')
        else:    
            titulo = ' EXTRATO '
            print()
            print(titulo.center(23,"="))
            print(extrato)
            print(f'Saldo: R${float(saldo):.2f}')
            print("="*23)
        input('\nTecle Enter para continuar...')
        os.system("cls")

    elif op == 3:
        print('\nObrigado por utilizar nossos serviços!')
        sleep(2)
        os.system("cls")
        break

    else:
        print('Operação inválida! Por favor selecione novamente a operação desejada')
        print(f'Redirecionando em ', end='')
        for i in range(5, 0, -1):
           print(f'{i}...')
           sleep(0.8)
        os.system("cls")
        