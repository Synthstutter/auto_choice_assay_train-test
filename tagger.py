import datetime
import time as t
import json
import os

def add_param(param, ard_val):
    if param == "datetime":
        date_handler = lambda obj: (
            obj.isoformat()
            if isinstance(obj, datetime.datetime)
            or isinstance(obj, datetime.date)
            else None)
        return json.dumps(datetime.datetime.now(), default=date_handler)
        # return t.localtime()
    if param == 'ard_sensor':
        return ard_val
    # if param == 'correct':
       # need this from analyzer- return 


class Data_handler():
    def __init__(self, experiment):
        self.save_file_name = experiment.save_file_name
        self.save_model = experiment.save_model
        self.line_to_save = []
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
                self.line_to_save.append(add_param(item, val_from_ard))
            self.save_data(self.line_to_save)
        t.sleep(0.1)
            
