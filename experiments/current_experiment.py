#the experiment name used for data file name
exp_name = "test_experiment"

# by default, serial name is /dev/ttyACM0, "dummy" will have a fake arduino input
serial_name = "dummy"

#the number of arduino sensors and thresholds and raspberry pi sensors
ard_sensors = [
    'ir' ,
    'ir' ,
    ]
    
rasp_sensors = [
    ]

#action of peripherals
program = "a_b_switching"

periphs =[['led_matrix', 'a' ],
          ['led_matrix', 'b' ]
          ['feeder', 'a', 1],
          ['feeder', 'b', 2]
         ]

switch_seconds = [30, 300] # min time, max time
testing_seconds = [1880, 120] # test every ___ seconds for ____ seconds


#database
data_file = "test_data.txt"

#data to tag
to_tag = [
    "ir_sensor",
    "datetime",
    "correct",
    ]

