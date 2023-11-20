from View.InputView import Command

class Note:
    def __init__(self,content):
        self.content = content
    # def getContent(self):
    #     return self.content
    # def setContent(self, content):
    #     self.content = content
    # def display(self):
    #     print(self.content)
    # def detail_display(self):
    #     print("The content for this note is {}".format(self.content))

# get note content
    def setPIMNote():
        # get_note_content = input("Enter your note:")
        # return get_note_content
        enter = Command()
        return enter.createNoteCommand()