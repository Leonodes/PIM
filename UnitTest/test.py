import unittest

class PIMTest(unittest.TestCase):
    def setup(self):
        self.filename = 'record.pim'
        content = """------Text------
                 Notes
                 hi

                 ------Task------
                 Description,Deadline
                 Assignment 2,2023/11/01 23:59
                 ------Contact------
                 Name,Address,Mobile_num
                 Max,PQ666,66666666

                 ------Event------
                 Description,Start_time,Alarm
                 Group Meeting,2023/11/11 13:00, 2023/11/11 12:50

                 ------End------"""
        with open (self.filename, 'w') as file:
            file.write(content)

    #create testing
    def test_createTask(self):
        pass
        expected_result = 'hi'
        self.assertEqual(expected_result)
        #a= ''
        #b= ''
        #self.assertEqual(a, b)    
    def test_createNote(self):
        pass
        # expected_test = 'Note'
        # filename = 'record.pim'
        # with open(filename, 'w') as file:
        #     file.write(expected_test)
        # with open(filename, 'r') as file:
        #     expected_result = file.read()
        # self.assertEqual(expected_result, expected_test)
    def test_createEvent(self):
        pass
        # expected_test = 'Event'
        # filename = 'record.pim'
        # with open(filename, 'w') as file:
        #     file.write(expected_test)
        # with open(filename, 'r') as file:
        #     expected_result = file.read()
        # self.assertEqual(expected_result, expected_test)
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
        expected_result = """
        Task:
        Description: Assignment 2
        Deadline: 2023/11/01 23:59
        """
    def test_displayNote(self):
        pass
        expected_result = """
        Note:
        Content: hi"""
    def test_displayEvent(self):
        pass
        expected_result = """
        Event:
        Description: Group Meeting
        Start time: 2023/11/11 13:00
        Alarm: 2023/11/11 12:50
        """
    def test_displayContact(self):
        pass
        expected_result = """
        Contact: 
        Name: Max
        Address: PQ666
        Mobile Number: 66666666"""
    def test_displayAll(self):
        expected_result = """"""
        with open(self.filename, 'r') as file:
            expected_output = print(file.read())
        self.assertEqual(expected_result, expected_output)

if __name__ == '__main__':
    unittest.main()