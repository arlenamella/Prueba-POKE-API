from get_module import get_info


def get_types_info(url):
    data = get_info(url)
    return data['damage_relations']

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/type/3/'
    print(get_types_info(url))