import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.remote.webelement import WebElement


class Main:
    START_URL = 'https://isafeevent.moe.edu.tw/'
    LOGIN_URL = 'https://isafeevent.moe.edu.tw/login/'
    EXAM_URL = 'https://isafeevent.moe.edu.tw/exam/'
    EXAM_PATTERN1 = r'https://isafeevent.moe.edu.tw/exam/do2/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/'
    EXAM_PATTERN2 = r'https://isafeevent.moe.edu.tw/exam/do/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/'
    EXAM_PATTERN3 = r'https://isafeevent.moe.edu.tw/exam/result/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/'
    EXAM_ANSWER = '2413334144243432'
    def __init__(self):
        load_dotenv()

    def scroll_click(self, element: WebElement):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).move_to_element(element).click(element).perform()

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.START_URL)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.START_URL))

    def manual_login(self):
        self.driver.get(self.LOGIN_URL)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.LOGIN_URL))
        email_input = self.driver.find_element('css selector', 'input#email')
        # The fxxk is passowrd???
        password_input = self.driver.find_element('css selector', 'input#passowrd')
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        if email == None:
            raise AttributeError('Email is not found in .env file')
        if password == None:
            raise AttributeError('Password is not found in .env file')
        email_input.send_keys(email)
        password_input.send_keys(password)
        # Enter captcha and click login button on yourself

        # Wait until you login successfully
        WebDriverWait(self.driver, 300).until(EC.url_to_be(self.START_URL))
        
    def exam(self):
        self.driver.get(self.EXAM_URL)
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.EXAM_URL))
        exam_button = self.driver.find_element('css selector', 'input+button')
        self.scroll_click(exam_button)
        
        # Part 1
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.EXAM_PATTERN1))
        # Click all "strongly agree"
        radios = self.driver.find_elements('css selector', 'input[value="5"]')
        for radio in radios:
            self.scroll_click(radio)
        # Click send
        send_button = self.driver.find_element('css selector', 'button.btnSendExam')
        self.scroll_click(send_button)

        # Part 2
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.EXAM_PATTERN2))
        for i,answer in enumerate(self.EXAM_ANSWER):
            option = self.driver.find_elements('css selector', f'input[value="{answer}"]')[i]
            self.scroll_click(option)
        # Click send
        send_button = self.driver.find_element('css selector', 'button.btnSendExam')
        self.scroll_click(send_button)
        
        # Part 3 (result)
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.EXAM_PATTERN3))
        
    def close(self):
        self.driver.close()
        

if __name__ == '__main__':
    main = Main()
    main.open()
    main.manual_login()
    for _ in range(300):
        main.exam()
    main.close()