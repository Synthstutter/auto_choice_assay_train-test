current_exp = False

class Current_experiment():
    def __init__(self, experiment_object):
        try:
            self.exp_name = experiment_object.exp_name
            self.save_file_name = experiment_object.save_file_name
            self.save_model = experiment_object.save_model
            self.serial_name = experiment_object.serial_name
            self.ard_sensors = experiment_object.ard_sensors
            self.rasp_sensors = experiment_object.rasp_sensors
            self.program = experiment_object.program
            self.periphs = experiment_object.periphs
            self.switch_seconds = experiment_object.switch_seconds
            self.testing_seconds = experiment_object.testing_seconds
            self.device_schedule = experiment_object.device_schedule
            
        except:
            print "selected experiment file is missing parameters. Check the template."
