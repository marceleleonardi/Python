MENU = """
[A] - DEPÓSITO
[B] - SAQUE
[C] - EXTRATO
[D] - SAIR
"""

saldo = 0
limite_saque_diario = 500
saques_realizados = 0
extrato = []

while True:
    print(MENU)
    opcao = input("Escolha uma opção: ").upper()

    if opcao == "A":  # Depósito
        valor_deposito = float(input("Informe o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "B":  # Saque
        if saques_realizados < 3:
            valor_saque = float(input("Informe o valor do saque: "))
            if valor_saque <= saldo and valor_saque <= limite_saque_diario:
                saldo -= valor_saque
                saques_realizados += 1
                extrato.append(f"Saque: R$ {valor_saque:.2f}")
                print("Saque realizado com sucesso.")
            else:
                print("Operação de saque inválida.")
        else:
            print("Limite diário de saques atingido.")

    elif opcao == "C":  # Extrato
        print("##### EXTRATO #####")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimentacao in extrato:
                print(movimentacao)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "D":  # Sair
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida. Escolha uma opção válida do menu.")
        