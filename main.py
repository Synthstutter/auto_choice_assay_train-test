#!/usr/bin/python
from importlib import import_module
from menu import Menu
from current_experiment import Current_experiment
from retriever import Retriever
from tagger import Data_handler
import arduino_serial as ser
from sensors import arduino_serial
from scheduler import Scheduler

import threading
import os

if __name__ == "__main__":
    menu = Menu()
    curr_exp = Current_experiment(import_module("experiments." + menu.experiments_prompt()))
    arduinos = [arduino_serial.Arduino(serial_name = curr_exp.serial_name,
                                       device_name = sensor[0],
                                       sensor_type = sensor[1],
                                       pin = sensor[2])
                    for sensor in curr_exp.ard_sensors]

    
    running = True

    scheduler = Scheduler(curr_exp)
    schedule_thread = threading.Thread(target=scheduler.run_program)
    schedule_thread.run()

    tagger = Data_handler(curr_exp)
    sensor_thread = threading.Thread(target = tagger.ard_grab_and_tag_data)
    sensor_thread.run()
    
    while running:
        for ard in arduinos:
            tagger.ard_grab_and_tag_data()
        for item in retriever.arduino_input:
            tagger.ard_grab_and_tag_data()
            tagger.save_data()
