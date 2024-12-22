import json

import progress
from items import inventory

data_to_store = {"progress": progress.progress_dict,
                 "inventory": inventory.inventory}

# Função para salvar dados
def store_data(data, archive="game_data.json"):
    with open(archive, "w") as f:
        json.dump(data, f)

# Função para carregar dados
def load_data(archive="game_data.json"):
    try:
        with open(archive, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Returns empty dict if file doesn't exist



store_data(data_to_store, "game_data.json")
