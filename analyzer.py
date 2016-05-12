from datetime import datetime

def lookup_event(schedule):
    now = datetime.now()
    seconds_since_midnight = int(round((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()))
    for timeslot in schedule:
        if seconds_since_midnight >= timeslot[0] and seconds_since_midnight - timeslot[0] < 30:
            return timeslot[1]


def check_cross_against_schedule(cross, schedule_a):
    try:
        current_status_of_a = lookup_event(schedule_a).split("_")[0]
        if cross == "a" and current_status_of_a == "correct":
            return "correct"
        if cross == "a" and current_status_of_a == "incorrect":
            return "incorrect"
        if cross == "b" and current_status_of_a == "correct":
            return "incorrect"
        if cross == "b" and current_status_of_a == "incorrect":
            return "correct"
    except:
        return "off"
def check_training_or_testing_against_schedule(schedule_a):
    try:
        current_status_of_a = lookup_event(schedule_a).split("_")[1]
        if current_status_of_a:
            return current_status_of_a
    except:
        return "off"
