import os
from typing import Dict

class PeopleFinderView:
    def find_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Pessoa \n\n')
        name = input('Determine o nome da pessoa para busca: ')

        person_finder_informations = {
            "name": name
        }

        return name 