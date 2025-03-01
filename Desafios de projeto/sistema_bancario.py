import os



def sistema_bancario(saldo_inicial):
    
    deposito = 0
    saque = 0
    opcao = 4
    extrato = ""
    soma_de_vezes_que_saque_foi_realizado = 0

    while opcao != 0:
        opcao = int(input("""
    Seja bem vindo à sua conta bancária!
                      
        Escolha Uma das opções a seguir:
        [0] Sair do menu
        [1] Depósito
        [2] Saque
        [3] Extrato
        """))
        if opcao == 0:
            print("Muito obrigado por confiar em nós, até a próxima!")

        elif opcao == 1:
            deposito = float(input("Quanto você deseja depositar? "))

            if(deposito > 0):
                saldo_inicial += deposito
                os.system('cls')
                print("Depósito efetuado com sucesso")
                extrato += f"""
             
Depósito de R${deposito} realizado
"""
            else:
                print("Valor inserido é invalido")

        elif opcao == 2:
                
                soma_de_vezes_que_saque_foi_realizado += 1
                
                if soma_de_vezes_que_saque_foi_realizado < 4:

                    saque = float(input("Quanto você deseja sacar? (Limite Máximo de R$500) "))
                
                    if saque <= 500 and saque > 0:
                        if saque <= saldo_inicial:
                            saldo_inicial -= saque
                            os.system('cls')
                            print("Saque realizado com sucesso!")
                            extrato += f"""
Saque de R${saque} realizado
"""
                        else:
                            print(f"Seu saldo de R${saldo_inicial:.2f} é insuficiente")
                    else:
                     print("Saque acima do limite de R$500")

                else:
                    print("Você já realizou 3 saques diários!")

        elif opcao == 3:
            if extrato == "":
                print("Você fez nenhuma movimentação ainda")
                print(f"""Seu saldo atual é de R${saldo_inicial:.2f}""")
            else:
                print(f"""
{extrato}
Seu saldo atual é de R${saldo_inicial:.2f}""")

        else:
            print("Escolha uma opção válida")

sistema_bancario(300)            

        
            

