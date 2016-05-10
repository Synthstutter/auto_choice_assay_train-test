from max7219 import led
import numpy as np
from peripheral import Peripheral
import time as t

#remember that to use max7219 library, SPI needs sudo access. Look at github page for max7219 library for directions on how to do this

class Led_matrix(Peripheral):
    def __init__(self, *args, **kwargs):
        Peripheral.__init__(self, *args, **kwargs)
        
    def start(self):
        if not self.dummy:
            self.led_init = led.matrix(cascaded = 1)
            self.mat = []
            self.update = self.update
        if self.dummy:
            self.draw_bars = self.dummy_draw_bars
            self.update = self.dummy_update
    
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
