
class Current_experiment():
    def __init__(self, experiment_object):
        self.exp_name = experiment_object.exp_name
        self.save_file_name = experiment_object.save_file_name
        self.save_model = experiment_object.save_model
        self.serial_name = experiment_object.serial_name
        self.ard_sensors = experiment_object.ard_sensors
        self.rasp_sensors = experiment_object.rasp_sensors
        self.program = experiment_object.program
        self.periphs = experiment_object.periphs
        self.training_switch_seconds = experiment_object.training_switch_seconds
        self.testing_duration_secs = experiment_object.testing_duration_secs
        self.testing_how_often = experiment_object.testing_how_often
        self.start_time = experiment_object.start_time
        self.end_time = experiment_object.end_time

