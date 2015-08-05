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

inputFileName = "kontakty-sonia.backup"

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
                if (phoneNumber != None):
                        contactName = "";
                        phoneNumber = getPhoneNumber(item).encode('utf-8', 'ignore');
                        if ((getFirstName(item) == '') and (getLastName(item) == '')):
                                contactName = getName(item).encode('utf-8', 'ignore')
                        else:
                                contactName = (getFirstName(item) + " " + getLastName(item)).encode('utf-8', 'ignore')
                        print "BEGIN:VCARD"
                        print "VERSION:3.0"
                        print "N:;" + contactName + ";;;"
                        print "FN:" + contactName
                        print "TEL;TYPE=CELL;TYPE=PREF:" + phoneNumber
                        print "END:VCARD"
        j = j + 1
print i
print j


