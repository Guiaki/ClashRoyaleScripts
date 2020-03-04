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

TAG = "#U9V2LPJ0"
URL_PLAYER = "https://api.clashroyale.com/v1/players/{TAG}"
KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhmZTU4ZThiLTk3OTQtNDRlMC04YWUzLTJlMzhjYmQ0MTQ0MCIsImlhdCI6MTU3NDI4Nzk0MSwic3ViIjoiZGV2ZWxvcGVyLzQwMTU4ZjAxLTU2ZGItNTFmNS0wZmMwLTNhZTFiMWM5MmUzZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODkuNC4xMTIuMjA4Il0sInR5cGUiOiJjbGllbnQifV19.AQiOtT7y3dp1xCtAikDFYS76uiWr1kZBJTy8qvorClt8KDMdkeH9SuxbH__oPE6g43dxaxvWxZZYP2K7zbnNHQ"
WIN_CONDITIONS = {"Mortar", "Royal Giant", "Elixir Golem", "Hog Rider", "Battle Ram", "Giant", "Royal Hogs", "Rocket", "Three Musketeers", "Goblin Barrel", "Balloon", "X-Bow", "Goblin Giant", "P.E.K.K.A", "Golem", "Miner", "Ram Rider", "Graveyard", "Sparky", "Lava Hound"}
LIGHT_SPELLS = {"Tornado", "The Log", "Poison", "Zap", "Giant Snowball", "Barbarian Barrel", "Arrows", "Earthquake"}
HEAVY_SPELLS = {"Poison", "Lightning", "Rocket", "Fireball"}
ANTI_AIR = {"Executioner", "Bats", "Magic Archer", "Electro Wizard", "Baby Dragon", "Ice Wizard", "Mega Minion", "Musketeer", "Tesla", "Archers", "Princess", "Inferno Dragon", "Dart Goblin", "Minions", "Inferno Tower", "Wizard", "Rascals", "Spear Goblins", "Witch", "Minion Horde", "Hunter", "Three Musketeers", "Electro Dragon", "Zappies"}
ELIXIR = {'Bomber': 3, 'Wizard': 5, 'Minions': 3, 'Fisherman': 3, 'Lava Hound': 7, 'Mirror': 1, 'Wall Breakers': 2, 'Prince': 5, 'Goblin Gang': 3, 'Hunter': 4, 'Clone': 3, 'Elixir Collector': 6, 'Lumberjack': 4, 'Mini P.E.K.K.A': 4, 'Bats': 2, 'Baby Dragon': 4, 'Golem': 8, 'Lightning': 6, 'Inferno Dragon': 4, 'Dart Goblin': 3, 'Goblin Cage': 4, 'Skeleton Army': 3, 'Elite Barbarians': 6, 'Royal Recruits': 7, 'Sparky': 6, 'Electro Dragon': 5, 'The Log': 2, 'Balloon': 5, 'Zappies': 4, 'Guards': 3, 'Graveyard': 5, 'Freeze': 4, 'Bowler': 5, 'Mega Minion': 3, 'Knight': 3, 'Goblin Hut': 5, 'Goblin Barrel': 3, 'Electro Wizard': 4, 'Tornado': 3, 'Magic Archer': 4, 'Arrows': 3, 'Goblin Giant': 6, 'Musketeer': 4, 'Royal Hogs': 5, 'Cannon Cart': 5, 'Spear Goblins': 2, 'Three Musketeers': 9, 'Rascals': 5, 'Fire Spirits': 2, 'Mortar': 4, 'Rocket': 6, 'X-Bow': 6, 'Cannon': 3, 'Bandit': 3, 'Giant': 5, 'Zap': 2, 'Furnace': 4, 'Poison': 4, 'Skeleton Barrel': 3, 'Barbarian Hut': 7, 'Fireball': 4, 'Ram Rider': 5, 'Bomb Tower': 4, 'Minion Horde': 5, 'Barbarians': 5, 'Dark Prince': 4, 'Heal': 1, 'Royal Giant': 6, 'Tombstone': 3, 'Elixir Golem': 3, 'Ice Wizard': 3, 'Miner': 3, 'Battle Ram': 4, 'Night Witch': 4, 'Executioner': 5, 'Rage': 2, 'Ice Spirit': 1, 'Mega Knight': 7, 'Giant Skeleton': 6, 'Tesla': 4, 'Goblins': 2, 'P.E.K.K.A': 7, 'Princess': 3, 'Witch': 5, 'Royal Ghost': 3, 'Flying Machine': 4, 'Ice Golem': 2, 'Archers': 3, 'Barbarian Barrel': 2, 'Earthquake': 3, 'Giant Snowball': 2, 'Hog Rider': 4, 'Inferno Tower': 5, 'Skeletons': 1, 'Valkyrie': 4}
IDS = {'Bomber': 26000013, 'Wizard': 26000017, 'Minions': 26000005, 'Fisherman': 26000061, 'Lava Hound': 26000029, 'Mirror': 28000006, 'Wall Breakers': 26000058, 'Prince': 26000016, 'Goblin Gang': 26000041, 'Hunter': 26000044, 'Clone': 28000013, 'Elixir Collector': 27000007, 'Lumberjack': 26000035, 'Mini P.E.K.K.A': 26000018, 'Bats': 26000049, 'Baby Dragon': 26000015, 'Golem': 26000009, 'Lightning': 28000007, 'Inferno Dragon': 26000037, 'Dart Goblin': 26000040, 'Goblin Cage': 27000012, 'Skeleton Army': 26000012, 'Elite Barbarians': 26000043, 'Royal Recruits': 26000047, 'Sparky': 26000033, 'Electro Dragon': 26000063, 'The Log': 28000011, 'Balloon': 26000006, 'Zappies': 26000052, 'Guards': 26000025, 'Graveyard': 28000010, 'Freeze': 28000005, 'Bowler': 26000034, 'Mega Minion': 26000039, 'Knight': 26000000, 'Goblin Hut': 27000001, 'Goblin Barrel': 28000004, 'Electro Wizard': 26000042, 'Tornado': 28000012, 'Magic Archer': 26000062, 'Arrows': 28000001, 'Goblin Giant': 26000060, 'Musketeer': 26000014, 'Royal Hogs': 26000059, 'Cannon Cart': 26000054, 'Spear Goblins': 26000019, 'Three Musketeers': 26000028, 'Rascals': 26000053, 'Fire Spirits': 26000031, 'Mortar': 27000002, 'Rocket': 28000003, 'X-Bow': 27000008, 'Cannon': 27000000, 'Bandit': 26000046, 'Giant': 26000003, 'Zap': 28000008, 'Furnace': 27000010, 'Poison': 28000009, 'Skeleton Barrel': 26000056, 'Barbarian Hut': 27000005, 'Fireball': 28000000, 'Ram Rider': 26000051, 'Bomb Tower': 27000004, 'Minion Horde': 26000022, 'Barbarians': 26000008, 'Dark Prince': 26000027, 'Heal': 28000016, 'Royal Giant': 26000024, 'Tombstone': 27000009, 'Elixir Golem': 26000067, 'Ice Wizard': 26000023, 'Miner': 26000032, 'Battle Ram': 26000036, 'Night Witch': 26000048, 'Executioner': 26000045, 'Rage': 28000002, 'Ice Spirit': 26000030, 'Mega Knight': 26000055, 'Giant Skeleton': 26000020, 'Tesla': 27000006, 'Goblins': 26000002, 'P.E.K.K.A': 26000004, 'Princess': 26000026, 'Witch': 26000007, 'Royal Ghost': 26000050, 'Flying Machine': 26000057, 'Ice Golem': 26000038, 'Archers': 26000001, 'Barbarian Barrel': 28000015, 'Earthquake': 28000014, 'Giant Snowball': 28000017, 'Hog Rider': 26000021, 'Inferno Tower': 27000003, 
'Skeletons': 26000010, 'Valkyrie': 26000011}

