import time 
import os 

def limpar_tela():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

"""
Cálculo do 1º dígito do CPF:
Multiplica os 9 primeiros dígitos por pesos de 10 a 2, soma tudo, multiplica por 10 e tira o resto da divisão por 11. Se o resto > 9, dígito = 0; senão, dígito = resto.
"""

resposta = "sim"
while resposta == "sim":
    while True: 
        cpf = input("Digite seu CPF(apenas números): ")
        sequencia = cpf[0] * len(cpf)
        if cpf.isdigit() and len(cpf) == 11 and cpf != sequencia:
            digitos = [int(d) for d in cpf]
            break
        else:
            print("Digite o CPF corretamente: apenas 11 números, sem pontos ou traços.")
                                    
    i = 10
    soma = 0

    for indice in range(9):
        soma += digitos[indice] * i
        i -= 1 

    resultado = (soma *10) % 11

    if resultado > 9:
        resultado = 0

    """
    Cálculo do 2º dígito do CPF:
    Multiplica os 9 primeiros dígitos + 1º dígito por pesos de 11 a 2, soma tudo, multiplica por 10 e tira o resto da divisão por 11. Se o resto > 9, dígito = 0; senão, dígito = resto.
    """

    x = 11
    soma2 = 0

    for indice in range(10):
        soma2 += digitos[indice] * x
        x -= 1 

    resultado2 = (soma2 *10) % 11

    if resultado2  > 9:
        resultado2 = 0

    if digitos[9] == resultado and digitos[10] == resultado2:
        print("CPF válido.")
    else:
        print("CPF Inválido")

    while True: 
        resposta = input("Deseja validar outro CPF? (SIM/NAO): ").lower()
        if resposta == "nao" or resposta == "não":
            break
        elif resposta == "sim":
            break
        else:
            print("Digite apenas 'sim' ou 'não'.")
    limpar_tela()
    

print("Programa encerrado.")
