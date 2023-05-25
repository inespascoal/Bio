import time
import RPi.GPIO as GPIO
class Buzzer:
    def __init__(self):
        GPIO.setwarnings(False)
        self.Buzzer_Pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Buzzer_Pin,GPIO.OUT)

    def run(self, d):
        if d < 15:
            GPIO.output(self.Buzzer_Pin,True)
        
    def stop(self):
        GPIO.output(self.Buzzer_Pin,False)

           

if __name__=='__main__':
    pass

