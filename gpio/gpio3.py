#!/usr/bin/python
# coding: utf-8

from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
from time import sleep


if __name__ == "__main__": 


    gpio.init() #Initialize module. Always called first

    gpio.setcfg(port.PA12, gpio.OUTPUT)  #Configure LED1 as output
    gpio.setcfg(port.PA12, 1)            #This is the same as above

    # gpio.setcfg(port.PE11, gpio.INPUT)   #Configure PE11 as input
    # gpio.setcfg(port.PE11, 0)   #Same as above

    # gpio.pullup(port.PE11, 0)   #Clear pullups
    # gpio.pullup(port.PE11, gpio.PULLDOWN)    #Enable pull-down
    # gpio.pullup(port.PE11, gpio.PULLUP)  #Enable pull-up


    while True:
        
        gpio.output(port.PA12, gpio.LOW)
        gpio.output(port.PA12, 0)
        sleep(1)
        gpio.output(port.PA12, gpio.HIGH)
        gpio.output(port.PA12, 1)
        sleep(1)