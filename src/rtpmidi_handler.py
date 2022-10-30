from rtpmidi import RtpMidi
from pymidi import server
from actuation import *
from midi_map import MidiNotes

class MyHandler(server.Handler):
    def on_peer_connected(self, peer):
        # Handler for peer connected
        print('Peer connected: {}'.format(peer))

    def on_peer_disconnected(self, peer):
        # Handler for peer disconnected
        print('Peer disconnected: {}'.format(peer))

    def on_midi_commands(self, peer, command_list):
        # Handler for midi msgs

        
        for command in command_list:
            if command.command == 'note_on':
                key = command.params.key
                midi_note = MidiNotes[key].value[0]
                #print('key {} -> on'.format(key))
                activate_solenoid(midi_note, True)

            elif command.command == 'note_off':
                key = command.params.key
                midi_note = MidiNotes[key].value[0]
                #print('key {} -> off'.format(key))
                activate_solenoid(midi_note, False)
            
            elif command.command == 'control_mode_change':
                controller = command.params.controller
                value = command.params.value
                if controller == 2:
                    activate_pump(value)


if __name__ == "__main__":
    ROBOT = "Your Robot"
    PORT = 5004
    rtp_midi = RtpMidi(ROBOT, MyHandler(), PORT)
    rtp_midi.run()
