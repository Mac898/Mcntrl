import rtmidi
import time

class midicntrl():
    def __init__(self, a_id, port):
        self.id = a_id
        self.midi = rtmidi.MidiOut()
        available = self.midi.get_ports()
        if available:
            self.midi.open_port(int(port))
        else:
            self.midi.open_virtual_port(str(a_id))
    
    def sendNote(self, note, velocity):
        with self.midi:
            note_send = [0x90, note, velocity]
            self.midi.send_message(note_send)
            time.sleep(0.1)

    def disconnect(self):
        del self.midi