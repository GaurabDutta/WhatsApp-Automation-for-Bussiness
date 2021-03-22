import time
import datetime
import pywhatkit
import pandas as pd

df = pd.read_excel('C:/Users/Gaurab/Workspace/my_scripts/Client_data.xls', parse_dates=['Date'])

for i in range(len(df.values)):
    now = datetime.datetime.now()
    
    if now.day == df.Date[i].day:
        
        if len(str(df.Number[0])) != 12:
            print('Please enter a valid phone number for id', i)
            break
        else:
            number = '+' + str(df.Number[i])
        
        message = 'Hi ' + df.Name[i] + ', ' + 'Please pay your fee.' + '\n' + 'This is an auto-generated message. Please ignore.'
        hour = now.hour
        minute = now.minute+1
        
        if minute >= 60:
            if hour >= 23:
                hour = 0
            else:
                hour += 1
            minute = 1
        
        print('Sending message to', df.Name[i], number, message, hour, minute)
        pywhatkit.sendwhatmsg(number, message, hour, minute)
        print(i)
        
        #time.sleep(30)