import sys
sys.path.append('C:\\Users\\Leon\\Desktop\\COMP3211\\PIM_group\\PIM')
from model.PIRNote import Note
from model.PIRTask import Task
from model.PIREvent import Event
from model.PIRContact import Contact
from controller.checkFormat import checkDateFormat,checkConditionFormat,checkOperatorFormat
from insert_delete_replace_search import insert, delete, replace,matches_text,matches_time,not_included_file
from findIndex import findIndex
from View.PIRView import PIRView
from View.InputView import Command
from View.OutputView import Board


class PIRController:
    def __init__(self):
        self.notes = Note
        self.tasks = Task
        self.events = Event
        self.contacts = Contact
    
    def create(self):
        enter = Command()
        board = Board()
        # print("1. Create Quick Notes")
        # print("2. Create tasks.")
        # print("3. Create contacts.")
        # print("4. Create events.")
        board.createBoard() # print commands instruction
        # command = int(input("Please enter 1, 2, 3, 4 to choose what you want to create.\n"))
        command = enter.createCommand() # ask user to input
        # insert PIR into PIM file
        if command == 1: # Note
            get_content = enter.createNoteCommand()
            note = Note()
            note.setNote(get_content)
            insert(note.NoteToPIR(),findIndex("note"))
        elif command == 2: #Task
            get_date = enter.getDateCommand()
            while not checkDateFormat(get_date):
                # print("Enter the right format date for task item:")
                # get_date = input()
                get_date = enter.getDateCommandAgain()
            date = get_date
            # taskItem = input("Enter task text:")
            taskItem = enter.createTaskTextCommand()
            task = Task()
            task.setTask(date, taskItem)
            insert(task.TaskToPIR(), findIndex("task"))
        elif command == 3: # Contact
            # get_name = input("Enter a name for contact item:")
            get_name = enter.createContactNameCommand()
            # get_addr = input("Enter an address for contact item: ")
            get_addr = enter.createContactAddrCommand()
            # get_mobileNum = int(input("Enter a number for contact item"))
            get_mobileNum = enter.createContactMobileNumCommand()
            contact = Contact()
            contact.setContact(get_name, get_addr,get_mobileNum)
            insert(contact.ContactToPIR(), findIndex("contact"))
        elif command == 4: # Event
            # get_description = input("Enter a description for this event: ")
            get_description = enter.createEventDescCommand()
            # get_start_time = input("Enter start time for event item (MM/dd/yy hh:mm): ")
            get_start_time = enter.getDateCommand()
            while not checkDateFormat(get_start_time):
                # print("Enter the right format date for start time:")
                # get_start_time = input()
                get_start_time = enter.getDateCommandAgain()
            # get_alarm = input("Enter a time to alarm you (MM/dd/yy hh:mm):")
            get_alarm = enter.getDateCommand()
            while not checkDateFormat(get_alarm):
                # print("Enter the right format date for alarm time:")
                # get_alarm = input()
                get_alarm = enter.getDateCommandAgain()
            event = Event()
            event.setEvent(get_description, get_start_time, get_alarm)
            insert(event.EventToPIR(), findIndex("event"))
        else:
            command = enter.createCommandAgain() # ask user to input again

    def search(self):
        enter = Command()
        board = Board() 
        board.searchBoard()
        command = enter.searchCommand()
        if command == 1: # search text
            text_criteria = enter.get_text_criteria()
            print(matches_text(text_criteria))
        elif command == 2: # search time
            time_criteria = enter.get_time_criteria()
            while not checkDateFormat(time_criteria):
                time_criteria = enter.get_time_criteria_again()
            condition = enter.get_time_condition()
            while not checkConditionFormat(condition):
                condition = enter.get_time_condition_again()
            print(matches_time(time_criteria,condition))
        elif command == 3: # search involve logical        
            operator = enter.get_operator()
            while not checkOperatorFormat(operator):
                operator = enter.get_operator_again()
            if operator == "!":
                not_logic = enter.get_not_logical_input()
                logic_type = not_logic[0]
                if logic_type == "text": 
                    print(not_included_file(matches_text(not_logic[1])))
                if logic_type == "time":
                    time_criteria = not_logic[1]
                    while not checkDateFormat(time_criteria):
                        time_criteria = enter.get_time_criteria_again()
                    print(not_included_file(matches_time(time_criteria,not_logic[2])))
            if operator == "||":
                or_logics = []
                while True:
                    or_logic = enter.get_or_logical_input()
                    if len(or_logic) == 1 and or_logic[0] == "":
                        break
                    or_logics.append(or_logic)
                for or_logic in or_logics:
                    logic_type = or_logic[0]
                    if logic_type == "text": 
                        print(matches_text(or_logic[1]))
                    if logic_type == "time":
                        time_criteria = or_logic[1] 
                        while not checkDateFormat(time_criteria):
                            time_criteria = enter.get_time_criteria_again()
                        print(matches_time(time_criteria,or_logic[2]))
            if operator == "&&":
                and_time_input,and_text_input = enter.get_and_logical_input()
                while not checkDateFormat(and_time_input[0]):
                    and_time_input = enter.get_time_criteria_again()
                list1 = matches_time(and_time_input[0],and_time_input[1])
                list2 = matches_text(and_text_input[0])
                set1 = set(list1)
                set2 = set(list2)
                common_elements = set1.intersection(set2)
                common_elements_list = list(common_elements)
                print(common_elements_list)

                
                        
                    








    

