import serial
import time as t
import random
from dummy_bee import Dummy_bee

class Arduino():
    def __init__(self, serial_name):
        self.serial_name = serial_name
        self.ser = False
        self.dummy = False
        if serial_name == "dummy":
            self.dummy = True
        self.start()        

    def start(self):
        if self.dummy:
            self.ser = None
            self.read = self.dummy_read
            self.write = self.dummy_write
            self.waiting = self.dummy_waiting
            
        else:
            self.ser = serial.Serial(self.serial_name)
            t.sleep(1)
            self.ser.write("1")
            t.sleep(1)
            self.ser.write("2")
            self.read = self.read
            self.write = self.write
            self.waiting = self.serial_waiting
                       
    def write(self,value):
        if not self.dummy:
            self.ser.write(value)
        if self.dummy:
            print "Sent " + str(value) + " to dummy arduino."
 
    def read(self):
        if self.ser.inWaiting()>0:
            retrieved_value =  self.ser.readline()[:-2]
        else:
            retrieved_value = None
        return retrieved_value       
  
    def weighted_choice(self, choices):
        'used just for dummy read'
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
            if upto + w >= r:
                return c
            upto += w
        assert False, "Shouldn't get here"

    def dummy_read(self):
        cross =  self.weighted_choice([[False,50],['a',1], ['b',2]])
        if cross:
            print cross 
        return cross
    
    def serial_write(self, channel=0, value=0):
        '''Write a high (1) or low (0) value to channels 0--7.'''
        self.ser.write(chr(channel*2 + 1 + 16*value))

    def dummy_write(self, value):
        print "sent " + str(value) + " to dummy arduino"

    def serial_waiting(self):
        print self.ser.inWaiting()

    def dummy_waiting(self):
        return randint(0,1)

  
