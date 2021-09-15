'''Crear, con un dictionary comprehension, un diccionario
cuyas llaves sean los 1000 primeros números naturales con
sus raices cuadradas como valores'''
from math import sqrt

def main():
    dict1 = {i: round(sqrt(i),3) for i in range(1,1001)}
    print('El diccionario es: ',dict1)


if __name__ == '__main__':
    main()