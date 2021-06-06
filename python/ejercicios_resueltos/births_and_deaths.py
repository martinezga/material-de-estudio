'''
Determinar el año que tuvo más personas vivas dando como datos: año de nacimiento y año de defunción.
Por ejemplo: La persona 1 nace en 1980 y muere en el 2010 y la persona 2 nace en el 2010 y muere en el 2040.
La respuesta es 2010 como el año que más personas vivas tuvo.

Análisis gráfico:
persona 1 vive durante los años: (nace) 1980 1981 1982 1983 ... 2010 (muere)
persona 2 vive durante los años: (nace)                         2010 2011 2012 .... 2040 (muere)
'''

import json


def year_max_people_alive(data):
    people_by_year = {}
    years_max_people = []

    for person in data:
        birth_year = person["birthYear"]
        death_year = person["deathYear"]

        for year in range(birth_year, death_year + 1):
            try:
                people_alive = people_by_year[year]
                people_by_year.update({year: people_alive + 1})
            except KeyError:
                people_by_year.setdefault(year, 1)

    people_list = list(people_by_year.values())
    sorted_people = sorted(people_list, reverse=True)
    first_max_people = sorted_people[0]

    for year, people in people_by_year.items():
        if people == first_max_people:
            years_max_people.append(year)

    return years_max_people


if __name__ == "__main__":
    with open("raw_input/data.json") as input_file:
        data = json.load(input_file)

    result = year_max_people_alive(data["data"])
    print(result)

# Solved by Gabriella Martínez. https://github.com/martinezga
