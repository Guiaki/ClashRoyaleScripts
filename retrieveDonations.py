DONATIONS_TOP_1 = ['Flap','Flap','Flap']
DONATIONS_TOP_2 = ['Duka', 'Duka', 'O time do povo', 'Thor', 'O time do povo']
DONATIONS_TOP_3 = ['junior ninão', 'Mtk', 'O time do povo', 'Gustavo clash', 'Bruno', 'junior ninão', 'Duka', 'Tiago', 'Thor', 'Bruno']

PLAYERS = []

def findInArray(player_aux):
    index = 0
    for row in PLAYERS:
        for key, val in row.items():
            if (key == player_aux):
                return index
        index = index + 1
    return -1

print("\t".join(str(x) for x in DONATIONS_TOP_1))
print("\t".join(str(x) for x in DONATIONS_TOP_2))
print("\t".join(str(x) for x in DONATIONS_TOP_3))

for x in DONATIONS_TOP_1:
    user = findInArray(x)
    if(user!=-1):
        PLAYERS[user][x] = PLAYERS[user][x] + 8
    else:
        PLAYERS.append({x: 8})

for x in DONATIONS_TOP_2:
    user = findInArray(x)
    if(user!=-1):
        PLAYERS[user][x] = PLAYERS[user][x] + 5
    else:
        PLAYERS.append({x: 5})

for x in DONATIONS_TOP_3:
    user = findInArray(x)
    if(user!=-1):
        PLAYERS[user][x] = PLAYERS[user][x] + 3
    else:
        PLAYERS.append({x: 3})

for player in PLAYERS:
    for key, val in player.items():
        print("%s\t%d"%(key, val))