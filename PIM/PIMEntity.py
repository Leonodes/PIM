from abc import ABC, abstractmethod
class PIMEntity(ABC):
    def findIndex(self,Type):
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
            
    @abstractmethod
    # extract and set state from user input
    def fromString(self):
        pass

    @abstractmethod
    # format and print
    def toString(self):
        pass
    