import os
from datetime import datetime

data_ultima_trasacao = None
data_atual = datetime.now()
quantidade_de_trasacoes_realizadas = 0
extrato = ""
saldo = 0

menu = f"""
    Seja bem vindo à sua conta bancária!
    {data_atual.strftime("%d/%m/%Y %H:%M")}
                      
        Escolha Uma das opções a seguir:
        [0] Sair do menu
        [1] Depósito
        [2] Saque
        [3] Extrato
    """

def deposito(valor):
    data_atual = datetime.now()

    global extrato
    extrato += f"Depósito de R${valor} foi realizado às {data_atual.strftime("%d/%m/%Y %H:%M")} \n"
    os.system('cls')
    print("Depósito realizado com sucesso!")

def saque(valor):
    data_atual = datetime.now()

    global extrato 
    extrato += f"Saque de R${valor} foi realizado às {data_atual.strftime("%d/%m/%Y %H:%M")} \n"
    os.system('cls')
    print("Saque realizado com sucesso!")


while True:
    opcao = int(input(menu))

    if opcao == 0:
        print("Muito obrigado por confiar em nós, até a próxima!")
        break

    elif opcao == 1:
        if quantidade_de_trasacoes_realizadas < 10:
            quantidade_de_trasacoes_realizadas += 1

            valor = int(input("Quanto você deseja depositar?"))

            saldo += valor
            deposito(valor)
            data_ultima_trasacao = data_atual
        
        elif quantidade_de_trasacoes_realizadas == 10 and data_ultima_trasacao.strftime("%d/%m/%Y") != data_atual.strftime("%d/%m/%Y"):

            quantidade_de_trasacoes_realizadas = 0
            quantidade_de_trasacoes_realizadas += 1
            valor = int(input("Quanto você deseja depositar?"))

            saldo += valor
            deposito(valor)
            data_ultima_trasacao = data_atual

        else:
            print("A quantidade de trasações diárias já foi atingida (10)")

    elif opcao == 2:
        if quantidade_de_trasacoes_realizadas < 10:

            quantidade_de_trasacoes_realizadas += 1
            valor = int(input("Quanto você deseja sacar? \n"))

            if saldo >= valor:
                saldo -= valor
                saque(valor)
                data_ultima_trasacao = data_atual
            else:
                print(f"O valor desejado é maior que o saldo atual de R${saldo}")
        
        elif quantidade_de_trasacoes_realizadas == 10 and data_ultima_trasacao.strftime("%d/%m/%Y") != data_atual.strftime("%d/%m/%Y"):

            quantidade_de_trasacoes_realizadas = 0
            quantidade_de_trasacoes_realizadas += 1
            valor = int(input("Quanto você deseja sacar? \n"))
            if saldo >= valor:
                saldo -= valor
                saque(valor)
                data_ultima_trasacao = data_atual
            else:
                print(f"O valor desejado é maior que o saldo atual de R${saldo}")

        else:
            print("A quantidade de trasações diárias já foi atingida (10)")
    
    elif opcao == 3:
        print(extrato)

    else:
        print("Opção inválida")



        

        
            

