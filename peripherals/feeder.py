from peripheral import Peripheral
try:
    import RPi.GPIO as GPIO
except:
    print "RPi.GRPIO library not installed. Is this even a raspberry pi?"
    
class Feeder(Peripheral):
    def __init__(self, *args, **kwargs):
        Peripheral.__init__(self, *args, **kwargs)
        
        
        if not self.dummy:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.gpio_pin, GPIO.OUT)
            self.servo = GPIO.PWM(self.gpio_pin, 50)    
            self.servo.start(7.5)
            
    def start(self):
        if not self.dummy:
            self.open_feeder = self.open_feeder
            self.close_feeder = self.close_feeder
            self.off = self.close_feeder
            self.activate_testing = self.close_feeder
            self.deactivate_testing = self.close_feeder
            
        if self.dummy:
            self.open_feeder = self.dummy_open_feeder
            self.close_feeder = self.dummy_close_feeder
            self.off = self.dummy_close_feeder
            self.activate_testing = self.dummy_close_feeder
            self.deactivate_testing = self.dummy_close_feeder
            
    def open_feeder(self):
        self.status = "open"
        self.servo.ChangeDutyCycle(2.5)
    def close_feeder(self):
        self.status = "closed"
        self.servo.ChangeDutyCycle(7.5)

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
   
 
            
