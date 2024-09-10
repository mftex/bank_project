# Depósito, saque e extrato
from datetime import date
import time
extrato = {}
saldo = 0
qtd_saques = 0

def depositar(valor):
    global saldo
    if valor > 0:
        saldo = saldo + valor
        extrato.update({f'Depósito de R$ {valor} - {datetime.datetime.today()}':saldo})
    else:
        print(f'Valor inválido: {valor}')

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
        extrato.update({f'Saque de R$ {valor} - {datetime.datetime.today()}':saldo})
        qtd_saques += 1
    
