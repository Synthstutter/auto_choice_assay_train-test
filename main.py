#!/usr/bin/python
from importlib import import_module
from menu import Menu
from current_experiment import Current_experiment
from retriever import Retriever
from tagger import Data_handler
from sensors import ard_sensors
from scheduler import Scheduler

import threading
import os

if __name__ == "__main__":
    menu = Menu()
    curr_exp = Current_experiment(import_module("experiments." + menu.experiments_prompt()))

    # retriever = Retriever(curr_exp)
    arduinos = [ard_sensors.Ard_sensor(device) for device in curr_exp.ard_sensors]
    tagger = Data_handler(curr_exp)
    scheduler = Scheduler(curr_exp)

    running = True
    run_thread = threading.Thread(target=scheduler.run_program)
    run_thread.run()
    
    while running:
        
        retriever.retrieve_ard()
        for item in retriever.arduino_input:
            tagger.ard_grab_and_tag_data()
            tagger.save_data()
