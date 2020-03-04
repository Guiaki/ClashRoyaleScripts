import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

scope = ['https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('ClashDecks-ada7d9db79c1.json', scope)

gc = gspread.authorize(credentials)

sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/16p634Ny_xAIlMjtPdCKItZxiEyQ6KSEmulqs55V-oIs/edit?usp=sharing')

worksheet = sht2.get_worksheet(0)
cell_list = worksheet.range('A2:C51')

PLAYER_LIST = []
currentUser = ""
for cell in cell_list:
    if(cell.value[0] != "[" and cell.value[0:3] != "htt"):
        currentUser = cell.value
    if(cell.value[0:3] == "htt"):
        deck = []
        link = cell.value.replace("https://link.clashroyale.com/deck/en?deck=","")
        card = ""
        for x in range (0,len(link)):
            if(x == len(link)-1):
                card = card + link[x]
                deck.append(card)
                break
            if(link[x] != ";"):
                card = card + link[x]
            else:
                deck.append(card)
                card = ""
        PLAYER_LIST.append({"name": currentUser, "deck": deck})
