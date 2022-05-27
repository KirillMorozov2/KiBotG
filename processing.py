import requests
request_url = "https://api.telegram.org/bot5309976823:AAE8RglgFdx2kOFYrmcYcZOfY1X2JRXFizQ/getUpdates"
updates = requests.get(request_url).json()

r = updates["result"][0]
m1 = updates["result"][0]["message"]["message_id"]
m2 = updates["result"][1]["message"]["message_id"]

print(r)
print(m1)
print(m2)


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
#    print("Последнее обновление устаовлено:")