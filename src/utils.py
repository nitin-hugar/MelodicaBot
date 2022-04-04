#helper class for reading and parsing midi files
import pretty_midi
import pandas as pd

class Utils:
	def __init__(self):
		pass

	def extract_midi_event(self, midi_file):
	
		'''
		function to parse midi
		inputs
			midi_file: path to the midi file 
		returns 
			midi_df: DataFrame of all midi events within columns Start, End, Pitch, Velocity
		'''

		midi = pretty_midi.PrettyMIDI(midi_file)
		midi_list = []

		for instrument in midi.instruments:
		     for note in instrument.notes:
		             start = note.start
		             end = note.end
		             pitch = note.pitch
		             velocity = note.velocity
		             midi_list.append([start, end, pitch, velocity])

		midi_df = pd.DataFrame(midi_list, columns=['Start', 'End', 'Pitch', 'Velocity'])
		return midi_df
