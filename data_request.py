import requests

def get_data (link : str = "") -> dict[str,any]:
    response = requests.get(link)
    response.raise_for_status()
    return response.json()

