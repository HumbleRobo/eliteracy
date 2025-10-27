from selenium import webdriver

class Main:
    url = 'https://isafeevent.moe.edu.tw'

    def __init__(self):
        pass

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

if __name__ == '__main__':
    main = Main()
    main.open()