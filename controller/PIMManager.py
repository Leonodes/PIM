# create a manager class that supports some simple text-based commands for creating and managing items
import re
import json
import sys
import datetime
class PIMManager:
    def __init__(self):
        self.PIMlist = PIMCollection()
        print("Welcome to PIM.")
        while True:
            self.c = input("---Enter a command (supported commands are List Create Delete Search Save Load Quit)---")
            match self.c:
                case "List": self.list()
                case "Create": self.create()
                case "Delete": self.delete()
                case "Search": self.search()
                case "Save": self.save()
                case "Load": self.load()
                case "Quit": sys.exit(1)
    
    def list(self):
        for item in self.PIMlist:
            print(item + "\n")
    def create(self):
        iType = input("Enter an item type ( todo, note, contact or appointment )")
        match iType:
            case "todo":
                todo = PIMTodo()
                todo.setPIMTodo()
                self.PIMlist.add(todo)
            case "note":
                note = PIMNote()
                note.setPIMNote()
                self.PIMlist.add(note)
            case "appointment":
                appointment = PIMAppointment()
                appointment.setPIMAppointment()
                self.PIMlist.add(appointment)
            case "contact":
                contact = PIMContact()
                contact.setPIMContact()
                self.PIMlist.add(contact)
    def save(self):
        for item in self.PIMlist:
            # how to design json key?
                json.dumps(item.toString(),open("PIRs.json","w"))
        print("Items have been saved.\n")
    def load(self):
        patternTODO = r"^TODO"
        patternNOTE = r"^NOTE"
        patternAPP = r"^APPOINTMENT"
        patternCON = r"^CONTACT"
        PIRs = json.load(open("PIRs.json","r"))
        for PIR in PIRs:
            if (re.search(patternTODO, PIR)):
                todo = PIMTodo()
                self.PIMlist.add(todo)
            elif (re.search(patternNOTE, PIR)):
                note = PIMNote()
                self.PIMlist.add(note)
            elif (re.search(patternAPP, PIR)):
                appointment = PIMAppointment()
                self.PIMlist.add(appointment)
            elif (re.search(patternCON, PIR)):
                contact = PIMContact()
                self.PIMlist.add(contact)
        print("Item hava been loaded from PIRs.json.")
    # def search(self):
    # def delete(self):
    # search: getTODO(); getNOTE(); getAPP(); getCON(); getDATE()



            






        
        



        