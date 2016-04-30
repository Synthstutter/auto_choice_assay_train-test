import serial
import time as t
import random

class Arduino():

    def start(self, serial_name='/dev/ttyACM0'):
        if serial_name=='dummy':
            self.ard = None
            self.read = self.dummy_read
            self.write = self.dummy_write
            self.waiting = self.dummy_waiting
        else:
            self.ard = serial.Serial(serial_name)
            self.read = self.serial_read
            self.write = self.serial_write
            self.waiting = self.serial_waiting
            
    def write(self,value):
        self.ard.write(value)
 
    def read(self):
        if self.ard.inWaiting()>0:
            retrieved_value =  self.ard.readline()
        else:
            retrieved_value = None
        return retrieved_value
       
    def serial_read(self, channel=0):
       self.ard.write(chr(channel*2)) #request reading the channel
       return ord(self.ard.read(1))

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
        return self.weighted_choice([[None,100000],['1\n',1], ['2\n',2]])
    
    def serial_write(self, channel=0, value=0):
        '''Write a high (1) or low (0) value to channels 0--7.'''
        self.ard.write(chr(channel*2 + 1 + 16*value))

    def dummy_write(self, value):
        print "sent " + str(value) + " to dummy arduino"

    def serial_waiting(self):
        print self.ard.inWaiting()

    def dummy_waiting(self):
        return randint(0,1)

  
