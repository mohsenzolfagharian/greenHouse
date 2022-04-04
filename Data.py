import Adafruit_DHT
import re
import serial

ser = serial.Serial('/dev/ttyACM0',9600)

sensorType = Adafruit_DHT.DHT11
gpio = 17

def SensorsData():
    analogsValue = []
    humidity, temperature = Adafruit_DHT.read_retry(sensorType, gpio)
    dataArduino = ser.readline()
    dataArduino = dataArduino.decode('utf8')
    dataArduino = re.sub("['a-zA-Z]","",dataArduino)
    while (len(analogsValue) < 2):
        analogsValue.append(float(dataArduino))
    mydata ={"temp_dht":temperature,
             "humidity_dht":humidity,
             "light":analogsValue[0],
             "dust_humidity":analogsValue[1],
             "pomp_status":False,
             "lamp_status":False}
    return mydata

# test functions
# x = SensorsData()
# print(x)
