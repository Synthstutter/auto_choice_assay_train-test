class Peripheral():
    def __init__(self, gpio_pin = False, dummy= False):
        self.gpio_pin = gpio_pin
        self.status = "inactive"
        self.dummy = dummy 
        
