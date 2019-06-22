import selenium

class BattlePage:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome()
    
    def get(self):
        self.driver.get("https://www.naver.com")
    