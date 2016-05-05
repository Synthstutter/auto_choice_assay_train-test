import arduinoserial as ardser

class Ard_sensor():
    def __init__(self, serial_name,device_name, sensor_type, pin):
        self.serial_name = serial_name    
        self.device_name = device_name
        self.sensor_type = sensor_type
        self.pin = pin

    def start(self):
        if serial_name=='dummy':
            self.ard = None
            self.grab = self.dummy_grab
            self.write = self.dummy_write
            self.waiting = self.dummy_waiting
        else:
            self.ard = ardser.SerialPort(serial_name, 19200)
            self.grab = self.grab
            self.write = self.serial_write
            self.waiting = self.serial_waiting
            
    def grab(self, threshold = False):
        grabbed_data = ard.read_until('\n')
        return grabbed_data 
    
    def dummy_grab(self):
        return "random stuff from dummy arduino"

    def write(self, to_write):
        ard.write(to_write)
