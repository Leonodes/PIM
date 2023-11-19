class Command:

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
    def createEventDescCommand():
        return input("Enter a description for this event: ")
    