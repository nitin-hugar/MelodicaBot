#Main file for Robotic Musicianship Group project 
#Group members
#Rhythm Jain
#Nitin Hugar
#Keith Ng

from rtpmidi_handler import MyHandler
from rtpmidi import RtpMidi
import RPi.GPIO as GPIO
from config import DATA, LATCH, CLOCK, PUMP
from pymidi.packets import MIDINote
from midi_map import MidiNotes
from actuation import reset_solenoids, reset_pump

# TODO : MAKE A FOOLPROOF FOR POLYPHONY MORE THAN 4
# TODO : Handle note ranges
# TODO: Handle cc ranges 

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DATA,GPIO.OUT)
    GPIO.setup(LATCH,GPIO.OUT)
    GPIO.setup(CLOCK,GPIO.OUT)
    GPIO.setup(PUMP,GPIO.OUT)

if __name__ == '__main__':

    # initialize raspberry pi
    
    setup()
    reset_solenoids()   
    reset_pump()
    # initialize midi server
    ROBOT = "Your Robot"
    PORT = 5004
    rtp_midi = RtpMidi(ROBOT, MyHandler(), PORT)
    rtp_midi.run()


	



