
from Servo import *
servo=Servo()


def forward():
    servo.setServoAngle(12,120) 
    servo.setServoAngle(6,60) 
    servo.setServoAngle(9,60) 
    servo.setServoAngle(3,120)
    
    servo.setServoAngle(2,90) 
    servo.setServoAngle(5,40)
    servo.setServoAngle(10,90)
    servo.setServoAngle(13,148) # antes estava 143
    
    servo.setServoAngle(7,75)
    servo.setServoAngle(8,100)
    
    time.sleep(5)
    
    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(12,120-i/3)
            servo.setServoAngle(6,60+i/3) # para de trás direita faz o mesmo
            
            #servo.setServoAngle(2,90 - i/3.6)
            #servo.setServoAngle(10, 90 + i/3.6)
           
        if i <= 90:
            servo.setServoAngle(3, 120 + i/9 ) # final 130
            servo.setServoAngle(9, 60 - i/9 ) # final 50
            
            
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        if i > 90:
            servo.setServoAngle(3, 130 - (i-90)/2.6) # final a 60
            servo.setServoAngle(9, 50 + (i-90)/2.6 ) # final a 120
        
        time.sleep(0.01)
     
    
        # estará ao contrário da posição inicial
    ################################################################
   
    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(3, 60+i/3)
            servo.setServoAngle(9,120-i/3) # para de trás direita faz o mesmo
            
            #servo.setServoAngle(2,90 - i/3.6)
            #servo.setServoAngle(10, 90 + i/3.6)
           
        if i <= 90:
            servo.setServoAngle(12, 60 + i/9 ) # final 130
            servo.setServoAngle(6, 120 - i/9 ) # final 50
            
            
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        if i > 90:
            servo.setServoAngle(12, 130 - (i-90)/2.6) # final a 60
            servo.setServoAngle(6, 50 + (i-90)/2.6 ) # final a 120
        
         
