import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_path)
path = os.path.join(parent_path,"model")
sys.path.append(path)
from model.PIRCollection import PIRCollection
from model.PIRContact import Contact
from model.PIREvent import Event
from model.PIRNote import Note

class PIMTest(unittest.TestCase):
    def setUp(self) :
        self.TypeC = "Contact"
        self.Name = "Max"
        self.Addr = "PQ666"
        self.MobileNum = "66666666"
        self.TypeE = "Event"
        self.Description = "Group Meeting"
        self.Start_time = "2023/11/11 13:00"
        self.Alarm = "2023/11/11 12:50"
    #test for contact
    def test_setContact(self):
        contact = Contact("Max","PQ666","66666666")
        # Name = "Max"
        # Addr = "PQ666"
        # MobileNum = "66666666"
        expected_result = 'Contact', self.Name, self.Addr, self.MobileNum
        result = contact.setContact(self.Name, self.Addr, self.MobileNum)
        self.assertEqual(expected_result, result)

    def test_getContact(self):
        contact = Contact("Max","PQ666","66666666")
        # Name = "Max"
        # Addr = "PQ666"
        # MobileNum = "66666666"
        expected_result = 'Contact', self.Name, self.Addr, self.MobileNum
        result = contact.getContact()
        self.assertEqual(expected_result, result)

    def test_ContactToString(self):
        contact = Contact("Max","PQ666","66666666")
        # Type = "Contact"
        # Name = "Max"
        # Addr = "PQ666"
        # MobileNum = "66666666"
        expected_result = self.TypeC + ":\nName: " + self.Name + "\nAddress:" + self.Addr + "\nMobile Number: " + self.MobileNum
        result = contact.ContactToString()
        self.assertEqual(expected_result, result)

    def test_ContactToPIR(self):
        contact = Contact("Max","PQ666","66666666")
        # Name = "Max"
        # Addr = "PQ666"
        # MobileNum = "66666666"
        expected_result = self.Name + "," + self.Addr + "," + self.MobileNum
        result = contact.ContactToPIR()
        self.assertEqual(expected_result, result)
    

    #test for event
    def test_setEvent(self):
        event = Event("Group Meeting","2023/11/11 13:00", "2023/11/11 12:50")
        # Description = "Group Meeting"
        # Start_time = "2023/11/11 13:00"
        # Alarm = "2023/11/11 12:50"
        expected_result = 'Event', self.Description, self.Start_time, self.Alarm
        result = event.setEvent(self.Description, self.Start_time, self.Alarm)
        self.assertEqual(expected_result, result)

    def test_getPIMEvent(self):
        event = Event("Group Meeting","2023/11/11 13:00", "2023/11/11 12:50")
        # Description = "Group Meeting"
        # Start_time = "2023/11/11 13:00"
        # Alarm = "2023/11/11 12:50"
        expected_result = 'Event', self.Description, self.Start_time, self.Alarm
        result = event.setEvent(self.Description, self.Start_time, self.Alarm)
        self.assertEqual(expected_result, result)

    def test_EventToString(self):
        event = Event("Group Meeting","2023/11/11 13:00", "2023/11/11 12:50")
        # Type = "Event"
        # Description = "Group Meeting"
        # Start_time = "2023/11/11 13:00"
        # Alarm = "2023/11/11 12:50"
        expected_result = self.TypeE + ":\nDescription: " + self.Description + "\nStart Time:" + self.Start_time + "\nAlarm Time: " + self.Alarm
        result = event.EventToString()
        self.assertEqual(expected_result, result)

    def test_EventToPIR(self):
        event = Event("Group Meeting","2023/11/11 13:00", "2023/11/11 12:50")
        # Description = "Group Meeting"
        # Start_time = "2023/11/11 13:00"
        # Alarm = "2023/11/11 12:50"
        expected_result = self.Description + "," + self.Start_time + "," + self.Alarm
        result = event.EventToPIR()
        self.assertEqual(expected_result, result)



if __name__ == '__main__':
    unittest.main()
    









