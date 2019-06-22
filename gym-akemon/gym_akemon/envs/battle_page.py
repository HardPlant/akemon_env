from selenium import webdriver

class BattlePage:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def get(self):
        self.driver.get("https://www.naver.com")
    