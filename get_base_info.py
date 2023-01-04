from get_module import get_info
from get_species_info import get_species
from get_types import get_types_info

def get_base_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    data = get_info(url)
    get_type_data = [get_types_info(elemento['type']['url']) for elemento in data['types']]
    get_species_data = get_species(data['species']['url'])

    #estas listas se van a llenar con el for de mas abajo
    base_info ={
        'double_damage_from':[],
        'double_damage_to':[],
        'half_damage_from':[],
        'half_damage_to':[],
        'no_damage_from':[],
        'no_damage_to':[],
    }
    for elemento in get_type_data:
        base_info['double_damage_from'] += [ elemento['name'] for elemento in elemento['double_damage_from'] ]
        base_info['double_damage_to'] += [ elemento['name'] for elemento in elemento['double_damage_to'] ]
        base_info['half_damage_from'] += [ elemento['name'] for elemento in elemento['half_damage_from'] ]
        base_info['half_damage_to'] += [ elemento['name'] for elemento in elemento['half_damage_to'] ]
        base_info['no_damage_from'] += [ elemento['name'] for elemento in elemento['no_damage_from'] ]
        base_info['no_damage_to'] += [ elemento['name'] for elemento in elemento['no_damage_to'] ]

    for item in base_info:
        base_info[item] = list(set(base_info[item])) #aquí repetía los tipos, por eso lo transformé a un set y luego lo devuelvo alista
    
    stats={} #este diccionario lo llenaré con el for
    for elemento in data['stats']:
        stats[elemento['stat']['name']] = elemento['base_stat']

        
    base_info ={
        'name' : data['name'],
        'id' : data['id'],
        'picture' : data['sprites']['other']['official-artwork']['front_default'],
        'stats' : stats,
        'types' : [elemento['type']['name'] for elemento in data['types']],
        'damage_relations' : base_info, #muestra directo los arreglos que declaré arriba
        'species' : get_species_data
        }

    return base_info
    

if __name__ == '__main__':
    name = 'charizard'
    print(get_base_pokemon(name))
