from model.PIRNote import Note
from model.PIRTask import Task
from model.PIREvent import Event
from model.PIRContact import Contact
from View.PIRView import NoteDetail, TaskDetail, EventDetail, ContactDetail


class PIRController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    # def setNoteContent(self, content):
        # self.model.setContent(content)

