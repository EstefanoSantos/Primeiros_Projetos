
menu = '''
    Bem Vindo ao nosso Banco. Para continuar,
    escolha a opção desejada.

    [1] Depositar
    [2] Saque
    [3] Extrato
    [4] Sair

'''


saldo = 0
valor_saque = 500
limite_saque = 3
saques_feitos = 0
extrato = ''

while True:

  opcao = int(input(menu))
  
  if opcao == 1:
    valor = float(input('Digite o valor à depositar: '))

    if valor > 0:
      saldo += valor
      extrato += f'Deposito: R$ {valor:.2f}\n'

    else:
      print('Operação falhou. Digite um valor válido.')  

  elif opcao == 2:

    valor = float(input('Digite a valor que deseja sacar: '))

    excedeu_saldo =  valor > saldo  

    excedeu_limite = valor > valor_saque

    excedeu_saques = saques_feitos >= limite_saque

    if excedeu_saldo:
      print('Operação falhou! Você não possui saldo suficiente.')

    elif excedeu_limite:
      print('Operação falhou! O valor de saque excede o limite.')

    elif excedeu_saques:
      print('Operação falhou! Limite de saques excedido.')

    elif valor > 0:
      saldo -= valor 
      extrato += f'Saque: R$: {valor:.2f}\n'
      saques_feitos += 1

    else:
      print('Operação falhou. Valor informado é invalido.') 

  elif opcao == 3:
    print('\n ---------Extrato--------')
    print('Não foram realizadas transações.' if not extrato else extrato)
    print(f'\nSaldo:{saldo:.2f}')
    print('\n --------Extrato---------')

  elif opcao == 4:
    break

  else:
    print('Operação inválida. Selecione novamente a operação desejada.')            
    

      


   