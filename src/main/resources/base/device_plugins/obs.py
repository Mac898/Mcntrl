import sys, os
import obswebsocket, obswebsocket.requests, obswebsocket.events

class OBS():
    def __init__(self, ip_address="localhost", ip_port="4444", ip_secret="", already_open=False):
        """Create instance of OBS control"""
        self.ip = ip_address
        self.port = ip_port
        self.secret = ip_secret
        self.open = already_open
        self.client = obswebsocket.obsws(self.ip, self.port, self.secret)


    def connect(self):
        """Connect to OBS"""
        if self.open == False:
            raise Exception("OBS not open")
        self.client.connect()
    
    def openOBS(self, dir_override='C:\\Program Files\\obs-studio\\bin\\64bit', exe_override='"C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"'):
        """Open a new OBS window"""
        os.chdir(dir_override)
        os.system(exe_override)
        self.open = True

    def getClient(self):
        """Get a raw client interface"""
        return self.client

    def disconnect(self):
        """Disconnect"""
        self.client.disconnect()

    def setScene(self, name):
        """Switch scene to <name>"""
        self.client.call(obswebsocket.requests.SetCurrentScene(str(name)))
    
    def transition(self):
        """In studio mode, transistion left content to right content"""
        self.client.call(obswebsocket.requests.TransitionToProgram("Fade"))

    def enableStudioMode(self):
        """Enables Studio Mode"""
        self.client.call(obswebsocket.requests.EnableStudioMode())

    def disableStudioMode(self):
        """Disables Studio Mode"""
        self.client.call(obswebsocket.requests.DisableStudioMode())

    def toggleStudioMode(self):
        """Toggles Current Studio Mode Status"""
        self.client.call(obswebsocket.requests.ToggleStudioMode())

    def openProjectorWindow(self, a_type, monitor, geometry, name):
        """Open a project window of your typing"""
        self.client.call(obswebsocket.requests.OpenProjector(str(a_type), int(monitor), str(geometry), str(name)))

    def startRecording(self):
        """Start recording"""
        self.client.call(obswebsocket.requests.StartRecording())

    def stopRecording(self):
        """Start recording"""
        self.client.call(obswebsocket.requests.StopRecording())

    def toggleMute(self, a_src):
        """Toggle Mute"""
        self.client.call(obswebsocket.requests.ToggleMute(str(a_src)))

