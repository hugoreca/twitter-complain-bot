from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

BINARY_LOCATION = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
PATH = "C:\Development\chromedriver.exe"
options = Options()
options.binary_location = BINARY_LOCATION
PROMISED = 20


class TweetBot:

    def tweet_at_provider(self, real_down, username, password):
        driver = webdriver.Chrome(options=options, executable_path=PATH)
        driver.get("https://twitter.com")
        time.sleep(2)
        login = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login.click()
        time.sleep(1)
        user = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label')
        user.send_keys(username)
        pwd = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label')
        pwd.send_keys(password)
        login_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login_button.click()
        time.sleep(3)
        tweet_area = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        if real_down < PROMISED:
            tweet_area.send_keys(
                f"Hey @izzi_mx , @ayudaizzi Mi servicio debe de ser de 20MB de bajada y actualmente tengo {real_down} ¿Me podrían ayudar por favor?")
        else:
            tweet_area.send_keys(
                f"Hey @izzi_mx , @ayudaizzi Mi servicio debe de ser de 20MB de bajada y actualmente tengo {real_down}MB los quiero felicitar y agradecer por cumplir con su servicio")
        send_tweet = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span')
        send_tweet.click()
