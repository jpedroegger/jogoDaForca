import random
from lista_de_palavras import lista
import string

# Função utilizada para importar uma palavra aleatória de uma lista externa.
def pegar_palavra(lista):
    palavra = random.choice(lista)

    return palavra.upper()


def forca():
    palavra = pegar_palavra(lista)
    letras_em_palavra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()  # Letras que o usuário digitou.

    vidas = 5

    print('Bem vindo ao Jogo!')
    # O Loop termina quando encerram as vidas ou quando o comprimento da palavra é igual a 0.
    while len(letras_em_palavra) > 0 and vidas > 0:
        print(f'Você ainda tem {vidas} vidas sobrando e já escolheu as letras: ', ' '.join(letras_usadas))

        lista_de_palavras = [letra if letra in letras_usadas else '_' for letra in palavra]
        print('Palavra: ', ' '.join(lista_de_palavras))

        letras_usuario = input('Digite uma letra: ').upper()
        if letras_usuario in alfabeto - letras_usadas:  # Se a letra for válida e não estiver em letras_usadas.
            letras_usadas.add(letras_usuario)
            if letras_usuario in letras_em_palavra:  # Se a letra for correta, ela será removida do set.
                letras_em_palavra.remove(letras_usuario)
                print('')

            else:
                vidas -= 1  # Diminui uma vida quando errada.
                print(f'\nA letra {letras_usuario} não foi encontrada na palavra chave.')

        elif letras_usuario in letras_usadas:
            print('\nVocê já digitou essa letra. Tente uma outra.')

        else:
            print('\nEssa não é uma letra válida.')


    if vidas == 0:
        print(f'Que pena, você perdeu!\nA palavra era {palavra}')
    else:
        print(f'Bom trabalho! Você adivinhou!\nA palavra era {palavra}!!')


forca()
