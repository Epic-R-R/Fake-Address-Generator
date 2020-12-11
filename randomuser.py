import requests


def request():
    url = f"https://randomuser.me/api/"
    response = requests.get(url).json()
    return response


print(request())