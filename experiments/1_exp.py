#the experiment name used for data file name
exp_name = "test_experiment"

# by default, serial name is /dev/ttyACM0, "dummy" will have a fake arduino input
serial_name = "dummy"

#the number of arduino sensors and pins and raspberry pi sensors and pins
ard_sensors = [
    ['left_box', 'ir', "A0"],
    ['right_box', 'ir', "A1"],
    ]

#not using sensors yet, but will in the near future
rasp_sensors = [
    ]

#action of peripherals
program = ["a_b_switching", "simple"]
               

#need to put raspberry pi pins here for these as the 3rd argument if needed. preface with "dummy_" for setting up a dummy version of peripheral device
periphs =[['dummy_led_matrix', 'a' ],
          ['dummy_led_matrix', 'b' ],
          ['dummy_feeder', 'a', 1],
          ['dummy_feeder', 'b', 2]
         ]

switch_seconds = [30, 300] # min time, max time
testing_seconds = [1880, 120] # test every ___ seconds for ____ seconds

#database to save to
save_file_name = "test_data.txt"

#data to tag
save_model = [
    "ard_sensor",
    "datetime",
    # ["correct"],
    ]

