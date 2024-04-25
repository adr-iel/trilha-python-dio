menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Opção escolhida: Depósito")
        valor_depositado = float(input("Digite a quantidade que deseja depositar:"))
        if valor_depositado >= 0:
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("Opção escolhida: Saque")
        valor_saque = float(input("Digite o valor que você deseja sacar: "))

        excedeu_limite = valor_saque > limite
        excedeu_saldo = valor_saque > saldo
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_limite:
            print("Operação falhou! Você ultrapassou seu limite por saques.")
        
        elif excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_saques:
            print("Operação falhou! Você excedeu seu número de saques por dia")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques+=1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("Opção escolhida: Extrato")
        print()
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")  

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
