from View.InputView import Command
from checkDateFormat import checkDate

class Task:
    def __init__(self, description, deadline):
        self.PIRType = 'Task'
        self.description = description
        self.deadline = deadline
    # def getDescription(self):
    #     return self.description
    # def setDescription(self, description):
    #     self.description = description
    # def getDeadline(self):
    #     return self.deadline
    # def setDeadline(self, deadline):
    #     self.deadline = deadline
    # def display(self):
    #     print(self.description)
    #     print(self.deadline)
    # def detail_display(self):
    #     print("The task is {}".format(self.description))
    #     print("The deadline for this task is {}".format(self.deadline))
    # get task content


    #create  
    def setTask(self, newDesc, newDeadline):
        self.description = newDesc
        self.deadline = newDeadline
        return self.PIRType, self.description, self.deadline
    
    # read
    def getPIMTask(self):
        return  self.PIRType, self.description, self.deadline

    # tostring
    def TaskToString(self):
        string = self.PIRType + ":\nDescription: " + self.description + "\nDeadline: " + self.deadline
        return string
    
    # task to PIR record form
    def TaskToPIR(self):
        return self.description + "," + self.deadline
    
    # update
    def updateTask(self, newDesc, newDeadline):
        if newDesc != self.description:
            self.description = newDesc
        if newDeadline != self.deadline:
            self.deadline = newDeadline
            return self.PIRType, self.description, self.deadline
    
    # delete