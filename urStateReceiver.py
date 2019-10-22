import json
import re
import socket
from state import State
import struct


class UrStateReceiver:
    HOST = ''
    PORT = 0
    states = {}
    Output = []

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

        with open('states.json') as json_file:
            self.states = json.load(json_file)

        for iii in self.states['states']:
            self.Output.append(State(iii['description'], iii['length'],
                                     iii['radian'], iii['start'], iii['valuetype'], iii['visible']))

    def PollDataFromSocket(self,timeout):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((self.HOST, self.PORT))
            receivedData = s.recv(2048)
        byteData = bytearray(receivedData)
        for iii in self.Output:
            iii.value = struct.unpack(iii.valuetype, byteData[int(
                iii.start):int(iii.start)+int(iii.length)])[0]
        return self.Output
