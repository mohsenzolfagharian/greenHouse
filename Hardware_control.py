import RPi.GPIO as GPIO
import Get_status

GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 22
RELAIS_2_GPIO = 20
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT)
def on_off():
    hardware_status = Get.get_Status()
    if hardware_status["pomp_status"]:
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    elif hardware_status["pomp_status"] == False:
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    if hardware_status["lamp_status"]:
        GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
    elif hardware_status["lamp_status"] == False:
        GPIO.output(RELAIS_2_GPIO, GPIO.LOW)




















