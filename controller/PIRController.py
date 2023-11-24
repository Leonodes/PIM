import sys
import os
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from model.PIRNote import Note
from model.PIRTask import Task
from model.PIREvent import Event
from model.PIRContact import Contact
from model.PIRCollection import PIRCollection
from controller.checkFormat import checkDateFormat,checkConditionFormat,checkOperatorFormat
from insert_delete_replace_search import insert, delete, replace
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
    
    def main(self):
        while True:
            board = Board()
            enter = Command()
            board.mainBoard()
            activity = enter.mainCommand()
            if activity == 1:
                self.create()
            elif activity == 2:
                self.search()
            elif activity == 3:
                self.modify()
            elif activity == 4:
                self.delete()
            elif activity == 5:
                self.display()
            elif activity == 6:
                sys.exit(0)
            else:
                board.getValidInput()
            
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
        board.searchTypeBoard()
        pircollection = PIRCollection()
        while True:
            searchType = int(enter.searchTypeCommand())
            if searchType in range(1,6):
                pircollection.updateSearchType(searchType)
                break
            elif searchType == 6:
                self.main()
            else:
                print("invalid input, please enter int number 1~6")
        pircollection.matches_type()

        # Search Note, Contact
        if pircollection.searchType == 1 or pircollection.searchType == 3:
            board.searchFilterForNoteContact()
            search_filter = enter.get_search_filterNoteContact()
            #search with single text
            if search_filter == 1:
                text_condition = enter.get_logical_condition_text()
                while True:
                    include_or_not = enter.get_include_or_not()
                    if include_or_not == "!":
                        text_condition.insert(0,"-")
                        break
                    elif include_or_not == "":
                        text_condition.insert(0,"+")
                        break
                    else:
                        print("invalid input, please === enter ! === or === press enter ===") 
                found_list =  pircollection.not_ornot_filter_text(text_condition[0],text_condition[1])         
                print(found_list)
                print(pircollection.get_index(found_list))
                return found_list
            if search_filter == 2:
            #search with combined logic
                text_conditions = []
                operators = []
                # include_or_not
                while True:
                    text_condition = enter.get_logical_condition_text()
                    while True:
                        include_or_not = enter.get_include_or_not()
                        if include_or_not == "!":
                            text_condition.insert(0,"-")
                            break
                        elif include_or_not == "":
                            text_condition.insert(0,"+")
                            break
                        else: 
                            print("invalid input, please === enter ! === or === press enter ===")                   
                    text_conditions.append(text_condition)
                    while True:
                        operator = enter.get_operator()
                        if operator == "||" or operator == "&&":
                            operators.append(operator)
                            break
                        if operator == "":
                            break
                        else:
                            print("invalid input, please enter === || === or === && ===")
                    if operator == "":
                        break
                filtered_list = []
                for text_condition in text_conditions:
                    filtered_list.append(pircollection.not_ornot_filter_text(text_condition[0],text_condition[1]))     
                found_list = self.get_union_or_intersection(filtered_list,operators)       
                print(pircollection.get_index(found_list))
                return found_list
            else:
                print("invalid input,please enter int number 1~2")
        
        # Search Task, Event
        else:
            board.searchFilterForTaskEvent()
            search_filter = enter.get_search_filterTaskEvent()

            #search with single text
            if search_filter == 1:
                text_condition = enter.get_logical_condition_text()
                while True:
                    include_or_not = enter.get_include_or_not()
                    if include_or_not == "!":
                        text_condition.insert(0,"-")
                        break
                    elif include_or_not == "":
                        text_condition.insert(0,"+")
                        break
                    else:
                        print("invalid input, please === enter ! === or === press enter ===") 
                found_list =  pircollection.not_ornot_filter_text(text_condition[0],text_condition[1])         
                print(found_list)
                print(pircollection.get_index(found_list))
                return found_list
            #search with single time
            if search_filter == 2:
                time_condition = enter.get_logical_condition_time()
                while True:
                    include_or_not = enter.get_include_or_not()
                    if include_or_not == "!":
                        not_ornot = "-"
                        break
                    elif include_or_not == "":
                        not_ornot = "+"
                        break
                    else:
                        print("invalid input, please === enter ! === or === press enter ===")   
                found_list =  pircollection.not_ornot_filter_time(not_ornot,time_condition[0],time_condition[1]) 
                print(found_list)
                print(pircollection.get_index(found_list))  
                return found_list
            #search with combined logic
            if search_filter == 3:
                conditions = []
                operators = []
                while True:
                    condition = enter.get_logical_condition_withtime()
                    while True:
                        include_or_not = enter.get_include_or_not()
                        if include_or_not == "!":
                            condition.insert(0,"-")
                            break
                        elif include_or_not == "":
                            condition.insert(0,"+")
                            break
                        else: 
                            print("invalid input, please === enter ! === or === press enter ===")                   
                    conditions.append(condition)
                    while True:
                        operator = enter.get_operator()
                        if operator == "||" or operator == "&&":
                            operators.append(operator)
                            break
                        if operator == "":
                            break
                        else:
                            print("invalid input, please enter === || === or === && ===")
                    if operator == "":
                        break
                filtered_list = []
                for condition in conditions:
                    if len(condition) == 3:
                        filtered_list.append(pircollection.not_ornot_filter_text(condition[0],condition[2]))
                    else:
                        filtered_list.append(pircollection.not_ornot_filter_time(condition[0],condition[2],condition[3])) 

                found_list = self.get_union_or_intersection(filtered_list,operators)       
                print(pircollection.get_index(found_list))
                return found_list
            else:
                print("invalid input,please enter int number 1~2")
        
    def get_union_or_intersection(self,filtered_list,operators):      
        list2 = [None] * (len(filtered_list) - 1) 
        if operators[0] == "&&":
            set1 = set(filtered_list[0])
            set2 = set(filtered_list[1])
            list2[0] = set1.intersection(set2)
        if operators[0] == "||":
            set1 = set(filtered_list[0])
            set2 = set(filtered_list[1])
            list2[0] = set1.union(set2)

        for i in range(2,len(filtered_list)):   
                                    #len(filtered_list)>=3
                                    #[1,2,3,4] 保持不變
                                    #[ 2",3",4"]儲存
                                    # 1&&2 -> 2" 2"&&3 -> 3" 3"||4 -> 4"
            if operators[i-1] == "&&":
                set1 = set(filtered_list[i])
                set2 = set(list2[i-2])                        
                list2.append(set1.intersection(set2))
            elif operators[i-1] == "||":
                set1 = set(filtered_list[i])
                set2 = set(list2[i-2])                        
                list2.append(set1.union(set2))  
        
        found_list =  list(list2[-1])        
        print(found_list)
        return found_list

    def delete(self):
        board = Board()
        board.deleteBoard()
        pircollection = PIRCollection()
        found_list = self.search()
        index_list = pircollection.get_index(found_list)
        pircollection.delete(index_list)

    def modify(self):
        board = Board()
        board.modifyBoard()
        enter = Command()
        while True:
            modify_option = enter.get_modify_option()
            if modify_option == 1 or modify_option ==2:
                break
            else:
                print("invalid input,please enter int number 1~2")
        pircollection = PIRCollection()
        if modify_option == 1:
            search_text, replace_text = enter.get_modify_text()
            pircollection.replace_global(search_text,replace_text)
        else:
            board.modify_specific()
            found_list = self.search()
            index_list = pircollection.get_index(found_list)
            search_text, replace_text = enter.get_modify_text()
            pircollection.replace_specific(search_text,replace_text,index_list)
    
    def display(self):
        board = Board()
        board.displayBoard()
        board.display()

        

if __name__ == '__main__':
    pircontroller = PIRController()
    pircontroller.main()
        


                
                


            


            

           
        








                
                        
                    








    

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
    


