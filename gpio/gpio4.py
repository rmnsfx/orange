#!/usr/bin/python
# coding: utf-8
#https://github.com/duxingkei33/orangepi_PC_gpio_pyH3


import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PA12

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)

try:
    
    while True:
        gpio.output(led, 1)
        sleep(1)
        gpio.output(led, 0)
        sleep(1)

        gpio.output(led, 1)
        sleep(1)
        gpio.output(led, 0)
        sleep(1)

        sleep(0.1)
except KeyboardInterrupt:
    
    print ("Goodbye.")