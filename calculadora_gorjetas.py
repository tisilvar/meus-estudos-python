"""
Projeto Final do Nível 1: Calculadora de Gorjetas Interativa

Este programa serve como uma ferramenta para calcular e dividir contas de forma justa e fácil.

Funcionalidades:
1.  Solicita ao usuário o valor total da conta.
2.  Pede uma avaliação da qualidade do serviço ("ruim", "bom", "excelente").
3.  Calcula uma porcentagem de gorjeta com base na avaliação (10%, 15% ou 20%).
4.  Pergunta com quantas pessoas a conta será dividida.
5.  Exibe um resumo final com o valor da gorjeta, o total com a gorjeta e o valor a ser pago por cada pessoa.
6.  O programa roda em um laço contínuo para permitir múltiplos cálculos.
"""
print(f"{"-" * 10}Boas-Vindas{"-" * 5}")
porcentagem = ""
valor_da_porcetagem = 0

while True:
    valor_da_conta = float(input("Insira o valor da conta:\n"))
    
    avaliacao_atendimento = input("Como avaliaria o atendimento?  \n[R]uim\n[B]om\n[E]xcelente\n[S]air\n").upper()
    
    numero_de_pessoas = int(input("A conta será divida em quantas pessoas:\n"))
    
    
    
    if  numero_de_pessoas == 0:
        print("\nERRO: O número de pessoas não pode ser zero. Por favor, tente novamente.\n")
        continue  
    elif avaliacao_atendimento == "R":
        porcentagem = "10%"
        valor_da_porcetagem = valor_da_conta * (10/100)
    elif avaliacao_atendimento == "B":
        porcentagem = "15%"
        valor_da_porcetagem = valor_da_conta * (15/100)
    elif avaliacao_atendimento == "E":
        porcentagem = "20%"
        valor_da_porcetagem = valor_da_conta * (20/100)
    elif avaliacao_atendimento == "S":
        break
    else:
        continue

    valor_total_com_gorjeta = valor_da_conta + valor_da_porcetagem
    valor_cada = valor_total_com_gorjeta / numero_de_pessoas
    
    print(f"{"-"*3} Resumo da Conta {"-"*3}\nValor Total: R$ {valor_da_conta}\nGorjeta: {porcentagem}: R$ {valor_da_porcetagem}\nValor Total com Gorjeta: R$ {valor_total_com_gorjeta}\nDividido por {numero_de_pessoas} pessoas\nCada pessoa deve pagar: R$ {valor_cada}\n{"-"*23}")