import requests
import FinallValues
#import Get
from time import sleep


postURL = "http://0ebfd90d5509.ngrok.io/api/v1/sensorlog"

while True:
#    y = Get.get_Status()
    x = FinallValues.SensorsData()
#    x["lamp_status"] = y["lamp_status"]
#    x["pomp_status"] = y["pomp_status"]
    r = requests.post(postURL,x)
    print(r.status_code, x)
    sleep(3)
    
    
    
    
