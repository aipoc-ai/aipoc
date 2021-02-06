import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
in3=  14
in4= 18
en = 23

def forward(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)    
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    sleep(x)
    GPIO.cleanup()
    
def backward(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23,GPIO.OUT)
    GPIO.setup(24,GPIO.OUT)
    GPIO.output(23,True)
    GPIO.output(24,True)
    sleep(x)
    GPIO.cleanup()

def rotate_r(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(23,True)
    GPIO.output(18,True)
    sleep(x)
    GPIO.cleanup()

def rotate_l(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(14,GPIO.OUT)
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(14,GPIO.HIGH)
    sleep(x)
    GPIO.cleanup()

forward(2)

