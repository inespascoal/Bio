import time
import RPi.GPIO as GPIO
class Buzzer:
    def __init__(self):
        GPIO.setwarnings(False)
        self.Buzzer_Pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Buzzer_Pin,GPIO.OUT)
        buzzer_pwm = GPIO.PWM(buzzer_pin, 100)
    def run(self, d):
        if (d<=20 and d>15):
            buzzer_pwm.start(1)
        elif (d<=15 and d>10):
            buzzer_pwm.start(3)
        elif (d<=10):
            buzzer_pwm.start(5)
            #GPIO.output(self.Buzzer_Pin,True)
    def stop(self):
        GPIO.output(self.Buzzer_Pin,False)
if __name__=='__main__':
    pass




