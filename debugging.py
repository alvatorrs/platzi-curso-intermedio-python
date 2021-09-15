'''Divisores de un número'''

def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print('Terminó mi programa')
    except ValueError:
        print('Debes ingresar un número') 


if __name__ == '__main__':
    print('Divisores de un número\n')
    main()