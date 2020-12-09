from device_plugins import obs, PowerPointControl, GefenMatrixControl, dot2, screenMonkeyControl
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

"""Config"""
listen_address = '0.0.0.0'
port = 7000
"""Setup/import device_plugins"""
obs_stream = obs.OBS(ip_port="4444", already_open=True)
obs_display_one = obs.OBS(ip_port="4445", already_open=True)
gefen = GefenMatrixControl.EXTHDSL444(ip_address="192.168.0.1", ip_port=23)
"""Map message to action"""
class Echo(Protocol):
    def dataReceived(self, data):
        message = data.decode('utf-8')
        cmd = message.split(";")
        print(str(cmd))
        target = cmd[0]
        print("Cmd: "+str(cmd)+" Args: "+str(cmd[1]))
        if target == "obs.stream.connect":
            obs_stream.connect()
            print("Connecting to OBS Stream")
        if target == "obs.display.connect":
            obs_display_one.connect()
            print("Connecting to OBS Display")
        if target == "obs.stream.setScene":
            obs_stream.setScene(cmd[1])
            print("Setting Scene " +str(cmd[1])+ "on OBS Stream")
        if target == "obs.display.setScene":
            obs_display_one.setScene(cmd[1])
            print("Setting Scene:" +str(cmd[1])+ "on OBS Display")
        if target == "obs.stream.transition":
            obs_stream.transition()
            print("Transitioning on OBS Stream")
        if target == "obs.display.transition":
            obs_display_one.transition()
            print("Transitioning on OBS Display")
        if target == "obs.stream.toggleStudioMode":
            obs_stream.toggleStudioMode()
            print("Toggling studio mode on OBS Stream")   
        if target == "obs.display.toggleStudioMode":
            obs_display_one.toggleStudioMode()
            print("Toggling studio mode on OBS Display")   
        if target == "obs.stream.startRecording":
            obs_stream.startRecording()
            print("Starting recording on OBS Stream")
        if target == "obs.display.startRecording":
            obs_display_one.startRecording()
            print("Starting recording on OBS Display")
        if target == "obs.stream.stopRecording":
            obs_stream.stopRecording()
            print("Stopped recording on OBS Stream")
        if target == "obs.display.stopRecording":
            obs_display_one.stopRecording()
            print("Stopped recording on OBS Display")
        #gefen control
        if target == "gefen.connectTelnet":
            print("Using user: "+str(cmd[1])+" | password: "+str(cmd[2]))
            gefen.connect_telnet(login_user=str([cmd[1]]), login_pass=str(cmd[2]))
            print("Connecting to Gefen Matrix via TELNET")
        if target == "gefen.set1":
            gefen.map(1, cmd[1])
            print("Setting Gefen screen 1 to "+str(cmd[1]))
        if target == "gefen.set2":
            gefen.map(2, cmd[1])
            print("Setting Gefen screen 2 to "+str(cmd[1]))
        if target == "gefen.set3":
            gefen.map(3, cmd[1])
            print("Setting Gefen screen 3 to "+str(cmd[1]))
        if target == "gefen.set4":
            gefen.map(4, cmd[1])
            print("Setting Gefen screen 4 to "+str(cmd[1]))
        
def main():
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(7000, f)
    reactor.run()

if __name__ == '__main__':
    main()
