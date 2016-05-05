from peripheral import Peripheral
try:
    import RPi.GPIO as GPIO
except:
    print "RPi.GRPIO library not installed. Is this even a raspberry pi?"
    
class Feeder(Peripheral):
    def __init__(self, *args, **kwargs):
        Peripheral.__init__(self, *args, **kwargs)
    
    def start(self):
        if not self.dummy:
            self.open_feeder = self.open_feeder
            self.close_feeder = self.close_feeder
            # self.update = update_feeder
        if self.dummy:
            self.open_feeder = self.dummy_open_feeder
            self.close_feeder = self.dummy_close_feeder
            # self.update = dummy_update_feeder
            
    def open_feeder(self):
        self.status = "open"
    def close_feeder(self):
        self.status = "closed"
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
   
            # def update(self):
    #     if self.status == "open":
    #         #set motor command here    
    #     if self.status == "closed":
