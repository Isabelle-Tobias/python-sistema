# Sistema Bancário: depositar, sacar e ver extrato:

usuario = input("Digite seu nome de usuário: \n")
senha = input("Digite sua senha: \n")
sair = False
saldo = 0.00
vl_deposito = 0.00
vl_saque = 0.00
qt_saque = 0
extrato = []

menu = f'''
    ------------------------------------------
    Olá, {usuario}!

    Seja bem-vindo(a) ao nosso menu:
    [1] - Depositar
    [2] - Sacar
    [3] - Ver extrato Bancário
    [0] - Sair
    
    ------------------------------------------
'''

while (not sair):
    print(menu)
    opcao = input("Digite o número da opção que deseja acessar: ")

    if (opcao == "1"):
        vl_deposito = float(input("Digite o valor do depósito (R$): "))
        if (vl_deposito <= 0):
            print("Valor inválido. O depósito não pode ser realizado!")
        else:
            saldo += vl_deposito
            extrato.append(f"Depósito de R${vl_deposito:.2f}")
            print("Depósito realizado com sucesso!\n")

    elif (opcao == "2"):
        if (qt_saque > 2):
            print("Você já atingiu o limite máximo de saque diário!\n")
        else:
            vl_saque = float(input("Digite o valor do saque (R$): "))
            if (vl_saque > 500.00):
                print(
                    "O valor do saque não pode ser maior do que R$ 500,00. Por favor, tente novamente.\n")
            elif (vl_saque > saldo):
                print("Você não tem saldo suficiente para fazer essa operação!\n")
            else:
                saldo -= vl_saque
                extrato.append(f"Saque de R${vl_saque:.2f}")
                print("Saque realizado com sucesso!\n")
                qt_saque += 1

    elif (opcao == "3"):
        print("Extrato Bancário: \n")
        for status in extrato:
            print(f"{status}\n")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif (opcao == "0"):
        sair = True

    else:
        print("Opção inválida. Tente novamente.\n")

print("Obrigado por utilizar o sistema. Até mais :)\n\n")
