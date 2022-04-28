import requests

BASE = "https://randomuser.me/api"

def gen_user():
    return requests.get(BASE).json()["results"][0]

def get_name(data):
    return data["name"]["first"] + " " + data["name"]["last"]

