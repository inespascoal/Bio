import time
import RPi.GPIO as GPIO
class Buzzer:
    def __init__(self):
        GPIO.setwarnings(False)
        self.Buzzer_Pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Buzzer_Pin,GPIO.OUT)
    def run(self, d):
        buzzer_pwm = GPIO.PWM(self.Buzzer_Pin, 100)
        if (d<=20 and d>15):
            buzzer_pwm.start(50)
            GPIO.output(self.Buzzer_Pin,True)
        elif (d<=15 and d>10):
            buzzer_pwm.start(70)
            GPIO.output(self.Buzzer_Pin,True)
        elif (d<=10):
            buzzer_pwm.start(100)
            GPIO.output(self.Buzzer_Pin,True)
    def stop(self):
        buzzer_pwm = GPIO.PWM(self.Buzzer_Pin, 100)
        buzzer_pwm.stop()
        GPIO.output(self.Buzzer_Pin,False)
if __name__=='__main__':
    pass




