import requests

# Стандатные переменные
TOKEN = "5309976823:AAE8RglgFdx2kOFYrmcYcZOfY1X2JRXFizQ"
API_URL = "https://api.telegram.org"

# Определение последней версии обновления
with open("offset", "r") as f:
    LAST_UPDATE = int(f.read())
print("Запрашиваем обновление: " + str(LAST_UPDATE+1))

# Вывод на экран URL запроса
request_url = f"{API_URL}/bot{TOKEN}/getUpdates?offset={LAST_UPDATE+1}"
print(request_url)

response = str(requests.get(request_url))

if response == "<Response [200]>":
    print("Запрос успешен: " + response)





#updates = updates["result"]


# for update in updates:
#    update_id = update["update_id"]
#    chat_id = update["message"]["chat"]["id"]
#    message = update["message"]["text"]
#
#
#    print("Последнее обновление: " + str(update_id))
#    print(f"{API_URL}/bot{TOKEN}/sendMesssage?chat_id={chat_id}&text={message}")
#    requests.get(f"{API_URL}/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}")
#    with open("offset", "w") as f:
#        f.write(str(update_id))
#    print("Последнее обновление устаовлено: