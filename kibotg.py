import requests
from datetime import datetime, date

# Стандатные переменные
TOKEN = "5309976823:AAE8RglgFdx2kOFYrmcYcZOfY1X2JRXFizQ"
API_URL = "https://api.telegram.org"
dt_now = datetime.now()
d_now = date.today()


# Определение последней версии обновления
with open("offset", "r", encoding='utf-8') as f:
    LAST_UPDATE = int(f.read())

d1 = d_now.strftime("%Y%m%d")
d2 = dt_now.strftime("%d/%m/%Y %H:%M:%S")
request_url = f"{API_URL}/bot{TOKEN}/getUpdates?offset={LAST_UPDATE+1}"

with open(f"logs/{d1}.log", "a", encoding='utf-8') as f:
    f.write(f"{d2} START, Last update: {LAST_UPDATE}, Request URL: {request_url}, Responce: {requests.get(request_url)} \n")

# START обработки

if str(requests.get(request_url)) != "<Response [200]>":
    with open(f"logs/{d1}.log", "a", encoding='utf-8') as f:
        f.write(f"{d2} STOP - Request Errore \n")
else:
    with open(f"logs/{d1}.log", "a", encoding='utf-8') as f:
        f.write(f"{d2} run processing \n")

        updates = requests.get(request_url).json()

    if len(updates["result"]) == 0:
        with open(f"logs/{d1}.log", "a", encoding='utf-8') as f:
            f.write(f"{d2} STOP - No updates. \n")
    else:
        updates = updates["result"]
        for update in updates:
            update_id = update["update_id"]
            chat_id = update["message"]["chat"]["id"]
            message = update["message"]["text"]

            requests.get(f"{API_URL}/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}")

            with open(f"logs/{d1}.log", "a", encoding='utf-8') as f:
                f.write(f"{d2} receive text:{message}, send message{message}:\n")

            with open("offset", "w") as f:
                f.write(str(update_id))

        with open(f"logs/{d1}.log", "a", encoding='utf-8') as f:
            f.write(f"{d2} STOP\n")