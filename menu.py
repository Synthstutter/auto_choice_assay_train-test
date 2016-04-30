from os import listdir
from os.path import isfile, join
from time import strftime
import experiments

experiments_path = "experiments"

def select_from_list(list_selection):
    prompt = []
    i = 1
    for choice in list_selection:
        to_append = "\n" + str(i) + ". " + choice
        prompt.append(to_append)
        i += 1
    user_choice = input("".join(prompt) + "\n>>>> ")
    return list_selection[user_choice - 1]
        
class Menu:
    def __init__(self):
        self.current_prompt = ""
        self.experiments_list = experiments.__all__
    # def input_prompt(self, to_display=">>>> "):
    #     choice = input(to_display)
    #     return choice

    def experiments_prompt(self):
        print "Run which experiment?"
        return select_from_list(self.experiments_list)

    def current_time(self):
        return strftime("%H:%M")

    def display_no_prompt(self, to_display):
        if isinstance(to_display, str):
            print to_display
        else:
            print str(to_display)

