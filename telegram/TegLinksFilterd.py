"""selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: None
Message: Dismissed user prompt dialog: https://careers.alrajhitakaful.com is requesting your username and password 

selenium.common.exceptions.TimeoutException: Message: Timeout loading page after 300000ms


selenium.common.exceptions.WebDriverException: Message: Reached error page:

"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re 
import os


partition = input("Enter Partition Letter :")
driver = webdriver.Chrome()
linksFile= open(partition+'://Teg.Whts//telegram//Links.txt')
links=linksFile.readlines()

for link in links:
    linkOpen = driver.get(link)
    time.sleep(10)
   #groupMembers = driver.find_element_by_class_name("tgme_page_extra").text
   

    try:
        groupJoin = driver.find_element_by_class_name("tgme_action_button_new").text
        
        if groupJoin == "JOIN GROUP":
            try:
                groupName = driver.find_element_by_class_name("tgme_page_title").text   
                if groupName:
                    print(link+"True")
                    url_link = driver.current_url
                    tegFilterdLinks=open(partition+'://Teg.Whts//telegram//tegFilterd.txt', 'a') # text file to save filterd links
                    tegFilterdLinks.write(url_link+"\n") 
                    #filterdLinks.append(link)
                    #print(filterdLinks)
                else:
                    print(link+"This is a false group")
            except NoSuchElementException as exception:
                print (link+"Element not found and test failed")
        else:
            print(link+"This is not Group/ Channel telegram, May be account")

            
    except NoSuchElementException as exception:
        print (link+"button Group join not found and test failed")

linksFile.close()  
tegFilterdLinks.close()   
