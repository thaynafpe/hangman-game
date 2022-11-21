import random
player1 = input('Digite seu nome:')
jogo1 = input('Você gostaria de jogar? S/N')
if jogo1 != 'S':
    exit()

palavras = ['bola', 'banana', 'rio', 'gato', 'travesseiro', 'lampada', 'porta', 'geladeira']
palavra = random.choice(palavras)
def jogo():
    print('-' * 30, '\n         JOGO DA FORCA\n', '-' * 30, '\n     Vamos jogar, {}\n'.format(player1), '-' * 30)

jogo()


alfabeto = list("abcdefghijklmnopqrstuvwxyz")
chances = 5
tentativas =[]

while True:
    print(tentativas)
    print(chances,"chances")
    for letra in palavra:
        if letra in tentativas:
            print(letra, end=' ')
        else:
            print ('_', end=' ')

    chute = input("Digite uma letra ou 'SAIR' se não quiser mais jogar.")
    if chute == 'SAIR':
        break

    elif chute not in alfabeto or chute == ' ':
        print('Isso não é uma letra, tente outra vez.')
    elif chute in tentativas:
        print('Ops! Parece que você já digitou essa letra. Bora tentar de novo?')
        continue

    tentativas.append(chute)
    if chute in palavra:
        print('isso aí, você acertou!'.upper())
    else:
        print('Errou, hein? Quem sabe na próxima?')
        print('Você tem mais', chances -1, 'chances')
        chances -=1
    if chances == 0:
        print('game over!'.upper())
        break
    elif set(palavra).issubset(set(tentativas)):
        print('parabéns, você ganhou o jogo!'.upper())
        print(palavra)
        break










