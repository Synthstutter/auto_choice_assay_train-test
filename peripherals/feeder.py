from peripheral import Peripheral
try:
    import RPi.GPIO as GPIO
except:
    print "RPi.GRPIO library not installed. Is this even a raspberry pi?"
    
class Feeder(Peripheral):
    def __init__(self, *args, **kwargs):
        if not dummy:
            self.open_feeder = open_feeder
            self.close_feeder = close_feeder
            # self.update = update_feeder
        if dummy:
            self.open_feeder = dummy_open_feeder
            self.close_feeder = dummy_close_feeder
            # self.update = dummy_update_feeder
        if len(self.gpio_pins) > 1:
            print "too many pins called. Feeder needs only 1 pin"    
    def open_feeder(self):
        self.status = "open"
    def close_feeder(self):
        self.status = "closed"
    def dummy_open_feeder(self):
        self.status = "open"
    def dummy_close_feeder(self):
        self.status = "closed"
    # def update(self):
    #     if self.status == "open":
    #         #set motor command here    
    #     if self.status == "closed":
