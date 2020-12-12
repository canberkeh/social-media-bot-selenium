from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Enables to using keyboard
import time
from getpass import getpass
username1 = input("username : ")
password1 = getpass("pass : ")
hashtag = input("Enter hashtag or something to search")
browser = webdriver.Firefox(executable_path="C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python39\\geckodriver.exe")
browser.get("https://www.twitter.com")
time.sleep(8)
login = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div')
login.click()

time.sleep(5)

username = browser.find_element_by_name('session[username_or_email]')
username.send_keys(username1)
 
password = browser.find_element_by_name('session[password]')
password.send_keys(password1)

login_click = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
login_click.click()

search_input = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
search_input.send_keys(hashtag)
time.sleep(3)
search_input.send_keys(Keys.ENTER)
time.sleep(3)

tweet_list = browser.find_elements_by_xpath('//div[@data-testid="tweet"]/div[2]/div[2]')

for item in tweet_list:
    print(item.text)