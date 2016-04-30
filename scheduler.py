from peripherals import feeder, max7219
import threading
import time as t

def create_devices(periphs):
    periphs_classes = []
    for item in periphs:
        if item[0] == "feeder":
            dev = feeder.Feeder(group = item[1], gpio_pins = item[2])
            devices_classes.append(dev)
        if item[0] == "led_matrix":
            dev = max7219.Led_matrix(group = item[1], gpio_pins = item[2])
            devices_classes.append(dev)
    return periphs_classes

class Scheduler():
    def __init__(current_experiment):
        self.running = False
        self.training = False
        self.testing = False
        self.current_experiment = current_experiment
        self.schedule = current_experiment.device_schedule
        self.program = current_experiment.program
        self.switch_seconds = current_experiment.switch_seconds
        self.testing_seconds = current_experiment.testing_seconds

        self.periphs = create_devices(current_experiment.periphs)

    def run_program(self):
        while self.running:
            if self.program[0] == "a_b_switching" and self.program[1] == "simple":
                for item in self.periphs:
                    if item.group == "a":
                        item.active()
                    if item.group == "b":
                        item.active()
                t.sleep(switch_seconds)
    

  
