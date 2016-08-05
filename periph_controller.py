from peripherals import feeder, led_matrix
from datetime import datetime
import os
import pdb

try:
    import pigpio
    os.system("pigpiod")    
except ImportError:
    print "pigpio library not installed. Is this even a raspberry pi?"
    
def create_devices(periphs, pi):
    "creates device objects and starts them. Starting them is important to set the variables for activate and deactivate. "
    devices_classes = []
    for item in periphs:
        if item[0] == "feeder":
            dev = feeder.Feeder(group=item[1], gpio_pin = item[2], pi = pi)
            devices_classes.append(dev)
        if item[0] == "dummy_feeder":
            dev = feeder.Feeder(group = item[1], gpio_pin = item[2], dummy = True, pi = pi)
            devices_classes.append(dev)
        if item[0] == "led_matrix":
            dev = led_matrix.Led_matrix()
            devices_classes.append(dev)
        if item[0] == "dummy_led_matrix":
            dev = led_matrix.Led_matrix(dummy = True)
            devices_classes.append(dev)
    return devices_classes

def lookup_event(schedule):
    now = datetime.now()
    seconds_since_midnight = int(round((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()))
    for timeslot in schedule:
        if seconds_since_midnight >= timeslot[0] and seconds_since_midnight - timeslot[0] < 30:
            return timeslot[1]

def lookup_and_send_feeders (devices, group, schedule):
    to_do = lookup_event(schedule)
    gen_exp = (device for device in devices if device.group == group)
    for device in gen_exp:
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


def lookup_and_send_led_matrix (devices, schedule):
    to_do = lookup_event(schedule)
    gen_exp = (device for device in devices if device.group == "mat")
    for device in gen_exp:
        if to_do == "off":
            device.off()
        if to_do == "a_vert_training":
            device.draw_alternate()
        if to_do == "b_vert_training":
            device.draw_alternate(vert_a = False)
        if to_do == "a_vert_testing":
            device.draw_alternate()
        if to_do == "b_vert_testing":
            device.draw_alternate(vert_a = False)
        if to_do == "a_on_training":
            device.draw_on()
        if to_do == "b_on_training":
            device.draw_on(on_a = False)
        if to_do == "a_on_testing":
            device.draw_on()
        if to_do == "b_on_training":
            device.draw_on(on_a = False)    

class Controller():
    "Looks at schedule and tells the peripheral devices what to do."
    def __init__(self, current_experiment, schedule_a, schedule_b, schedule_mat):
        try:
            pi = pigpio.pi()
        except:
            pi = None
        self.devices = create_devices(current_experiment.periphs, pi)
        for device in self.devices:
            device.start()
        self.schedule_a = schedule_a
        self.schedule_b = schedule_b
        self.schedule_mat = schedule_mat
    def send_scheduled_commands(self):
        lookup_and_send_feeders(self.devices, "a", self.schedule_a)
        lookup_and_send_feeders(self.devices, "b", self.schedule_b)
        lookup_and_send_led_matrix(self.devices, self.schedule_mat)
