import RPi.GPIO as GPIO       
import time
GPIO.setmode(GPIO.BORAD)
servo_30 = 11
servo_180 =12

GPIO.setup(servo_30, GPIO.OUT)
pwm = GPIO.PWM(servo_30,50)
pwm.start(0)
while(True):
    for i in range(0,30):
        degree = 1.0/18.0*i+1
        pwm.ChangeDutyCycle(degree)
        time.sleep(0.05)
    for i in range(30,0,-1):
        degree = 1.0/18.0*i+1
        pwm.ChangeDutyCycle(degree)
        time.sleep(0.05)

pwm.stop()
GPIO.cleanup()

