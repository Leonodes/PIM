from model.PIRNote import Note
from model.PIRTask import Task
from model.PIREvent import Event
from model.PIRContact import Contact
from View.PIRView import NoteDetail, TaskDetail, EventDetail, ContactDetail
import re
from datetime import datetime
from controller.insert_delete_replace import insert, delete, replace
import re
from datetime import datetime
from controller.insert_delete_replace import insert
import sys

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
    print("1. Create Quick Notes")
    print("2. Create tasks.")
    print("3. Create contacts.")
    print("4. Create events.")
    command = int(input("Please enter 1, 2, 3, 4 to choose what you want to create.\n"))
    if command == 1:
        notes = input("Please enter your note: ") # string
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


def displayPIR(type):
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
        
def matches_text_criteria(text_criteria):
    found_lines = []
    with open("records.pim", "r") as file:
        for line in file:
            if text_criteria in line:
                found_lines.append(line.strip())
    return found_lines

def get_text_criteria():
    text_criteria = input("Enter text: ")
    return text_criteria

def matches_time_criteria(time_criteria):
    found_lines = []
    with open("records.pim", "r") as file:
        for line in file:
            parts = line.split(",")
            for part in parts:
                if checkDateFormat(part.strip()):
                    time = datetime.strptime(time_criteria[0].strip(),"%m/%d/%y %H:%M")
                    value = datetime.strptime(part.strip(),"%Y/%m/%d %H:%M")
                    condition = time_criteria[1]
                    if condition == "<" and value < time:
                        found_lines.append(line.strip())
                    elif condition == ">" and value > time:
                        found_lines.append(line.strip())
                    elif condition == "=" and value == time:
                        found_lines.append(line.strip())
                    else:
                        pass
        return found_lines

def get_time_criteria():
    time = input("Enter time (MM/dd/yy hh:mm): ")
    while not checkFormat(time):
        print("Enter the right format date for task item:")
        time = input()
    condition = input("Enter condition: ")
    return [time,condition]


def matches_logical_criteria(pir, logical_criteria):
    for criterion in logical_criteria:
        if criterion[0] == "!":
            if matches_logical_criteria(pir, criterion[1:]) is True:
                return False
        elif criterion[0] == "&&":
            if not all(matches_logical_criteria(pir, crit) for crit in criterion[1:]):
                return False
        elif criterion[0] == "||":
            if not any(matches_logical_criteria(pir, crit) for crit in criterion[1:]):
                return False

    return True

#main
def main():
    while True:
        print("Hi! Here is Personal Information Manager. Please choose what you want to do.")
        print("1. Create Personal Information Records.")
        print("2. Search Personal Information Records.")
        print("3. Modify Personal Information Records.")
        print("4. Delete Personal Information Records.")
        print("5. Display Personal Information Records.")
        print("6. Exit the system")
        # string command
        command = int(input("Please enter 1, 2, 3, 4, 5 to choose what you want to do."))
        if command == 1:
            print("create")
            create() # create PIR
        elif command == 2:
            print("search")
            print("1.text criteria")
            print("2.time criteria")
            print("3.logical criteria")
            criteria = int(input("Please enter search criteria. 1,2,3"))
            if criteria == 1:
                print(matches_text_criteria(get_text_criteria()))
            if criteria == 2:
                print(matches_time_criteria(get_time_criteria()))
        elif command == 3:
            pass
        elif command == 4:
            pass
        elif command == 5:
            pass
        elif command == 6:
            sys.exit()
        else:
            command = int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5, 6 to choose again."))


main()



def get_PIR():
    lines = []
    with open("records.pim", "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines


def get_logical_criteria():
    logical_criteria = []
    while True:
        operator = input("Enter operator (!, ||, or &&), or press Enter to finish: ")
        if not operator:
            break
        condition = input("Enter condition (field, condition, value): ")
        condition = condition.split(",")
        logical_criteria.append((operator, condition))
    return logical_criteria

def matches_logical_criteria(logical_criteria):
    for criterion in logical_criteria:
        if criterion[0] == "!":
            if matches_logical_criteria(get_PIR(), criterion[1:]) is True:
                return False
        elif criterion[0] == "&&":
            if not all(matches_logical_criteria(pir, crit) for crit in criterion[1:]):
                return False
        elif criterion[0] == "||":
            if not any(matches_logical_criteria(pir, crit) for crit in criterion[1:]):
                return False

    return True
