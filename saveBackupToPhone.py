import gammu
import sys

# Create state machine object
sm = gammu.StateMachine()

# Read ~/.gammurc
sm.ReadConfig()

# Connect to phone
sm.Init()

# Reads network information from phone
netinfo = sm.GetNetworkInfo()

print netinfo

inputFileName = "newmybak.backup"

backup = gammu.ReadBackup(inputFileName)

phoneBook = backup['PhonePhonebook']

#sm.DeleteAllMemory('SM')

start = 481

i = 0
for item in phoneBook:
        i = i + 1;
        if i < start:
                continue              
        #print item        
        sm.SetMemory(item)
        print i
        if i > start + 240:
                break
print i
