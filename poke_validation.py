with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()
    

pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]
import data as d

def validate(name, p_l = pokemon_lista, mensaje = d.validacion_pokemon):
    if name =='codigo-cero':
        name = 'type-null'
    while name not in p_l:
        name = input(mensaje).lower()
    return name


if __name__ == '__main__':
    name = 'codigo-cero'
    print(validate(name))
