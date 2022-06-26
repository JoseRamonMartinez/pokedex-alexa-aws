import json
import ast
from api import http

def get_pokemon_by_name(name):

    pokemon_list = ast.literal_eval(json.loads(http('/prod/pokemons/name/{}'.format(name))))

    speech_output = f"The pokemon {pokemon_list[0]['name']} is "

    speech_output+=f"the national pokedex number {pokemon_list[0]['id']}"

    speech_output+=f" and is type "

    if len(pokemon_list[0]['data']['type']) > 1:
        speech_output += f" {pokemon_list[0]['data']['type'][0]} and {pokemon_list[0]['data']['type'][1]}"
    else:
        speech_output += f" {pokemon_list[0]['data']['type'][0]}"


    return speech_output