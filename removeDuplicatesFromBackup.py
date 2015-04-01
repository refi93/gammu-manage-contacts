import gammu
import sys



def getField(phoneBookItem, fieldName):
        ret = None
        for entry in phoneBookItem['Entries']:
                if entry['Type'] == fieldName:
                        ret = entry['Value']
        if ret == None:
                ret = ''
        return ret

def getPhoneNumber(phoneBookItem):
        ret = getField(phoneBookItem, 'Number_Mobile')
        if ret == '':
                return getField(phoneBookItem, 'Number_General')
        return ret

def getFirstName(phoneBookItem):
        return getField(phoneBookItem, 'Text_FirstName')

def getLastName(phoneBookItem):
        return getField(phoneBookItem, 'Text_LastName')

def getName(phoneBookItem):
        return getField(phoneBookItem, 'Text_Name')

# Create state machine object
sm = gammu.StateMachine()

# Read ~/.gammurc
sm.ReadConfig()

inputFileName = "newmybak.backup"

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
                if ((getFirstName(item) == '') and (getLastName(item) == '')):
                        print (getName(item) + " " + getPhoneNumber(item)).encode('utf-8', 'ignore')
                else:
                        print (getFirstName(item) + " " + getLastName(item) + "; " + getPhoneNumber(item)).encode('utf-8', 'ignore')
        if (phoneNumber == None):
                print item
        j = j + 1
print i
print j

backup['PhonePhonebook'] = newPhoneBook


gammu.SaveBackup("new"+inputFileName, backup)
