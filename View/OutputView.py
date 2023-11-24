from model.PIRCollection import PIRCollection
from View.InputView import Command
class Board:
    def __init__(self):
        pass
    # instruction hints
    def mainBoard(self):
        print("----------------------------------------------------")
        print("-     Hi! Here is Personal Information Manager     -")
        print("----------------------------------------------------")
        print("-       1.Create Personal Information Records      -")
        print("-       2.Search Personal Information Records      -")
        print("-       3.Modify Personal Information Records      -")
        print("-       4.Delete Personal Information Records      -")
        print("-       5.Display Personal Information Records     -")
        print("-       6.Exit the system                          -")
        print("----------------------------------------------------")
    
    def createBoard(self):
        print("----------------------------------------------------")
        print("-             Create data type to choose           -")
        print("----------------------------------------------------")
        print("-               1.Create Quick Notes               -")
        print("-               2.Create tasks                     -")
        print("-               3.Create contacts                  -")
        print("-               4.Create events                    -")
        print("-               5.Back to the Home Page            -")
        print("----------------------------------------------------")

    def searchFilterForTaskEvent(self):
        print("----------------------------------------------------")
        print("-             Search filter to choose              -")
        print("----------------------------------------------------")
        print("-              1.Search with single text           -")
        print("-              2.Search with single time           -")
        print("-              3.Search with combined logic        -")
        print("----------------------------------------------------")

    def searchFilterForNoteContact(self):
        print("----------------------------------------------------")
        print("-             Search filter to choose              -")
        print("----------------------------------------------------")
        print("-              1.Search with single text           -")
        print("-              2.Search with combined logic        -")
        print("----------------------------------------------------")
    
    def searchTypeBoard(self):
        print("----------------------------------------------------")
        print("-                Data type to search               -")
        print("----------------------------------------------------")
        print("-                 1.Search Note                    -")
        print("-                 2.Search Task                    -")
        print("-                 3.Search Contact                 -")
        print("-                 4.Search Event                   -")
        print("-                 5.Search All                     -")
        print("-                 6.Back to the Home Page          -")
        print("----------------------------------------------------")

    def getValidInput(self):
        print("invalid input, please input again")

    def modifyBoard(self):
        print("----------------------------------------------------")
        print("-                  Modify Option                   -")
        print("----------------------------------------------------")
        print("-                 1.Global Modify                  -")
        print("-                 2.Specific Modify                -")
        print("----------------------------------------------------")
        

    def deleteBoard(self):
        #first search for PIR, then delete(use delete function)
        print("please search for PIRs you want to delete")
        
    def modify_specific(self):
        #first search for PIR, then delete(use delete function)
        print("please search for PIRs you want to modify")


    def displayBoard(self):
        # displayall
        # display single PIR
        print("----------------------------------------------------")
        print("-                  Display Option                  -")
        print("----------------------------------------------------")
        print("-                 1.Display Note                   -")
        print("-                 2.Display Task                   -")
        print("-                 3.Display Contact                -")
        print("-                 4.Display Event                  -")
        print("-                 5.Display All                    -")
        print("-                 6.Back to the Home Page          -")
        print("----------------------------------------------------")

    def display(self):
        pircollection = PIRCollection()
        enter = Command()
        while True:
            display_option = enter.get_dispaly_option()
            if display_option in range(1,7):
                break
            else:
                print("invalid input,please enter int number 1~6") 
        pircollection.updateSearchType(display_option)
        content_to_display = pircollection.matches_type()
        if display_option in range(1,6):
            for lines in content_to_display:
                print(lines)
            
    