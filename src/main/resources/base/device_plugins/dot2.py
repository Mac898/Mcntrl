#global imports
import sys, rtmidi
from dlib import midicntrl

#MA lighting Dot2 Platform
class MAdot2():
    def __init__(self, a_port, a_id=1):
        """Create new instance of MAdot2"""
        self.id = a_id
        self.port = a_port

    def connect_midi(self):
        self.con = midicntrl.midicntrl(self.id, self.port)
        print("Successfully connected to MAdot2 ID: "+str(self.id))

    def d(self, a_button, a_velocity):
        """Send command to MAdot2, button is actually note, and velocity is either 0 or 1 for buttons (off or on), but for sliders is mapped to the %"""
        self.con.sendNote(a_button, a_velocity)
        print("Set midi note: "+str(a_button)+" to velocity "+str(a_velocity))
