import requests
import FinallValues
from time import sleep


postURL = "http://0ebfd90d5509.ngrok.io/api/v1/sensorlog"

while True:
    x = FinallValues.SensorsData()
    r = requests.post(postURL,x)
    print(r.status_code, x)
    sleep(3)
    
    
    
    
