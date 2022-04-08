#Ahorcado Facundo de Platzi

import random 
import os

def run():
    DB = [
            'C',
            'PHP',
            'PYTHON',
            'JAVA',
            'JAVASCRIPT',
            'GO',
            'RUST',
            'RUBY']

    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    word = random.choice(DB)
    spaces = ['_'] * len(word)
    attemps = 0

    while True:
        os.system('clear')
        print('Descubre el lenguaje de programación')
        for character in spaces:
            print(character, end=' ')

        print(IMAGES[attemps])
        letter = input('Escribe una letra: ').upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attemps += 1

        if '_' not in  spaces:
            os.system('clear')
            print('Ganaste!!')
            break
 
        if attemps == 6:
            os.system('clear')
            print('Perdiste!!')
            break           


if __name__ == '__main__':
    run()
