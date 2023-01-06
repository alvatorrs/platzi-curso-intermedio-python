def get_population():
    keys = ['col', 'bol']
    values = [300, 400]
    return keys, values


def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    for i in result:
        print(f"País: {i['Country']}, Ciudad: {i['City']}")


MENSAJE = 'Hola, este es el modulo mod'
