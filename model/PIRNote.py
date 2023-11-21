from View.InputView import Command

class Note:
    def __init__(self,content):
        self.PIRType = 'Note'
        self.content = content
    # def getContent(self):
    #     return self.content
    # def setContent(self, content):
    #     self.content = content
    # def display(self):
    #     print(self.content)
    # def detail_display(self):
    #     print("The content for this note is {}".format(self.content))

    # create
    # def setPIMNote():
    #     # get_note_content = input("Enter your note:")
    #     # return get_note_content
    #     enter = Command()
    #     return enter.createNoteCommand()
    
    def setNote(self, newContent):
        self.content = newContent
        return self.PIRType, self.content
    
    # read
    def getPIMNote(self):
        return self.PIRType, self.content
    
    # tostring
    def NoteToString(self):
        string = self.PIRType + ":\nContent: " + self.content
        return string
    
    # note to PIR record form
    def NoteToPIR(self):
        return self.content

    # update
    def updateNote(self, newContent):
        if newContent != self.content:
            self.content = newContent
        return self.PIRType, self.content
    
    # delete
