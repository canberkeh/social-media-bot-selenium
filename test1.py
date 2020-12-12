from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Enables to using keyboard
import time
from getpass import getpass
username1 = input("username : ")
password1 = getpass("pass : ")

browser = webdriver.Firefox(executable_path="C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python39\\geckodriver.exe") #Execute browser


browser.get("https://www.twitter.com")  #Go to twitter.com
time.sleep(4)
login = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div') #click button path
login.click() #Click to path
time.sleep(3)

username = browser.find_element_by_name('session[username_or_email]')#username path
username.send_keys(username1)#send username given before
 
password = browser.find_element_by_name('session[password]')#pass path
password.send_keys(password1)#send pass given before

login_click = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div') #login click button path
login_click.click()#login click
time.sleep(5)

browser.get(f"https://www.twitter.com/{username1}/following")
time.sleep(5)
fol_list = []
following = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[2]/div[1]')
for a in following:
    follower = a.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[2]/div[1]').text
    print(follower)
