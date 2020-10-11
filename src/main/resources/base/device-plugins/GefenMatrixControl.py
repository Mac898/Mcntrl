#global imports
import sys
from lib import telnethost

#Gefen Matrix 4x4 (EXT-HD-SL-444)
class EXTHDSL444():
    def __init__(self, ip_address = "192.168.0.1", ip_port = 23, a_id=1):
        """Create new instance of Gefen Matrix 4x4 with ip `ip_address` and port `ip_port`"""
        self.ip = ip_address
        self.port = ip_port
        self.id = a_id
    
    def connect_telnet(self, login_user = "admin", login_pass = "admin", login_required = True, password_required = True):
        """Connect to Gefen Matrix 4x4 with telnet for control"""
        t = telnethost.Telnet(login_user, login_pass)
        self.t = t
        if login_required and password_required:
            t.login(login_user, login_pass, a_pass_req=password_required)
        elif login_required:
            t.login(login_user, login_pass)
        print("Successfully connected to Gefen Matrix 4x4 (EXT-HD-SL-4444) ID: "+str(self.id))

    def map(self, a_screen, b_screen):
        """Map input a_screen (number 1-4) to b_screen (output, number 1-4)"""
        self.t.write("r "+a_screen+" "+b_screen)
        print("Mapped screen "+a_screen+" to screen "+b_screen)
