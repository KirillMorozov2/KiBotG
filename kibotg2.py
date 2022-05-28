import requests
import time
from datetime import datetime, date

def processing(chat_id,message,API_URL,d1,d2):
    # Функция обработчик ответов
    requests.get(f"{API_URL}/sendMessage?chat_id={chat_id}&text={message}")
 #   print(f"Receive text: {message}, send message: {message}:\n")   
    with open(f"LOG{d2}.log", "a", encoding='utf-8') as f:
            f.write(f"{d1} Receive text: {message}, send message: {message}\n")

def main():
    
    TOKEN = "5309976823:AAE8RglgFdx2kOFYrmcYcZOfY1X2JRXFizQ"
    API_URL = f"https://api.telegram.org/bot{TOKEN}"
    
       
    last_update = 0

    while True:
        time.sleep(5)
        dt_now = datetime.now()
        d_now = date.today()
        d1 = dt_now.strftime("%d/%m/%Y %H:%M:%S")
        d2 = d_now.strftime("%Y%m%d")
        request_url = f"{API_URL}/getUpdates?offset={last_update+1}"
              
#        print(f"{d1} REQUEST Last update: Request URL: {request_url}, Responce: {requests.get(request_url)}")
        with open(f"LOG{d2}.log", "a", encoding='utf-8') as f:
            f.write(f"{d1} REQUEST URL: {request_url}, Responce: {requests.get(request_url)} \n")

        updates = requests.get(request_url).json()

        if len(updates["result"]) == 0:
            with open(f"LOG{d2}.log", "a", encoding='utf-8') as f:
                f.write(f"{d1} No updates \n")
     #       print(f"{d1} No updates \n")
            continue
        else:
            updates = updates["result"]
            for update in updates:
                update_id = update["update_id"]
                chat_id = update["message"]["chat"]["id"]
                message = update["message"]["text"]

                processing(chat_id,message,API_URL,d1,d2)
                
                last_update = update_id

if __name__ == "__main__":
    main()