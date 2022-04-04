#Main file for Robotic Musicianship Group project 
#Group members
#Rhythm Jain
#Nitin Hugar
#Keith Ng

from utils import Utils

if __name__ == '__main__':
	utils = Utils()
	file = input('Enter the path of the midi file') #try by entering '../midi_files/midi1.mid'
	df = utils.extract_midi_event(file)
	print(df)



