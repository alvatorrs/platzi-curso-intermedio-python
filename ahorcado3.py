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


def word_hunter(selected_word,game_words,letter):
    ''''''
    if letter in selected_word:
        for i in range(len(selected_word)):
            if letter == selected_word[i]:
                game_words[i] = letter
    return ''.join(game_words)


def main():
    selected_word = choose_world() 
    game_words = ['_' for _ in range(len(selected_word))]
    letter = ''
    while True:  
        os.system('clear')
        print('''\nBienvenido al juego del ahorcado ( ͡° ͜ʖ ͡°)\n''')
        print('Adivina la palabra')
        print(word_hunter(selected_word, game_words, letter))
        try:
            letter = input('\nIngresa una letra: ').upper()
            if len(letter) != 1 or letter.isnumeric():
                raise TypeError('Ingrese solo una letra')
            else:
                if word_hunter(selected_word, game_words, letter).count('_') > 0:
                    if letter in word_hunter(selected_word, game_words, letter):
                        os.system('clear') 
                        print('''\nBienvenido al juego del ahorcado ( ͡° ͜ʖ ͡°)\n''')
                        print('Adivina la palabra')       
                        print(word_hunter(selected_word,game_words, letter))
                        letter = input('\nIngrese otra letra: ').upper()
                else:
                    print('GANASTE!!! la palabra es:',word_hunter(selected_word,game_words,letter))
                    break
        except TypeError as te:
            print(f'\n{te}')


if __name__=='__main__':
    main()
