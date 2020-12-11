import requests


def request(gender):
    url = f"https://randomuser.me/api/?gender={gender}"
    response = requests.get(url).json()
    return response


if __name__ == "__main__":
    gender = input("Enter gender you want: ").strip()