PARAMS = {'Authorization':'Bearer '+KEY, 'Accept':'application/json'} 
TAG = TAG.replace("#", "%23")
request = requests.get(url = URL_PLAYER.replace("{TAG}", TAG), params = PARAMS) 
playerInfo = request.json()
totalMax = 0
cardList = {}
highestLevel = 0
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
HLWC = []
HLLS = []
HLHS = []
HLAA = []
HLCARDS = []

begin = datetime.datetime.now()
#print("%s start"%playerInfo["name"])
for card in cardList:
    if(cardList[card] == highestLevel or cardList[card] == highestLevel-1):
        if(card in WIN_CONDITIONS):
            HLWC.append(card)
            HLCARDS.append(card)
        if(card in LIGHT_SPELLS):
            HLLS.append(card)
        if(card in HEAVY_SPELLS):
            HLHS.append(card)
        if(card in ANTI_AIR):
            HLAA.append(card)
            HLCARDS.append(card)
#print("%s make CardList max/semi"%playerInfo["name"])
if(len(HLCARDS)<10):
    for card in cardList:
        if(cardList[card] == highestLevel-2):
            if(card in WIN_CONDITIONS):
                HLWC.append(card)
                HLCARDS.append(card)
            if(card in LIGHT_SPELLS):
                HLLS.append(card)
            if(card in HEAVY_SPELLS):
                HLHS.append(card)
            if(card in ANTI_AIR):
                HLAA.append(card)
                HLCARDS.append(card)
    #print("%s increase with -2 levels"%playerInfo["name"])

