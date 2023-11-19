import unittest

class PIMTest(unittest.TestCase):
    #create testing
    def test_createTask(self):
        #set the content of the task
        expected_test = 'Task'
        filename = 'record.pim'
        with open(filename, 'w') as file:
            file.write(expected_test)
        #open the file and get the content
        with open(filename, 'r') as file:
            expected_result = file.read()
        self.assertEqual(expected_result, expected_test)
        #a= ''
        #b= ''
        #self.assertEqual(a, b)    
    def test_createNote(self):
        expected_test = 'Note'
        filename = 'record.pim'
        with open(filename, 'w') as file:
            file.write(expected_test)
        with open(filename, 'r') as file:
            expected_result = file.read()
        self.assertEqual(expected_result, expected_test)
    def test_createEvent(self):
        expected_test = 'Event'
        filename = 'record.pim'
        with open(filename, 'w') as file:
            file.write(expected_test)
        with open(filename, 'r') as file:
            expected_result = file.read()
        self.assertEqual(expected_result, expected_test)
    def test_createContact(self):
        pass
    #search testing
    def test_searchTask(self):
        pass
    def test_seachNote(self):
        pass
    def test_searchEvent(self):
        pass
    def test_searchContact(self):
        pass
    #modify testing
    def test_modifyTask(self):
        pass
    def test_modifyNote(self):
        pass
    def test_modifyEvent(self):
        pass
    def test_modifyContact(self):
        pass
    #delect testing
    def test_delectTask(self):
        pass
    def test_delectNote(self):
        pass
    def test_delectEvent(self):
        pass
    def test_delectContact(self):
        pass
    #display testing
    def test_displayTask(self):
        pass
    def test_displayNote(self):
        pass
    def test_displayEvent(self):
        pass
    def test_displayContact(self):
        pass

if __name__ == '__main__':
    unittest.main()