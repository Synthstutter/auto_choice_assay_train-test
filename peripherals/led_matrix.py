from max7219 import led
import numpy as np
from peripheral import Peripheral
import time as t
import pdb

#remember that to use max7219 library, SPI needs to be activated via raspi-config. Look at github page for rm-hull max7219 library for directions on how to do this
# connect as follows:
#+5V -> RPi pin 2, +5V
#GND -> RPi pin 6, GND
#DIN -> RPi pin 19, GPIO 10(MOSI)
#CS  -> RPi pin 24, GPIO 8(SPI CE0)
#CLK -> RPi pin 23, GPIO 11(SPI CLK)

class Led_matrix(Peripheral):
    def __init__(self, *args, **kwargs):
        Peripheral.__init__(self, *args, **kwargs)
        self.group = "mat"
        
    def start(self):
        if not self.dummy:
            self.device = led.matrix(cascaded = 2)
            self.mat = []
            self.update = self.update
            
        if self.dummy:
            self.update = self.dummy_update
            self.draw_alternate = self.dummy_draw_alternate
            self.draw_same = self.dummy_draw_same
            self.draw_on = self.dummy_draw_on
            
    def clear_matrix(self):
        self.mat = np.matrix(
            [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ])
        self.status = "off"
        height = self.mat.shape[0]
        width = self.mat.shape[1]
        for i in range(0, height):
            for k in range(0, width):
                self.device.pixel(k,i, self.mat[i,k], redraw = False)
        self.status = "off"

    def dummy_clear_matrix(self):
        self.status = "off" 
        
    def update(self):
        self.device.flush()

    def dummy_update(self):
        print self.status + " drawn on ledmatrix @ " + t.strftime('%H:%M:%S') 
        
    def off(self):
        if not self.dummy:
            self.clear_matrix()
            self.update()
        if self.dummy:
            self.dummy_clear_matrix()
            self.dummy_update()
        print "Matrix is off"
        
    def draw_alternate(self, vert_a = True):
        if vert_a:
            self.mat=np.matrix(
                [
                [1,1,1,1,1,1,1,1, 1,1,0,0,0,0,1,1],
                [1,1,1,1,1,1,1,1, 1,1,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0, 1,1,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0, 1,1,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0, 1,1,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0, 1,1,0,0,0,0,1,1],
                [1,1,1,1,1,1,1,1, 1,1,0,0,0,0,1,1],
                [1,1,1,1,1,1,1,1, 1,1,0,0,0,0,1,1]
                ])
        if not vert_a:
            self.mat=np.matrix(
                [
                [1,1,0,0,0,0,1,1, 1,1,1,1,1,1,1,1],
                [1,1,0,0,0,0,1,1, 1,1,1,1,1,1,1,1],
                [1,1,0,0,0,0,1,1, 0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,1,1, 0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,1,1, 0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,1,1, 0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,1,1, 1,1,1,1,1,1,1,1],
                [1,1,0,0,0,0,1,1, 1,1,1,1,1,1,1,1]
                ])
        height = self.mat.shape[0]
        width = self.mat.shape[1]
        for i in range(0, height):
            for k in range(0, width):
                self.device.pixel(k,i, self.mat[i,k], redraw = False)
        self.update()
        print "Matrix alternate. Is A vertical? " + str(vert_a)

    def draw_on(self, on_a = True):
        if on_a:
            self.mat=np.matrix(
                [
                [0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1]
                ])
        if not on_a:
            self.mat=np.matrix(
                [
                [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0]
                ])

        height = self.mat.shape[0]
        width = self.mat.shape[1]
        for i in range(0, height):
            for k in range(0, width):
                self.device.pixel(k,i, self.mat[i,k], redraw = False)
        self.update()
        print "Matrix on/off. Is A on? " + str(on_a)


    def draw_same(self, vertical = True):
        if vertical:
            self.mat=np.matrix(
                [
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1]
                ])
        if not vertical:
            self.mat=np.matrix(
                [
                [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1]
                ])
        height = self.mat.shape[0]
        width = self.mat.shape[1]
        for i in range(0, height):
            for k in range(0, width):
                self.device.pixel(k,i, self.mat[i,k], redraw = False)
        self.update()
        print "Matrix same. Are both vertical? " + str(vert)

    def dummy_draw_on(self, on_a = True):
        if on_a:
            self.status = "A is on. B is off"
        if not on_a:
            self.status = "A is off. B is on"
        self.update()
    
    def dummy_draw_alternate(self, vert_a = True):
        if vert_a:
            self.mat=np.matrix(
                [
                [1,1,1,1,1,1,1,1, 1,1,0,0,0,0,1,1],
                [1,1,1,1,1,1,1,1, 1,1,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0, 1,1,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0, 1,1,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0, 1,1,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0, 1,1,0,0,0,0,1,1],
                [1,1,1,1,1,1,1,1, 1,1,0,0,0,0,1,1],
                [1,1,1,1,1,1,1,1, 1,1,0,0,0,0,1,1]
                ])
            self.status = "Vertical bars on A"
        if not vert_a:
            self.mat=np.matrix(
                [
                [1,1,0,0,0,0,1,1, 1,1,1,1,1,1,1,1],
                [1,1,0,0,0,0,1,1, 1,1,1,1,1,1,1,1],
                [1,1,0,0,0,0,1,1, 0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,1,1, 0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,1,1, 0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,1,1, 0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,1,1, 1,1,1,1,1,1,1,1],
                [1,1,0,0,0,0,1,1, 1,1,1,1,1,1,1,1]
                ])
            self.status = "Vertical bars on B"
        self.update()

    def dummy_draw_same(self, vert = True):
        if vert:
            self.mat=np.matrix(
                [
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1],
                [1,1,0,0,0,0,1,1, 1,1,0,0,0,0,1,1]
                ])
            self.status = "Vertical bars both"
        if not vertical:
            self.mat=np.matrix(
                [
                [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1]
                ])
            self.status = "Horizontal bars both"
        self.update()    
