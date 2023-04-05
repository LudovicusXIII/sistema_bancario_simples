import datetime
menu = """
[ D ] Depositar
[ S ] Sacar
[ E ] Extrato
[ Q ] Sair
"""


saldo = 0
limite = float(500)
extratos_bancarios = {
    "Extrato de Deposito":[],
    "Extrato de Saques":[],
    "Extrato Geral":[]
}
numeros_saques = 0
LIMITE_SAQUES = 3
data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S') #DATA atual e hora

while True:
    opcao = input(menu)

    if opcao.upper() == 'D':
        valor_deposito = float(input('Valor de deposito: R$ '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extratos_bancarios['Extrato de Deposito'].append(f'Data: {str(data)} - Deposito: R$ {valor_deposito:.2f}')
            extratos_bancarios['Extrato Geral'].append(f'Data: {str(data)} - Deposito: R$ {valor_deposito:.2f}')
        else:
            print('A operação falhou. O valor informado é inválido')

    elif opcao.upper() == 'S':
        if numeros_saques < LIMITE_SAQUES:
            valor_saque = float(input('Valor de saque: R$ '))
            if valor_saque > 0:
                if valor_saque <= limite and valor_saque <= saldo:
                    extratos_bancarios['Extrato de Saques'].append(f'Data: {str(data)} - Saque: R$ {valor_saque:.2f}')
                    extratos_bancarios['Extrato Geral'].append(f'Data: {str(data)} - Saque: R$ {valor_saque:.2f}')
                    print('Saque Realizado com Sucesso!')
                    numeros_saques+=1
                else:
                    print(f'Não foi possível realizar o saque.')
            else:
                print('A operação falhou. VO valor do saque excede o limite!')
        else:
            print('Operação falhou. Limite diário de saques atingido')

    elif opcao.upper() == 'E':
      print("\n===========EXTRATO===========\n")
      print("Não foram realizadas movimentações" if not extratos_bancarios else extratos_bancarios)
      print(f"\nsaldo: R$ {saldo:.2f}")
      print("===========================")

    elif opcao.upper()  ==  "Q":
        break
    
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')
print('Tenha um bom dia!')