import requests
from datetime import datetime, date


# Стандатные переменные
TOKEN = "5309976823:AAE8RglgFdx2kOFYrmcYcZOfY1X2JRXFizQ"
API_URL = "https://api.telegram.org"
dt_now = datetime.now()
d_now = date.today()


# Определение последней версии обновления
with open("offset", "r") as f:
    LAST_UPDATE = int(f.read())

d1 = d_now.strftime("%Y%m%d")
d2 = dt_now.strftime("%d/%m/%Y %H:%M:%S")
request_url = f"{API_URL}/bot{TOKEN}/getUpdates?offset={LAST_UPDATE+1}"


with open(f"logs/{d1}log.log", "a") as f:
    f.write(d2 + " Запрашиваем обновление: " + str(LAST_UPDATE) + "\n")
    f.write(d2 + " Запрашиваем обновление: " + request_url + "\n")
    f.write(d2 + " Запрашиваем обновление: " + str(requests.get(request_url)) + "\n")


# START обработки

if str(requests.get(request_url)) != "<Response [200]>":
    with open(f"logs/{d1}log.log", "a") as f:
        f.write(d2 + " STOP Request Errore \n")
else:
    with open(f"logs/{d1}log.log", "a") as f:
        f.write(d2 + " Start processing \n")





