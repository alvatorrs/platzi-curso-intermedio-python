# filter
print('Uso de filter')
my_list1 = [1,4,5,6,9,13,19,21]
print('Lista1: ',my_list1)
odd = list(filter(lambda x: x%2 != 0, my_list1))
print('Filtro de números impares: ', odd)

# map
print('\n\nUso de map')
my_list2 = [1,2,3,4,5]
print('Lista2: ', my_list2)
squares = list(map(lambda x: x**2, my_list2))
print('Mapeo del cuadrado de la lista: ', squares)

# reduce
print('\n\nUso de reduce')
from functools import reduce

my_list3 = [2,2,2,2,2]
print('lista3: ', my_list3)
all_multiplied = reduce(lambda a, b: a*b, my_list3)
print('Multiplicacion de todos los elementos de la lista : ',all_multiplied)
