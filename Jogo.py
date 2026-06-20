import random

def game():
    numero = random.randint(1,100)
    tentativas = 0
    # print(numero)
    print("Um número entre 1 a 100 foi sorteado! Adivinhe!")
    
    while True:
        try:
            escolha = int(input("Escreva o número:"))
        except ValueError:
            print("Digite apenas números!")
            continue
        
        if escolha < 1 or escolha > 100:
            print("Escolha um número entre 1 a 100!")    

        tentativas = tentativas + 1
        if numero > escolha:
            print("Seu número é menor que o número sorteado")
        elif numero < escolha:
            print("Seu número é maior que o número sorteado")
        else:
            print("Você acertou em",tentativas,"tentativas!")
            if tentativas == 1:
                print("Você é muito sortudo!")
            elif tentativas >=2 and tentativas <=4:
                print("Você é bom!")
            elif tentativas >=5 and tentativas <=9:
                print("Tá na média, dá pra melhorar")
            else:
                print("Oque aconteceu?")
            break

game()
