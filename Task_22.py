from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class instagram:
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Extract the total number of followers
    def tot_no_followers(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(4)
    # Locate the No of followers
            followers = self.driver.find_element(by=By.XPATH, value="//button[@class='_acan _acao _acat _aj1-']//span[@class='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs' and text()='106K']").text
            print("Number of followers :", followers)
            sleep(4)
    # Locate the number following
            following = self.driver.find_element(by=By.XPATH, value="//button[@class='_acan _acao _acat _aj1-']//span[@class='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs' and text()='4']").text
            print("Following :", following)

        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            self.driver.quit()



url = "https://www.instagram.com/guviofficial/"

follow = instagram(url)
follow.tot_no_followers()


