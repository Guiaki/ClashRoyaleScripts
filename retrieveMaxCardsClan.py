import requests 
import json

PLAYER_ARRAY = []
START_DATE = "14/05/2019"
CLAN_KEY = "#2JJYLY2"
CLAN_KEY = CLAN_KEY.replace("#", "%23") if CLAN_KEY.find("#") != -1 else "%23"+CLAN_KEY
RESOURCE = "members"
URL = "https://api.clashroyale.com/v1/clans/{CLAN_KEY}/{RESOURCE}"
URL_PLAYER = "https://api.clashroyale.com/v1/players/{TAG}"
KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImEwNGZjZTIwLWRlMzItNDk2MS1iOGQ1LTMwOTgzMGM4MmRkYyIsImlhdCI6MTU3NDA3OTgwNCwic3ViIjoiZGV2ZWxvcGVyLzQwMTU4ZjAxLTU2ZGItNTFmNS0wZmMwLTNhZTFiMWM5MmUzZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzIuNjguMjcuODgiXSwidHlwZSI6ImNsaWVudCJ9XX0.h1dH24SLYqbY2onWqpHkDOI8eN7XTUwb-cWjr_kuyTOXKiMxGLVVOkywfiQ-MPtufleBBUg7Xz9gqHpkZq5t7w"
URL = URL.replace("{CLAN_KEY}", CLAN_KEY)
URL = URL.replace("{RESOURCE}", RESOURCE)

PARAMS = {'Authorization':'Bearer '+KEY, 'Accept':'application/json'} 
r = requests.get(url = URL, params = PARAMS)   
data = r.json()
print (data)
for item in data["items"]:
    TAG = item["tag"].replace("#", "%23")
    request = requests.get(url = URL_PLAYER.replace("{TAG}", TAG), params = PARAMS) 
    playerInfo = request.json()
    totalMax = 0
    for card in playerInfo["cards"]:
        if(card["level"] == card["maxLevel"]):
            totalMax = totalMax + 1
    print("%s\t%d"%(playerInfo["name"], totalMax))