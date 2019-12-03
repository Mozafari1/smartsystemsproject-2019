import RPi.GPIO as GPIO
import time
import numpy as np
servo_y = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_y, GPIO.OUT)
pwm_y = GPIO.PWM(servo_y, 50)
pwm_y.start(0)
arr = [radius_inner_c]
def ser_y(arr):
    







if __name__ == "__main__":
    ser_y()

    