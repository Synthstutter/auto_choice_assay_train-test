# by default, serial name is /dev/ttyACM0, "dummy" will have a fake arduino input
serial_name = "dummy"

#the number of arduino sensors and pins and raspberry pi sensors and pins
ard_sensors = 'ir'
    
#not using sensors yet, but will in the near future
rasp_sensors = [
    ]

########################################################################    
#action of peripherals
program = "on_off"
               

#need to put raspberry pi pins here for these as the 3rd argument if needed. preface with "dummy_" for setting up a dummy version of peripheral device, for pin use GPIO pin, not the regular raspberry pi board pin
periphs =[['led_matrix'],
          ['dummy_feeder', 'a', 21],
          ['dummy_feeder', 'b', 20]
         ]

training_switch_seconds = [30, 300] # min time, max time
testing_duration_secs = 120 # test for ____ seconds
testing_how_often = [900, 1800] # [test every min secs, max secs]

#for start and end times use minute of day. 6 am would be 360 for instance
start_time = 360 
end_time = 1080 
#########################################################################

#the experiment name used for data file name
exp_name = "test_experiment"

#prefix of file name ex. save_file_name + "_date.txt"
save_file_name = "test_data"

#data to tag
save_model = [
    "program",
    "ard_sensor",
    "datetime",
    "correct?",
    "training?"
    ]

