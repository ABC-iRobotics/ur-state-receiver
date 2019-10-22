from urStateReceiver import UrStateReceiver
import time
from os import system, name
from datetime import datetime
import signal
import sys
import socket


def signal_handler(sig, frame):
    print('You pressed Ctrl+C! terminating the program...')
    sys.exit(0)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


HOST = '192.168.56.101'
PORT = 30003
TIMEOUT = 2
signal.signal(signal.SIGINT, signal_handler)
receiver = UrStateReceiver(HOST, PORT)

while True:
    start = time.perf_counter()
    try:
        received = receiver.PollDataFromSocket(TIMEOUT)
    except socket.error as msg:
        print("[socket-server] {}. Terminating the program...".format(msg))
        sys.exit(1)
    clear()
    print(datetime.now().time())
    for iii in received:
        if iii.visible == 'True':
            print(iii)
    print("\n\ntime taken {}".format(time.perf_counter()-start))
    print('\nPress Ctrl+C to quit...\n\n')
    time.sleep(0.3)
