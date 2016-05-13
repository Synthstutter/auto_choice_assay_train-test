from max7219 import led
import numpy as np
from peripheral import Peripheral
import time as t
import pdb
#remember that to use max7219 library, SPI needs to be activated via raspi-config. Look at github page for max7219 library for directions on how to do this
# connect as follows:
#+5V -> RPi pin 2, +5V
#GND -> RPi pin 6, GND
#DIN -> RPi pin 19, GPIO 10(MOSI)
#CS  -> RPi pin 24, GPIO 8(SPI CE0)
#CLK -> RPi pin 23, GPIO 11(SPI CLK)

class Led_matrix(Peripheral):
    def __init__(self, *args, **kwargs):
        Peripheral.__init__(self, *args, **kwargs)
                
    def start(self):
        if not self.dummy:
            self.led_init = led.matrix(cascaded = 1)
            self.mat = []
            self.update = self.update
            self.activate_testing = self.activate
            self.deactivate_testing = self.deactivate
        if self.dummy:
            self.draw_bars = self.dummy_draw_bars
            self.update = self.dummy_update
            self.activate_testing = self.activate
            self.deactivate_testing = self.deactivate

    def draw_bars(self, vertical = True):
        if vertical:
            self.mat=np.matrix(
            [
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1]
            ])
            self.status = "vertical_bars"
        if not vertical:
            self.mat=np.matrix(
            [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1]
            ])
            self.status = "horizontal_bars"
        height = mat.shape[0]
        width = mat.shape[1]
        for i in range(0, height):
            for k in range(0, width):
                self.device.pixel(k,i, mat[i,k], redraw = False)

    def clear_matrix(self):
        
        self.mat = np.matrix(
            [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
            ])
        self.status = "off"
        height = mat.shape[0]
        width = mat.shape[1]
        for i in range(0, height):
            for k in range(0, width):
                self.device.pixel(k,i, mat[i,k], redraw = False)
        self.status = "off"

    def dummy_clear_matrix(self):
        self.status = "off" 
        
    def update(self):
        self.device.flush()

    def dummy_draw_bars(self, vertical = True):
        if vertical:
            self.mat=np.matrix(
            [
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1]
            ])
            self.status = "vertical_bars"
        if not vertical:
            self.mat=np.matrix(
            [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1]
            ])
            self.status = "horizontal_bars"

    def dummy_update(self):
        print self.status + " drawn on group " + self.group + " ledmatrix @ " + t.strftime('%H:%M:%S') 

    def activate(self):
        if not self.dummy:
            self.draw_bars(vertical = True)
            self.update()
        elif self.dummy:
            self.dummy_draw_bars(vertical = True)
            self.dummy_update()

    def deactivate(self):
        if not self.dummy:
            self.draw_bars(vertical = False)
            self.update()
        elif self.dummy:
            self.dummy_draw_bars(vertical = False)
            self.dummy_update()

    def off(self):
        if not self.dummy:
            self.clear_matrix()
            self.update()
        if self.dummy:
            self.dummy_clear_matrix()
            self.dummy_update()