averageElixir = 5.5
start_time = datetime.datetime.now()
#print("%s start deckManager time: %d"%(playerInfo["name"],(start_time-begin).microseconds))
while(averageElixir > 4.5):
    newDeck = []
    if(HLWC):
        newDeck.append(random.choice(HLWC))
    if(HLAA):
        newDeck.append(random.choice(HLAA))
    rInt = random.randint(0,100)
    if(rInt <= 50):
        if (HLHS):
            newDeck.append(random.choice(HLHS))
    else:
        if(HLLS):
            newDeck.append(random.choice(HLLS))
    
    #print("%s made first picks time: %d"%(playerInfo["name"],(datetime.datetime.now()-begin).seconds))
    loopStart = datetime.datetime.now()
    if(rInt <= 50):
        if(HLLS):
            escolhido = random.choice(HLLS)
            while escolhido in newDeck:
                escolhido = random.choice(HLLS)
                if((loopStart - datetime.datetime.now()).seconds > 10):
                    break
            newDeck.append(escolhido)
    if(rInt <= 10):
        if(HLLS):
            escolhido = random.choice(HLLS)
            while escolhido in newDeck:
                escolhido = random.choice(HLLS)
                if((loopStart - datetime.datetime.now()).seconds > 10):
                    break
            newDeck.append(escolhido)
        
    #print("%s made spells picks time: %d"%(playerInfo["name"],(datetime.datetime.now()-begin).seconds))
    iteracoes = 0
    while len(newDeck) < 8:
        if(HLCARDS):
            escolhido = random.choice(HLCARDS)
            loopStart = datetime.datetime.now()
            while escolhido in newDeck:
                escolhido = random.choice(HLCARDS)
                if((loopStart - datetime.datetime.now()).seconds > 10):
                    break
            newDeck.append(escolhido)
        iteracoes = iteracoes + 1
        if(iteracoes >= 30):
            newDeck = "DEU RUIM"
    elixirSum = 0
    #print("%s create full deck time: %d"%(playerInfo["name"],(datetime.datetime.now()-begin).seconds))
    link = "https://link.clashroyale.com/deck/en?deck="
    if(newDeck != "DEU RUIM"):
        countWC = 0
        for card in newDeck:
            link = link + str(IDS[card]) + ";"
            elixirSum = elixirSum + ELIXIR[card]
            if(card in HLWC):
                countWC = countWC+1
        averageElixir = elixirSum/len(newDeck)
        cardsToPrint = []
        if(countWC>3):
            averageElixir = 6
        for card in newDeck:
            cartinha = {}
            cartinha["name"] = card.replace("-","").replace(" ","").replace(".","")
            cartinha["level"] = cardList[card]
            cardsToPrint.append(cartinha)
        
        #print("%s everything is done, averageElixir: %f time: %d"%(playerInfo["name"], averageElixir, (datetime.datetime.now()-begin).seconds))
    else:
        #print("%s DEU RUIM time: %d"%(playerInfo["name"],(datetime.datetime.now()-begin).seconds))
        break

    if ((datetime.datetime.now() - start_time).seconds >= 20):
        #print("%s exceed max time time: %d"%(playerInfo["name"],(datetime.datetime.now()-begin).seconds))
        newDeck = "DEU RUIM"
        break

img = Image.new('RGBA', (335, 210), (255,255,255,0))            
printCards(img, cardsToPrint)
img.save(os.path.join('deckList',playerInfo["name"].replace('*','')+'.png'), format="png")
print("%s\t%s\t%s"%(playerInfo["name"], newDeck, link[:-1]))
