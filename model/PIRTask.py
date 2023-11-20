from View.InputView import Command
from checkDateFormat import checkDate

class Task:
    def __init__(self, description, deadline):
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

    def setPIMTask():
        # get_date = input("Enter date and time for task item ( in format MM/dd/yy hh:mm): ")
        enter = Command()
        get_date = enter.getDateCommand()
        while not checkDate(get_date):
            # print("Enter the right format date for task item:")
            # get_date = input()
            get_date = enter.getDateCommandAgain()
        date = get_date
        # taskItem = input("Enter task text:")
        taskItem = enter.createTaskTextCommand()
        return date, taskItem