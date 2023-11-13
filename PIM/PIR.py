class Note:
    def __init__(self,content):
        self.content = content
    def getContent(self):
        return self.content
    def setContent(self, content):
        self.content = content
    # def display(self):
    #     print(self.content)
    # def detail_display(self):
    #     print("The content for this note is {}".format(self.content))


# class deadline:
#     def __init__(self, d_date, d_time):
#         self.d_date = d_date
#         self.d_time = d_time
        
#     def display(self):
#         print(self.d_date, " ", self.d_time)

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
    def getDescription(self):
        return self.description
    def setDescription(self, description):
        self.description = description
    def getDeadline(self):
        return self.deadline
    def setDeadline(self, deadline):
        self.deadline = deadline
    # def display(self):
    #     print(self.description)
    #     print(self.deadline)
    # def detail_display(self):
    #     print("The task is {}".format(self.description))
    #     print("The deadline for this task is {}".format(self.deadline))

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

class Contact:
    def __init__(self, name, address, mobile_num):
        self.name = name
        self.address = address
        self.mobile_num = mobile_num
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAddress(self):
        return self.address
    def setAddress(self, address):
        self.address = address
    def getMobileNum(self):
        return self.mobile_num
    def setMobileNum(self, mobile_num):
        self.mobile_num = mobile_num
    # def display(self):
    #     print(self.name)
    #     print(self.address)
    #     print(self.mobile_num)
    # def detail_display(self):
    #     print("The name is {}".format(self.name))
    #     print("His/Her address is {}". format(self.address))
    #     print("His/Her mobile number is {}".format(self.mobile_num))