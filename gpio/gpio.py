#!/usr/bin/python
# coding: utf-8
#https://forum.armbian.com/topic/5662-pygpio-a-more-general-python-gpio-library/

import os, sys

# if not os.getegid() == 0:
    # sys.exit('start script as root')
    
from pyGPIO.gpio import gpio, port
from time import sleep

if __name__ == "__main__": 

    gpio.init()
    gpio.setcfg(port.GPIO2, 1)  #gpio4 as output

    gpio.output(port.GPIO2, 0)
    print('gpio 0')
    sleep(3)
    gpio.output(port.GPIO2, 1)
    print('gpio 1')
    sleep(3)
    
    sys.exit('finished ;-)')