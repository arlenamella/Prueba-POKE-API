from poke_validation import validate
from show import show_pics
import data as d
from get_base_info import get_base_pokemon
from build_pokemon_html import build_html

while True: 
    
    opciones= input('''Bienvenido a la Poke-App:
            ¿Qué desea conocer del mundo Pokemon?
            
            1. Pokedex
           
            0. Salir
            > ''') 

    opciones = int(validate(opciones, ['0','1'], d))

    if opciones == 1:
        pokemon = input(''' Ingrese el nombre del Pokemon para verlo en el Pokedex.
                        Nota: Si el nombre del pokemon tiene espacios, reemplace por "-".
                        No coloque ningún signo de puntuación adicional.
                        Ejemplo: Mr. Mime, se debe ingresar como mr-mime o Mr-Mime
                        > ''').lower()
        pokemon = validate(pokemon) # esto lo trae desde data d
        base_info = get_base_pokemon(pokemon)
        html=build_html(base_info) #aqui se construye el html
        show_pics(html, pokemon)

    else:
        exit() #para finalizar el ciclo
