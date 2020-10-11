import telnetlib

class Telnet():
    def __init__(self,a_ip, a_port):
        self.ip = a_ip
        self.port = a_port
        self.t = telnetlib.Telnet(self.ip, self.port)
    def login(self, a_user, a_pass, a_pass_req = True):
        t = self.t
        t.read_until(b"login: ")
        t.write(a_user.encode('ascii') + b"\n")
        print("Logged in")
        if a_pass_req:
            t.read_until(b"Password: ")
            t.write(a_pass.encode('ascii') + b"\n")
            print("Password Entered")

    def getRawTelenet(self):
        return self.t

    def write(self, msg):
        self.t.write(msg.encode('ascii') + b"\n")

    def read_until(self, phrase):
        self.t.read_until(phrase.encode('ascii'))
        


