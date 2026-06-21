import random
import winsound
import time

def game():
    tentativas = 0
    
    try:
        reais = int(input("Quantos reais você quer apostar?\n->"))
        if reais <= 0:
            print("Digite um valor maior que zero!")
            return
        print("Sorteando multiplicador...")
        time.sleep(2)
        multiplicador = random.choices(range(1, 16),weights=[90, 40, 25, 15, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k=1)[0]
        print("Multiplicador Sorteado =",multiplicador,"\n")
        menu = int(input("Escolha uma dificuldade!\n1 para 100 números\n2 para 500 números\n3 para 1000 números\nEscreva aqui->"))
    except ValueError:
        print("Digite apenas números!")
        return
    if menu == 1:
        limite = 100
    elif menu == 2:
        limite = 500
    elif menu == 3:
        limite = 1000
    else:
        print("Número inválido")
        return
    
    numero = random.randint(1,limite)
    print("Um número de 1 a",limite,"foi sorteado! Tente encontra-lo!")
    
    while True:
        try:
            escolha = int(input("Escreva o número:"))
        except ValueError:
            print("Digite apenas números!")
            continue
        if escolha < 1 or escolha > limite:
            print("Escolha um número entre 1 e",limite,"!")
            continue
        
        tentativas = tentativas + 1
        if numero > escolha:
            print("Seu número é menor que o número sorteado")
        elif numero < escolha:
            print("Seu número é maior que o número sorteado")
        else:
            print("Você acertou em",tentativas,"tentativas!")
            if tentativas == 1:
                print("Você ganhou",(reais*multiplicador)*100,"reais!")
                winsound.Beep(1000, 150)
                winsound.Beep(1500, 150)
                winsound.Beep(2000, 150)
                print("Você é muito sortudo!")
            elif tentativas >=2 and tentativas <=4:
                print("Você ganhou",(reais*multiplicador)*4,"reais!")
                print("Você é bom!")
            elif tentativas >=5 and tentativas <=9:
                print("Você ganhou",reais*multiplicador,"reais!")
                print("Tá na média, dá pra melhorar")
            else:
                print("Você perdeu a aposta!")
            break

game()
