import requests
import re
from randomuser import request

BOT_TOKEN = "1463819644:AAEJ7cZLqHr5wrEROJL_lWDxzklQsBTZ6nc"
base_url = f"https://api.telegram.org/bot{BOT_TOKEN}"


# create func that get chat id
def get_chat_id(update):
    chat_id = update["message"]["chat"]["id"]
    return chat_id


# create func that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# create func that get last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]


# create func that let bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(base_url + "sendMessage", data=params)
    return response


# create main func for navigate or reply message back
def main():
    update_id = last_update(req=base_url)["update_id"]
    while True:
        update = last_update(req=base_url)
        if update_id == update["update_id"]:
            if (
                get_message_text(update).lower() == "hi"
                or get_message_text(update) == "/start"
                or get_message_text(update).lower() == "hello"
            ):
                send_message(
                    get_chat_id(update),
                    "Commands:👇\n /fake: Send Fake Address",
                )

            elif get_message_text(update).lower() == "/fake":
                data = request()
                message = f"""
                Name: {data["results"][0]['name']}
                """
                send_message(get_chat_id(update), request())
                print(
                    f"\033[33mFake Address Send. \nDog Picture Url -> {get_dog_pic()}\033[39m"
                )
            else:
                send_message(
                    get_chat_id(update), "Sorry Not Understand What You Inputted :("
                )
            update_id += 1


if __name__ == "__main__":
    print("\033[32mBot Starting\033[39m")
    main()