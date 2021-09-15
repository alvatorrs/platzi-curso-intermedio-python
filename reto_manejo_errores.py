'''Utiliza las palabras claves try, except, raise para elevar un error
si el usuario ingresa un número negativo en nuestro programa de divisores'''

def divisors(num):
    divisors = []
    try:
        if num <= 0:
            raise ValueError('Ingrese un número positivo')
    except ValueError as ve:
        print(ve)
        return str(num) + ' no es un número mayor a cero'
    else:
        for i in range(1, num +1):
            if num % i == 0:
                divisors.append(i)
        print(divisors)
        return 'Termino mi programa'        


def main():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
    except ValueError:
        print('Debes ingresar un número') 


if __name__ == '__main__':
    print('Divisores de un número\n')
    main()