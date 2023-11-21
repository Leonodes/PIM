from model.PIRNote import Note
from model.PIRTask import Task
from model.PIREvent import Event
from model.PIRContact import Contact
from View.PIRView import NoteDetail, TaskDetail, EventDetail, ContactDetail
from datetime import datetime
from controller.insert_delete_replace import insert, delete, replace
import re
import sys

def create():
    # create quick notes, task, contact, event
    print("1. Create Quick Notes")
    print("2. Create tasks.")
    print("3. Create contacts.")
    print("4. Create events.")
    command = int(input("Please enter 1, 2, 3, 4 to choose what you want to create.\n"))
    if command == 1:
        # note = setPIMNote()
        insert(setPIMNote(),findIndex("note"))
    elif command == 2:
        date,taskItem = setPIMTask()
        insert([taskItem,date],findIndex("task"))
    elif command == 3:
        name, address, mobileNum = setPIMContact()
        insert([name, address, mobileNum], findIndex("contact"))
    elif command == 4:
        description, start_time, alarm = setPIMEvent()
        insert([description, start_time, alarm], findIndex("event"))
    else:
        command = int(input("Your input is wrong. Please enter 1, 2, 3, 4, 5 to choose again."))


def displayPIR(type):
    pass

def checkDateFormat(date):
    if date is None:
        return False
    date_format = "%Y/%m/%d %H:%M"
    try:
        datetime.strptime(date.strip(), date_format)
    except ValueError:
        return False
    return True

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

def setPIMNote():
    get_note_content = input("Enter your note:")
    return get_note_content

def setPIMTask():
    get_str = input("Enter date for task item (MM/dd/yy hh:mm): ")
    while not checkFormat(get_str):
        print("Enter the right format date for task item:")
        get_str = input()
    date = get_str
    taskItem = input("Enter task text:")
    return date, taskItem

def setPIMContact():
    get_name = input("Enter a name for contact item:")
    get_addr = input("Enter an address for contact item: ")
    get_mobileNum = int(input("Enter a number for contact item"))
    return get_name, get_addr, get_mobileNum

def setPIMEvent():
    get_description = input("Enter a description for this event: ")
    get_start_time = input("Enter start time for event item (MM/dd/yy hh:mm): ")
    while not checkFormat(get_start_time):
        print("Enter the right format date for task item:")
        get_start_time = input()
    get_alarm = input("Enter a time to alarm you (MM/dd/yy hh:mm):")
    while not checkFormat(get_alarm):
        print("Enter the right format date for task item:")
        get_alarm = input()
    return get_description, get_start_time, get_alarm
    
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


def get_logical_criteria():
    logical_criteria = []
    while True:
        operator = input("Enter operator (!, ||, or &&), or press Enter to finish: ")
        if not operator:
            break
        condition = input("Enter condition (time, condition, value) or (text, value): ")
        condition = condition.split(",")
        logical_criteria.append([operator, condition])
    return logical_criteria

def remove_from_file(strings_to_remove):
    with open("records.pim", 'r') as file:
        for line in file:
            if not any(string in line for string in strings_to_remove):
                print(line.rstrip())  


def get_logical_criteria():
    logical_conditions = []
    conditions = []
    operator = input("Enter operator (!, ||, or &&) ")
    while True:
        if operator == "!":
            condition = input("Enter condition (time, value, condition) or (text, value): ")
            condition = condition.split(",")
            logical_conditions.append(condition)
            break
        if operator == "||":         
            condition = input("Enter condition (time, value, condition) or (text, value): , or press enter to finish. ")
            if not condition:
                break            
            condition = condition.split(",")  
            conditions.append(condition)
            logical_conditions.append(conditions)
        if operator == "&&":         
            condition = input("Enter time condition (value MM/dd/yy hh:mm, condition)")
            condition = condition.split(",")  
            conditions.append(condition)
            logical_conditions.append(conditions)
            condition = input("Enter text condition (value)")
            condition = condition.split(",")  
            conditions.append(condition)
            logical_conditions.append(conditions)
            break
    return [operator,logical_conditions]

def matches_logical_criteria(logical_criteria):
    operator = logical_criteria[0]
    logical_conditions = logical_criteria[1][0]
    if operator == "!":
        if logical_conditions[0] == "text": 
            remove_from_file(matches_text_criteria(logical_conditions[1]))
        if logical_conditions[0] == "time":
            remove_from_file(matches_time_criteria(logical_conditions[0], logical_conditions[1]))
    if operator == "||": 
        for logical_condition in logical_conditions: 
            if logical_condition[0] == "text": 
                print(matches_text_criteria(logical_condition[1]))
            if logical_condition[0] == "time":
                print(matches_time_criteria([logical_condition[1], logical_condition[2]]))
    if operator == "&&":
        list1 = matches_time_criteria(logical_conditions[0])
        list2 = matches_text_criteria(logical_conditions[1][0])
        set1 = set(list1)
        set2 = set(list2)
        common_elements = set1.intersection(set2)
        common_elements_list = list(common_elements)
        print(common_elements_list)
        

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
            criteria = int(input("Please enter search criteria: 1,2,3."))
            if criteria == 1:
                print(matches_text_criteria(get_text_criteria()))
            if criteria == 2:
                print(matches_time_criteria(get_time_criteria()))
            if criteria == 3:
                print(matches_logical_criteria(get_logical_criteria()))          
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


