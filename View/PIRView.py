from model.PIRContact import Contact
from model.PIREvent import Event
from model.PIRNote import Note
from model.PIRTask import Task
from controller.findIndex import findIndex

class PIRView:
    def __init__(self):
        self.notes = Note
        self.tasks = Task
        self.events = Event
        self.contacts = Contact

    def displayAll(self):
        print("----------All Personal Information Records----------")
        # note
        noteStart = 1
        noteEnd = findIndex("note") #taskStart = noteEnd+2
        taskEnd = findIndex("task") #contactStart = taskEnd+2
        contactEnd = findIndex("contact") #eventStart = contactEnd+2
        eventEnd = findIndex("event")
        
        with open("records.pim", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if i >= noteStart & i <= noteEnd:
                self.NoteDetail(line) # line is content
            if i >= noteEnd+2 & i <= taskEnd:
                taskDescr, deadline = line.strip().split(",")
                self.TaskDetail(taskDescr, deadline)
            if i >= taskEnd+2 & i <= contactEnd:
                name, address, mobileNum = line.strip().split(",")
                self.ContactDetail(name, address, mobileNum)
            if i >= contactEnd+2 & i <= eventEnd:
                eventDescr, startTime, alarm = line.strip().split(",")
                self.ContactDetail(eventDescr, startTime, alarm)
        print("------------------------END-------------------------")
    
    # def displayNote(self):
    #     #search-> index


    @staticmethod
    def NoteDetail(content):
        # note = Note()
        print("Note: ")
        print("Content: "+ content)
        print("----------------------------------------------------")
    
    @staticmethod
    def TaskDetail(description, deadline):
        print("Task: ")
        print("Description: " + description)
        print("Deadline: " + deadline)
        print("----------------------------------------------------")
    
    @staticmethod
    def ContactDetail(name, address, mobileNum):
        print("Contact: ")
        print("Name: " + name)
        print("Address: " + address)
        print("Mobile Number" + mobileNum)
        print("----------------------------------------------------")

    @staticmethod
    def EventDetail(description, start_time, alarm):
        print("Event:")
        print("Description: " + description)
        print("Start time: " + start_time)
        print("Alarm: " + alarm)
        print("----------------------------------------------------")

    