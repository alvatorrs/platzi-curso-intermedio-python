import mod

DATA = [
    {
        'Country': 'Colombia',
        'City': 'Bogota'
    },
    {
        'Country': 'Mexico',
        'City': 'Jalisco'
    },
    {
        'Country': 'Mexico',
        'City': 'CDMX'
    }
]

def run():
    keys, values = mod.get_population()
    print(keys)
    print(values)

    print(mod.MENSAJE)


    mod.population_by_country(DATA, 'Mexico')


if __name__ == '__main__':
    run()
