def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Alvaro', 'lastname': 'Torres'}

    super_list = [ 
            {'firstname': 'Facundo', 'lastname': 'García'},
            {'firstname': 'Miguel', 'lastname': 'Sánchez'},
            {'firstname': 'Erick', 'lastname': 'Perez'},
            {'firstname': 'Susana', 'lastname': 'Diaz'},
            {'firstname': 'Ana', 'lastname': 'Moreno'}
            ]

    for item in super_list:
        print(item['firstname'], '-', item['lastname'])


    super_dict = {
            'natural_nums': [1,2,3,4,5],
            'integer_nums': [-2,-1,0,1,2],
            'floating_nums': [1.1,4.5,6.43,2.35]
            }

    for key,value in super_dict.items():
        print(key, value)

if __name__ == '__main__':
    run()
