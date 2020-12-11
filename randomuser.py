import json

with open("tes.json", "r") as fp:
    data = json.loads(fp.read())

name = data["results"][0]["name"]
location = data["results"][0]["location"]
print(
    f"""
Name       : {name["title"]}.{name["first"]} {name["last"]}
Street     : {location["street"]["number"]} {location["street"]["name"]}
city       : {location["city"]}
state      : {location["state"]}
country    : {location["country"]}
postcode   : {location["postcode"]}
email      : {data["results"][0]["email"]}
phone      : {data["results"][0]["phone"]}
"""
)
