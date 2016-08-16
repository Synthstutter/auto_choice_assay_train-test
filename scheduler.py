from random import shuffle, randint
import os
import cPickle as pickle
import time as t

class Scheduler():
    def __init__(self, current_experiment):
        self.program = current_experiment.program
        self.training_switch_seconds_min = current_experiment.training_switch_seconds[0]
        self.training_switch_seconds_max = current_experiment.training_switch_seconds[1]
        self.testing_duration_secs = current_experiment.testing_duration_secs
        self.testing_how_often = current_experiment.testing_how_often
        self.start_time = current_experiment.start_time
        self.end_time = current_experiment.end_time
       
        self.schedule_a = None
        self.schedule_b = None
        self.schedule_mat = None
        
        schedule_file = "schedules/schedule" + t.strftime('_%Y_%m_%d.txt')

        if os.path.exists(schedule_file):
            schedule = self.load_schedule(schedule_file)
            self.schedule_a = schedule["schedule_a"]
            self.schedule_b = schedule["schedule_b"]
            self.schedule_mat = schedule["schedule_mat"]        
        else:
            self.create_schedules()
            self.save_schedule()
        
    def create_schedules(self):
        resolution = 30 #seconds per smallest resolution
        group_a_schedule = [None] * (24*3600/resolution)
        group_b_schedule = [None] * (24*3600/resolution)
        group_mat_schedule = [None] * (24*3600/resolution)
        start_step = self.start_time*60/resolution
        end_step = self.end_time*60/resolution
        
        for time_interval in range(start_step):
            group_a_schedule[time_interval] = "off"
            group_b_schedule[time_interval] = "off"
            group_mat_schedule[time_interval] = "off"
        for time_interval in range(end_step, 24*3600/resolution):
            group_a_schedule[time_interval] = "off"
            group_b_schedule[time_interval] = "off"
            group_mat_schedule[time_interval] = "off"
            
        time_interval = start_step
        
        building_training_schedule = True
        building_testing_schedule = True

        led_correct_condition = None
        if self.program == "a_b_switching":
            led_correct_condition = "vert"
        if self.program == "on_off":
            led_correct_condition = "on"
            
        while building_training_schedule:
            how_long_before_switch = randint(self.training_switch_seconds_min/resolution, self.training_switch_seconds_max/resolution)
            groups = ["a", 'b']
            shuffle(groups)
            for t in range(time_interval,time_interval + how_long_before_switch):
                if t >= end_step:
                    break
                if groups[0] == "a":
                    group_a_schedule[t] = "correct_training"
                    group_b_schedule[t] = "incorrect_training"
                    group_mat_schedule[t] = "a_" + led_correct_condition + "_training"
                elif groups[0] == "b":
                    group_a_schedule[t] = "incorrect_training"
                    group_b_schedule[t] = "correct_training"
                    group_mat_schedule[t] = "b_" + led_correct_condition + "_training"
                    
            time_interval += how_long_before_switch
            group_a_schedule[time_interval] = "off"
            group_b_schedule[time_interval] = "off"
            group_mat_schedule[time_interval] = "off"
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
                    group_a_schedule[t] = "correct_testing"
                    group_b_schedule[t] = "incorrect_testing"
                    group_mat_schedule[t] = "a_" + led_correct_condition + "_testing"
                elif groups[0] == "b":
                    group_a_schedule[t] = "incorrect_testing"
                    group_b_schedule[t] = "correct_testing"
                    group_mat_schedule[t] = "b_" + led_correct_condition + "_testing"
            time_interval += testing_interval_duration
            group_a_schedule[time_interval] = "off"
            group_b_schedule[time_interval] = "off"
            group_mat_schedule[time_interval] = "off"
            time_interval += 1
            if time_interval >= end_step:
                building_testing_schedule = False
        for i in range(len(group_a_schedule)):
            group_a_schedule[i] = [i*resolution, group_a_schedule[i]]
            group_b_schedule[i] = [i*resolution, group_b_schedule[i]]
            group_mat_schedule[i] = [i*resolution, group_mat_schedule[i]]
        self.schedule_a, self.schedule_b, self.schedule_mat = group_a_schedule, group_b_schedule, group_mat_schedule

    def save_schedule(self):
        if not os.path.exists("schedules/"):
            os.makedirs("schedules/")
        to_pickle = {"schedule_a": self.schedule_a, "schedule_b": self.schedule_b, "schedule_mat": self.schedule_mat}
        f = "schedules/schedule" + t.strftime('_%Y_%m_%d.txt')  
        with open(f, 'wb') as outfile:
            pickle.dump(to_pickle,outfile)
            
    def load_schedule(self, file_to_load):
        with open(file_to_load, 'r') as loadfile:
            unpickled_schedule = pickle.load(loadfile)
            return unpickled_schedule
        
        
