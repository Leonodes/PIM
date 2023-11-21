from View.InputView import Command

class Contact:
    def __init__(self, name, address, mobile_num):
        self.PIRType = 'Contact'
        self.name = name
        self.address = address
        self.mobile_num = mobile_num
    # def getName(self):
    #     return self.name
    # def setName(self, name):
    #     self.name = name
    # def getAddress(self):
    #     return self.address
    # def setAddress(self, address):
    #     self.address = address
    # def getMobileNum(self):
    #     return self.mobile_num
    # def setMobileNum(self, mobile_num):
    #     self.mobile_num = mobile_num
    # def display(self):
    #     print(self.name)
    #     print(self.address)
    #     print(self.mobile_num)
    # def detail_display(self):
    #     print("The name is {}".format(self.name))
    #     print("His/Her address is {}". format(self.address))
    #     print("His/Her mobile number is {}".format(self.mobile_num))
    # get contact content

    # create
    # def setPIMContact():
    #     enter = Command()
    #     # get_name = input("Enter a name for contact item:")
    #     get_name = enter.createContactNameCommand()
    #     # get_addr = input("Enter an address for contact item: ")
    #     get_addr = enter.createContactAddrCommand()
    #     # get_mobileNum = int(input("Enter a number for contact item"))
    #     get_mobileNum = enter.createContactMobileNumCommand()
    #     return get_name, get_addr, get_mobileNum
    
    def setContact(self, newName, newAddr, newMobileNum):
        self.name = newName
        self.address = newAddr
        self.mobile_num = newMobileNum
        return self.PIRType, self.name, self.address, self.mobile_num
        
    # read
    def getContact(self):
        return self.PIRType, self.name, self.address, self.mobile_num

    # tostring
    def ContactToString(self):
        string = self.PIRType + ":\nName: " + self.name + "\nAddress:" + self.address + "\nMobile Number: " + self.mobile_num
        return string
    
    # contact to PIR record form
    def ContactToPIR(self):
        return self.name + "," + self.address + "," + self.mobile_num
    
    
    # update
    def updateContact(self, newName, newAddress, newMobileNum):
        if newName != self.name:
            self.name = newName
        if newAddress != self.address:
            self.address = newAddress
        if newMobileNum != self.mobile_num:
            self.mobile_num = newMobileNum
        return self.PIRType, self.name, self.address, self.mobile_num


    # delete

