import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings('ignore')

options = Options()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome('C:/Users/Gaurab/Workspace/my_scripts/chromedriver.exe', options=options)
# driver = webdriver.Chrome()
# driver.maximize_window()
driver.get('https://web.whatsapp.com')

df = pd.read_excel('C:/Users/Gaurab/Workspace/my_scripts/Client_data.xls', parse_dates=['Date'])
# print(df)

# time.sleep(5)
input('Please open whatsApps by scanning the QR code and hit enter to continue.')

for i in range(len(df.values)):
    now = datetime.datetime.now()
    
    if now.day == df.Date[i].day:
        print('Date: ', df.Date[i])
        
        message = 'Hi ' + df.Name[i] + ', ' + 'Please pay your fee.' + '\n' + 'This is an auto-generated message. Please ignore.'
        # message = 'Hacked'
        print('Message: ', message)

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(df.Name[i]))
        user.click()

        # msg_box = driver.find_element_by_class_name('_2A8P4')
        msg_box = driver.find_element_by_xpath("/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

        for j in range(1):
            msg_box.send_keys(message)
            msg_box.send_keys(Keys.RETURN)
            
            # button = driver.find_element_by_class_name('_1E0Oz')
            # button = driver.find_element_by_xpath("/html/body/div/div/div/div[4]/div/footer/div[1]/div[3]/button")
            # button.click()

        print('Message sent to ', df.Name[i])

        time.sleep(5)