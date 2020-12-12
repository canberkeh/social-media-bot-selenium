from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Enables to using keyboard
import time
from getpass import getpass
username1 = input("username : ")
password1 = getpass("pass : ")
# hashtag = input("Enter hashtag or something to search")
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
followings_list = []
followers_list = []
who_not_follows = [] 
who_you_not_follow = []


browser.get(f"https://www.twitter.com/{username1}/following")
time.sleep(5)
# following = browser.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[2]/div[1]/span')
# time.sleep(4)
# print(following.text)
last_height_following = browser.execute_script("return document.documentElement.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight); ")
    time.sleep(3)
    new_height_following = browser.execute_script("return document.documentElement.scrollHeight")
    if new_height_following == last_height_following:
        break
    last_height_following = new_height_following

following = browser.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[2]/div[1]/span')
# for item in following:
#     followings_list.append(item.text)

print(following)



# browser.get(f"https://www.twitter.com/{username1}/followers")
# followers = browser.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div/div[1]/a/div/div[2]/div[1]/span')
# print(followers.text)
