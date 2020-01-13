import json
import requests

raw = requests.get("http://api.vexdb.io/v1/get_matches?team=2616J&season=Tower Takeover")
results = raw.json()['result']
for elem in results:
    if(elem['red1'] == "2616J" or elem['red2'] == "2616J"):
        print(elem['redscore'])
    elif(elem['blue1'] == "2616J" or elem['blue2'] == "2616J"):
        print(elem['bluescore'])
