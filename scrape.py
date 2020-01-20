import json
import requests
from datetime import datetime
teamList = []
rawTeams = requests.get("http://api.vexdb.io/v1/get_teams?region=Pennsylvania&program=VRC&grade=High School")
resultsTeam = rawTeams.json()['result']
for team in resultsTeam:
    teamNum = team['number']
    teamList.append(teamNum)
datetimes = []
scores = []
for team in teamList:
    raw = requests.get("http://api.vexdb.io/v1/get_matches?team=" + team + "&season=Tower Takeover")
    results = raw.json()['result']
    for elem in results:
        if((elem['red1'] == team or elem['red2'] == team) and "1970-01-01" not in elem['scheduled']):
            datetime_obj = datetime.fromisoformat(elem['scheduled'])
            datetimes.append(datetime_obj.date())
            scores.append((elem['redscore']))
        if((elem['blue1'] == team or elem['blue2'] == team) and "1970-01-01" not in elem['scheduled']):
            datetime_obj = datetime.fromisoformat(elem['scheduled'])
            datetimes.append(datetime_obj.date())
            scores.append((elem['bluescore']))
datetimes, scores = (list(t) for t in zip(*sorted(zip(datetimes, scores))))
i = 0
with open('Pennsylvania.csv', 'a') as f:
    f.write("Pennsylvania\n")
    while(i < len(datetimes)):
        f.write(str(scores[i]) + "\n")
        i+=1
