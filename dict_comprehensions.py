'''Crear un diccionario, cuyas llaves sean los primeros 100
números naturales y cuyos valores sean esos números al cubo.'''

def main():

    #alternativa
    dict1 = {}
    for i in range(1,101):
        if i%3 != 0:
            dict1[i] = i**3
    print("Dict1: ",dict1)

    #con list comprehension
    dict2 = {i:i**3 for i in range(1,101) if i%3 != 0}
    print("\n\nDict2: ",dict2)

if __name__ == '__main__':
    main()
