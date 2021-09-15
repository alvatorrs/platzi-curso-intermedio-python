'''Crear con un list comprehension una lista de todos los
    múltiplos de 4, 6 y 9, hasta 5 digitos'''

def main():
    list1 = [i for i in range(1,100000) if i%36 ==0]
    print(list1,"\n")

    list2 = [i for i in range(1,100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print("\n",list2)


if __name__ == '__main__':
    main()