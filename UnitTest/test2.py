import unittest
from model.PIRNote import Note

# #test for note
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