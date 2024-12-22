import json

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



