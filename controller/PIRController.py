from PIRNote import Note
from PIRContact import Contact
from PIRTask import Task
from PIREvent import Event
import NoteView
import TaskView
import EventView
import ContactView

class PIRController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    # def setNoteContent(self, content):
        # self.model.setContent(content)

