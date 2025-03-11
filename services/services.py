import requests
from utils.env import BASE_URL



def createUser(user):
    url = f"{BASE_URL}/users/"
    response = requests.post(url, json=user)
    
    if response.status_code == 200 or 201:
        data = response.json()
        return data
    else:
        print(response.status_code)
        
        
def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
        
        
        
def getAnime():
    url = f"{BASE_URL}/anime/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['results']
    else:
        print(response.status_code)
        return []
    
def getEpisodesList():
    url = f"{BASE_URL}/episodes/"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        return data['data']['results']
    else:
        return []

def getEpisodeFromID(episode_id):
    url = f"{BASE_URL}/episodes/episode/{episode_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']
    raise Exception("Episode not foun!")
    
    
def getEpisode(anime_id):
    url = f"{BASE_URL}/episodes/anime/{anime_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print(response.status_code)
        return []
    
    