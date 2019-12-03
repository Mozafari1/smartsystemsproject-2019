import RPi.GPIO as GPIO
import time
from numpy import arange

servo_180 = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_180, GPIO.OUT)
pwm = GPIO.PWM(servo_180, 50)

pwm.start(0)
def ser():
    try:
        while True:
            for i in arange(3.0,12.0,0.5):
                pwm.ChangeDutyCycle(i)
                time.sleep(.5)
                print("i = ",i)
                
            for i in arange(12.0,3.0,-0.5):
                pwm.ChangeDutyCycle(i)
                time.sleep(.5)
                print("i = ",i)

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    print(ser())
    
