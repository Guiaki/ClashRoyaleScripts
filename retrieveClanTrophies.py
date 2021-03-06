import requests 
import json
import threading

class retrieveThread(threading.Thread):
    def __init__(self, TAG):
        threading.Thread.__init__(self)
        self.curBest = 0
        self.tag = TAG

    def run(self):
        request = requests.get(url = URL_PLAYER.replace("{TAG}", self.tag), params = PARAMS) 
        playerInfo = request.json()
        if "previousSeason" in playerInfo["leagueStatistics"]:
            self.curBest = playerInfo["leagueStatistics"]["previousSeason"]["trophies"]
        points = ((self.curBest-4000)*0.75)+4000  
        if(points > 5800):
            points = 5800
        bestSeasonTrophies = points
        if "bestTrophies" in playerInfo["leagueStatistics"]["currentSeason"]:
            bestSeasonTrophies = playerInfo["leagueStatistics"]["currentSeason"]["bestTrophies"]
        if (self.curBest<4000):
            points = bestSeasonTrophies
        print("%s--%d--%d--%d"%(playerInfo["name"], bestSeasonTrophies, points, bestSeasonTrophies-points))

PLAYER_ARRAY = []
START_DATE = "14/05/2019"
CLAN_KEY = "#2JJYLY2"
CLAN_KEY = CLAN_KEY.replace("#", "%23") if CLAN_KEY.find("#") != -1 else "%23"+CLAN_KEY
RESOURCE = "members"
URL = "https://api.clashroyale.com/v1/clans/{CLAN_KEY}/{RESOURCE}"
URL_PLAYER = "https://api.clashroyale.com/v1/players/{TAG}"
KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjIxNDk4M2YxLTU2NjQtNGIyNS04OWFjLTE2NTRiOWRhYjU3OSIsImlhdCI6MTU4MzE2Njg3Mywic3ViIjoiZGV2ZWxvcGVyLzQwMTU4ZjAxLTU2ZGItNTFmNS0wZmMwLTNhZTFiMWM5MmUzZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTEuMTkxLjI2LjEyNiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.pAKhsiIFxCA5SwNm9RTRmnjA6WsGr0NZbVjgRjYDYmsF7Tky1sCqL97VzdZhbcZ6ipmXekMtbhl4G8k32S21tQ"
URL = URL.replace("{CLAN_KEY}", CLAN_KEY)
URL = URL.replace("{RESOURCE}", RESOURCE)

threadLock = threading.Lock()
threads = []
PARAMS = {'Authorization':'Bearer '+KEY, 'Accept':'application/json'} 
r = requests.get(url = URL, params = PARAMS)   
data = r.json()
for item in data["items"]:
    TAG = item["tag"].replace("#", "%23")
    try:
        thread = retrieveThread(TAG).start()
        threads.append(thread)
    except:
        print ("Error: unable to start thread")