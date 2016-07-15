from peripheral import Peripheral

try:
    import pigpio
except:
    pass
    
class Feeder(Peripheral):
    def __init__(self, group, pi = None, *args, **kwargs):
        Peripheral.__init__(self, *args, **kwargs)
        self.pi = pi
        self.group = group
    def start(self):
        self.status = "closed"
        if not self.dummy:
            self.pi.set_servo_pulsewidth(self.gpio_pin, 0)

            self.off = self.close_feeder
            self.activate_testing = self.close_feeder
            self.deactivate_testing = self.close_feeder
            
        if self.dummy:
            self.open_feeder = self.dummy_open_feeder
            self.close_feeder = self.dummy_close_feeder
            self.off = self.dummy_close_feeder
            self.activate_testing = self.dummy_close_feeder
            self.deactivate_testing = self.dummy_close_feeder
        self.close_feeder()
    def open_feeder(self):
        if self.status == "closed":
            self.pi.set_servo_pulsewidth(self.gpio_pin, 700)
        self.status = "open"
    def close_feeder(self):
        if self.status == "open":
            self.pi.set_servo_pulsewidth(self.gpio_pin, 1400)
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
   
 
            
