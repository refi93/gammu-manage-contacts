import gammu
import sys



def getField(phoneBookItem, fieldName):
        for entry in phoneBookItem['Entries']:
                if entry['Type'] == fieldName:
                        return entry['Value'] 

def getPhoneNumber(phoneBookItem):
        ret = getField(phoneBookItem, 'Number_Mobile')
        if ret == None:
                return getField(phoneBookItem, 'Number_General')
        return ret

def getFirstName(phoneBookItem):
        return getField(phoneBookItem, 'Text_FirstName')

def getLastName(phoneBookItem):
        return getField(phoneBookItem, 'Text_LastName') 

# Create state machine object
sm = gammu.StateMachine()

# Read ~/.gammurc
sm.ReadConfig()

inputFileName = "mybak.backup"

backup = gammu.ReadBackup(inputFileName)

phoneBook = backup['PhonePhonebook']

newPhoneBook = []
seenNumbers = set()


i = 1
j = 1
for item in phoneBook:
        phoneNumber = getPhoneNumber(item)
        if (phoneNumber not in seenNumbers):                              
                seenNumbers.add(phoneNumber)
                item['Location'] = i
                i = i + 1
        if (phoneNumber == None):
                print item
        j = j + 1#
print i
print j

backup['PhonePhonebook'] = newPhoneBook


gammu.SaveBackup("new"+inputFileName, backup)
