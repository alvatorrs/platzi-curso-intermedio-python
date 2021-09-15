from random import choice
import os

def choose_world():
    '''Selecciona una palabra aleatoria de data.txt'''
    words = []
    with open('./archivos/data.txt','r', encoding='utf-8') as f:
        for word in f:
            words.append(word.upper().strip())
        selected_word = choice(words)
        return selected_word


def word_hunter(selected_word):
    ''''''
    game_words = ['_' for i in range(len(selected_word))]
    try:
        letter = input('\nIngresa una letra: ')
        if len(letter) != 1 or letter.isnumeric():
            raise TypeError('Ingrese solo una letra')
    except TypeError as te:
        os.system('clear')
        print(te)

    if letter in selected_word:
        for i in range(len(selected_word)):
            if letter == selected_word[i]:
                game_words[i] = letter

    print(''.join(game_words))
    


def main():
    os.system('clear')
    print('''\nBienvenido al juego del ahorcado ( ͡° ͜ʖ ͡°)\n''')
    print('Por favor adivina la palabra')
    selected_word = choose_world()

    word_hunter(selected_word)

 

if __name__=='__main__':
    main()