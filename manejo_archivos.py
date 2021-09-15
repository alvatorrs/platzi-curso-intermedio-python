def read():
    '''Lee el archivo numbers.txt y convierte a cada una de sus lineas
    en elementos de una lista'''
    numbers = []
    with open('./archivos/numbers.txt','r', encoding ='utf-8') as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)


def write():
    '''Crea un archivo dioses.txt donde inserta los elementos de una lista
    en cada una de sus lineas'''
    names = ['Athenea', 'Hermes', 'Zeus', 'Ares', 'Poseidon', 'Hades']
    with open('./archivos/dioses.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)  #tambien se puede usar f.write(name + '\n')
            f.write('\n')
        


def main():
    read()
    write()


if __name__=='__main__':
    main()