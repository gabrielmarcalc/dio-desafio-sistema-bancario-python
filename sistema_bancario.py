
menu = '''
-------------------- BEM-VINDO! --------------------
Digite a opção que corresponde à operação desejada:
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
Opção: '''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("\nInforme o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += "Depósito: R$ {:0.2f}\n".format(valor)
            print("\n\033[32mDepósito realizado com sucesso! Cheque seu extrato.\033[m\n\n")
        else:
            print("\n\033[31mA operação falhou! O valor informado é inválido.\033[m\n\n")
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("\nInforme o valor do saque: R$ "))
            if valor > 0:
                if valor <= limite:
                    if valor <= saldo:
                        saldo -= valor
                        extrato += "Saque: R$ {:0.2f}\n".format(valor)
                        numero_saques += 1
                        print("\n\033[32mSaque realizado com sucesso! Cheque seu extrato.\033[m\n\n")
                    else:
                        print("\n\033[31mA operação falhou! Seu saldo é insuficiente.\033[m\n\n")
                else:
                    print("\n\033[31mA operação falhou! O limite máximo por saque é de R$ {:0.2f}.\033[m\n\n".format(limite))
            else:
                print("\n\033[31mA operação falhou! O valor informado é inválido.\033[m\n\n")
        else:
            print("\n\033[31mA operação falhou! Número máximo de saques diários atingido.\033[m\n\n")
    elif opcao == "e":
        print("\n--------------- EXTRATO ---------------")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print("\nSaldo atual: R$ {:0.2f}".format(saldo))
        print("---------------------------------------\n")
    elif opcao == "q":
        print("\nObrigado por usar o sistema!\n\n")
        break
    else:
        print("\n\033[31mA operação falhou! Escolha uma opção válida.\033[m\n\n")