import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
import time
import math

CHROMEDRIVER_PATH = r"./drivers/chromedriver"

class RiceGetter:
    def __init__(self):
        url = 'https://freerice.com/categories/multiplication-table'
        options = Options()
        options.headless = True
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
        self.driver.get(url)
        with open('jquery-3.5.0.slim.min.js', 'r') as jquery_js: 
            jquery = jquery_js.read() #read the jquery from a file
            self.driver.execute_script(jquery) #active the jquery lib
        self.rice = 0
    
    def play_game(self):
        question_el = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "card-title")))
        question_text = question_el.get_attribute('innerHTML')
        answer = int(question_text.split("x")[0]) * int(question_text.split("x")[1])
        answer_el = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, f'//div[@data-target="a{answer}"]')))
        self.driver.execute_script(f"$('div[data-target=\"a{answer}\"]').click()")
        rice_recieved = self.driver.find_element_by_xpath('//div[@class="rice-counter__value"]/span')
        self.rice = int(rice_recieved.get_attribute('innerHTML').replace(',',''))

    def get_rice(self):
        return math.ceil( float(self.rice) / 10) * 10


# #     actions = ActionChains(driver)
# #     actions.move_to_element(answer_el)
# #     actions.click()
# #     actions.pause(1)
# #     actions.perform()
