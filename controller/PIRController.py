from model.PIRNote import Note
from model.PIRTask import Task
from model.PIREvent import Event
from model.PIRContact import Contact
from View.PIRView import NoteDetail, TaskDetail, EventDetail, ContactDetail
from datetime import datetime
from insert_delete_replace import insert, delete, replace

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
            insert(note,self.findIndex("note"))
        elif command == 2:
            date,taskItem = self.setPIMTask()
            task = Task(date, taskItem)
            insert(task, self.findIndex("task"))
        elif command == 3:
            name, address, mobileNum = self.setPIMContact()
            contact = Contact(name, address, mobileNum)
            insert(contact, self.findIndex("contact"))
        elif command == 4:
            description, start_time, alarm = self.setPIMEvent()
            event = Event(description, start_time, alarm)
            insert(event, self.findIndex("event"))
        else:
            command = int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))

    # get note content
    @staticmethod
    def setPIMNote():
        get_note_content = input("Enter your note:")
        return get_note_content
    
    # get task content
    @staticmethod
    def setPIMTask(self):
        get_str = input("Enter date for task item (MM/dd/yy hh:mm): ")
        while not self.checkDateFormat(get_str):
            print("Enter the right format date for task item:")
            get_str = input()
        date = get_str
        taskItem = input("Enter task text:")
        return date, taskItem
    
    # get contact content
    @staticmethod
    def setPIMContact():
        get_name = input("Enter a name for contact item:")
        get_addr = input("Enter an address for contact item: ")
        get_mobileNum = int(input("Enter a number for contact item"))
        return get_name, get_addr, get_mobileNum

    # get event content
    @staticmethod
    def setPIMEvent(self):
        get_description = input("Enter a description for this event: ")
        get_start_time = input("Enter start time for event item (MM/dd/yy hh:mm): ")
        while not self.checkDateFormat(get_start_time):
            print("Enter the right format date for start time:")
            get_start_time = input()
            
        get_alarm = input("Enter a time to alarm you (MM/dd/yy hh:mm):")
        while not self.checkDateFormat(get_alarm):
            print("Enter the right format date for alarm time:")
            get_alarm = input()
        return get_description, get_start_time, get_alarm
    
    #check date for
    @staticmethod
    def checkDateFormat(date):
        if date is None:
            return False
        date_format = "%m/%d/%y %H:%M"
        if len(date.strip()) != len(date_format):
            return False
        try:
            datetime.strptime(date.strip(), date_format)
        except ValueError:
            return False
        return True
    
    # find insert line_index of inserted content
    @staticmethod
    def findIndex(Type):
        with open("records.pim", "r") as file:
            lines = file.readlines()
        if Type == "note":
            word_to_find = "Task"
        elif Type == "task":
            word_to_find = "Contact"
        elif Type == "contact":
            word_to_find = "Event"
        else:
            word_to_find = "End"
        # error handling
        for i, line in enumerate(lines):
            if word_to_find in line:
                index = i
                return index

