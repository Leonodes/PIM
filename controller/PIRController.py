from model.PIRNote import Note
from model.PIRTask import Task
from model.PIREvent import Event
from model.PIRContact import Contact
# from View.PIRView import NoteDetail, TaskDetail, EventDetail, ContactDetail
from checkDateFormat import checkDate
from insert_delete_replace import insert, delete, replace
from findIndex import findIndex
from View.PIRView import PIRView


class PIRController:
    def __init__(self):
        self.notes = Note
        self.tasks = Task
        self.events = Event
        self.contacts = Contact
    
    def create(self):
        print("1. Create Quick Notes")
        print("2. Create tasks.")
        print("3. Create contacts.")
        print("4. Create events.")
        command = int(input("Please enter 1, 2, 3, 4 to choose what you want to create.\n"))
        # insert PIR into PIM file
        if command == 1:
            note_content = self.setPIMNote()
            note = Note(note_content)
            insert(note,findIndex("note"))
        elif command == 2:
            date,taskItem = self.setPIMTask()
            task = Task(date, taskItem)
            insert(task, findIndex("task"))
        elif command == 3:
            name, address, mobileNum = self.setPIMContact()
            contact = Contact(name, address, mobileNum)
            insert(contact, findIndex("contact"))
        elif command == 4:
            description, start_time, alarm = self.setPIMEvent()
            event = Event(description, start_time, alarm)
            insert(event, findIndex("event"))
        else:
            command = int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))

    def displayAll():
        view = PIRView()
        noteStart = 1
        noteEnd = findIndex("note") #taskStart = noteEnd+2
        taskEnd = findIndex("task") #contactStart = taskEnd+2
        contactEnd = findIndex("contact") #eventStart = contactEnd+2
        eventEnd = findIndex("event")
        
        with open("records.pim", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if i >= noteStart & i <= noteEnd:
                view.NoteDetail(line) # line is content
            if i >= noteEnd+2 & i <= taskEnd:
                taskDescr, deadline = line.strip().split(",")
                view.TaskDetail(taskDescr, deadline)
            if i >= taskEnd+2 & i <= contactEnd:
                name, address, mobileNum = line.strip().split(",")
                view.ContactDetail(name, address, mobileNum)
            if i >= contactEnd+2 & i <= eventEnd:
                eventDescr, startTime, alarm = line.strip().split(",")
                view.ContactDetail(eventDescr, startTime, alarm)
    
    def displayNote(index):
        noteView = PIRView()
        with open("records.pim", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if i == index:
                noteView.NoteDetail(line) # line is content

    def displayTask(index):
        taskView = PIRView()
        with open("records.pim", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if i == index:
                taskDescr, deadline = line.strip().split(",")
                taskView.TaskDetail(taskDescr, deadline)
    
    def displayContact(index):
        contactView = PIRView()
        with open("records.pim", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if i == index:
                name, address, mobileNum = line.strip().split(",")
                contactView.ContactDetail(name, address, mobileNum)
    
    def displayEvent(index):
        eventView = PIRView()
        with open("records.pim", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if i == index:
                eventDescr, startTime, alarm = line.strip().split(",")
                eventView.ContactDetail(eventDescr, startTime, alarm)

    # get note content
    @staticmethod
    def setPIMNote():
        get_note_content = input("Enter your note:")
        return get_note_content
    
    # get task content
    @staticmethod
    def setPIMTask():
        get_date = input("Enter date and time for task item ( in format MM/dd/yy hh:mm): ")
        while not checkDate(get_date):
            print("Enter the right format date for task item:")
            get_date = input()
        taskItem = input("Enter task text:")
        return get_date, taskItem
    
    # get contact content
    @staticmethod
    def setPIMContact():
        get_name = input("Enter a name for contact item:")
        get_addr = input("Enter an address for contact item: ")
        get_mobileNum = int(input("Enter a number for contact item"))
        return get_name, get_addr, get_mobileNum

    # get event content
    @staticmethod
    def setPIMEvent():
        get_description = input("Enter a description for this event: ")
        get_start_time = input("Enter start time for event item (MM/dd/yy hh:mm): ")
        while not checkDate(get_start_time):
            print("Enter the right format date for start time:")
            get_start_time = input()
            
        get_alarm = input("Enter a time to alarm you (MM/dd/yy hh:mm):")
        while not checkDate(get_alarm):
            print("Enter the right format date for alarm time:")
            get_alarm = input()
        return get_description, get_start_time, get_alarm

