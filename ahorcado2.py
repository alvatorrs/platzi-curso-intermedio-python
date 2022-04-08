import os
import random


def read_words(filepath='./archivos/data.txt'):

    with open(filepath, 'r', encoding='utf-8') as f:
        list_words = [word.strip().upper() for word in f] # el strip() quita ese espacio final
        choosen_word = list_words[random.randint(0, len(list_words))]

    return choosen_word


def game(selected_word, letter, game_word):
    if letter in selected_word:
        for i in range(len(selected_word)):
            if letter == selected_word[i]:
                game_word[i] = letter

    return ' '.join(game_word)


def run():
    lives = 5
    letter = ''
    selected_word = read_words()
    game_word = ['_' for i in range(len(selected_word))]

    while lives > 0:
        os.system('clear')
        print(f'Vidas restantes: {"❤" * (lives)}')
        print('¡Adivina la palabra!')
        print(game(selected_word, letter, game_word))
        try:
            if len(letter) > 1:
                raise ValueError('Solo puedes ingresar una letra')
            else:
                if game(selected_word, letter, game_word).count('_') > 0:
                    if letter in game(selected_word, letter, game_word):
                        letter = input('Escoge una letra: ').upper()
                    else:
                        lives -= 1
                        if lives > 0:
                            os.system('clear')
                            print(f'Vidas restantes: {"❤" * (lives)}')
                            print('¡Adivina la palabra!')
                            print(game(selected_word, letter, game_word))
                            letter = input('Escoge una letra: ').upper()
                        else:
                            os.system('clear')
                            print('¡Te quedaste sin vidas!\nJuego terminado...\n')
                            print('La palabra era: ' + selected_word)
                else:
                    print('¡Ganaste! √')
                    break

        except ValueError as ve:
            return print(ve)
    

if __name__ == '__main__':
    run()
