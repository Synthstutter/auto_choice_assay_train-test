#!/usr/bin/python
from importlib import import_module
from datetime import datetime

from menu import Menu
from current_experiment import Current_experiment
from tagger import Data_handler
from sensors import arduino_serial
from scheduler import Scheduler
from periph_controller import Controller


def main():
    menu = Menu()
    curr_exp = Current_experiment(import_module("experiments." + menu.experiments_prompt()))
    
    arduinos = [arduino_serial.Arduino(serial_name = curr_exp.serial_name,
                                       device_name = sensor[0],
                                       sensor_type = sensor[1],
                                       pin = sensor[2])
                    for sensor in curr_exp.ard_sensors]    
    for arduino in arduinos:
        arduino.start()
        
    running = True

    scheduler = Scheduler(curr_exp)
    controller = Controller(curr_exp, scheduler.schedule_a, scheduler.schedule_b)
    
    
    tagger = Data_handler(curr_exp)
    previous_time = datetime.now()
        
    while running:
        if (datetime.now() - previous_time).total_seconds() > 5:
            controller.send_scheduled_commands()
            previous_time = datetime.now()
            
        for arduino in arduinos:
            tagger.ard_grab_and_tag_data(arduino)
        
if __name__ == "__main__":
    main()    
