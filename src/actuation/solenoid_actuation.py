from time import sleep
import RPi.GPIO as GPIO

#GPIO is in BOARD mode so setting the data, latch and clock to the respective pin numbers.
data=16
latch=18
clock=22

"""
modes : 
s1- only solenoid 1 is HIGH, solenoid 2 is LOW
s2- only solenoid 2 is HIGH, solenoid 1 is LOW
s1s2- Both solenoids 1 and 2 are HIGH
none- Both solenoids are LOW
"""
s1 = 2
s2 = 512
s1s2 = 514
none = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(data,GPIO.OUT)
GPIO.setup(latch,GPIO.OUT)
GPIO.setup(clock,GPIO.OUT)

def intTo16Bin(val):
    l = len(bin(val)[2:])
    pad = 16- l
    sBinVal ='0'*pad + bin(val)[2:]
    return sBinVal

def reset(val='0000000000000000'):
    GPIO.output(latch, 0)
    for i in val:
        GPIO.output(data, int(i))
        GPIO.output(clock, 1)
        GPIO.output(clock, 0)
    GPIO.output(latch, 1)
def main():
    reset()
    seq = [s2,none]
    finalSeq = [intTo16Bin(i) for i in seq]
    for i in range(0):
        for values in finalSeq:
            GPIO.output(latch, 0)
            for i in values:
                print(i)
                GPIO.output(data, int(i))
                GPIO.output(clock, 1)
                GPIO.output(clock, 0)
            
            GPIO.output(latch, 1)
            sleep(0.5)
    reset()

if __name__ == "__main__":
    main()
