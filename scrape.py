import json
import requests
from datetime import datetime
teamList = ["81P",
"91A",
"574C",
"905A",
"2011C",
"2616J",
"4001A",
"4478D",
"4478V",
"5203R",
"6105C",
"7701T",
"7701X",
"7870E",
"8349E",
"9181Z",
"9922Z",
"41364A",
"45464Z",
"81118P"]
datetimes = []
scores = []
for team in teamList:
    raw = requests.get("http://api.vexdb.io/v1/get_matches?team=" + team + "&season=Tower Takeover")
    results = raw.json()['result']
    for elem in results:
        if((elem['red1'] == team or elem['red2'] == team) and "1970-01-01" not in elem['scheduled']):
            datetime_obj = datetime.fromisoformat(elem['scheduled'])
            datetimes.append(datetime_obj.date())
            # day = str(datetime_obj.day)
            # month = str(datetime_obj.month)
            #
            # if(len(day) == 1):
            #     day = "0" + day
            #     #print(day)
            # if(len(month) == 1):
            #     month = "0" + month
            #     #print(month)
            # datetimes.append( day + "-" + month + "-" + str(datetime_obj.year)[2:])
            scores.append((elem['redscore']))
        if((elem['blue1'] == team or elem['blue2'] == team) and "1970-01-01" not in elem['scheduled']):
            datetime_obj = datetime.fromisoformat(elem['scheduled'])
            datetimes.append(datetime_obj.date())
            # day = str(datetime_obj.day)
            # month = str(datetime_obj.month)
            #
            # if(len(day) == 1):
            #     day = "0" + day
            #     #print(day)
            # if(len(month) == 1):
            #     month = "0" + month
            # datetimes.append( day + "-" + month + "-" + str(datetime_obj.year)[2:])
            scores.append((elem['bluescore']))
datetimes, scores = (list(t) for t in zip(*sorted(zip(datetimes, scores))))
i = 0
while(i < len(datetimes)):
    print(str(scores[i]))
    i+=1
#print(datetimes)
