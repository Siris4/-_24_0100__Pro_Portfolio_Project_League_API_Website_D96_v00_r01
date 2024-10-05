import requests

API_KEY = 'YOUR_RIOT_API_KEY'
BASE_URL = 'https://REGION.api.riotgames.com'


def get_summoner_id(summoner_name, region='na1'):
    url = f'{BASE_URL}/lol/summoner/v4/summoners/by-name/{summoner_name}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['id']
    else:
        return None


def get_live_game(summoner_id, region='na1'):
    url = f'{BASE_URL}/lol/spectator/v4/active-games/by-summoner/{summoner_id}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None
