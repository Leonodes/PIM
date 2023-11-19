from model.PIRContact import Contact
from model.PIREvent import Event
from model.PIRNote import Note
from model.PIRTask import Task

class PIRView:
    def __init__(self):
        self.notes = Note
        self.tasks = Task
        self.events = Event
        self.contacts = Contact

    def displayAll(self):
        
        self.NoteDetail()

    @staticmethod
    def NoteDetail(note):
        # note = Note()
        print("Note: ")
        print("Content: "+ note.content)
    
    @staticmethod
    def TaskDetail(task):
        print("Task: ")
        print("Description: " + task.description)
        print("Deadline: " + task.deadline)

    @staticmethod
    def EventDetail(event):
        print("Event:")
        print("Description: " + event.description)
        print("Start time: " + event.start_time)
        print("Alarm: " + event.alarm)

    @staticmethod
    def ContactDetail(contact):
        print("Contact: ")
        print("Name: " + contact.name)
        print("Address: " + contact.address)
        print("Mobile Number" + contact.mobileNum)