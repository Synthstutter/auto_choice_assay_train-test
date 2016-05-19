import pigpio
import pdb
from peripheral import Peripheral
try:
    import RPi.GPIO as GPIO
except:
    print "RPi.GRPIO library not installed. Is this even a raspberry pi?"
    
class Feeder(Peripheral):
    def __init__(self, pi = None, *args, **kwargs):
        Peripheral.__init__(self, *args, **kwargs)
        self.pi = pi
        
        # if not self.dummy:
        #     GPIO.setmode(GPIO.BOARD)
        #     GPIO.setup(self.gpio_pin, GPIO.OUT)
        #     self.servo = GPIO.PWM(self.gpio_pin, 50)    
        #     self.servo.start(7.5)
            
    def start(self):
        self.status = "closed"
        if not self.dummy:
            self.pi.set_servo_pulsewidth(self.gpio_pin, 0)

            self.off = self.close_feeder
            self.activate_testing = self.close_feeder
            self.deactivate_testing = self.close_feeder
            pdb.set_trace()    
        if self.dummy:
            self.open_feeder = self.dummy_open_feeder
            self.close_feeder = self.dummy_close_feeder
            self.off = self.dummy_close_feeder
            self.activate_testing = self.dummy_close_feeder
            self.deactivate_testing = self.dummy_close_feeder
            
    def open_feeder(self):
        if self.status == "closed":
            self.pi.set_servo_pulsewidth(self.gpio_pin, 700)
        self.status = "open"
    def close_feeder(self):
        if self.status == "open":
            self.pi.set_servo_pulsewidth(self.gpio_pin, 1500)
        self.status = "closed"
    def end(self):
        if not self.dummy():
            self.servo.stop()
    
    def dummy_open_feeder(self):
        self.status = "open"
    def dummy_close_feeder(self):
        self.status = "closed"

    def activate(self):
        if not self.dummy:
            self.open_feeder()
        if self.dummy:
            self.dummy_open_feeder()
    def deactivate(self):
        if not self.dummy:
            self.close_feeder()
        if self.dummy:
            self.dummy_close_feeder()
   
 
            