if __name__ == '__main__':
    pircontroller = PIRController()
    pircontroller.search()








            









    # # get note content
    # @staticmethod
    # def setPIMNote():
    #     # get_note_content = input("Enter your note:")
    #     # return get_note_content
    #     enter = Command()
    #     return enter.createNoteCommand()
    
    # # get task content
    # @staticmethod
    # def setPIMTask():
    #     # get_date = input("Enter date and time for task item ( in format MM/dd/yy hh:mm): ")
    #     enter = Command()
    #     get_date = enter.getDateCommand()
    #     while not checkDate(get_date):
    #         # print("Enter the right format date for task item:")
    #         # get_date = input()
    #         get_date = enter.getDateCommandAgain()
    #     date = get_date
    #     # taskItem = input("Enter task text:")
    #     taskItem = enter.createTaskTextCommand()
    #     return date, taskItem
        
    # # get contact content
    # @staticmethod
    # def setPIMContact():
    #     enter = Command()
    #     # get_name = input("Enter a name for contact item:")
    #     get_name = enter.createContactNameCommand()
    #     # get_addr = input("Enter an address for contact item: ")
    #     get_addr = enter.createContactAddrCommand()
    #     # get_mobileNum = int(input("Enter a number for contact item"))
    #     get_mobileNum = enter.createContactMobileNumCommand()

    #     return get_name, get_addr, get_mobileNum

    # # get event content
    # @staticmethod
    # def setPIMEvent():
    #     enter = Command()
    #     # get_description = input("Enter a description for this event: ")
    #     get_description = enter.createEventDescCommand()
        
    #     # get_start_time = input("Enter start time for event item (MM/dd/yy hh:mm): ")
    #     get_start_time = enter.getDateCommand()
    #     while not checkDate(get_start_time):
    #         # print("Enter the right format date for start time:")
    #         # get_start_time = input()
    #         get_start_time = enter.getDateCommandAgain()
        
    #     # get_alarm = input("Enter a time to alarm you (MM/dd/yy hh:mm):")
    #     get_alarm = enter.getDateCommand()
    #     while not checkDate(get_alarm):
    #         # print("Enter the right format date for alarm time:")
    #         # get_alarm = input()
    #         get_alarm = enter.getDateCommandAgain()

    #     return get_description, get_start_time, get_alarm
    
    # Display PIRs

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

