import colorama

# Cores para o menu principal
colorama.init()
cores = {'menu': colorama.Fore.CYAN, 'opcao': colorama.Fore.YELLOW, 'valor': colorama.Fore.MAGENTA}

# Variáveis globais
menu = f"""
{cores['menu']}[d] Depositar
{cores['menu']}[s] Sacar
{cores['menu']}[e] Extrato
{cores['menu']}[q] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2
TAXA_SAQUE = 0.01

while True:
    # Exibe o menu principal com cores
    opcao = input(colorama.Fore.RESET + menu)

    if opcao == "d":
        valor = float(input(f"{cores['valor']}Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
        else:
            print(f"{cores['menu']}Operação falhou! O valor informado é inválido. Tente novamente!")

    elif opcao == "s":
        valor = float(input(f"{cores['valor']}Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"{cores['menu']}Operação falhou! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print(f"{cores['menu']}Operação falhou! O valor do saque excedeu o limite.")
        elif excedeu_saques:
            print(f"{cores['menu']}Operação falhou! Número de saques foi excedido.")
        elif valor > 0:
            taxa = valor * TAXA_SAQUE  # Calcula a taxa de saque
            valor_final = valor + taxa  # Adiciona a taxa ao valor do saque
            if valor_final <= saldo:  # Verifica se o valor final não excede o saldo
                saldo -= valor_final  # Debita o valor final do saldo
                extrato += f'Saque: R$ {valor:.2f} + Taxa: R$ {taxa:.2f} = R$ {valor_final:.2f}\n'
                numero_saques += 1
            else:
                print(f"{cores['menu']}Operação falhou! Saldo insuficiente para cobrir a taxa de saque.")
        else:
            print(f"{cores['menu']}Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print(f"\n{cores['menu']}=============EXTRATO==============")
        print(f"{cores['menu']}Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n{cores['menu']}Saldo: R$ {saldo:.2f}")
        print(f"{cores['menu']}===============================")

    elif opcao == "q":
        break

    else:
        print(f"{cores['menu']}Operação inválida, por favor selecione novamente a operação desejada.")

