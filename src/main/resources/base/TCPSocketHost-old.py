from device_plugins import obs, PowerPointControl, GefenMatrixControl, dot2, screenMonkeyControl
from twisted.internet import task, reactor
import socket
from twisted.internet.protocol import Protocol

"""Config"""
listen_address = '0.0.0.0'
port = 7000
"""Socket Setup"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (listen_address, port)
print("Starting up on "+str(server_address))
sock.bind(server_address)
timeout = 0.05
sock.listen(2)
connection, client_address = sock.accept()
"""Setup/import device_plugins"""
obs_stream = obs.OBS(ip_port="4444", already_open=True)
obs_display = obs.OBS(ip_port="4445", already_open=True)
gefen = GefenMatrixControl.EXTHDSL444(ip_address="192.168.0.1", ip_port=23)
"""Action Map"""
arg1 = ""
arg2 = ""
arg3 = ""
arg4 = ""
actions = {
    "obs.stream.connect": obs_stream.connect(),
    "obs.displays.connect": obs_display.connect(),
    "obs.stream.setScene": obs_stream.setScene(arg1),
    "obs.displays.setScene": obs_stream.setScene(arg1),

}
"""Map message to action"""
def process(msg, args):
    arg1 = args[0]
    arg2 = args[1]
    arg3 = args[2]
    arg4 = args[3]
    a = actions[msg]
    return a
"""Procesing Loop"""
def MainLoop():
    incoming = connection.recv(1024)
    print("Received MSG: %s" % incoming.decode('utf-8'))
    message = incoming.decode('utf-8')
    cmd = message.split(";")
    args = cmd
    args.pop(0)
    process(cmd[0], args)

#begin MainLoop cycle
taskloop = task.LoopingCall(MainLoop)
taskloop.start(timeout)

reactor.run()