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