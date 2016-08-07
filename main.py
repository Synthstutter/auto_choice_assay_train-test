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
    curr_exp = None
    experiments = import_module("experiments").__all__
    for exp_name in experiments:
        if exp_name.startswith("*"):
            curr_exp = Current_experiment(import_module("experiments." + exp_name))
            break
    if not curr_exp:
        curr_exp = Current_experiment(import_module("experiments." + menu.experiments_prompt()))

    arduino = arduino_serial.Arduino(serial_name = curr_exp.serial_name)
    arduino.start()
        
    scheduler = Scheduler(curr_exp)

    controller = Controller(curr_exp, scheduler.schedule_a, scheduler.schedule_b, scheduler.schedule_mat)
    controller.send_scheduled_commands()
    
    tagger = Data_handler(curr_exp, scheduler.schedule_a, scheduler.schedule_b)
    previous_time = datetime.now()

    running = True
    while running:
        try:
            if (datetime.now() - previous_time).total_seconds() > 5:
                controller.send_scheduled_commands()
                previous_time = datetime.now()
            
            tagger.ard_grab_and_tag_data(arduino)
        except KeyboardInterrupt:
            running = False
        
if __name__ == "__main__":
    main()    

    
