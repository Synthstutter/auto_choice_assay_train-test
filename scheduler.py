from peripherals import feeder, led_matrix
import threading
import time as t
from random import shuffle, randint
import numpy as np
import pdb

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
        self.training_switch_seconds_min = current_experiment.training_switch_seconds[0]
        self.training_switch_seconds_max = current_experiment.training_switch_seconds[1]
        self.testing_duration_secs = current_experiment.testing_duration_secs
        self.testing_how_often = current_experiment.testing_how_often
        self.periphs = create_devices(current_experiment.periphs)
        self.start_time = current_experiment.start_time
        self.end_time = current_experiment.end_time
        
        self.schedule = None

    # def run_program(self):
    #     if self.program[0] == "a_b_switching" and self.program[1] == "simple":
    #         groups = ["a","b"]
    #         shuffle(groups)
    #         for item in self.periphs:
    #             if item.group == groups[0]:
    #                 item.activate()
    #             if item.group == groups[1]:
    #                 item.deactivate()
    #         t.sleep(randint(self.switch_seconds_min, self.switch_seconds_max))
            
    def create_schedule(self):
        resolution = 30 #seconds per smallest resolution
        self.group_a_schedule = [None] * (24*3600/resolution)
        self.group_b_schedule = [None] * (24*3600/resolution)

        start_step = self.start_time*60/resolution
        end_step = self.end_time*60/resolution
        
        for time_interval in range(start_step):
            self.group_a_schedule[time_interval] = "off"
            self.group_b_schedule[time_interval] = "off"

        for time_interval in range(end_step, 24*3600/resolution):
            self.group_a_schedule[time_interval] = "off"
            self.group_b_schedule[time_interval] = "off"

        time_interval = start_step
        
        building_training_schedule = True
        building_testing_schedule = True
        while building_training_schedule:
            how_long_before_switch = randint(self.training_switch_seconds_min/resolution, self.training_switch_seconds_max/resolution)
            groups = ["a", 'b']
            shuffle(groups)
            for t in range(time_interval,time_interval + how_long_before_switch):
                if t >= end_step:
                    break
                if groups[0] == "a":
                    self.group_a_schedule[t] = "correct_training"
                    self.group_b_schedule[t] = "incorrect_training"
                elif groups[0] == "b":
                    self.group_a_schedule[t] = "incorrect_training"
                    self.group_b_schedule[t] = "correct_training"
            time_interval += how_long_before_switch
            self.group_a_schedule[time_interval] = "off"
            self.group_b_schedule[time_interval] = "off"
            time_interval += 1
            if time_interval >= end_step:
                building_training_schedule = False

        time_interval = start_step
        while building_testing_schedule:
            testing_interval_duration = self.testing_duration_secs/resolution
            time_between_testing = randint(self.testing_how_often[0]/30,self.testing_how_often[1]/30)
            groups = ["a", 'b']
            shuffle(groups)
            time_interval = time_interval + time_between_testing
            for t in range(time_interval,time_interval + testing_interval_duration):
                if t >= end_step:
                    break
                if groups[0] == "a":
                    self.group_a_schedule[t] = "correct_testing"
                    self.group_b_schedule[t] = "incorrect_testing"
                elif groups[0] == "b":
                    self.group_a_schedule[t] = "incorrect_testing"
                    self.group_b_schedule[t] = "correct_testing"
            time_interval += testing_interval_duration
            self.group_a_schedule[time_interval] = "off"
            self.group_b_schedule[time_interval] = "off"
            time_interval += 1
            if time_interval >= end_step:
                # pdb.set_trace()
                building_testing_schedule = False
        self.schedule = [self.group_a_schedule, self.group_b_schedule]
