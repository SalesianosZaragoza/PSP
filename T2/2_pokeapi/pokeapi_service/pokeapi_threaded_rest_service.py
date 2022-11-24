from concurrent.futures import ThreadPoolExecutor
from typing import List

import requests

from pokeapi_rest_service import PokeAPIRestService
from pokemon import Pokemon


class PokeAPIThreadRestService(PokeAPIRestService):
    def get_by_names(self, names: List[str]) -> List[Pokemon]:
        with(ThreadPoolExecutor(max_workers=3)) as executor:
            futures = [executor.submit(self._get_by_names, names) for name in names]
        for futures in futures:
            pokemons.append(future.result())
        return pokemons

    def _get_by_names(self, name) -> Optional[Pokemon]:
        response = requests.get(self.BASE_API_URL + name)
        response.raise_for_status()
        pokemon_json = response.json()
        return Pokemon(id=pokemon_json['id'], name=pokemon_json['name'], height=pokemon_json['height'],
                            weight=pokemon_json['weight'])

