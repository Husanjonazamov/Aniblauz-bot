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
    
    
    
def getEpisode(anime_id):
    url = f"{BASE_URL}/episodes/anime/{anime_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print(response.status_code)
        return []
    
    