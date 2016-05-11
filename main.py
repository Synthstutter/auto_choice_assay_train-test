#!/usr/bin/python
from importlib import import_module
from menu import Menu
from current_experiment import Current_experiment
from tagger import Data_handler
from sensors import arduino_serial
from scheduler import Scheduler

# import threading

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
    scheduler.create_schedule()
    # schedule_thread = threading.Thread(target=scheduler.run_program)
    # schedule_thread.run()

    tagger = Data_handler(curr_exp)
    # sensor_thread = threading.Thread(target=tagger.ard_grab_and_tag_data)
    # sensor_thread.run()

    while running:
        for arduino in arduinos:
            # scheduler.run_program()
            tagger.ard_grab_and_tag_data(arduino)
        
if __name__ == "__main__":
    main()    
