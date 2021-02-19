import requests
import json
import datetime
import sched, time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
daysList = []
valuesList = []

def today():
    today = datetime.date.today()
    print(f"{today.year}-{today.month}-{today.day-1}")
    return f"{today.year}-{today.month}-{today.day-1}"


def get_btc_price():
    json_req = requests.get(f"https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-05&end=2021-02-18").text
    print(json_req)
    dico = json.loads(json_req)
    dicoValeurs = dico['bpi']
    daysList = []
    valuesList = []
    for i in dicoValeurs.keys():
        daysList.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
        valuesList.append(dicoValeurs[i])
        
    return (daysList,valuesList)
        
    
ax.clear()
price = get_btc_price()
ax.plot(price[0], price[1])
    
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.title('Bitcoin price over time')
plt.ylabel('price (USD)')
plt.xlabel('time')

plt.show()
