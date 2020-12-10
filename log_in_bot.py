from selenium import webdriver
import time
from getpass import getpass

class SocialMediaBot():      
    browser_dict = {
        "1": "C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python39\\chromedriver.exe",
        "2": "C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python39\\geckodriver.exe"
    }
    

    def choose_browser(self):
        """MAIN - At first choose browser """
        continue_on = True
        while continue_on:
            print("Instagram / Twitter Bot ")
            print("Choose Browser\n1- Chrome\n2- Firefox ")
            select = input("Make selection 1/2 : ")
            if select in self.browser_dict:
                self.choose_social_media(select, self.browser_dict.get(select))
            
            else:
                print("Wrong Choice ! 1-2 ")
                continue

    def choose_social_media(self, browser_name, browser_path):
        """Second select social media """
        continue_on = True
        while continue_on:
            print("\nChoose Social Media\n1- Instagram\n2- Twitter")
            select = input("Make selection 1/2 : ")
            if select == "1":
                given_username = input("Enter Instagram Username : ")
                given_password = getpass("Enter Insragram Password :")
                self.instagram_login_bot(given_username, given_password, browser_name, browser_path)

            elif select == "2":
                given_username = input("Enter Twitter Username : ")
                given_password = getpass("Enter Twitter Password :")
                self.twitter_login_bot(given_username, given_password, browser_name, browser_path)

            else:
                print("Wrong Choice ! 1-2")
                continue

    def twitter_login_bot(self, given_username, given_password, browser_name, browser_path):

        print("Twitter Login Bot")
        """Open site from browser"""
        if browser_name == "1":
            browser = webdriver.Chrome(executable_path=browser_path)

        elif browser_name == "2":
            browser = webdriver.Firefox(executable_path=browser_path)

        
        browser.get("https://www.twitter.com")
        """First click the login button"""
        login = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div')
        login.click()
        time.sleep(5)
        """ Enter username"""
        username = browser.find_element_by_name('session[username_or_email]')
        username.send_keys(given_username)

        """Enter pasword"""
        password = browser.find_element_by_name('session[password]')
        password.send_keys(given_password)

        """Clicks to loging button"""
        login_click = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
        login_click.click()

    def instagram_login_bot(self, given_username, given_password, browser_name, browser_path):
        
        print("Instagram Login Bot")
        #Open site from browser
        if browser_name == "1":
            browser = webdriver.Chrome(executable_path=browser_path)

        elif browser_name == "2":
            browser = webdriver.Firefox(executable_path=browser_path)

        browser.get("https://www.instagram.com")
        time.sleep(8)
        """ Enter username"""
        username = browser.find_element_by_name("username")
        username.send_keys(given_username)

        """Enter pasword"""
        password = browser.find_element_by_name('password')
        password.send_keys(given_password)

        """Clicks to loging button"""
        login_click = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login_click.click()

        # def instagram_get_followers(self, browser_name):
        #     browser.get("https://www.instagram.com")
        #     get_followers = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        #     get_followers.click() 


work = SocialMediaBot()
work.choose_browser()