from selenium import webdriver

class Config:
    @staticmethod
    def config():
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver