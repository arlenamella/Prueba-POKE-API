from get_module import get_info
import random 

def get_species(url):
    data = get_info(url)
    species_info={
        'evolves_from_species': None
    }
    #voy a declarar si etapa previa no es None, entonces trae la etapa previa
    if data['evolves_from_species'] is not None:
        species_info['evolves_from_species'] = data['evolves_from_species']['name'].capitalize()
    #el flavor_text_entries me da la descripcion del pokemon, y le coloco el random para que escoja cualquier definición. utilicé el if para que tome solo las que estan en español
    species_info['flavor_text_entries'] = random.choice([ elemento['flavor_text'] for elemento in data['flavor_text_entries'] if elemento['language']['name'] == 'es'])
    #y ahora los tipos especiales
    species_info['is_baby'] = data['is_baby']
    species_info['is_legendary'] = data['is_legendary']
    species_info['is_mythical'] = data['is_mythical']
    return species_info


if __name__=='__main__':
    print(get_species('https://pokeapi.co/api/v2/pokemon-species/6/'))
    print(get_species('https://pokeapi.co/api/v2/pokemon-species/132/'))