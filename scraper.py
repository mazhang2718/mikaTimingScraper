from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
import time
import datetime
import os

currentTime = time.time()
timestamp = datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d %H:%M:%S')


path_to_chromedriver = '/Users/mazhang/Downloads/chromedriver' # change path as needed
driver = webdriver.Chrome(executable_path = path_to_chromedriver)


driver.get("http://houston-intranet.r.mikatiming.de/2017/?pid=statistics")

username = driver.find_element_by_css_selector('#form_auth > div > input[type="text"]:nth-child(3)')
username.send_keys("intranet-stats")
password = driver.find_element_by_css_selector('#form_auth > div > input[type="password"]:nth-child(6)')
password.send_keys("houston")

button = driver.find_element_by_css_selector('#form_auth > div > button')
button.click()

driver.implicitly_wait(15)

fullTimes = {}
fullTimes["started"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.global_data_table_2.pull-left > div > table > tr:nth-child(3) > td:nth-child(2)').text
fullTimes["onCourse"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.global_data_table_2.pull-left > div > table > tr:nth-child(5) > td:nth-child(2)').text
fullTimes["finished"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.global_data_table_2.pull-left > div > table > tr:nth-child(5) > td:nth-child(2)').text
fullTimes["timestamp"] = timestamp

j = 3

for i in range(5,46,5):
	fullTimes['k' + str(i)] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.event_splits_4 > div > table > tr:nth-child(2) > td:nth-child(' + str(j) + ')').text
	j+=2


driver.implicitly_wait(25)

select = Select(driver.find_element_by_css_selector('#global-option-bar-nav > form > div > select'))
stuff = select.select_by_value("HALF")

time.sleep(25)

halfTimes = {}
halfTimes["k5"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.event_splits_4 > div > table > tr:nth-child(2) > td:nth-child(3)').text
halfTimes["k10"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.event_splits_4 > div > table > tr:nth-child(2) > td:nth-child(5)').text
halfTimes["k15"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.event_splits_4 > div > table > tr:nth-child(2) > td:nth-child(7)').text
halfTimes["k20"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.event_splits_4 > div > table > tr:nth-child(2) > td:nth-child(9)').text
halfTimes["k25"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.event_splits_4 > div > table > tr:nth-child(2) > td:nth-child(11)').text

halfTimes["started"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.global_data_table_2.pull-left > div > table > tr:nth-child(3) > td:nth-child(2)').text
halfTimes["onCourse"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.global_data_table_2.pull-left > div > table > tr:nth-child(4) > td:nth-child(2)').text
halfTimes["finished"] = driver.find_element_by_css_selector('#res2_statisticscontainer-content-0 > div.global_data_table_2.pull-left > div > table > tr:nth-child(5) > td:nth-child(2)').text

halfTimes["timestamp"] = timestamp

driver.quit()

append_write = 'a'



### Writes FullMarathon Times

if os.path.exists('/Users/mazhang/Desktop/mikaTimingFull.csv'):
	append_write = 'a'
else:
	append_write = 'w'

with open('mikaTimingFull.csv', append_write) as csvfile:
    fieldnames = ['timestamp','started', 'finished', 'onCourse','k5','k10','k15','k20','k25','k30','k35','k40','k45']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if append_write == 'w':
    	writer.writeheader()
    writer.writerow(fullTimes)


### Writes HalfMarathon Times

if os.path.exists('/Users/mazhang/Desktop/mikaTimingHalf.csv'):
	append_write = 'a'
else:
	append_write = 'w'

with open('mikaTimingHalf.csv', append_write) as csvfile:
    fieldnames = ['timestamp','started', 'finished', 'onCourse','k5','k10','k15','k20','k25']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if append_write == 'w':
    	writer.writeheader()
    writer.writerow(halfTimes)


### Writes total started/onCourse/finished numbers

with open('mikaTiming.csv', 'w') as csvfile:
    fieldnames = ['started', 'finished', 'onCourse']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    times = {}
    times['started'] = int(fullTimes['started']) + int(halfTimes['started'])
    times['onCourse'] = int(fullTimes['onCourse']) + int(halfTimes['onCourse'])
    times['finished'] = int(fullTimes['finished']) + int(halfTimes['finished'])

    writer.writeheader()
    writer.writerow(times)






