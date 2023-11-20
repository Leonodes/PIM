from View.InputView import Command
from checkDateFormat import checkDate

class Event:
    def __init__(self, description, start_time, alarm):
        self.description = description
        self.start_time = start_time
        self.alarm = alarm
    # def getDescription(self):
    #     return self.description
    # def setDescription(self, description):
    #     self.description = description
    # def getStartTime(self):
    #     return self.start_time
    # def setStartTime(self, start_time):
    #     self.start_time = start_time
    # def getAlarm(self):
    #     return self.alarm
    # def setAlarm(self, alarm):
    #     self.alarm = alarm
    # def display(self):
    #     print(self.description)
    #     print(self.start_time)
    #     print(self.alarm)
    # def detail_display(self):
    #     print("The event is {}".format(self.description))
    #     print("The event starts at {}". format(self.start_time))
    #     print("The system will alarm you at {}".format(self.alarm))
    # get event content

    def setPIMEvent():
        enter = Command()
        # get_description = input("Enter a description for this event: ")
        get_description = enter.createEventDescCommand()
        
        # get_start_time = input("Enter start time for event item (MM/dd/yy hh:mm): ")
        get_start_time = enter.getDateCommand()
        while not checkDate(get_start_time):
            # print("Enter the right format date for start time:")
            # get_start_time = input()
            get_start_time = enter.getDateCommandAgain()
        
        # get_alarm = input("Enter a time to alarm you (MM/dd/yy hh:mm):")
        get_alarm = enter.getDateCommand()
        while not checkDate(get_alarm):
            # print("Enter the right format date for alarm time:")
            # get_alarm = input()
            get_alarm = enter.getDateCommandAgain()

        return get_description, get_start_time, get_alarm
