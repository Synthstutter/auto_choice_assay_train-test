from peripherals import feeder, led_matrix
import threading
import time as t
from random import shuffle, randint

def create_devices(periphs):
    devices_classes = []
    for item in periphs:
        if item[0] == "feeder":
            dev = feeder.Feeder(group = item[1], gpio_pins = item[2])
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

class Scheduler():
    def __init__(self, current_experiment):
        self.training = False
        self.testing = False
        # self.schedule = current_experiment.device_schedule
        self.program = current_experiment.program
        self.switch_seconds_min = current_experiment.switch_seconds[0]
        self.switch_seconds_max = current_experiment.switch_seconds[1]
        self.testing_seconds = current_experiment.testing_seconds
        self.periphs = create_devices(current_experiment.periphs)

    def run_program(self):
        if self.program[0] == "a_b_switching" and self.program[1] == "simple":
            groups = ["a","b"]
            shuffle(groups)
            for item in self.periphs:
                if item.group == groups[0]:
                    item.activate()
                if item.group == groups[1]:
                    item.deactivate()
            t.sleep(randint(self.switch_seconds_min, self.switch_seconds_max))
