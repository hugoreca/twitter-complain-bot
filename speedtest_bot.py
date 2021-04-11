from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

BINARY_LOCATION = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
PATH = "C:\Development\chromedriver.exe"
options = Options()
options.binary_location = BINARY_LOCATION


class SpeedTest:

    def get_internet_speed(self):
        driver = webdriver.Chrome(options=options, executable_path=PATH)
        driver.get("https://www.speedtest.net/")
        go_button = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(55)
        down = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(down.text)
        return float(down.text)
