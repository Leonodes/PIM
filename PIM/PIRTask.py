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