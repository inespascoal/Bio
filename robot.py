
# Quase de certeza que não vai funcionar 

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
    servo.setServoAngle(13,143)
    servo.setServoAngle(7,75)
    servo.setServoAngle(8,100)
    
    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(3,120-i/3)
            servo.setServoAngle(2,90-i/3) 

            servo.setServoAngle(9,60+i/3) # para de trás direita faz o mesmo
            servo.setServoAngle(10, 90+i/3) 
        
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        if i > 90:
            servo.setServoAngle(12, 120 - (i-90)/3 )
            servo.setServoAngle(13, 143 - (i-90)/3 ) 

            servo.setServoAngle(6,60 + (i-90)/3 ) # a pata frente esquerda anda para a frente
            servo.setServoAngle(5, 40 + (i-90)/3 ) 
        
        time.sleep(0.05)
     
    
        # estará ao contrário da posição inicial
    
   
    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estao a mover-se de tras para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(6,120-i/3)
            servo.setServoAngle(5,90-i/3) 

            servo.setServoAngle(12,60+i/3) 
            servo.setServoAngle(13, 90+i/3) 
        
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrarias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        if i > 90:
            servo.setServoAngle(9, 120 - (i-90)/3 )
            servo.setServoAngle(10, 143 - (i-90)/3 ) 

            servo.setServoAngle(3,60 + (i-90)/3 ) 
            servo.setServoAngle(2, 40 + (i-90)/3 ) 
        
        time.sleep(0.05)
        
        # em principio estará na posição inicial
        
        
       
     

# a próxima é cada pata a começar em tempo diferente, supostamente é mais realista, mas not sure         
        
def forward1():
    servo.setServoAngle(12,120) 
    servo.setServoAngle(6,60) 
    servo.setServoAngle(9,60) 
    servo.setServoAngle(3,120)
    
    servo.setServoAngle(2,90) 
    servo.setServoAngle(5,40)
    servo.setServoAngle(10,90)
    servo.setServoAngle(13,143)
    servo.setServoAngle(7,75)
    servo.setServoAngle(8,100)
    
    for i in range(450):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estão a mover-se de trás para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(9,60+i/3) 
            servo.setServoAngle(10, 90+i/3) 
            
        if i > 90 and i <= 270:
            servo.setServoAngle(3,120 - (i-90)/3 )
            servo.setServoAngle(2,90 - (i-90)/3 ) 
             
        
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrárias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        if i > 180 and i <= 360:
            servo.setServoAngle(6,60 + (i-180)/3 ) 
            servo.setServoAngle(5, 40 + (i-180)/3 ) 
            
        if i > 270 and i <= 450:
            servo.setServoAngle(12, 120 - (i-270)/3 )
            servo.setServoAngle(13, 143 - (i-270)/3 ) 

        
        time.sleep(0.1)
     
    
        # estará ao contrário da posição inicial
    
   
    for i in range(270):
        
        # quando chegar a 180, ou seja, quando andar 60º as patas que estao a mover-se de tras para a frente param
        # como andamos (i)/3 faz com que vá de (0)/3 = 0 até (180)/3 = 60
        if i <= 180:
            servo.setServoAngle(6,120-i/3)
            servo.setServoAngle(5,90-i/3) 

            servo.setServoAngle(12,60+i/3) # para de trás direita faz o mesmo
            servo.setServoAngle(13, 90+i/3) 
        
        # a meio do movimento das outras patas, ou seja, apos andarem 30º, as contrarias vao começar a mover-se de frente para trás
        # como andamos (i-90)/3 faz com que vá de (91-90)/3 = 1/3 até (270-90)/3 = 60
        if i > 90:
            servo.setServoAngle(9, 120 - (i-90)/3 )
            servo.setServoAngle(10, 143 - (i-90)/3 ) 

            servo.setServoAngle(3,60 + (i-90)/3 ) # a pata frente esquerda anda para a frente
            servo.setServoAngle(2, 40 + (i-90)/3 ) 
        
        time.sleep(0.1)
        
        # em principio estará na posição inicial
        


def right():
    servo.setServoAngle(4,0)
    servo.setServoAngle(3,0)
    servo.setServoAngle(2,90)
    
    servo.setServoAngle(7,0)
    servo.setServoAngle(6,0)
    servo.setServoAngle(5,90)
    
    servo.setServoAngle(8,0)
    servo.setServoAngle(9,0)
    servo.setServoAngle(10,90)
    
    servo.setServoAngle(11,0)
    servo.setServoAngle(12,0)
    servo.setServoAngle(13,90)
    try:
        for i in range(30): 
            servo.setServoAngle(4,90-i) # anda para a frente uma pata
            servo.setServoAngle(7,90-i) # anda para a frente a para de trás correspondente
            time.sleep(0.01)
            
            for i in range(30):
                servo.setServoAngle(11,90-i) # anda para a frente a outra pata
                servo.setServoAngle(8,90-i) # anda para a frente a para de trás correspondente

                servo.setServoAngle(4,90+i) # a 1ª pata volta à posição inicial (como se estivesse sem resistência)
                servo.setServoAngle(7,90+i) # o mesmo
                time.sleep(0.01)
            
            servo.setServoAngle(11,90+i) # o correspondente para a outra pata
            servo.setServoAngle(8,90+i) # o mesmo
            
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")
        


def left():
    servo.setServoAngle(4,0)
    servo.setServoAngle(3,0)
    servo.setServoAngle(2,90)
    
    servo.setServoAngle(7,0)
    servo.setServoAngle(6,0)
    servo.setServoAngle(5,90)
    
    servo.setServoAngle(8,0)
    servo.setServoAngle(9,0)
    servo.setServoAngle(10,90)
    
    servo.setServoAngle(11,0)
    servo.setServoAngle(12,0)
    servo.setServoAngle(13,90)
    try:
        for i in range(30): 
            servo.setServoAngle(11,90-i) # anda para a frente uma pata
            servo.setServoAngle(8,90-i) # anda para a frente a para de trás correspondente
            time.sleep(0.01)
            
            for i in range(30):
                servo.setServoAngle(4,90-i) # anda para a frente a outra pata
                servo.setServoAngle(7,90-i) # anda para a frente a para de trás correspondente

                servo.setServoAngle(11,90+i) # a 1ª pata volta à posição inicial (como se estivesse sem resistência)
                servo.setServoAngle(8,90+i) # o mesmo
                time.sleep(0.01)
            
            servo.setServoAngle(4,90+i) # o correspondente para a outra pata
            servo.setServoAngle(7,90+i) # o mesmo
            
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")


        
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



        
