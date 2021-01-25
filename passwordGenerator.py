import random
import string

def gerador(tamanho, maiusculo, minusculo, numero):

    letraMaiuscula = string.ascii_uppercase
    letraMinuscula = string.ascii_lowercase

    senha = []

    for _ in range(tamanho):

        escolha = random.randint(1,3)

        if escolha == 1:
            if maiusculo == 1:
                caracterMa = ''.join(random.choice(letraMaiuscula))
                senha.append(caracterMa)
            else:
                caracterMa = ""
                while caracterMa == "":
                    caracterMa = gerador(1, maiusculo, minusculo, numero)
                senha.append(caracterMa)

        elif escolha == 2:
            if minusculo == 1:
                caracterMi = ''.join(random.choice(letraMinuscula))
                senha.append(caracterMi)
            else:
                caracterMi = ""
                while caracterMi == "":
                    caracterMi = gerador(1, maiusculo, minusculo, numero)
                senha.append(caracterMi)

        elif escolha == 3:
            if numero == 1:
                numeral = str(random.randint(0,9))
                senha.append(numeral)
            else:
                numeral = ""
                while numeral == "":
                    numeral = gerador(1, maiusculo, minusculo, numero)
                senha.append(numeral)
        
    senhaFinal = ''.join(senha)

    return senhaFinal

tamanho = int(input("Digite o tamanho da sua senha: "))
escolhaMai = int(input("\nDeseja letra maiuscula? \nSim - 1 \nNão - 0\n   Resposta: "))
escolhaMin = int(input("\n\nDeseja letra minuscula? \nSim - 1 \nNão - 0\n   Resposta: "))
escolhaNum = int(input("\n\nDeseja numero? \nSim - 1 \nNão - 0\n   Resposta: "))

print("A senha final é: " + gerador(tamanho, escolhaMai, escolhaMin, escolhaNum))