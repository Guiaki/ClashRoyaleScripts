import requests 
import datetime
import json

def findInArray(player_aux):
    index = 0
    for jogador in PLAYER_ARRAY:
        if (jogador['user']["name"] == player_aux):
            return index
        index = index + 1
    return -1

SEASON_MAX_COLLECT = []
PLAYER_ARRAY = []
START_DATE = "14/05/2019"
DATE_START = datetime.datetime.strptime(START_DATE, "%d/%m/%Y")
CLAN_KEY = "#2JJYLY2"
CLAN_KEY = CLAN_KEY.replace("#", "%23") if CLAN_KEY.find("#") != -1 else "%23"+CLAN_KEY
RESOURCE = "warlog"
URL = "https://api.clashroyale.com/v1/clans/{CLAN_KEY}/{RESOURCE}"
KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjUyNTAxNzcyLTFmOTEtNGVhOS1hMzdlLTcxMWI0NzdhM2EyYyIsImlhdCI6MTU2MjAyNzI4Nywic3ViIjoiZGV2ZWxvcGVyLzQwMTU4ZjAxLTU2ZGItNTFmNS0wZmMwLTNhZTFiMWM5MmUzZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODkuNC43Ni4xNzIiXSwidHlwZSI6ImNsaWVudCJ9XX0.Szjwc_eeYb0NuXqar3vEM5iYyftVwWUfyqM8CTxPlLrpk_yciCh_kFby1k1qV4wHoReyyBedYFFjJz-X5Jt9tg"
URL = URL.replace("{CLAN_KEY}", CLAN_KEY)
URL = URL.replace("{RESOURCE}", RESOURCE)

PARAMS = {'Authorization':'Bearer '+KEY, 'Accept':'application/json'} 
r = requests.get(url = URL, params = PARAMS)   
data = r.json()
indexSeason = 0
for item in data["items"]:
    dateTimeStr = item["createdDate"]
    dateTime = datetime.datetime.strptime(dateTimeStr[:8], "%Y%m%d")
    if(dateTime >= DATE_START):
        print("Season: %d"%item["seasonId"])
        FIRST = True
        for player_aux in item["participants"]:
            user = findInArray(player_aux["name"])
            if(FIRST):
                SEASON_MAX_COLLECT.append({indexSeason : player_aux["cardsEarned"]})
                FIRST = False
            if(player_aux["cardsEarned"] > SEASON_MAX_COLLECT[indexSeason][indexSeason]):
                SEASON_MAX_COLLECT[indexSeason] = {indexSeason : player_aux["cardsEarned"]}
            if(user!=-1):
                PLAYER_ARRAY[user]['winsWar'].append({indexSeason : player_aux["wins"]})
                PLAYER_ARRAY[user]['cardsCollected'].append({indexSeason : player_aux["cardsEarned"]})
            else:
                player = {}
                player['user'] = player_aux
                player['winsWar'] = []
                player['winsWar'].append({indexSeason : player_aux["wins"]})
                player['cardsCollected'] = []
                player['cardsCollected'].append({indexSeason : player_aux["cardsEarned"]})
                PLAYER_ARRAY.append(player)
        indexSeason = indexSeason + 1

for jogador in PLAYER_ARRAY:
    pontosCol = 0
    for row in jogador['cardsCollected']:
        for key, val in row.items():
            if(val == SEASON_MAX_COLLECT[key][key]):
                pontosCol = pontosCol + 2
    pontosWin = 0
    for row in jogador['winsWar']:
        for key, val in row.items():
            pontosWin = pontosWin + 3*val
    print("%s\t%s\t%s\t%s\t%s"%(jogador['user']["name"],jogador['cardsCollected'],jogador['winsWar'],pontosCol,pontosWin))
print(SEASON_MAX_COLLECT)