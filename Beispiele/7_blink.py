import RPi.GPIO
import time

def blink(pin):
        RPi.GPIO.output(pin,RPi.GPIO.HIGH)
        time.sleep(1)
        RPi.GPIO.output(pin,RPi.GPIO.LOW)
        time.sleep(1)
        return

RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(11, RPi.GPIO.OUT)
for i in range(0,50):
        blink(11)
RPi.GPIO.cleanup()
