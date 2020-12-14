'''
Welcome! You can perform some operations with social medias made below.
'''
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlsxwriter

class SocialMediaBot():
    '''
    1- Choose browser.2- Choose social media.3- Choose operation. Saves tweets on a notepad. Saves followers data on an excel table.
    '''
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
            print("99- Exit ")
            select = input("Make selection (1-2-99) : ")
            if select in self.browser_dict:
                self.choose_social_media(select, self.browser_dict.get(select))
            elif select == "99":
                raise SystemExit
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
                self.choose_operation_instagram(browser_name, browser_path)
            elif select == "2":
                self.choose_operation_twitter(browser_name, browser_path)
            else:
                print("Wrong Choice ! 1-2")
                continue

    def choose_operation_twitter(self, browser_name, browser_path):
        '''
        Have to choose operation on twitter.
        '''
        continue_on = True
        while continue_on:
            print("\n1- Get followers list and compare\n2- Get tweets on wanted search")
            select = input("Make selection 1/2 : ")
            if select == "1":
                self.twitter_follower_diff(browser_name, browser_path)
            elif select == "2":
                self.get_tweets(browser_name, browser_path)
            else:
                print("Wrong Choice ! 1-2")
                continue
    
    def choose_operation_instagram(self, browser_name, browser_path):
        continue_on = True
        while continue_on:
            print("\n1- Get followers list and compare\n2- Auto like photos\n3- Auto follow wanted account")
            select = input("Make selection 1/2/3 : ")
            if select == "1":
                self.instagram_follower_dif(browser_name, browser_path)
            elif select == "2":
                pass
            elif select == "3":
                pass
            else:
                print("Wrong Choice ! 1-2")
                continue

    def instagram_follower_dif(self, browser_name, browser_path):
        '''
        Logs in instagram. Get follower/following list on an excel table with count numbers.
        '''
        given_username = input("Enter Instagram Username : ")
        given_password = getpass("Enter Insragram Password :")
        #KEEP MOVING FROM HERE !!!
        
        print("Instagram Login Bot")
        if browser_name == "1":#Open site from browser
            browser = webdriver.Chrome(executable_path=browser_path)

        elif browser_name == "2":
            browser = webdriver.Firefox(executable_path=browser_path)

        browser.get("https://www.instagram.com")
        time.sleep(8)
        username = browser.find_element_by_name("username")
        username.send_keys(given_username)
        password = browser.find_element_by_name('password')
        password.send_keys(given_password)

        login_click = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login_click.click()

    def twitter_follower_diff(self, browser_name, browser_path):
        '''
        Gets followers data on an excel table.
        '''
        given_username = input("Enter Twitter Username : ")
        given_password = getpass("Enter Twitter Password :")

        if browser_name == "1":
            browser = webdriver.Chrome(executable_path=browser_path)

        elif browser_name == "2":
            browser = webdriver.Firefox(executable_path=browser_path)

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
            follows_you = False

            for following_you in followers_list:
                if following == following_you:
                    follows_you = True

            if not follows_you:

                who_not_follows_you.append(following)

        for follow in followers_list:
            you_follow = False

            for follower in followings_list:
                if follow == follower:
                    you_follow = True

            if not you_follow:

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

        workbook = xlsxwriter.Workbook(f'{given_username}_data.xlsx')
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})
        worksheet.write('A1', 'Followers', bold)
        worksheet.write('B1', 'Following', bold)
        worksheet.write('C1', 'Who Not Follows You', bold)
        worksheet.write('D1', 'Who You Not Follow', bold)
        worksheet.write('E1', 'Followers Count', bold)
        worksheet.write('F1', 'Following Count', bold)
        worksheet.write('G1', 'Count : Who Not Follows You', bold)
        worksheet.write('H1', 'Count : Who You Not Follow', bold)
        worksheet.write('E2', '=COUNTA(A:A) -1', bold)
        worksheet.write('F2', '=COUNTA(B:B) -1', bold)
        worksheet.write('G2', '=COUNTA(C:C) -1', bold)
        worksheet.write('H2', '=COUNTA(D:D) -1', bold)

        row = 1 # Start from
        col = 0
        for item in followers_list: # Iterate over the data and write it out row by row.
            worksheet.write(row, col, item)
            row += 1

        row = 1
        col = 1

        for item in followings_list:
            worksheet.write(row, col, item)
            row += 1

        row = 1
        col = 2

        for item in who_not_follows_you:
            worksheet.write(row, col, item)
            row += 1

        row = 1
        col = 3

        for item in who_not_followed:
            worksheet.write(row, col, item)
            row += 1
        workbook.close()
        self.choose_browser()

    def get_tweets(self, browser_name, browser_path):
        '''
        Gets given tweets by given page number.
        '''
        given_username = input("Enter Twitter Username : ")
        given_password = getpass("Enter Twitter Password :")
        hashtag = input("Type Hashtag or Search Tweets : ")
        pages = int(input("How many pages you want to load (1 - ~): "))
        filename = input("Type a file name to save : ")
        if browser_name == "1":
            browser = webdriver.Chrome(executable_path=browser_path)

        elif browser_name == "2":
            browser = webdriver.Firefox(executable_path=browser_path)

        browser.get("https://www.twitter.com")  #Go to twitter.com
        time.sleep(4) #Wait browser loading
        browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div').click() #click button path
        time.sleep(3) #Wait browser loading

        browser.find_element_by_name('session[username_or_email]').send_keys(given_username)#Type username to the path

        browser.find_element_by_name('session[password]').send_keys(given_password) #Type password to the path

        browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div').click() #Login click
        time.sleep(5)

        search_input = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        search_input.send_keys(hashtag)
        time.sleep(3)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

        results = []

        browser.implicitly_wait(5)

        for tweet in browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]"):
            results.append(tweet.text)

        time.sleep(3)

        loop_counter = 0
        last_height = browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loop_counter > pages:
                break
            browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(3)

            for tweet in browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]"):
                results.append(tweet.text)

            browser.implicitly_wait(5)

            new_height = browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loop_counter+=1

        count = 1
        with open(f"{filename}.txt","w",encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}-{item}\n")
                count+=1
        self.choose_browser()

work = SocialMediaBot()
work.choose_browser()
#onwork
