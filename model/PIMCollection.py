# create a class for each item type, and that each class extends an abstract base class provided for you
from collections.abc import Collection
class PIMCollection(Collection):
    def __init__(self, PIMlist):
        # self.PIMlist = PIMEntity()
        self.PIMlist = PIMlist
        for value in self.PIMlist:
            PIMlist.append(value)