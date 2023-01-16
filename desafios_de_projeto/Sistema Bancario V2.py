from time import sleep
import os

def saque(*, valor, limite, saldo, extrato, num_saques):

    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo

    if excedeu_limite:
        print('Operação falhou! Valor acima do limite')
        return saldo, extrato, num_saques
    elif excedeu_saldo:
        print('Operação falhou! Saldo insuficiente')
        return saldo, extrato, num_saques
    elif valor > 0:
        saldo -= valor
        num_saques += 1
        extrato += f'Saque: R${valor:.2f}\n'
        print(f'\nSaque de R${valor:.2f} efetuado com sucesso!')
        return saldo, extrato, num_saques
    else:
        print('Operação falhou! Valor informado é inválido')
        return saldo, extrato, num_saques

def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'
        print(f'\nDepósito de R${valor:.2f} efetuado com sucesso!')
        return saldo, extrato
    else:
        print('Operação falhou! Valor informado é inválido')

def extrato_func(saldo, /, *, extrato):
    titulo = ' EXTRATO '
    print()
    print(titulo.center(23,"="))
    print(extrato)
    print(f'Saldo: R${float(saldo):.2f}')
    print("="*23)

def criar_usuario(usuarios):
    usuario = {}

    usuario['nome'] = input("Nome: ")
    usuario['nasc'] = input("Data de nascimento: ")
    while True:
        cpf = int(input("CPF(somente números): "))
        indice_cpf_cadastrados = {d['CPF']: d for d in usuarios}
        if cpf in indice_cpf_cadastrados:
            print("ERRO: CPF já cadastrado.")
            op = input("\n[0] - Digitar novamente\n[1] - Voltar para o menu\n\nDigite sua opção: ")
            if op == 1:
                return usuarios
                break
        else:
            usuario['CPF'] = cpf
            usuario['endereco'] = input("Endereço: ")
    
            usuarios.append(usuario)

            print(f"\nUsuário adicionado com sucesso! Seja bem vindo(a) {usuario['nome']} :)\n")
            return usuarios
'''(rua, nro, bairro, cidade/sigla estado)
'''

def criar_cc(contas, num_cc, usuarios):
    conta = {"agencia": "0001",}
    num_cc += 1
    conta["num_cc"] = num_cc

    while True:
        cpf = int(input("Digite o CPF a ser vinculado(somente numeros): "))
        if not usuarios:
            print("Impossível criar conta, nenhum usuário registrado.")
            input('\nTecle Enter para continuar e criar usuário...')
            os.system("cls")
            usuarios = criar_usuario(usuarios)
        else:
            indice_pessoas_por_cpf = {d['cpf']: d for d in usuarios}
            for i in indice_pessoas_por_cpf:
                if i == cpf:
                    conta["usuario"] = cpf
                    contas.append(conta)
                    print(f"\nConta {conta['agencia']} {conta['num_cc']} cadastrada com sucesso!")
                    return contas, num_cc
                    break
                else:
                    print("Usuário não encontrado, digite um CPF cadastrado para prosseguir.")
                    op = int(input("[0] - Digitar novamente\n[1] - Criar usuário\n\nDigite sua opção: "))
                    if op == 1:
                        os.system("cls")
                        usuarios = criar_usuario(usuarios)

def redireciona():
    print(f'Redirecionando em ', end='')
    for i in range(5, 0, -1):
        print(f'{i}...')
        sleep(0.8)
    os.system("cls")


menu = '''
======== BANCO ========

[0] - Saque
[1] - Depósito
[2] - Extrato
[3] - Criar usuário
[4] - Criar conta corrente 
[5] - Sair

=======================
'''
saldo = 0
limite = 500
extrato = ''
num_saques = 0
LIMITE_DE_SAQUES = 3
usuarios = []
contas = []
num_cc = 0

while True:
    print(menu)
    op = int(input('Digite a operação desejada: '))

    if op == 0:
        excedeu_saque = num_saques >= LIMITE_DE_SAQUES
        if excedeu_saque:
            print('Limite de saques diários atingido')
        else:
            valor = float(input('Informe o valor do saque: '))
            (saldo, extrato, num_saques) = saque(valor=valor, limite=500, saldo=saldo, extrato=extrato, num_saques=num_saques)

            redireciona()        
            
    elif op == 1:
        valor = float(input('Informe o valor do depósito: '))
        (saldo, extrato) = deposito(valor, saldo, extrato)

        redireciona()

    elif op == 2:
        if not extrato:
            print('\nNão foram realizadas movimentações')
        else:
            extrato_func(saldo, extrato=extrato) 

        input('\nTecle Enter para continuar...')
        os.system("cls")

    elif op == 3:
        usuarios = criar_usuario(usuarios)
        redireciona()

    elif op == 4:
        (contas, num_cc) = criar_cc(contas, num_cc, usuarios)
        redireciona()

    elif op == 5:
        print('\nObrigado por utilizar nossos serviços!')
        sleep(2)
        os.system("cls")
        break

    else:
        print('\nOperação inválida! Por favor selecione novamente a operação desejada')
        redireciona()
