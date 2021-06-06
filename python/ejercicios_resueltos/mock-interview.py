# Ordenar los vehiculos por tipo, marca, cc si es moto y modelo


import json


with open("raw_input/vehiculos.json") as input_file:
    data = json.load(input_file)
    print(data["vehiculos"])

# 