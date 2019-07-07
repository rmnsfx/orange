import os
import sys
import socket
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9000        # Port to listen on (non-privileged ports are > 1023)

led = port.PA12

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            gpio.output(led, 1)
            sleep(1)
            gpio.output(led, 0)
            sleep(1)

            gpio.output(led, 1)
            sleep(1)
            gpio.output(led, 0)
            sleep(1)

