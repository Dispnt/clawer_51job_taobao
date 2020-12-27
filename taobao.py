from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import base64
import re
import pymongo

class Crawler(object):
    def __init__(self, search_content='美食'):
        self.search_content = search_content
        client = pymongo.MongoClient('127.0.0.1')
        self.db = client['taobao']
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.browser = webdriver.Chrome()# options=options
        self.wait = WebDriverWait(self.browser, 20)
        self.browser.get('http://www.taobao.com/')

    def save_to_mongo(self ,result, table_name='product'):
        try:
            if self.db[table_name].insert_one(result): # insert is deprecated
                print('保存成功', result)
        except Exception:
            print('失败辣', result)

    def search_first_page(self):
        search_bar = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="q"]')))
        submit = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button')))
        search_bar.send_keys(self.search_content)
        submit.click()

    def login_alipay_scan(self):
        alipay_login = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-form"]/div[5]/a[2]')))
        alipay_login.click()

    def login_by_pwd(self):
        login_account = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fm-login-id"]')))
        login_pwd = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fm-login-password"]')))
        account_info = '=='.encode()
        pwd_info = '=='.encode()
        login_account.send_keys(base64.b64decode(account_info).decode())
        login_pwd.send_keys(base64.b64decode(pwd_info).decode())
        login_submit = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-form"]/div[4]/button')))
        login_submit.click()

    def get_search_page(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainsrp-itemlist"]/div/div/div[1]')))
        html = self.browser.page_source
        page = BeautifulSoup(html, 'lxml')
        return page

    def get_total(self,page_content):
        current_n_all = page_content.find('span', class_='current').parent.get_text()
        return current_n_all.split('/')[1]

    def get_item_list(self, page_content):
        items = page_content.find('div', class_='grid g-clearfix').find_all('div', class_='items')[0]
        item_list = items.find_all('div', class_='item J_MouserOnverReq')
        return item_list

    def extract_save_item(self, items):
        for item in items:
            product = {
                'image': item.find('a', class_='J_ClickStat').find('img').attrs["data-src"],
                'price': item.find('div', class_='price g_price g_price-highlight').get_text().strip(),
                'deal': re.match(r'\d+', item.find('div', class_='deal-cnt').get_text()).group(),
                'title': item.find('a', class_='J_ClickStat').find('img').attrs["alt"],
                'shop': item.find('a', class_='shopname').get_text().strip(),
                'location': item.find('div', class_='location').get_text()
            }
            self.save_to_mongo(product,self.search_content)

    def next_page(self, page_number):
        input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[2]/input'))
        )
        submit = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]'))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="J_relative"]/div[1]/div/div[2]/ul/li[2]/span'),
                str(page_number))
        )
        print(f'正在保存第{page_number}页')
        item_list = self.get_item_list(self.get_search_page())
        self.extract_save_item(item_list)

    def run(self):
        self.search_first_page()
        self.login_by_pwd()
        item_list = self.get_item_list(result_page := self.get_search_page())
        self.extract_save_item(item_list)

        total = self.get_total(result_page)
        for i in range(2, int(total) + 1):
            self.next_page(i)

f18011433 = Crawler('soundcore liberty 2 pro')
f18011433.run()


# page = 2
# query = ""
# browser.get(f'https://s.taobao.com/search?q={query}&s={44*(page-1)}')
