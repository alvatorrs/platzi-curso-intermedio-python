import os
from random import choice

def word_selector():
    with open('./archivos/data.txt','r',encoding='utf-8') as f:
        words = []
        for word in f:
            words.append(word.strip().upper())
        word_selected = choice(words)
        ocult_word = '_'*len(word_selected)
        return word_selected, ocult_word


def replace_word(word_selected, ocult_word, letter):
    letter_count = word_selected.count(letter)
    point_start = 0
    for _ in range(letter_count):
        position = word_selected.find(letter, point_start)
        ocult_word = ocult_word[:position] + letter + ocult_word[position+1:]
        point_start = position + 1
    return ocult_word


def main():
    lives = 6
    os.system('clear')
    print('Bienvenido al juego del ahorcado 👾🤖👽')
    print(f'vidas: {"💜" * (lives)}')
    input('Presiona enter para coninuar: ')
    word_selected, ocult_word = word_selector()
    deaths = 0

    while ocult_word != word_selected and deaths < lives:
        os.system('clear')
        print(f'vidas: {"💜" * (lives - deaths)}')
        print(ocult_word)
        letter = input('Escoge una letra: ').upper()
        if letter in word_selected:
            ocult_word = replace_word(word_selected, ocult_word, letter)
        else:
            deaths += 1

    if ocult_word == word_selected:
        os.system('clear')
        print(f'Felicidades!! ganaste ✨🎉 la palabra es {ocult_word} 🎊')
    else:
        os.system('clear')
        print(f'Has perdido 😈 la palabra era {word_selected} 👻')


if __name__ == '__main__':
    main()
