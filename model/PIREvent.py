class Event:
    def __init__(self, description, start_time, alarm):
        self.description = description
        self.start_time = start_time
        self.alarm = alarm
    def getDescription(self):
        return self.description
    def setDescription(self, description):
        self.description = description
    def getStartTime(self):
        return self.start_time
    def setStartTime(self, start_time):
        self.start_time = start_time
    def getAlarm(self):
        return self.alarm
    def setAlarm(self, alarm):
        self.alarm = alarm
    # def display(self):
    #     print(self.description)
    #     print(self.start_time)
    #     print(self.alarm)
    # def detail_display(self):
    #     print("The event is {}".format(self.description))
    #     print("The event starts at {}". format(self.start_time))
    #     print("The system will alarm you at {}".format(self.alarm))
