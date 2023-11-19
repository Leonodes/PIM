class PIRView:
    @staticmethod
    def NoteDetail(noteContent):
        print("Note: ")
        print("Content: "+ noteContent)
    
    @staticmethod
    def TaskDetail(taskDesc, taskDeadline):
        print("Task: ")
        print("Description: " + taskDesc)
        print("Deadline: " + taskDeadline)

    @staticmethod
    def EventDetail(eventDesc, eventStart, eventAlarm):
        print("Event:")
        print("Description: " + eventDesc)
        print("Start time: " + eventStart)
        print("Alarm: " + eventAlarm)

    @staticmethod
    def ContactDetail(contactName,contactAddr, contactNo):
        print("Contact: ")
        print("Name: " + contactName)
        print("Address: " + contactAddr)
        print("Mobile Number" + contactNo)