import time
#import numpy as np
import RPi.GPIO as GPIO
class Buzzer:
    def __init__(self):
        GPIO.setwarnings(False)
        self.Buzzer_Pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Buzzer_Pin,GPIO.OUT)

    def run(self, d):

        if (d<=20 and d>15):
            periodo = 0.5

        elif (d<=15 and d>10):
            periodo = 0.25

        elif (d<=10):
            periodo = 1/6

        if (time.time() - t0) >= periodo:
            GPIO.output(self.Buzzer_Pin,True)
            time.sleep(0.01)
            GPIO.output(self.Buzzer_Pin,False)
            t0 = time.time()


        # outra opção
        #if np.sin(2*np.pi / periodo * time.time()) > 0:
            #GPIO.output(self.Buzzer_Pin,True)
            #time.sleep(0.01)
            #GPIO.output(self.Buzzer_Pin,False)
            
        #else:
            #GPIO.output(self.Buzzer_Pin,False)

if __name__=='__main__':
    pass




