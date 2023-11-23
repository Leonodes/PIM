class Command:
    def __init__(self):
        pass

    # choice for creating PIR
    def createCommand():
        return int(input("Please enter 1, 2, 3, 4 to choose what you want to create.\n"))
    
    def createCommandAgain():
        return int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))
    
    # create date command
    def getDateCommand():
        return input("Enter date and time for task item ( in format MM/dd/yy hh:mm): ")
    
    def getDateCommandAgain():
        return input("Enter the right format date for task item:")

    # create note command
    def createNoteCommand():
        return input("Enter your note:")
    
    # create task (text) command
    def createTaskTextCommand():
        return input("Enter task text:")
    
    # create contact command
    def createContactNameCommand():
        return input("Enter a name for contact item:")
    
    def createContactAddrCommand():
        return input("Enter an address for contact item: ")
    
    def createContactMobileNumCommand():
        return int(input("Enter a number for contact item"))
    
    # create event command
    def createEventDescCommand(self):
        return input("Enter a description for this event: ")

    def searchCommand(self):
        return int(input("Please enter search criteria: 1,2,3."))
    
    def get_text_criteria(self):
        return input("Enter text for search: ")
    
    def get_time_criteria(self):
        return input("Enter date and time for search (YYYY/MM/DD hh:mm): ")
    
    def get_time_criteria_again(self):
        return input("Enter the right format search date: ")
    
    def get_time_condition(self):
        return input("Enter condition: < , = , >")
    
    def get_time_condition_again():
        return input("Enter the right time search condition: ")
    
    def get_operator(self):
        return input("Enter the logical operator (!, ||, or &&), or press Enter to finish: ")
    
    def get_operator_again(self):
        return input("Enter the right format logical opeartor: ")
    
    def get_not_logical_input(self):
        not_input = input("Enter condition (time, value, condition) or (text, value): ")
        not_input = not_input.split(",")
        return not_input
    
    def get_or_logical_input(self):
        or_input = input("Enter condition (time, value, condition) or (text, value): , or press enter to finish. ")
        or_input = or_input.split(",")
        return or_input

    def get_and_logical_input(self):
        and_time_input = input("Enter time criteria: value (YYYY/MM/DD hh:mm), condition: ")
        and_time_input = and_time_input.split(",")
        and_text_input = input("Enter text criteria: value: ")
        and_text_input = and_text_input.split(",")
        return and_time_input,and_text_input

    
    
    