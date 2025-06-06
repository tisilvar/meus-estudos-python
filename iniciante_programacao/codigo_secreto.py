codigo_secreto = 69855
solicitacao_codigo = input("Digite o código secreto: ")
numero_proibido = 7


try:

    int(solicitacao_codigo)
    if '7' in solicitacao_codigo:
        print("Acesso negado. O número 7 é proibido.")
    else:
        print("Acesso concedido!")

except ValueError:
    print("Erro: O código deve ser um número.")