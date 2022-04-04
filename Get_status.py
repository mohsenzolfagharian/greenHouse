import requests


urlGet="http://0ebfd90d5509.ngrok.io/api/v1/state"

def get_Status():
    status = requests.get(urlGet)
    return status.json()


