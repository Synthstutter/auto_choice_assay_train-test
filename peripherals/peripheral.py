class Peripheral():
    def __init__(self, group, gpio_pins = False, dummy= False):
        self.gpio_pins = gpio_pins
        self.group = group
        self.status = "inactive"
        self.dummy = dummy 
        
