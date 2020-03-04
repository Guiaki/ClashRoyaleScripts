import requests 
import json
import os
import re
import datetime
import random
from PIL import Image, ImageDraw, ImageFont

def printCards(img, cardList):
    x=2
    y=0
    count=0
    folder = 'TCards'
    fnt = ImageFont.truetype('Clash-Regular.ttf', 10)
    for card in cardList:
        cardImg = Image.open(os.path.join(folder,card['name'].replace(' ','').lower()+'.png'),'r')
        img.paste(cardImg,(x,y),mask=cardImg)
        d = ImageDraw.Draw(img)
        if(' ' in card['name']):
            fchar = card['name'][0]
            cname = re.sub(r'.+ ', '', card['name'])
            cname = fchar+'. '+cname
            if(len(cname)>=9):
                cname=cname[0:9]+'.'
        else:
            cname = card['name']
        d.text((x,y+90), cname+' '+str(card['level']), font=fnt, fill=(0,0,0,255))
        x=x+80
        count=count+1
        if(count==4):
            x=2
            y=105
        elif (count==8):
            break

RESOURCE = "members"
URL_PLAYER = "https://api.clashroyale.com/v1/players/{TAG}"
KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhmZTU4ZThiLTk3OTQtNDRlMC04YWUzLTJlMzhjYmQ0MTQ0MCIsImlhdCI6MTU3NDI4Nzk0MSwic3ViIjoiZGV2ZWxvcGVyLzQwMTU4ZjAxLTU2ZGItNTFmNS0wZmMwLTNhZTFiMWM5MmUzZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODkuNC4xMTIuMjA4Il0sInR5cGUiOiJjbGllbnQifV19.AQiOtT7y3dp1xCtAikDFYS76uiWr1kZBJTy8qvorClt8KDMdkeH9SuxbH__oPE6g43dxaxvWxZZYP2K7zbnNHQ"
DECK = ["Giant", "Hunter", "Minion Horde", "Dart Goblin", "Zap", "Goblin Barrel", "Princess", "Mega Minion"]
IDS = {'Bomber': 26000013, 'Wizard': 26000017, 'Minions': 26000005, 'Fisherman': 26000061, 'Lava Hound': 26000029, 'Mirror': 28000006, 'Wall Breakers': 26000058, 'Prince': 26000016, 'Goblin Gang': 26000041, 'Hunter': 26000044, 'Clone': 28000013, 'Elixir Collector': 27000007, 'Lumberjack': 26000035, 'Mini P.E.K.K.A': 26000018, 'Bats': 26000049, 'Baby Dragon': 26000015, 'Golem': 26000009, 'Lightning': 28000007, 'Inferno Dragon': 26000037, 'Dart Goblin': 26000040, 'Goblin Cage': 27000012, 'Skeleton Army': 26000012, 'Elite Barbarians': 26000043, 'Royal Recruits': 26000047, 'Sparky': 26000033, 'Electro Dragon': 26000063, 'The Log': 28000011, 'Balloon': 26000006, 'Zappies': 26000052, 'Guards': 26000025, 'Graveyard': 28000010, 'Freeze': 28000005, 'Bowler': 26000034, 'Mega Minion': 26000039, 'Knight': 26000000, 'Goblin Hut': 27000001, 'Goblin Barrel': 28000004, 'Electro Wizard': 26000042, 'Tornado': 28000012, 'Magic Archer': 26000062, 'Arrows': 28000001, 'Goblin Giant': 26000060, 'Musketeer': 26000014, 'Royal Hogs': 26000059, 'Cannon Cart': 26000054, 'Spear Goblins': 26000019, 'Three Musketeers': 26000028, 'Rascals': 26000053, 'Fire Spirits': 26000031, 'Mortar': 27000002, 'Rocket': 28000003, 'X-Bow': 27000008, 'Cannon': 27000000, 'Bandit': 26000046, 'Giant': 26000003, 'Zap': 28000008, 'Furnace': 27000010, 'Poison': 28000009, 'Skeleton Barrel': 26000056, 'Barbarian Hut': 27000005, 'Fireball': 28000000, 'Ram Rider': 26000051, 'Bomb Tower': 27000004, 'Minion Horde': 26000022, 'Barbarians': 26000008, 'Dark Prince': 26000027, 'Heal': 28000016, 'Royal Giant': 26000024, 'Tombstone': 27000009, 'Elixir Golem': 26000067, 'Ice Wizard': 26000023, 'Miner': 26000032, 'Battle Ram': 26000036, 'Night Witch': 26000048, 'Executioner': 26000045, 'Rage': 28000002, 'Ice Spirit': 26000030, 'Mega Knight': 26000055, 'Giant Skeleton': 26000020, 'Tesla': 27000006, 'Goblins': 26000002, 'P.E.K.K.A': 26000004, 'Princess': 26000026, 'Witch': 26000007, 'Royal Ghost': 26000050, 'Flying Machine': 26000057, 'Ice Golem': 26000038, 'Archers': 26000001, 'Barbarian Barrel': 28000015, 'Earthquake': 28000014, 'Giant Snowball': 28000017, 'Hog Rider': 26000021, 'Inferno Tower': 27000003, 
'Skeletons': 26000010, 'Valkyrie': 26000011}

PARAMS = {'Authorization':'Bearer '+KEY, 'Accept':'application/json'}

TAG = "#RL9JYYQP"
TAG = TAG.replace("#", "%23")
request = requests.get(url = URL_PLAYER.replace("{TAG}", TAG), params = PARAMS) 
playerInfo = request.json()
totalMax = 0
cardList = {}
highestLevel = 0
newDeck = []

for card in playerInfo["cards"]:
    level = card["level"]
    if (level > highestLevel):
        highestLevel = level
    if(card["maxLevel"]==11):
        level+=2
    if(card["maxLevel"]==5):
        level+=8
    if(card["maxLevel"]==8):
        level+=5
    cardList[card["name"]] = level

elixirSum = 0
link = "https://link.clashroyale.com/deck/en?deck="
cardsToPrint = []

for x in range (0,len(DECK)):
    print('%s'%DECK[x])
    link = link + str(IDS[DECK[x]]) + ";"
    cartinha = {}
    cartinha["name"] = DECK[x].replace("-","").replace(" ","").replace(".","")
    cartinha["level"] = cardList[DECK[x]]
    cardsToPrint.append(cartinha)

img = Image.new('RGBA', (335, 210), (255,255,255,0))            
printCards(img, cardsToPrint)
img.save(os.path.join('deckList',playerInfo["name"].replace('*','')+'.png'), format="png")
print("%s\t%s\t%s"%(playerInfo["name"], DECK, link[:-1]))
