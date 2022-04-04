#classes for actuation solenoid, pump
import pandas as pd

class Solenoid:
	def __init__(self, note, duration):
		self.shift_reg_value =  note_to_shift_reg(note)
		self.duration =duration
		self.df_dict = pd.read_csv('note_to_shiftreg.csv')

	def note_to_shift_reg(self, note):
		'''
		return mappings from note value to the shift register
		'''
		return self.df['ShiftReg'][self.df['NoteNumber']==note]		 


class Pump:
	'''
	We might not need this class if we figure out a way to incorporate it in 
	'''
	def __init__(self, velocity):
		self.velocity= velocity
