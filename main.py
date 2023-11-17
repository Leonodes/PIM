from model.PIRNote import Note
from model.PIRTask import Task
from model.PIREvent import Event
from model.PIRContact import Contact
import View.NoteView
import View.TaskView 
import View.EventView
import View.ContactView
from controller.PIRController import PIRController
import re
from datetime import datetime
from controller.insert_delete_replace import insert, delete, replace

def createNote(note_to_insert):
    
    with open("records.pim", "r") as file:
        lines = file.readlines()
    # find "task"
    word_to_find = "Task"
    # line_num = None
    
    for i, line in enumerate(lines):
        if word_to_find in line:
            line_num = i
            print(i)
            break 
    print(line_num)
    if line_num == None:
        return

    # # insert note in the line before "Task"
    # with open("records.pim", "w") as file:
    #     for i, line in enumerate(lines):
            
    #         if i == line_num - 1:
    #             file.write(note_to_insert + "\n")
    #         file.write(line)

def create():
    # create quick notes, task, contact, event
    print("1. Create Quick Notes\n")
    print("2. Create tasks.\n")
    print("3. Create contacts.\n")
    print("4. Create events.\n")
    command = int(input("Please enter 1, 2, 3, 4 to choose what you want to create.\n"))
    if command == 1:
        notes = input("Please enter your note: \n") # string
        createNote(notes) #save notes
        print("")
    elif command == 2:
        date,taskItem = setPIMTask()
        insert([taskItem,date],findIndex("task"))
        pass
    elif command == 3:
        pass
    elif command == 4:
        pass
    else:
        command = int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))

def searchNote(file, Key_Note):
    with open("records.pim", "r") as file:
        lines = file.readlines()
    #search the note
        if Key_Note in lines:
            print("the criteria is found in this file.") 
            key = open(file, 'r')
            print(key.read())
        else:
            print("The criteria is not found. Please try again.")

def searchDescription(file, Key_Description):
    with open("records.pim", "r") as file:
        lines = file.readlines()
    #search the description
        if Key_Description in lines:
            print("the criteria is found in this file.") 
            key = open(file, 'r')
            print(key.read())
        else:
            print("The criteria is not found. Please try again.")

def searchName(file, Key_Name):
    with open("records.pim", "r") as file:
        lines = file.readlines()
    #search the name
        if Key_Name in lines:
            #print out the content
            print("the criteria is found in this file.") 
            key = open(file, 'r')
            print(key.read())
        else:
            print("The criteria is not found. Please try again.")

def searchAddress(file, Key_Address):
    with open("records.pim", "r") as file:
        lines = file.readlines()
    #search the address
        if Key_Address in lines:
            #print out the content
            print("the criteria is found in this file.") 
            key = open(file, 'r')
            print(key.read())
        else:
            print("The criteria is not found. Please try again.")
    
def searchMobileNo(file, Key_Mobile_No):
    with open("records.pim", "r") as file:
        lines = file.readlines()
    #search the mobile no.
        if Key_Mobile_No in lines:
            #print out the content
            print("the criteria is found in this file.") 
            key = open(file, 'r')
            print(key.read())
        else:
            print("The criteria is not found. Please try again.")

def search():
    #search for PIRs based on criteria
    print("Criteria:")
    print("1. Note")
    print("2. Description")
    print("3. Name")
    print("4. Address")
    print("5. Mobile Number\n")
    print("6. Deadline\n")
    print("7. Starting time\n")
    print("8. Alarm\n")
    command = input("Please enter 1, 2, 3, 4, 5 to choose the criteria of what you want to search.\n")
    # string command
    while True:
        if command == 1:
            Key_Note = input("Please enter the note: \n") # string
            searchNote(Key_Note)
        elif command == 2:
            Key_Description = input("Please enter the description: \n") # string
            searchDescription(Key_Description)
        elif command == 3:
            Key_Name = input("Please enter the name: \n") # string
            searchName(Key_Name)
        elif command == 4:
            Key_Address = input("Please enter the address: \n") # string
            searchAddress(Key_Address)
        elif command == 5:
            pass
        else:
            command = int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))

def modifyPIR():
    # replace() in controller/insert_delete_replace.py
    pass 
def deletePIR():
    # delete() in controller/insert_delete_replace.py
    pass

def displayPIR():
    
    pass


def checkFormat(date):
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
    
def setPIMTask():
    get_str = input("Enter date for task item (MM/dd/yy hh:mm): ")
    while not checkFormat(get_str):
        print("Enter the right format date for task item:")
        get_str = input()
    date = get_str
    taskItem = input("Enter task text:")
    return date, taskItem

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


#main
def main():
    while True:
        print("Hi! Here is Personal Information Manager. Please choose what you want to do.\n")
        print("1. Create Personal Information Records.\n")
        print("2. Search Personal Information Records.\n")
        print("3. Modify Personal Information Records.\n")
        print("4. Delete Personal Information Records.\n")
        print("5. Display Personal Information Records.\n")
        # string command
        command = int(input("Please enter 1, 2, 3, 4, 5 to choose what you want to do.\n"))
        if command == 1:
            print("create")
            create() # create PIR
        elif command == 2:
            print("search")
            search() # search PIR
        elif command == 3:
            pass
        elif command == 4:
            pass
        elif command == 5:
            pass
        else:
            command = int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))


main()
