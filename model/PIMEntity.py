from abc import ABC, abstractmethod
class PIMEntity(ABC):
    @abstractmethod
    # extract and set state from user input
    def fromString(self):
        pass

    @abstractmethod
    # format and print
    def toString(self):
        pass
    