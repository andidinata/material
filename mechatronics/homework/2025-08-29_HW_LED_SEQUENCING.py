import board
import digitalio
import time

#leftside
led1 = board.GP0
led2 = board.GP1
led3 = board.GP2
led4 = board.GP3
led5 = board.GP4
led6 = board.GP5
led7 = board.GP6
led8 = board.GP7

#rightside
led9 = board.GP16
led10 = board.GP17
led11 = board.GP18
led12 = board.GP19
led13 = board.GP26
led14 = board.GP27
led15 = board.GP28
led16 = board.GP29

#set the pin as digital
LED1 = digitalio.DigitalInOut(led1)
LED2 = digitalio.DigitalInOut(led2)
LED3 = digitalio.DigitalInOut(led3)
LED4 = digitalio.DigitalInOut(led4)
LED5 = digitalio.DigitalInOut(led5)
LED6 = digitalio.DigitalInOut(led6)
LED7 = digitalio.DigitalInOut(led7)
LED8 = digitalio.DigitalInOut(led8)

LED9 = digitalio.DigitalInOut(led9)
LED10 = digitalio.DigitalInOut(led10)
LED11 = digitalio.DigitalInOut(led11)
LED12 = digitalio.DigitalInOut(led12)
LED13 = digitalio.DigitalInOut(led13)
LED14 = digitalio.DigitalInOut(led14)
LED15 = digitalio.DigitalInOut(led15)
LED16 = digitalio.DigitalInOut(led16)

#set the direction
LED1.direction = digitalio.Direction.OUTPUT
LED2.direction = digitalio.Direction.OUTPUT
LED3.direction = digitalio.Direction.OUTPUT
LED4.direction = digitalio.Direction.OUTPUT
LED5.direction = digitalio.Direction.OUTPUT
LED6.direction = digitalio.Direction.OUTPUT
LED7.direction = digitalio.Direction.OUTPUT
LED8.direction = digitalio.Direction.OUTPUT

LED9.direction = digitalio.Direction.OUTPUT
LED10.direction = digitalio.Direction.OUTPUT
LED11.direction = digitalio.Direction.OUTPUT
LED12.direction = digitalio.Direction.OUTPUT
LED13.direction = digitalio.Direction.OUTPUT
LED14.direction = digitalio.Direction.OUTPUT
LED15.direction = digitalio.Direction.OUTPUT
LED16.direction = digitalio.Direction.OUTPUT

RIGHTSIDE = [LED1,LED2,LED3,LED4,LED5,LED6,LED7,LED8]
LEFTSIDE  = [LED9,LED10,LED11,LED12,LED13,LED14,LED15,LED16]
BOTHSIDE  = RIGHTSIDE + LEFTSIDE

while True:
    #Model 1: All leds on both side turn on and off 10 times with faster blinking rate
    print("Model 1:All leds on both side turn on and off 10 times with faster blinking rate")
    t = 0.15
    for i in range(10):
        print(i,end=",")
        for led in BOTHSIDE:
            led.value = 1
        time.sleep(max(0.01,t))
        for led in BOTHSIDE:
            led.value = 0
        time.sleep(max(0.01,t))
        t -= 0.01
    print("-> Completed")
    
    #Model 2: led in left and right side move synchronously
    print("Model 2: led in left and right move synchronously, steady rate")
    t = 0.1
    for j in range(5):
        print(j,end=",")
        for i in range(8):
            LEFTSIDE[i].value = 1
            RIGHTSIDE[i].value = 1
            time.sleep(t)    
        
        for i in range(8):
            LEFTSIDE[7-i].value = 0
            RIGHTSIDE[7-i].value = 0
            time.sleep(t)   
    print("-> Completed")
    
    #Model 3: led in left and right side move synchronously
    print("Model 3: led in left and right move synchronously repeat 10 times")
    t = 0.05
    for i in range(10):
        print(i, end = ",")
        for led in RIGHTSIDE:
            led.value = 1
            time.sleep(max(0.01,t))
            led.value = 0
            
        LEFTSIDE.reverse()
        for led in LEFTSIDE:
            led.value = 1
            time.sleep(max(0.01,t))
            led.value = 0
        LEFTSIDE.reverse()
        
        t -= 0.01
    print("-> Completed")
    
    #Model 4: led in left and right runs back and forth
    print("Model 4: led in left and right runs back and forth repeat 10 times and getting faster")
    t = 0.07
    for j in range(10):
        print(j, end = ",")
        for i in range(8):
            LEFTSIDE[i].value = 1
            RIGHTSIDE[i].value = 1
            time.sleep(max(0.01,t))
            LEFTSIDE[i].value = 0
            RIGHTSIDE[i].value = 0
        
        LEFTSIDE.reverse()
        RIGHTSIDE.reverse()
        
        t -= 0.01
    print("-> Completed")

