class Board:
    def __init__(self):
        pass
    # instruction hints
    def mainBoard():
        print("Hi! Here is Personal Information Manager. Please choose what you want to do.")
        print("1. Create Personal Information Records.")
        print("2. Search Personal Information Records.")
        print("3. Modify Personal Information Records.")
        print("4. Delete Personal Information Records.")
        print("5. Display Personal Information Records.")
        print("6. Exit the system")
    
    def createBoard():
        print("1. Create Quick Notes")
        print("2. Create tasks.")
        print("3. Create contacts.")
        print("4. Create events.")
        print("5. Back to the Home Page")

    def searchBoardFilter(self):
        print("----------------------------------------------------")
        print("-             Search filter to choose              -")
        print("----------------------------------------------------")
        print("-              1.Search with single text           -")
        print("-              2.Search with single time           -")
        print("-              3.Search with combined logic        -")
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

    def modifyBoard():
        #first search for PIR, then modify(use replace function)
        pass

    def deleteBoard():
        #first search for PIR, then delete(use delete function)
        pass

    def displayBoard():
        # displayall
        # display single PIR
        pass