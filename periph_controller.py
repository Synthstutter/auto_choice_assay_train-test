from peripherals import feeder, led_matrix
from datetime import datetime
import pdb

def create_devices(periphs):
    "creates device objects and starts them. Starting them is important to set the variables for activate and deactivate. "
    devices_classes = []
    for item in periphs:
        if item[0] == "feeder":
            dev = feeder.Feeder(group=item[1], gpio_pins=item[2])
            dev.start()
            devices_classes.append(dev)
        if item[0] == "dummy_feeder":
            dev = feeder.Feeder(group = item[1], gpio_pins = item[2], dummy = True)
            dev.start()
            devices_classes.append(dev)
        if item[0] == "led_matrix":
            dev = led_matrix.Led_matrix(group = item[1])
            dev.start()
            devices_classes.append(dev)
        if item[0] == "dummy_led_matrix":
            dev = led_matrix.Led_matrix(group = item[1], dummy = True)
            dev.start
            devices_classes.append(dev)    
    return devices_classes

def lookup_event(schedule):
    now = datetime.now()
    seconds_since_midnight = int(round((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()))
    for timeslot in schedule:
        if seconds_since_midnight >= timeslot[0] and seconds_since_midnight - timeslot[0] < 30:
            return timeslot[1]

def lookup_and_send (devices, group, schedule):
    to_do = lookup_event(schedule)
    for device in devices:
        if device.group == group:
            if to_do == "off":
                device.off()
            if to_do == "correct_training":
                print "training:"
                device.activate()
            if to_do == "incorrect_training":
                device.deactivate()
            if to_do == "correct_testing":
                print "TESTING:"
                device.activate_testing()
            if to_do == "incorrect_testing":
                device.deactivate_testing()


class Controller():
    "Looks at schedule and tells the peripheral devices what to do."
    def __init__(self, current_experiment, schedule_a, schedule_b):
        self.devices = create_devices(current_experiment.periphs)
        for device in self.devices:
            device.start()
        self.schedule_a = schedule_a
        self.schedule_b = schedule_b
    def send_scheduled_commands(self):
        lookup_and_send(self.devices, "a", self.schedule_a)
        lookup_and_send(self.devices, "b", self.schedule_b)
