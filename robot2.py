
from Servo import *
servo=Servo()


def forward():
    servo.setServoAngle(12,120) 
    servo.setServoAngle(6,60) 
    servo.setServoAngle(9,60) 
    servo.setServoAngle(3,120)
    
    servo.setServoAngle(2,70) 
    servo.setServoAngle(5,25)
    servo.setServoAngle(10,110)
    servo.setServoAngle(13,163) # antes estava 143
    
    servo.setServoAngle(7,75)
    servo.setServoAngle(8,100)
    
    time.sleep(5)
    '''
    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(12,120-i/3)
            servo.setServoAngle(6,60+i/3) # para de trás direita faz o mesmo
            
            servo.setServoAngle(13,90 - i/3.6)
            servo.setServoAngle(5, 90 + i/3.6)
           
        if i <= 90:
            servo.setServoAngle(3, 120 + i/9 ) # final 130
            servo.setServoAngle(9, 60 - i/9 ) # final 50
            
            servo.setServoAngle(2,90 - i/9) # final 70
            servo.setServoAngle(10, 90 + i/9) #final 110           
            
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        if i > 90:
            servo.setServoAngle(3, 130 - (i-90)/2.6) # final a 60
            servo.setServoAngle(9, 50 + (i-90)/2.6 ) # final a 120
            
        if i > 90 and i < 100:
            servo.setServoAngle(2, 70 + (i-90))
            servo.setServoAngle(10, 110 - (i-90)) 
        
        time.sleep(0.03)
     '''
    
        # estará ao contrário da posição inicial
    ################################################################
    
    '''
    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(3, 60+i/3)
            servo.setServoAngle(9,120-i/3) # para de trás direita faz o mesmo
            
            servo.setServoAngle(2,90 + i/3.6)
            servo.setServoAngle(10, 90 - i/3.6)
           
        if i <= 90:
            servo.setServoAngle(12, 60 - i/9 ) # final 50
            servo.setServoAngle(6, 120 + i/9 ) # final 130
            
            servo.setServoAngle(13,90 + i/3.6) # final 110
            servo.setServoAngle(5, 90 - i/3.6) # final 70    
            
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        if i > 90:
            servo.setServoAngle(12, 130 - (i-90)/2.6) # final a 60
            servo.setServoAngle(6, 50 + (i-90)/2.6 ) # final a 120
            
        if i > 90 and i <100:
            servo.setServoAngle(13, 110 - (i-90)) # final a 60
            servo.setServoAngle(5, 70 + (i-90) ) # final a 120
        
        time.sleep(0.03)
    '''
    
# Main program logic follows:
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the device")
        exit() 
    if sys.argv[1] == 'Forward':
        forward()
    elif sys.argv[1] == 'Forward1':
        forward1()
    elif sys.argv[1] == 'Right': 
        right()              
    elif sys.argv[1] == 'Left':   
        left() 
         
