class NoteView:
    def printNoteDetail(self, noteContent):
        print("Note: ")
        print("Content: "+ noteContent)

class TaskView:
    def printTaskDetail(self, taskDesc, taskDeadline):
        print("Task: ")
        print("Description: " + taskDesc)
        print("Deadline: " + taskDeadline)

class EventView:
    def printEventDetail(self, eventDesc, eventStart, eventAlarm):
        print("Event:")
        print("Description: " + eventDesc)
        print("Start time: " + eventStart)
        print("Alarm: " + eventAlarm)

class ContactView:
    def printContactDetail(self, contactName,contactAddr, contactNo):
        print("Contact: ")
        print("Name: " + contactName)
        print("Address: " + contactAddr)
        print("Mobile Number" + contactNo)