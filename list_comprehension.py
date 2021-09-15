''' imprimir en una lista del cuadrado de los números que no
    sean divisibles entre 3'''

def main():

    #alternativa1
    squares1 = []
    for i in range(1,101):
        if i%3 == 0:
            continue
        x = i**2
        squares1.append(x)
    print('Lista1: ',squares1)

    #alternativa2
    squares2 = []
    for i in range(1,101):
        if i%3 != 0:
            squares2.append(i**2)
    print('\nLista2: ', squares2)

    #con list comprehension
    squares3 = [i**2 for i in range(1,101) if i%3 !=0]
    print('\nLista3: ',squares3)


if __name__ == '__main__':
    main()