
from Servo import *
servo=Servo()


def forward():
    servo.setServoAngle(12,120) 
    servo.setServoAngle(6,60) 
    servo.setServoAngle(9,60) 
    servo.setServoAngle(3,120)
    
    servo.setServoAngle(2,70) 
    servo.setServoAngle(5,20)
    servo.setServoAngle(10,110)
    servo.setServoAngle(13,165) 
    
    servo.setServoAngle(7,75)
    servo.setServoAngle(8,100)
    servo.setServoAngle(11,90)
    
    time.sleep(5)

    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(12,120-i/3) # final 60
            servo.setServoAngle(6,60+i/3) # final 120
            
            servo.setServoAngle(13,165 - i/3.27) #final 110
            servo.setServoAngle(5, 20 + i/3.6) # final 70
           
        if i <= 90:
            servo.setServoAngle(3, 120 + i/9 ) # final 130
            servo.setServoAngle(9, 60 - i/9 ) # final 50
            
            servo.setServoAngle(2, 69 - i/4.74) # final 50
            servo.setServoAngle(10, 111 + i/4.74) #final 130        
        
        

        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        
        if i > 90:
            servo.setServoAngle(3, 130 - (i-90)/2.6) # final a 60
            servo.setServoAngle(9, 50 + (i-90)/1.8 ) # final a 120
            
        if i > 90 and i < 110:
            servo.setServoAngle(2, 60 + (i-90)/2) # final 70
            servo.setServoAngle(10, 120 - (i-90)/2) # final 110
        
        
        if i > 180:
            servo.setServoAngle(2, 70 - (i-90)/1.28)    # final 
            servo.setServoAngle(10, 110 + (i-90)/1.2) # final 185
        
        
        time.sleep(0.03)

    
        # estará ao contrário da posição inicial
    ################################################################
'''
    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(9,120-i/3) # final 60
            servo.setServoAngle(3,60+i/3) # final 120
            
            servo.setServoAngle(10,165 - i/3.27) #final 110
            servo.setServoAngle(2, 20 + i/3.6) # final 70
           
        if i <= 90:
            servo.setServoAngle(6, 120 + i/9 ) # final 130
            servo.setServoAngle(12, 60 - i/9 ) # final 50
            
            servo.setServoAngle(5, 69 - i/9) # final 60
            servo.setServoAngle(13, 111 + i/9) #final 120           
        
        
        # até aqui está a funcionar como quero!!! omddddd
        
 
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        
        if i > 90:
            servo.setServoAngle(6, 130 - (i-90)/2.6) # final a 60
            servo.setServoAngle(12, 50 + (i-90)/2.6 ) # final a 120
            
        if i > 90 and i < 110:
            servo.setServoAngle(5, 60 - (i-90)) # final 40
            servo.setServoAngle(13, 120 + (i-90)) # final 140
        
        if i > 180:
            servo.setServoAngle(5, 40 - (i-90)/9)    # final 20
            servo.setServoAngle(13, 140 + (i-90)/7.2) # final 165
        
        
        time.sleep(0.03)
'''
def backwards():
    servo.setServoAngle(12,120) 
    servo.setServoAngle(6,60) 
    servo.setServoAngle(9,60) 
    servo.setServoAngle(3,120)
    
    servo.setServoAngle(2,70) 
    servo.setServoAngle(5,20)
    servo.setServoAngle(10,110)
    servo.setServoAngle(13,165) 
    
    servo.setServoAngle(7,75)
    servo.setServoAngle(8,100)
    
    time.sleep(5)

    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(9,120-i/3) # final 60
            servo.setServoAngle(3,60+i/3) # final 120
            
            servo.setServoAngle(10,165 - i/3.27) #final 110
            servo.setServoAngle(2, 20 + i/3.6) # final 70
           
        if i <= 90:
            servo.setServoAngle(6, 120 + i/9 ) # final 130
            servo.setServoAngle(12, 60 - i/9 ) # final 50
            
            servo.setServoAngle(5, 69 - i/9) # final 60
            servo.setServoAngle(13, 111 + i/9) #final 120           
        
        
        # até aqui está a funcionar como quero!!! omddddd
        
 
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        
        if i > 90:
            servo.setServoAngle(6, 130 - (i-90)/2.6) # final a 60
            servo.setServoAngle(12, 50 + (i-90)/2.6 ) # final a 120
            
        if i > 90 and i < 110:
            servo.setServoAngle(5, 60 - (i-90)/2) # final 50
            servo.setServoAngle(13, 120 + (i-90)/2) # final 130
        
        if i > 180:
            servo.setServoAngle(5, 50 - (i-90)/6)    # final 20
            servo.setServoAngle(13, 130 + (i-90)/5.14) # final 165
        
        
        time.sleep(0.03)
        

        ############################ estará ao contrário da posição inicial ####################################
        
        for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
            if i <= 180:
                servo.setServoAngle(12,120-i/3) # final 60
                servo.setServoAngle(6,60+i/3) # final 120

                servo.setServoAngle(13,165 - i/3.27) #final 110
                servo.setServoAngle(5, 20 + i/3.6) # final 70

            if i <= 90:
                servo.setServoAngle(3, 120 + i/9 ) # final 130
                servo.setServoAngle(9, 60 - i/9 ) # final 50

                servo.setServoAngle(2, 69 - i/9) # final 60
                servo.setServoAngle(10, 111 + i/9) #final 120           


            # até aqui está a funcionar como quero!!! omddddd


            # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
            # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60

            if i > 90:
                servo.setServoAngle(3, 130 - (i-90)/2.6) # final a 60
                servo.setServoAngle(9, 50 + (i-90)/2.6 ) # final a 120

            if i > 90 and i < 110:
                servo.setServoAngle(2, 60 - (i-90)/2) # final 50
                servo.setServoAngle(10, 120 + (i-90)/2) # final 130

            if i > 180:
                servo.setServoAngle(2, 50 - (i-90)/6)    # final 20
                servo.setServoAngle(10, 130 + (i-90)/5.14) # final 165


            time.sleep(0.03)





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
         
