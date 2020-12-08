from device_plugins import obs, PowerPointControl, GefenMatrixControl, dot2, screenMonkeyControl
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

"""Config"""
listen_address = '0.0.0.0'
port = 7000
"""Setup/import device_plugins"""
obs_stream = obs.OBS(ip_port="4444", already_open=True)
obs_display = obs.OBS(ip_port="4445", already_open=True)
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
            obs_display.connect()
            print("Connecting to OBS Display")
        if target == "obs.stream.setScene":
            obs_stream.setScene(cmd[1])
            print("Setting Scene on OBS Stream")
        if target == "obs.display.setScene":
            obs_display.setScene(cmd[1])
            print("Setting Scene on OBS Display")

def main():
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(7000, f)
    reactor.run()

if __name__ == '__main__':
    main()
