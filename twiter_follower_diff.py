'''
Gives you:
Twitter followers, followings, who you not follow and who does not follows you.
With lists and count numbers.
'''
import time
from getpass import getpass
from selenium import webdriver

given_username = input("username : ") #Ask username
given_password = getpass("pass : ") #Ask password (hidden)

browser = webdriver.Firefox(executable_path="C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python39\\geckodriver.exe") #Execute browser

browser.get("https://www.twitter.com")  #Go to twitter.com
time.sleep(4) #Wait browser loading
browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div').click() #click button path
time.sleep(3) #Wait browser loading

browser.find_element_by_name('session[username_or_email]').send_keys(given_username)#Type username to the path

browser.find_element_by_name('session[password]').send_keys(given_password) #Type password to the path

browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div').click() #Login click
time.sleep(5)

followings_list = [] #List of following
followers_list = [] #List of followers

browser.get(f"https://www.twitter.com/{given_username}/following") #Go to following page
time.sleep(5)

last_height_following = browser.execute_script("return document.documentElement.scrollHeight") #Scroll down
while True:
    followings = browser.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section//div[@dir="ltr"]')
    for following in followings:
        each_following = following.text
        if each_following not in followings_list:
            followings_list.append(each_following) #Append to the followings_list

    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight); ")#Keep scrolling down
    time.sleep(3)
    new_height_following = browser.execute_script("return document.documentElement.scrollHeight")

    if new_height_following == last_height_following:
        break
    last_height_following = new_height_following

browser.get(f"https://www.twitter.com/{given_username}/followers")#Go to followers page
time.sleep(5)

last_height_following = browser.execute_script("return document.documentElement.scrollHeight")
while True:
    followers = browser.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section//div[@dir="ltr"]')
    for follower in followers:
        each_follower = follower.text
        if each_follower not in followers_list:
            followers_list.append(each_follower)

    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight); ")
    time.sleep(3)
    new_height_following = browser.execute_script("return document.documentElement.scrollHeight")

    if new_height_following == last_height_following:
        break
    last_height_following = new_height_following

who_not_followed = []
who_not_follows_you = []

for following in followings_list:
    FOLLOWS_YOU = False

    for following_you in followers_list:
        if following == following_you:
            FOLLOWS_YOU = True

    if not FOLLOWS_YOU:

        who_not_follows_you.append(following)

for follow in followers_list:
    YOU_FOLLOW = False

    for follower in followings_list:
        if follow == follower:
            YOU_FOLLOW = True

    if not YOU_FOLLOW:

        who_not_followed.append(follow)

print("following list count : ")
print(len(followings_list))
print(followings_list)
print("\n")
print("followers list count : ")
print(len(followers_list))
print(followers_list)
print("\n")
print(who_not_follows_you)
print(len(who_not_follows_you))
print("\n")
print(who_not_followed)
print(len(who_not_followed))
