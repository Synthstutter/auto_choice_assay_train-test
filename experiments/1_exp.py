#the experiment name used for data file name
exp_name = "test_experiment"

# by default, serial name is /dev/ttyACM0, "dummy" will have a fake arduino input
serial_name = "dummy"

#the number of arduino sensors and thresholds and raspberry pi sensors
ard_sensors = [
    ['left_box', 'ir', "A0"],
    ['right_box', 'ir', "A1"],
    ]
    
rasp_sensors = [
    ]

#action of peripherals
program = ["a_b_switching", "simple"]
               

#need to put raspberry pi pins here for these as the 3rd argument. 
periphs =[['led_matrix', 'a' ],
          ['led_matrix', 'b' ],
          ['test_feeder', 'a', 1],
          ['test_feeder', 'b', 2]
         ]

switch_seconds = [30, 300] # min time, max time
testing_seconds = [1880, 120] # test every ___ seconds for ____ seconds


#database
save_file_name = "test_data.txt"

#data to tag
save_model = [
    ["ard_sensor", 0],
    ["ard_sensor", 1],
    ["datetime"],
    ["correct"],
    ]

