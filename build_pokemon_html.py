import data as d
from get_base_info import get_base_pokemon
from show import show_pics

def build_html(data):

    tiposPokemon= [d.span.substitute(class_=tipo, value_=d.tipos_espanol[tipo] ) for tipo in data['types']]
    #ahora se definane la relaciones de daño
    debil = [d.span.substitute(class_=tipo, value_=d.tipos_espanol[tipo] ) for tipo in data['damage_relations']['double_damage_from']]
    super_efectivo = [d.span.substitute(class_=tipo, value_=d.tipos_espanol[tipo] ) for tipo in data['damage_relations']['double_damage_to']]
    resistente_contra = [d.span.substitute(class_=tipo, value_=d.tipos_espanol[tipo] ) for tipo in data['damage_relations']['half_damage_from']]
    poco_ef = [d.span.substitute(class_=tipo, value_=d.tipos_espanol[tipo] ) for tipo in data['damage_relations']['half_damage_to']]
    inmune = [d.span.substitute(class_=tipo, value_=d.tipos_espanol[tipo] ) for tipo in data['damage_relations']['no_damage_from']]
    inef = [d.span.substitute(class_=tipo, value_=d.tipos_espanol[tipo] ) for tipo in data['damage_relations']['no_damage_to']]

    #estos datos aparecen solo sin lo tiene el pokemón
    if data['species']['is_legendary']:
        tiposPokemon.append(d.span.substitute(class_='legendary', value_=d.special_es['legendary']))
    if data['species']['is_mythical']:
        tiposPokemon.append(d.span.substitute(class_='mythical', value_=d.special_es['mythical']))
    if data['species']['is_baby']:
        tiposPokemon.append(d.span.substitute(class_='baby', value_=d.special_es['baby']))

    #esto va a rellenar la tabla del html
    dataTable = d.tabla_pokemon.substitute(
            hp= data['stats']['hp'],
            attack=data['stats']['attack'],
            defense= data['stats']['defense'],
            esAttck= data['stats']['special-attack'],
            esDef= data['stats']['special-defense'],
            speed= data['stats']['speed'])

    single_card=d.single_card.substitute(
            id= data['id'],
            name= data['name'].capitalize(),
            url = data['picture'],
            etapa_previa= data['species']['evolves_from_species'],
            table = dataTable,
            tipos = ''.join(tiposPokemon),
            description= data['species']['flavor_text_entries'],
            super_efectivo= ''.join(super_efectivo),
            debil= ''.join(debil),
            resistente= ''.join(resistente_contra),
            poco_ef= ''.join(poco_ef),
            inmune= ''.join(inmune),
            inef= ''.join(inef))

    return d.document_template.substitute(body = single_card)

if __name__ == '__main__':
    """ data= get_base_pokemon('charizard')
    show_pics(build_html(data),'charizard') """
    data= get_base_pokemon('articuno') #con anticuno aparece lengendario
    show_pics(build_html(data),'articuno')
