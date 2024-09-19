# Depósito, saque e extrato
from datetime import date, datetime
import time
movimentacoes = []
saldo = 0
qtd_saques = 0
usuarios = []
contas = {}

def cadastrar_usuario(nome):
    global usuarios
    if nome not in usuarios:
        usuarios.append(nome)
        return '\n Usuário cadastrado com sucesso\n'
    else:
        return '\n Usuário já existe! \n'

def cadastrar_conta(usuario):
    global contas 
    if usuario in contas.keys():
        return '\n Usuário já possui conta cadastrada \n'
    else:
        if len(contas) == 0:
            contas.update({usuario:1})
        else:
            contas.update({usuario:max(contas.values())})
        return '\n Conta cadastrada com sucesso!\n '

def depositar(usuario, valor):
    global saldo
    global contas
    if valor > 0:
        if usuario in contas.keys():
            saldo = saldo + valor
            movimentacoes.append(f'Depósito na conta de: {usuario} de R$ {valor} - {datetime.today()} - Saldo: {saldo}')
            return '\nDepósito realizado com sucesso!\n'
        else:
            return '\nUsuário e/ou conta não localizado\n'
    else:
        return 'Valor inválido'

def sacar(valor):
    global saldo
    global qtd_saques
    if qtd_saques >= 3:
        print('Operação excede o limite diário de 3 saques')
    elif valor > 500:
        print('Valor excede o limite diário de R$ 500,00!')
    elif valor > saldo:
        print('Saldo insuficiente')        
    else:
        saldo -= valor
        movimentacoes.update({f'Saque de R$ {valor} - {datetime.today()}':saldo})
        qtd_saques += 1

def extrato(usuario):
    global movimentacoes

    if usuario not in contas.keys():
        return 'Usuário e/ou conta não encontrado'
    else:
        results = [user for user in movimentacoes if usuario in user]
    
    if len(results) > 0:
        return results
    else:
        return '\nNão existem movimentações para o usuário\n'


while True:
    print('===Bem-vindo!===')
    print('===Selecione uma opção abaixo: ===')
    print('Cadastrar um usuário: 1')
    print('Cadastrar uma conta: 2')
    print('Efetuar um depósito: 3')
    print('Efetuar um saque: 4')
    print('Emitir extrato: 5')
    print('Sair: S')
    option = input('Digite a opção: ')

    if option.upper() == 'S':
        break

    if option == '1':
        user = input('Informe o nome de usuário que deseja cadastrar: ')

        exec = cadastrar_usuario(user)
        print(exec)

    if option == '2':
        user = input('Informe o nome de usuário que deseja criar uma conta: ')

        exec = cadastrar_conta(user)
        print(exec)

    if option == '3':
        user = input('Informe o usuário para o qual deseja efetuar o depósito: ')
        valor = float(input('Informe o valor do depósito: '))

        exec = depositar(user, valor)
        print(exec)

    if option == '5':
        user = input('Informe o usuário para o qual deseja emitir o extrato: ')

        exec = extrato(user)
        print(exec)