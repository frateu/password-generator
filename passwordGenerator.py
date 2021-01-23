import random
import string

letraMaiuscula = string.ascii_uppercase
letraMinuscula = string.ascii_lowercase

tamanho = int(input("Digite o tamanho da sua senha: "))

escolhaMai = int(input("\nDeseja letra maiuscula? \nSim - 1 \nNão - 0\n   Resposta: "))
escolhaMin = int(input("\n\nDeseja letra minuscula? \nSim - 1 \nNão - 0\n   Resposta: "))
escolhaNum = int(input("\n\nDeseja numero? \nSim - 1 \nNão - 0\n   Resposta: "))

senha = []

for _ in range(tamanho):

    escolha = random.randint(1,3)

    if escolha == 1:
        if escolhaMai == 1:
            caracter = ''.join(random.choice(letraMaiuscula))
            senha.append(caracter)

    if escolha == 2:
        if escolhaMin == 1:
            caracter = ''.join(random.choice(letraMinuscula))
            senha.append(caracter)

    if escolha == 3:
        if escolhaNum == 1:
            numeral = str(random.randint(0,9))
            senha.append(numeral)
    
senhaFinal = ''.join(senha)

print("A senha final é: " + senhaFinal)