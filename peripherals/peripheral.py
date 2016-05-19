class Peripheral():
    def __init__(self, group, gpio_pin = False, dummy= False):
        self.gpio_pin = gpio_pin
        self.group = group
        self.status = "inactive"
        self.dummy = dummy 
        
