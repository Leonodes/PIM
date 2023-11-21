import unittest
from model.PIRNote import Note
from model.PIRTask import Task

#test for note
class PIMTest(unittest.TestCase):
    def test_setNote(self):
        note = Note("hi")
        content = "hi"
        expected_result = 'Note', content
        result = note.setNote(content)
        self.assertEqual(expected_result, result)

    def test_getNote(self):
        note = Note("hi")
        content = "hi"
        expected_result = 'Note', content
        result = note.getPIMNote()
        self.assertEqual(expected_result, result)

    def test_NoteToString(self):
        note = Note("hi")
        Type = "Note"
        content = "hi"
        expected_result = Type + ":\nContent: " + content
        result = note.NoteToString()
        self.assertEqual(expected_result, result)

    def test_NoteToPIR(self):
        note = Note("hi")
        content = "hi"
        expected_result = content
        result = note.NoteToPIR()
        self.assertEqual(expected_result, result)

    # def test_NoteToString(self):
    #     note = Note("hi")
    #     Type = "Note"
    #     content = "hi"
    #     expected_result = Type + ":\nContent: " + content
    #     result = note.NoteToString()
    #     self.assertEqual(expected_result, result)

    # def test_NoteToPIR(self):
    #     note = Note("hi")
    #     content = "hi"
    #     expected_result = content
    #     result = note.NoteToPIR()
    #     self.assertEqual(expected_result, result)

    def test_updateNote(self):
        note = Note("hi")
        note.content = "hi"
        result = note.updateNote("Bye")
        self.assertEqual(note.content, "Bye")

    #test for task
    def test_setTask(self):
        task = Task("Assignment 2","2023/11/01 23:59")
        Description = "Assignment 2"
        DDL = "2023/11/01 23:59"
        expected_result = 'Task', Description, DDL
        result = task.setTask(Description, DDL)
        self.assertEqual(expected_result, result)


    def test_getPIMTask(self):
        task = Task("Assignment 2","2023/11/01 23:59")
        Description = "Assignment 2"
        DDL = "2023/11/01 23:59"
        expected_result = 'Task', Description, DDL
        result = task.getPIMTask()
        self.assertEqual(expected_result, result)

    def test_TaskToString(self):
        task = Task("Assignment 2","2023/11/01 23:59")
        Type = "Task"
        Description = "Assignment 2"
        DDL = "2023/11/01 23:59"
        expected_result = Type + ":\nDescription: " + Description + "\nDeadline: " + DDL
        result = task.TaskToString()
        self.assertEqual(expected_result, result)

    def test_TaskToPIR(self):
        task = Task("Assignment 2","2023/11/01 23:59")
        Description = "Assignment 2"
        DDL = "2023/11/01 23:59"
        expected_result = Description + "," + DDL
        result = task.TaskToPIR()
        self.assertEqual(expected_result, result)

    def test_updateTask(self):
        task = Task("Assignment 2","2023/11/01 23:59")
        task.Description = "Assignment 2"
        task.DDL = "2023/11/01 23:59"
        result = task.updateTask("Assignment 3", "2023/11/29 23:59")
        self.assertEqual(task.description, "Assignment 3")
        self.assertEqual(task.deadline, "2023/11/29 23:59")











if __name__ == '__main__':
    unittest.main()
