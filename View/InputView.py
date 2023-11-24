class Command:
    def __init__(self):
        pass

    def mainCommand(self):
        return int(input("Please choose what you want to do. 1,2,3,4,5,6: "))
    
    # choice for creating PIR
    def createCommand(self):
        return int(input("Please enter 1, 2, 3, 4 to choose what you want to create.\n"))
    
    def createCommandAgain(self):
        return int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))
    
    # create date command
    def getDateCommand(self):
        return input("Enter date and time for task item ( in format YYYY/MM/DD hh:mm): ")
    
    def getDateCommandAgain(self):
        return input("Enter the right format date for task item:")

    # create note command
    def createNoteCommand(self):
        content = input("Enter your note:")
        return content
    
    # create task (text) command
    def createTaskTextCommand(self):
        return input("Enter task text:")
    
    # create contact command
    def createContactNameCommand(self):
        return input("Enter a name for contact item:")
    
    def createContactAddrCommand(self):
        return input("Enter an contact address: ")
    
    def createContactMobileNumCommand(self):
        return input("Enter a contact number: ")
    
    def createContactNumCommandAgain(self):
        return input("Please enter number without space: ")
    
    # create event command
    def createEventDescCommand(self):
        return input("Enter a description for this event: ")

    def searchTypeCommand(self):
        return int(input("Please enter data type you want to search: 1,2,3,4,5,6: "))

    def get_logical_condition_withtime(self):
        conditon = input("Enter condition (time, value, condition) or (text, value): , or press enter to finish. ")
        conditon = conditon.split(",")
        return conditon
    
    def get_logical_condition_text(Self):
        conditon = input("Enter text filter: ")
        conditon = conditon.split(",")
        return conditon

    def get_include_or_not(self):
        not_operator = input("Enter === ! === to search excluding this condition, or === press enter === to search including this condition: ")
        return not_operator
    
    def get_operator(self):
        operator = input("Enter operator: ||, && : , or press enter to finish. ")
        return operator
    
    def get_search_filterNoteContact(self):
        searchFilter = int(input("Enter search filter: 1.2: "))
        return searchFilter        

    def get_search_filterTaskEvent(self):
        searchFilter = int(input("Enter search filter: 1.2.3: "))
        return searchFilter

    def get_logical_condition_time(Self):
        conditon = input("Enter time: value(YYYY/MM/DD HH:MM), condition(<, = , >): ")
        conditon = conditon.split(",")
        return conditon
    
    def get_modify_option(self):
        return int(input("Enter modify option: 1,2: "))
    
    def get_modify_text(self):
        search_text = input("Enter original text you want to modify: ")
        replace_text = input("Enter replaced text: ")
        return search_text,replace_text
    
    def get_display_option(self):
        return int(input("Enter display option: 1,2,3,4,5,6: "))
    