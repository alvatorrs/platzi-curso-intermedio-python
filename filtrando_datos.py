DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():

    # con list comprehensions
    print('##List comprehensions##')
    print('\nProgramadores en Python:')
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    for worker in all_python_devs:
        print(worker)


    print('\nTrabajadores en Platzi:')
    all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    for worker in all_Platzi_workers:
        print(worker)


    print('\nMayores de 18 años:')
    mayores = [worker['name'] for worker in DATA if worker['age'] > 18]
    print(mayores)


    print('\nAgregando un key a DATA verificando si es  un adulto mayor:')
    #adultos_mayores = [worker | {'old': worker['age'] > 70} for worker in DATA] Python==3.9
    adultos_mayores = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    for worker in adultos_mayores:
        print(worker)



    # con filter y map
    print('\n##High order functions##')
    print('\nProgramadores en Python:')
    devs_py = list(filter(lambda worker: worker['language'] == 'python',DATA))
    names_devs_py = list(map(lambda worker: worker['name'], devs_py))
    for worker in names_devs_py:
        print(worker)


    print('\nTrabajadores en Platzi:')
    all_platzi = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    names_platzi = list(map(lambda worker: worker['name'], all_platzi))
    for worker in names_platzi:
        print(worker)


    print('\nMayores de 18 años:')
    adults = list(filter(lambda worker: worker['age'] > 18,DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    print(adults)


    print('\nAgregando un key a DATA para verificar si es un adulto mayor:')
    #old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA)) Python==3.9
    old_people = list(map(lambda worker: {**worker, **{'old': worker['age'] > 70} }, DATA))
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    main()
