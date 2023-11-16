from PIRNote import Note
from PIRTask import Task
from PIREvent import Event
from PIRContact import Contact
import NoteView
import TaskView 
import EventView
import ContactView
from PIRController import PIRController

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

    # insert note in the line before "Task"
    with open("records.pim", "w") as file:
        for i, line in enumerate(lines):
            
            if i == line_num - 1:
                file.write(note_to_insert + "\n")
            file.write(line)

def create():
    # create quick notes, task, contact, event
    print("1. Create Quick Notes\n")
    print("2. Create tasks.\n")
    print("3. Create contacts.\n")
    print("4. Create events.\n")
    command = int(input("Please enter 1, 2, 3, 4 to choose what you want to create.\n"))
    while True:
        if command == 1:
            notes = input("Please enter your note: \n") # string
            createNote(notes) #save notes
            print("")
        elif command == 2:
            pass
        elif command == 3:
            pass
        elif command == 4:
            pass
        else:
            command = int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))

# def searchMobileNo(Mobile_No):
#     with open("records.pim", "r") as file:
#         lines = file.readlines()
#     #search the mobile no.
#     for i, line in enumerate(lines):
#         if Mobile_No in line:
#             line_num = i
#             print(i)


def search():
    #search for PIRs based on criteria
    print("Criteria:\n")
    print("1. Note\n")
    print("2. Description\n")
    print("3. Name\n")
    print("4. Adddress\n")
    print("5. Mobile Number\n")
    command = input("Please enter 1, 2, 3, 4, 5 to choose the criteria of what you want to search.\n")
    # string command
    command = int(input("Please enter 1, 2, 3, 4, 5 to choose what you want to do.\n"))
    while True:
        if command == 1:
            pass
        elif command == 2:
            pass
        elif command == 3:
            pass
        elif command == 4:
            pass
        elif command == 5:
            Mobile_No = input("Please enter your mobile number: \n") # string
            searchMobileNo(Mobile_No)
        else:
            command = int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))



#main
def main():
    print("Hi! Here is Personal Information Manager. Please choose what you want to do.\n")
    print("1. Create Personal Information Records.\n")
    print("2. Search Personal Information Records.\n")
    print("3. Modify Personal Information Records.\n")
    print("4. Delete Personal Information Records.\n")
    print("5. Display Personal Information Records.\n")
    # string command
    command = int(input("Please enter 1, 2, 3, 4, 5 to choose what you want to do.\n"))
    while True:
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
