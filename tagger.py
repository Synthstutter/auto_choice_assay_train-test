import datetime
import time as t
import json
import os
from analyzer import check_cross_against_schedule, check_training_or_testing_against_schedule

def add_param(param, program, ard_val, schedule_a):
    if param == "program":
        return program
    if param == "datetime":
        return datetime.datetime.now()
        # date_handler = lambda obj: (
        #     obj.isoformat()
        #     if isinstance(obj, datetime.datetime)
        #     or isinstance(obj, datetime.date)
        #     else None)
        # return json.dumps(datetime.datetime.now(), default=date_handler)
    if param == 'ard_sensor':
        return ard_val
    if param == 'correct?':
        return check_cross_against_schedule(ard_val, schedule_a)
    if param == 'training?':
        return check_training_or_testing_against_schedule(schedule_a)

           

class Data_handler():
    def __init__(self, experiment, schedule_a, schedule_b):
        self.save_file_name = experiment.save_file_name
        self.save_model = experiment.save_model
        self.program_name = experiment.program
        self.line_to_save = []
        self.schedule_a = schedule_a

        if not os.path.exists("data/"):
            os.makedirs("data/")
        
    def save_data(self, data):
        sav_f = "data/" + self.save_file_name + t.strftime('_%Y_%m_%d.txt')  
        with open(sav_f, 'a') as outfile:
            json.dump(self.line_to_save, outfile)
            outfile.write("\n")

    def ard_grab_and_tag_data(self, arduino_sensor):
        self.line_to_save = []
        val_from_ard= arduino_sensor.read()
        if val_from_ard:
            for item in self.save_model:
                self.line_to_save.append(add_param(item, self.program_name, val_from_ard, self.schedule_a))
            self.save_data(self.line_to_save)
            print self.line_to_save
        t.sleep(0.1)
            
