from View.InputView import Command
from checkDateFormat import checkDate

class Event:
    def __init__(self, description, start_time, alarm):
        self.PIRType = 'Event'
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

    # create event    
    def setEvent(self, newDesc, newStartTime, newAlarm):
        self.description = newDesc
        self.start_time = newStartTime
        self.alarm = newAlarm
        return self.PIRType, self.description, self.start_time, self.alarm

    def getPIMEvent(self):
        return self.PIRType, self.description, self.start_time, self.alarm
    
    def EventToString(self):
        string = self.PIRType + ":\nDescription: " + self.description + "\nStart Time:" + self.start_time + "\nAlarm Time: " + self.alarm
        return string
    
    # event to PIR record form
    def EventToPIR(self):
        return self.description + "," + self.start_time + "," + self.alarm
    
    # update
    def updateEvent(self, newDesc, newStartTime, newAlarm):
        if newDesc != self.description:
            self.description = newDesc
        if newStartTime != self.start_time:
            self.start_time = newStartTime
        if newAlarm != self.alarm:
            self.alarm = newAlarm
        return self.PIRType, self.description, self.start_time, self.alarm

    # delete
