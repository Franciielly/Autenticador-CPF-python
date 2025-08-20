import random

qnt = int(input("Quantos CPF deseja gerar: "))
n = 0

while n < qnt:
    cpf = ""
    for i in range(9):
        cpf += str(random.randint(0,9))

    digitos = [int(d) for d in cpf]
                                
    i = 10
    soma = 0

    for indice in range(9):
        soma += digitos[indice] * i
        i -= 1 

    resultado = (soma *10) % 11

    if resultado > 9:
        resultado = 0

    digitos.append(resultado)

    x = 11
    soma2 = 0

    for indice in range(10):
        soma2 += digitos[indice] * x
        x -= 1 

    resultado2 = (soma2 *10) % 11

    if resultado2  > 9:
        resultado2 = 0
    print(f"{cpf}-{resultado}{resultado2}")
    n+=1