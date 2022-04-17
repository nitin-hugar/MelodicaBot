#classes and functions for actuation of solenoid, pump
from config import *
import RPi.GPIO as GPIO
import numpy as np
from utils import modifyBit


# map midi note values to binary shift values for shift registers
# here format() is used to convert the int to binary 

midi2sol = {str(i + 60) : format(1 << i, 'b') for i in range(num_of_solenoids)} # 60 -> middle C


temp = ''
sol_state = temp.zfill(num_of_solenoids)


def activate_solenoid(note : int, state: bool):
    global sol_state

    value = midi2sol[str(note)] 
    bit_index = value[::-1].index('1')
    
    if state:
        sol_state = sol_state[:bit_index] + '1' + sol_state[bit_index + 1:]

    else:
        sol_state = sol_state[:bit_index] + '0' + sol_state[bit_index + 1:]
        
    GPIO.output(LATCH, 0)
    for i in reversed(range(len(sol_state))):
        GPIO.output(DATA, int(sol_state[i]))
        print(sol_state)
        GPIO.output(CLOCK, 1)
        GPIO.output(CLOCK, 0)
    GPIO.output(LATCH, 1)
        
    

def activate_pump(cc : int):
    if cc < 0:
        cc == 0
    elif cc > 127:
        cc == 127
    else:
        voltage = int(np.interp(cc, cc_range, voltage_range))
        GPIO.output(PUMP, voltage)
        

def reset_solenoids():
    a = ''
    a = a.zfill(num_of_solenoids)
    GPIO.output(LATCH, 0)
    for i in a:
        GPIO.output(DATA, int(i))
        GPIO.output(CLOCK, 1)
        GPIO.output(CLOCK, 0)
    GPIO.output(LATCH, 1)
    print(" >> Solenoids Reset")
    

def reset_pump():
    activate_pump(0)




    
