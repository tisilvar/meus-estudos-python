"""
Jogo da Adivinhação

Este programa define um número secreto e pede ao usuário para tentar adivinhar qual é este número.

A cada palpite, o programa fornecerá uma das seguintes dicas:
- 'Muito baixo, tente de novo!'
- 'Muito alto, tente de novo!'

Quando o usuário acertar o número, o jogo terminará e exibirá uma mensagem de parabéns com o total de tentativas realizadas.
"""
numero_secreto = 42
tentativas = 0
while True:
    numero_palpite = int(input("Insira seu palpite: "))
    tentativas += 1
    if numero_palpite < numero_secreto:
        print("Muito baixo, tente novamente!")
    elif numero_palpite > numero_secreto:
            print("Muito alto, tente de novo!")
    else:
        print(f"Parabéns! Você acertou o {numero_secreto} em {tentativas} tentativas!")
        break