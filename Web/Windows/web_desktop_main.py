from selenium import webdriver
import time
from time import sleep
import random
import datetime
import unittest
import HTMLTestRunner
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pytesseract
from PIL import Image
from urllib.request import urlopen, urlretrieve
import re
import web_error_inspect
import web_common_component
import web_common_flow
import web_classified_page
import web_index
import web_search
import web_backend
import web_article_page


class SuperTaste(unittest.TestCase):

    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    # initial setting
    def setUp(self):
        chrome_path = 'C:/workspace/selenium_driver_chrome/chromedriver.exe'  # 改成你的chromedriver路徑
        options = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_setting_values': {
                'notifications': 2
            }
        }
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_path, options=options)

    # 登入頁面欄位、邏輯
    def test_memberCenterLoginPageCheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://member-st.tvbs.com.tw/index?back_url=https://'
                            'supertaste-shop-ec-test.tvbs.com.tw/?menucat=0&site=SupertasteEC&t=1594025730')
            self.driver.maximize_window()

            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('account')
            account_blank_text = account_blank.get_attribute('placeholder')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('password')
            password_blank_text = password_blank.get_attribute('placeholder')
            # 定位驗證碼欄位
            captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
            captcha_blank_text = captcha_blank.get_attribute('placeholder')
            # 定位登入按鈕
            login_btn = self.driver.find_element_by_id('signin')
            print('\n=======欄位驗證=======')
            self.assertEqual(account_blank_text, '請輸入註冊 Email')  # 判斷帳號欄位placeholder
            print('登入帳號欄位placeholder為 : ' + account_blank_text)
            self.assertEqual(password_blank_text, '請輸入密碼')  # 判斷密碼欄位placeholder
            print('登入密碼欄位placeholder為 : ' + password_blank_text)
            self.assertEqual(captcha_blank_text, '請輸入右圖文字')  # 判斷驗證碼欄位placeholder
            print('登入驗證碼欄位placeholder為 : ' + captcha_blank_text)

            # 不輸入帳號、密碼、驗證碼登入
            print('\n=======不輸入帳號、密碼、驗證碼登入=======')
            login_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '請輸入Email')
            print('不輸入帳號登入跳出wording : ' + account_message)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '請輸入密碼')
            print('不輸入密碼登入跳出wording : ' + password_message)
            captcha_message = self.driver.find_element_by_id('message_InputCaptcha1').text
            self.assertEqual(captcha_message, '請輸入驗證碼')
            print('不輸入驗證碼登入跳出wording : ' + captcha_message)

            # 只輸入不合格式帳號登入
            print('\n=======只輸入不合格式帳號登入=======')
            account_blank.send_keys('tvbs')
            login_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '帳號格式錯誤，請填寫完整Email！')
            print('輸入不合格式帳號登入跳出wording : ' + account_message)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '請輸入密碼')
            print('不輸入密碼登入跳出wording : ' + password_message)
            captcha_message = self.driver.find_element_by_id('message_InputCaptcha1').text
            self.assertEqual(captcha_message, '請輸入驗證碼')
            print('不輸入驗證碼登入跳出wording : ' + captcha_message)

            # 只輸入符合格式帳號(未註冊)登入
            print('\n=======只輸入符合格式帳號登入(未註冊)=======')
            account_blank.clear()
            account_blank.send_keys('tvbs@gmail.com')
            login_btn.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id('message_account').text)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_password').text)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '請輸入密碼')
            print('不輸入密碼登入跳出wording : ' + password_message)
            captcha_message = self.driver.find_element_by_id('message_InputCaptcha1').text
            self.assertEqual(captcha_message, '請輸入驗證碼')
            print('不輸入驗證碼登入跳出wording : ' + captcha_message)

            # 只輸入密碼登入
            print('\n=======只輸入密碼登入=======')
            account_blank.clear()
            password_blank.send_keys('tvbs')
            login_btn.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id('message_password').text)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '請輸入Email')
            print('不輸入帳號登入跳出wording : ' + account_message)
            captcha_message = self.driver.find_element_by_id('message_InputCaptcha1').text
            self.assertEqual(captcha_message, '請輸入驗證碼')
            print('不輸入驗證碼登入跳出wording : ' + captcha_message)

            # 只輸入錯誤驗證碼登入
            print('\n=======只輸入錯誤驗證碼登入=======')
            password_blank.clear()
            captcha_blank.send_keys('tvbs')
            login_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '請輸入Email')
            print('不輸入帳號登入跳出wording : ' + account_message)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '請輸入密碼')
            print('不輸入密碼登入跳出wording : ' + password_message)
            captcha_message = self.driver.find_element_by_id('message_InputCaptcha1').text
            self.assertEqual(captcha_message, '驗證碼錯誤，請再試一次！')
            print('輸入錯誤驗證碼登入跳出wording : ' + captcha_message)

            # 只輸入正確驗證碼登入
            print('\n=======只輸入正確驗證碼登入=======')
            captcha_blank.clear()
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            # 輸入驗證碼
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            login_btn.click()
            sleep(2)
            while True:
                if '驗證碼錯誤，請再試一次！' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('InputCaptcha1'))
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                elif '請輸入驗證碼' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('InputCaptcha1'))
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                else:
                    break
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id('message_InputCaptcha1').text)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '請輸入Email')
            print('不輸入帳號登入跳出wording : ' + account_message)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '請輸入密碼')
            print('不輸入密碼登入跳出wording : ' + password_message)

            # 輸入符合格式帳號(未註冊)、密碼、錯誤驗證碼登入
            print('\n=======輸入符合格式帳號(未註冊)、密碼、錯誤驗證碼登入=======')
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('account')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('password')
            # 定位驗證碼欄位
            captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
            # 定位登入按鈕
            login_btn = self.driver.find_element_by_id('signin')
            captcha_blank.clear()
            account_blank.send_keys('tvbs@gmail.com')
            password_blank.send_keys('tvbs')
            captcha_blank.send_keys('tvbs')
            login_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_InputCaptcha1').text)
            captcha_message = self.driver.find_element_by_id('message_InputCaptcha1').text
            self.assertEqual(captcha_message, '驗證碼錯誤，請再試一次！')
            print('輸入錯誤驗證碼登入跳出wording : ' + captcha_message)

            # 輸入符合格式帳號(未註冊)、密碼、正確驗證碼登入
            print('\n=======輸入符合格式帳號(未註冊)、密碼、正確驗證碼登入=======')
            account_blank.clear()
            password_blank.clear()
            captcha_blank.clear()
            account_blank.send_keys('tvbs@gmail.com')
            password_blank.send_keys('tvbs')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            # 輸入驗證碼
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            login_btn.click()
            sleep(2)
            while True:
                if '驗證碼錯誤，請再試一次！' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('tvbs@gmail.com')
                    password_blank.send_keys('tvbs')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                elif '請輸入驗證碼' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('tvbs@gmail.com')
                    password_blank.send_keys('tvbs')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                else:
                    break
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '查無此帳號！')
            print('輸入符合格式帳號(未註冊)登入跳出wording : ' + account_message)

            # 輸入符合格式帳號(已註冊)、錯誤密碼、正確驗證碼登入
            print('\n=======輸入符合格式帳號(已註冊)、錯誤密碼、正確驗證碼登入=======')
            account_blank.clear()
            password_blank.clear()
            captcha_blank.clear()
            account_blank.send_keys('s0932748681@gmail.com')
            password_blank.send_keys('tvbs')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            # 輸入驗證碼
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            login_btn.click()
            sleep(2)
            while True:
                if '驗證碼錯誤，請再試一次！' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('s0932748681@gmail.com')
                    password_blank.send_keys('tvbs')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                elif '請輸入驗證碼' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('s0932748681@gmail.com')
                    password_blank.send_keys('tvbs')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                else:
                    break
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('message_password').text)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '帳號或密碼錯誤，請重新輸入！')
            print('輸入錯誤密碼登入跳出wording : ' + password_message)

            # 輸入符合格式帳號(已註冊)、正確密碼、刷新前驗證碼登入
            print('\n=======輸入符合格式帳號(已註冊)、正確密碼、之前的驗證碼登入=======')
            account_blank.clear()
            password_blank.clear()
            captcha_blank.clear()
            account_blank.send_keys('s0932748681@gmail.com')
            password_blank.send_keys('s23321286')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            self.driver.find_element_by_class_name('resetCaptcha').click()  # 重取驗證碼
            sleep(1)
            login_btn.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id('message_password').text)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_InputCaptcha1').text)
            captcha_message = self.driver.find_element_by_id('message_InputCaptcha1').text
            self.assertEqual(captcha_message, '驗證碼錯誤，請再試一次！')
            print('輸入刷新前的驗證碼登入跳出wording : ' + captcha_message)

            # 輸入被禁用帳號
            print('\n=======輸入被禁用帳號=======')
            account_blank.clear()
            password_blank.clear()
            captcha_blank.clear()
            account_blank.send_keys('freyjachen0204@gmail.com')
            password_blank.send_keys('a123456')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            login_btn.click()
            sleep(2)
            while True:
                if '驗證碼錯誤，請再試一次！' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('freyjachen0204@gmail.com')
                    password_blank.send_keys('a123456')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                elif '請輸入驗證碼' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('freyjachen0204@gmail.com')
                    password_blank.send_keys('a123456')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                else:
                    break
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '此帳號被禁用! 任何疑問請與客服(service@tvbs.com.tw)聯絡')
            print('輸入被禁用帳號登入跳出wording : ' + account_message)

            # 使用已透過 Fb 註冊的帳號登入
            print('\n=======使用已透過 Fb 註冊的帳號登入=======')
            account_blank.clear()
            password_blank.clear()
            captcha_blank.clear()
            account_blank.send_keys('s23321286@gmail.com')
            password_blank.send_keys('qa23321286')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            login_btn.click()
            sleep(2)
            while True:
                if '驗證碼錯誤，請再試一次！' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('s23321286@gmail.com')
                    password_blank.send_keys('qa23321286')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                elif '請輸入驗證碼' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('s23321286@gmail.com')
                    password_blank.send_keys('qa23321286')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                else:
                    break
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('message_password').text)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '帳號或密碼錯誤，請重新輸入！')
            print('輸入已透過 Fb 註冊的帳號登入跳出wording : ' + password_message)

            # 使用已透過 Apple ID 註冊的帳號登入
            print('\n=======使用已透過 Apple ID 註冊的帳號登入=======')
            account_blank.clear()
            password_blank.clear()
            captcha_blank.clear()
            account_blank.send_keys('tvbstest0727@gmail.com')
            password_blank.send_keys('tvbs2020')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            login_btn.click()
            sleep(2)
            while True:
                if '驗證碼錯誤，請再試一次！' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('tvbstest0727@gmail.com')
                    password_blank.send_keys('tvbs2020')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                elif '請輸入驗證碼' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位密碼欄位
                    password_blank = self.driver.find_element_by_id('password')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位登入按鈕
                    login_btn = self.driver.find_element_by_id('signin')
                    account_blank.send_keys('tvbstest0727@gmail.com')
                    password_blank.send_keys('tvbs2020')
                    pic = self.driver.find_element_by_xpath(
                        '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    login_btn.click()
                    sleep(2)
                else:
                    break
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('message_password').text)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '帳號或密碼錯誤，請重新輸入！')
            print('輸入已透過 Apple ID 註冊的帳號登入跳出wording : ' + password_message)

            # Footer驗證
            print('\n=======Footer驗證=======')
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name('footer').text)
            footer_text = self.driver.find_element_by_class_name('footer').text
            self.assertEqual(footer_text, '聯利媒體股份有限公司\n© TVBS Media Inc. All Rights Reserved.')
            print('登入頁Footer為 : ' + footer_text)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../.../../../screenshot/supertasteWebFail/memberCenterLoginPageCheck_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 登入TVBS會員
    def test_memberCenterLoginTVBS(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://member-st.tvbs.com.tw/index?back_url=https://'
                            'supertaste-shop-ec-test.tvbs.com.tw/?menucat=0&site=SupertasteEC&t=1594025730')
            self.driver.maximize_window()

            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('account')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('password')
            # 定位驗證碼欄位
            captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
            # 定位登入按鈕
            login_btn = self.driver.find_element_by_id('signin')

            # 登入TVBS會員
            print('\n=======登入TVBS會員=======')
            account_blank.clear()
            password_blank.clear()
            captcha_blank.clear()
            account_blank.send_keys('s0932748681@gmail.com')
            password_blank.send_keys('s23321286')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            login_btn.click()
            sleep(2)
            url = self.driver.current_url
            while url.find('member') != -1:
                print('驗證碼辨識失敗，重整頁面')
                self.driver.refresh()
                sleep(2)
                # 定位帳號欄位
                account_blank = self.driver.find_element_by_id('account')
                # 定位密碼欄位
                password_blank = self.driver.find_element_by_id('password')
                # 定位驗證碼欄位
                captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                # 定位登入按鈕
                login_btn = self.driver.find_element_by_id('signin')
                account_blank.send_keys('s0932748681@gmail.com')
                password_blank.send_keys('s23321286')
                # 圖形辨識
                pic = self.driver.find_element_by_xpath(
                    '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                pytesseract.pytesseract.tesseract_cmd = \
                    '../../Tesseract-OCR/tesseract.exe'
                img = Image.open('../../../screenshot/Captcha/get.png')
                img = img.convert('L')
                captcha = pytesseract.image_to_string(img)
                print('此次驗證碼為 : ' + captcha)
                captcha_blank.send_keys(captcha)
                login_btn.click()
                sleep(2)
                url = self.driver.current_url
                if url == 'https://supertaste-shop-ec-test.tvbs.com.tw/?menucat=0':
                    break

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('bt-member'))
            self.driver.find_element_by_id('bt-member').click()
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_link_text('登出'))
            print('登入TVBS會員成功')
            self.driver.find_element_by_partial_link_text('登出').click()
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('bt-member').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_link_text('登入 / 註冊'))
            print('登出TVBS會員成功')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/memberCenterLoginTVBS_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 登入FB會員
    def test_memberCenterLoginFB(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://member-st.tvbs.com.tw/index?back_url=https://'
                            'supertaste-shop-ec-test.tvbs.com.tw/?menucat=0&site=SupertasteEC&t=1594025730')
            self.driver.maximize_window()

            # 登入FB會員
            print('\n=======登入FB會員=======')
            self.driver.find_element_by_id('singinWithFacebook').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('email'))
            self.driver.find_element_by_id('email').send_keys('s23321286@gmail.com')
            self.driver.find_element_by_id('pass').send_keys('Tvbs2020')
            self.driver.find_element_by_id('loginbutton').click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('bt-member'))
            self.driver.find_element_by_id('bt-member').click()
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_link_text('登出'))
            print('登入FB會員成功')
            self.driver.find_element_by_partial_link_text('登出').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('bt-member'))
            self.driver.find_element_by_id('bt-member').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_link_text('登入 / 註冊'))
            print('登出FB會員成功')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/memberCenterLoginFB_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 登入Apple ID會員
    def test_memberCenterLoginAppleID(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://member-st.tvbs.com.tw/index?back_url=https://'
                            'supertaste-shop-ec-test.tvbs.com.tw/?menucat=0&site=SupertasteEC&t=1594025730')
            self.driver.maximize_window()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]'))

            # 登入Apple ID會員
            print('\n=======登入Apple ID會員=======')
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account_name_text_field'))
            self.driver.find_element_by_id('account_name_text_field').clear()
            self.driver.find_element_by_id('account_name_text_field').send_keys('s0932748681@gmail.com')
            self.driver.find_element_by_class_name('icon_sign_in').click()
            sleep(1)
            self.driver.find_element_by_id('password_text_field').clear()
            self.driver.find_element_by_id('password_text_field').send_keys('Qa23321286')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('icon_sign_in'))
            self.driver.find_element_by_class_name('icon_sign_in').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('overflow-text'))
            # self.driver.find_element_by_class_name('overflow-text').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('bt-member'))
            # self.driver.find_element_by_id('bt-member').click()
            # WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_link_text('登出'))
            # print('登入Apple ID會員成功')
            # self.driver.find_element_by_partial_link_text('登出').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('bt-member'))
            # self.driver.find_element_by_id('bt-member').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_link_text('登入 / 註冊'))
            # print('登出Apple ID會員成功')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../.../../../screenshot/supertasteWebFail/memberCenterLoginAppleID_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 註冊頁面欄位、邏輯
    def test_memberCenterRegisterPageCheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://member-st.tvbs.com.tw/index?back_url=https://'
                            'supertaste-shop-ec-test.tvbs.com.tw/?menucat=0&site=SupertasteEC&t=1594025730')
            self.driver.maximize_window()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_link_text('註冊新會員'))

            # 註冊頁面跳轉
            self.driver.find_element_by_link_text('註冊新會員').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))

            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('account')
            account_blank_text = account_blank.get_attribute('placeholder')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('password')
            password_blank_text = password_blank.get_attribute('placeholder')
            # 定位確認密碼欄位
            confirm_password_blank = self.driver.find_element_by_id('confirmPassword')
            confirm_password_blank_text = confirm_password_blank.get_attribute('placeholder')
            # 定位註冊按鈕
            register_btn = self.driver.find_element_by_id('registerbutton')

            print('\n=======欄位驗證=======')
            self.assertEqual(account_blank_text, '請輸入註冊 Email')  # 判斷帳號欄位placeholder
            print('登入帳號欄位placeholder為 : ' + account_blank_text)
            self.assertEqual(password_blank_text, '請設定密碼 (6-12個英數字)')  # 判斷密碼欄位placeholder
            print('登入密碼欄位placeholder為 : ' + password_blank_text)
            self.assertEqual(confirm_password_blank_text, '請再次輸入密碼')  # 判斷確認密碼欄位placeholder
            print('登入驗證碼欄位placeholder為 : ' + confirm_password_blank_text)

            # 不輸入帳號、密碼、確認密碼註冊
            print('\n=======不輸入帳號、密碼、確認密碼註冊=======')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '請輸入Email')
            print('不輸入帳號註冊跳出wording : ' + account_message)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '請輸入密碼')
            print('不輸入密碼註冊跳出wording : ' + password_message)
            confirm_password_message = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(confirm_password_message, '請再次輸入密碼')
            print('不輸入確認密碼註冊跳出wording : ' + confirm_password_message)

            # 只輸入不合格式帳號註冊
            print('\n=======只輸入不合格式帳號註冊=======')
            account_blank.send_keys('tvbs')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '帳號格式錯誤，請填寫完整Email！')
            print('輸入不合格式帳號註冊跳出wording : ' + account_message)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '請輸入密碼')
            print('不輸入密碼註冊跳出wording : ' + password_message)
            confirm_password_message = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(confirm_password_message, '請再次輸入密碼')
            print('不輸入確認密碼註冊跳出wording : ' + confirm_password_message)

            # 只輸入符合格式帳號註冊
            print('\n=======只輸入符合格式帳號註冊=======')
            account_blank.clear()
            account_blank.send_keys('tvbs@gmail.com')
            register_btn.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id('message_account').text)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_password').text)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '請輸入密碼')
            print('不輸入密碼註冊跳出wording : ' + password_message)
            confirm_password_message = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(confirm_password_message, '請再次輸入密碼')
            print('不輸入確認密碼註冊跳出wording : ' + confirm_password_message)

            # 只輸入密碼註冊
            print('\n=======只輸入密碼註冊=======')
            account_blank.clear()
            password_blank.send_keys('tvbs')
            register_btn.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id('message_password').text)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '請輸入Email')
            print('不輸入帳號註冊跳出wording : ' + account_message)
            confirm_password_message = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(confirm_password_message, '請再次輸入密碼')
            print('不輸入確認密碼註冊跳出wording : ' + confirm_password_message)

            # 只輸入確認密碼註冊
            print('\n=======只輸入確認密碼註冊=======')
            password_blank.clear()
            confirm_password_blank.send_keys('tvbs')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '請輸入Email')
            print('不輸入帳號註冊跳出wording : ' + account_message)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '請輸入密碼')
            print('不輸入密碼註冊跳出wording : ' + password_message)
            confirm_password_message = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(confirm_password_message, '密碼與確認密碼不符，請重新確認!')
            print('只輸入確認密碼註冊跳出wording : ' + confirm_password_message)

            # 輸入不符合格式帳號、不符合格式密碼、錯誤確認密碼註冊
            print('\n=======輸入不符合格式帳號、不符合格式密碼、錯誤確認密碼註冊=======')
            confirm_password_blank.clear()
            account_blank.send_keys('tvbs')
            password_blank.send_keys('tvbs')
            confirm_password_blank.send_keys('tvbs2020')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '帳號格式錯誤，請填寫完整Email！')
            print('輸入不符合格式帳號註冊跳出wording : ' + account_message)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '密碼建議為6~12位數，必須是英文數字混合！')
            print('輸入不符合格式密碼註冊跳出wording : ' + password_message)
            confirm_password_message = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(confirm_password_message, '密碼與確認密碼不符，請重新確認!')
            print('輸入錯誤確認密碼註冊跳出wording : ' + confirm_password_message)

            # 輸入不符合格式帳號、不符合格式密碼、正確確認密碼註冊
            print('\n=======輸入不符合格式帳號、不符合格式密碼、正確確認密碼註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('tvbs')
            password_blank.send_keys('tvbs')
            confirm_password_blank.send_keys('tvbs')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '帳號格式錯誤，請填寫完整Email！')
            print('輸入不符合格式帳號註冊跳出wording : ' + account_message)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '密碼建議為6~12位數，必須是英文數字混合！')
            print('輸入不符合格式密碼註冊跳出wording : ' + password_message)

            # 輸入不符合格式帳號、符合格式密碼、錯誤確認密碼註冊
            print('\n=======輸入不符合格式帳號、符合格式密碼、錯誤確認密碼註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('tvbs')
            password_blank.send_keys('tvbs2020')
            confirm_password_blank.send_keys('tvbs')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '帳號格式錯誤，請填寫完整Email！')
            print('輸入不符合格式帳號註冊跳出wording : ' + account_message)
            confirm_password_message = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(confirm_password_message, '密碼與確認密碼不符，請重新確認!')
            print('輸入錯誤確認密碼註冊跳出wording : ' + confirm_password_message)

            # 輸入不符合格式帳號、符合格式密碼、正確確認密碼註冊
            print('\n=======輸入不符合格式帳號、符合格式密碼、正確確認密碼註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('tvbs')
            password_blank.send_keys('tvbs2020')
            confirm_password_blank.send_keys('tvbs2020')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '帳號格式錯誤，請填寫完整Email！')
            print('輸入不符合格式帳號註冊跳出wording : ' + account_message)

            # 輸入符合格式帳號、不符合格式密碼、錯誤確認密碼註冊
            print('\n=======輸入符合格式帳號、不符合格式密碼、錯誤確認密碼註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('tvbs@gmail.com')
            password_blank.send_keys('tvbs')
            confirm_password_blank.send_keys('tvbs1')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_password').text)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '密碼建議為6~12位數，必須是英文數字混合！')
            print('輸入不符合格式密碼註冊跳出wording : ' + password_message)
            confirm_password_message = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(confirm_password_message, '密碼與確認密碼不符，請重新確認!')
            print('輸入錯誤確認密碼註冊跳出wording : ' + confirm_password_message)

            # 輸入符合格式帳號、不符合格式密碼、正確確認密碼註冊
            print('\n=======輸入符合格式帳號、不符合格式密碼、正確確認密碼註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('tvbs@gmail.com')
            password_blank.send_keys('tvbs')
            confirm_password_blank.send_keys('tvbs')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_password').text)
            password_message = self.driver.find_element_by_id('message_password').text
            self.assertEqual(password_message, '密碼建議為6~12位數，必須是英文數字混合！')
            print('輸入不符合格式密碼註冊跳出wording : ' + password_message)

            # 輸入符合格式帳號、符合格式密碼、錯誤確認密碼註冊
            print('\n=======輸入符合格式帳號、符合格式密碼、錯誤確認密碼註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('tvbs@gmail.com')
            password_blank.send_keys('tvbs2020')
            confirm_password_blank.send_keys('tvbs')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_confirmPassword').text)
            confirm_password_message = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(confirm_password_message, '密碼與確認密碼不符，請重新確認!')
            print('輸入錯誤確認密碼註冊跳出wording : ' + confirm_password_message)

            # 輸入已註冊過帳號註冊
            print('\n=======輸入已註冊過帳號註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('s0932748681@gmail.com')
            password_blank.send_keys('tvbs2020')
            confirm_password_blank.send_keys('tvbs2020')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '此帳號已透過 Email 註冊為會員！')
            print('輸入已註冊過帳號註冊跳出wording : ' + account_message)

            # 輸入已用 FB 註冊過的帳號註冊
            print('\n=======輸入已用 FB 註冊過的帳號註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('s0932748681@yahoo.com.tw')
            password_blank.send_keys('tvbs2020')
            confirm_password_blank.send_keys('tvbs2020')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '此帳號已透過 FB 註冊為會員！')
            print('輸入已註冊過 FB 帳號註冊跳出wording : ' + account_message)

            # 輸入已用 Apple ID 註冊過的帳號註冊
            print('\n=======輸入已用 Apple ID 註冊過的帳號註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('tvbstest0727@gmail.com')
            password_blank.send_keys('tvbs2020')
            confirm_password_blank.send_keys('tvbs2020')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '此帳號已透過 Apple ID 註冊為會員！')
            print('輸入已註冊過 Apple ID 帳號註冊跳出wording : ' + account_message)

            # 輸入被禁用的帳號註冊
            print('\n=======輸入被禁用的帳號註冊=======')
            account_blank.clear()
            password_blank.clear()
            confirm_password_blank.clear()
            account_blank.send_keys('freyjachen0204@gmail.com')
            password_blank.send_keys('tvbs2020')
            confirm_password_blank.send_keys('tvbs2020')
            register_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '此帳號被禁用! 任何疑問請與客服(service@tvbs.com.tw)聯絡')
            print('輸入被禁用的帳號註冊跳出wording : ' + account_message)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/memberCenterRegisterPageCheck_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 忘記密碼頁面欄位、邏輯檢查
    def test_memberCenterForgotPasswordPageCheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://member-st.tvbs.com.tw/index/forget_pass?back_url=https%3A%2F%2Fsupertaste-shop'
                            '-ec-test.tvbs.com.tw%2F%3Fmenucat%3D0&site=SupertasteEC&t=1592878881')
            self.driver.maximize_window()
            print('\n=======忘記密碼頁面欄位、邏輯檢查=======')
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('account')
            # 定位驗證碼欄位
            captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
            # 寄送密碼重設信按鈕
            forgot_pwd_btn = self.driver.find_element_by_id('forgotPWDButton')

            # 不輸入帳號跟驗證碼
            print('\n=======不輸入帳號跟驗證碼=======')
            forgot_pwd_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '請輸入Email')
            print('不輸入帳號送出跳出wording : ' + account_message)
            captcha_message = self.driver.find_element_by_id('message_captcha').text
            self.assertEqual(captcha_message, '請輸入驗證碼')
            print('不輸入驗證碼送出跳出wording : ' + captcha_message)

            # 輸入錯誤格式帳號
            print('\n=======輸入錯誤格式帳號=======')
            account_blank.send_keys('tvbs2020')
            forgot_pwd_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '帳號格式錯誤，請填寫完整Email！')
            print('輸入錯誤格式帳號送出跳出wording : ' + account_message)
            captcha_message = self.driver.find_element_by_id('message_captcha').text
            self.assertEqual(captcha_message, '請輸入驗證碼')
            print('不輸入驗證碼送出跳出wording : ' + captcha_message)

            # 輸入錯誤驗證碼
            print('\n=======輸入錯誤驗證碼=======')
            captcha_blank.send_keys('1234')
            forgot_pwd_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '帳號格式錯誤，請填寫完整Email！')
            print('輸入錯誤格式帳號送出跳出wording : ' + account_message)
            captcha_message = self.driver.find_element_by_id('message_captcha').text
            self.assertEqual(captcha_message, '驗證碼錯誤，請再試一次！')
            print('不輸入驗證碼送出跳出wording : ' + captcha_message)

            # 輸入未註冊過帳號
            print('\n=======輸入未註冊過帳號=======')
            account_blank.clear()
            captcha_blank.clear()
            account_blank.send_keys('tvbs2020@gmail.com')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            # 輸入驗證碼
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            forgot_pwd_btn.click()
            sleep(2)
            while True:
                if '驗證碼錯誤，請再試一次！' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位寄送密碼重設信按鈕
                    forgot_pwd_btn = self.driver.find_element_by_id('forgotPWDButton')
                    account_blank.send_keys('tvbs2020@gmail.com')
                    pic = self.driver.find_element_by_xpath(
                        '/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    forgot_pwd_btn.click()
                    sleep(2)
                elif '請輸入驗證碼' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位寄送密碼重設信按鈕
                    forgot_pwd_btn = self.driver.find_element_by_id('forgotPWDButton')
                    account_blank.send_keys('tvbs2020@gmail.com')
                    pic = self.driver.find_element_by_xpath(
                        '/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    forgot_pwd_btn.click()
                    sleep(2)
                else:
                    break
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_account').text)
            account_message = self.driver.find_element_by_id('message_account').text
            self.assertEqual(account_message, '查無此帳號！')
            print('輸入未註冊過帳號送出跳出wording : ' + account_message)

            # 輸入被禁用帳號
            print('\n=======輸入被禁用帳號=======')
            account_blank.clear()
            captcha_blank.clear()
            account_blank.send_keys('freyjachen0204@gmail.com')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            # 輸入驗證碼
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            forgot_pwd_btn.click()
            sleep(3)
            while True:
                if '驗證碼錯誤，請再試一次！' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位寄送密碼重設信按鈕
                    forgot_pwd_btn = self.driver.find_element_by_id('forgotPWDButton')
                    account_blank.send_keys('freyjachen0204@gmail.com')
                    pic = self.driver.find_element_by_xpath(
                        '/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    forgot_pwd_btn.click()
                    sleep(3)
                elif '請輸入驗證碼' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位寄送密碼重設信按鈕
                    forgot_pwd_btn = self.driver.find_element_by_id('forgotPWDButton')
                    account_blank.send_keys('freyjachen0204@gmail.com')
                    pic = self.driver.find_element_by_xpath(
                        '/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    forgot_pwd_btn.click()
                    sleep(3)
                else:
                    break
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message').text)
            message = self.driver.find_element_by_id('message').text
            self.assertEqual(message, '此帳號被禁用! 任何疑問請與客服(service@tvbs.com.tw)聯絡')
            print('輸入被禁用帳號送出跳出wording : ' + message)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/'
                    'memberCenterForgotPasswordPageCheck_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 註冊TVBS會員
    def test_memberCenterRegisterTVBS(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://member-st.tvbs.com.tw/index?back_url=https://'
                            'supertaste-shop-ec-test.tvbs.com.tw/?menucat=0&site=SupertasteEC&t=1594025730')
            self.driver.maximize_window()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_link_text('註冊新會員'))

            # 註冊TVBS會員
            print('\n=======註冊TVBS會員=======')
            self.driver.find_element_by_link_text('註冊新會員').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))

            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('account')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('password')
            # 定位確認密碼欄位
            confirm_password_blank = self.driver.find_element_by_id('confirmPassword')
            # 定位註冊按鈕
            register_btn = self.driver.find_element_by_id('registerbutton')

            # 註冊TVBS會員
            js = 'window.open("http://www.yopmail.com/zh/email-generator.php");'
            self.driver.execute_script(js)
            # 獲取當前視窗控制代碼集合（列表型別）
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('login'))
            register_account = self.driver.find_element_by_id('login').get_attribute('value')
            print('此次註冊帳號為 : ' + register_account)
            self.driver.switch_to.window(handles[0])
            account_blank.send_keys(register_account)
            password_blank.send_keys('tvbs2020')
            confirm_password_blank.send_keys('tvbs2020')
            register_btn.click()

            # 填寫性別生日頁
            # 不填寫性別生日送出
            print('\n=======性別生日頁防呆=======')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('registersexbutton'))
            sleep(2)
            self.driver.find_element_by_id('registersexbutton').click()
            # 性別
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_sex').text)
            check_sex_message = self.driver.find_element_by_id('message_sex').text
            self.assertEqual(check_sex_message, '請輸入性別')
            print('未填寫性別送出跳出wording :　' + check_sex_message)
            # 生日
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_birth').text)
            check_birth_message = self.driver.find_element_by_id('message_birth').text
            self.assertEqual(check_birth_message, '請輸入生日')
            print('未填寫生日送出跳出wording :　' + check_birth_message)
            # 服務條款及隱私權政策
            check_privacy_message = self.driver.find_element_by_id('message_chk_privacy').text
            self.assertEqual(check_privacy_message, '請同意TVBS會員中心的服務條款及隱私權政策。')
            print('未勾選同意服務條款及隱私權政策送出跳出wording :　' + check_privacy_message)

            # 勾選性別
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('registersexbutton'))
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="1"]').click()
            print('男性按鈕可正常勾選')
            self.driver.find_element_by_xpath('//*[@id="2"]').click()
            print('女性按鈕可正常勾選')

            # 填寫格式不正確的生日
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('registersexbutton'))
            sleep(2)
            born_year = Select(self.driver.find_element_by_id('register_sex_year'))
            born_year.select_by_value("1994")
            born_month = Select(self.driver.find_element_by_id('register_sex_month'))
            born_month.select_by_value("9")
            self.driver.find_element_by_id('chk_privacy').click()  # 勾選同意服務條款及隱私權政策
            self.driver.find_element_by_id('registersexbutton').click()  # 送出按鈕
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_birth').text)
            check_birth_message = self.driver.find_element_by_id('message_birth').text
            self.assertEqual(check_birth_message, '輸入生日格式錯誤')
            print('填寫格式不正確的生日送出跳出wording :　' + check_birth_message)

            # 填寫晚於今日的生日
            born_year = Select(self.driver.find_element_by_id('register_sex_year'))
            born_year.select_by_value("2020")
            born_month = Select(self.driver.find_element_by_id('register_sex_month'))
            born_month.select_by_value("12")
            born_day = Select(self.driver.find_element_by_id('register_sex_day'))
            born_day.select_by_value("31")
            self.driver.find_element_by_id('registersexbutton').click()  # 送出按鈕
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_birth').text)
            check_birth_message = self.driver.find_element_by_id('message_birth').text
            self.assertEqual(check_birth_message, '輸入生日格式錯誤')
            print('填寫晚於今日的生日送出跳出wording :　' + check_birth_message)

            # 填寫正常生日
            born_year = Select(self.driver.find_element_by_id('register_sex_year'))
            born_year.select_by_value("1994")
            born_month = Select(self.driver.find_element_by_id('register_sex_month'))
            born_month.select_by_value("9")
            born_day = Select(self.driver.find_element_by_id('register_sex_day'))
            born_day.select_by_value("8")
            self.driver.find_element_by_id('registersexbutton').click()  # 送出按鈕
            print('同意服務條款及隱私權政策可正常送出')
            sleep(5)

            # 切換回拋棄式信箱分頁
            print('\n=======註冊認證信驗證=======')
            self.driver.switch_to.window(handles[1])
            self.driver.find_element_by_xpath(
                '/html/body/center/div/div/div[3]/table[2]/tbody/tr/td[2]/div/div[2]/div[1]/input').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('slientext'))
            for i in range(3):
                self.driver.find_element_by_class_name('slientext').click()

            # 點選認證信連結
            self.driver.switch_to.frame('ifmail')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('mailmillieu'))
            self.driver.find_element_by_partial_link_text('https://member-st.tvbs.com.tw/index/v_code_check/').click()
            print('點選認證信成功')

            # 認證成功頁面
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[2])
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('t1'))
            print(self.driver.find_element_by_class_name('t1').text)
            # print('註冊成功！！')

            # 跳轉到忘記密碼分頁
            print('\n=======忘記密碼=======')
            self.driver.get('https://member-st.tvbs.com.tw/index/forget_pass?back_url=https%3A%2F%2Fsupertaste-shop'
                            '-ec-test.tvbs.com.tw%2F%3Fmenucat%3D0&site=SupertasteEC&t=1592790542')
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('account')
            # 定位驗證碼欄位
            captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
            # 定位寄送密碼重設信按鈕
            forgot_pwd_btn = self.driver.find_element_by_id('forgotPWDButton')
            account_blank.send_keys(register_account)
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            # 輸入驗證碼
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            forgot_pwd_btn.click()
            sleep(2)
            while True:
                if '驗證碼錯誤，請再試一次！' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位寄送密碼重設信按鈕
                    forgot_pwd_btn = self.driver.find_element_by_id('forgotPWDButton')
                    account_blank.send_keys(register_account)
                    pic = self.driver.find_element_by_xpath(
                        '/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    forgot_pwd_btn.click()
                    sleep(2)
                elif '請輸入驗證碼' in self.driver.page_source:
                    print('驗證碼辨識失敗，重整頁面')
                    self.driver.refresh()
                    sleep(3)
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account'))
                    # 定位帳號欄位
                    account_blank = self.driver.find_element_by_id('account')
                    # 定位驗證碼欄位
                    captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                    # 定位寄送密碼重設信按鈕
                    forgot_pwd_btn = self.driver.find_element_by_id('forgotPWDButton')
                    account_blank.send_keys(register_account)
                    pic = self.driver.find_element_by_xpath(
                        '/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
                    sleep(2)
                    urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                    pytesseract.pytesseract.tesseract_cmd = \
                        '../../Tesseract-OCR/tesseract.exe'
                    img = Image.open('../../../screenshot/Captcha/get.png')
                    img = img.convert('L')
                    captcha = pytesseract.image_to_string(img)
                    print('此次驗證碼為 : ' + captcha)
                    captcha_blank.send_keys(captcha)
                    forgot_pwd_btn.click()
                    sleep(2)
                else:
                    break
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message').text)
            forgot_pwd_message = self.driver.find_element_by_id('message').text
            print(forgot_pwd_message)
            sleep(3)

            # 切換回拋棄式信箱分頁
            print('\n=======忘記密碼認證信驗證=======')
            self.driver.switch_to.window(handles[1])
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('slientext'))
            for i in range(3):
                self.driver.find_element_by_class_name('slientext').click()

            # 點選認證信連結
            self.driver.switch_to.frame('ifmail')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('mailmillieu'))
            self.driver.find_element_by_partial_link_text('https://member-st.tvbs.com.tw/index/reset_password').click()
            print('點選認證信成功')

            # 重設密碼頁面
            print('\n=======不輸入密碼、確認密碼送出=======')
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[3])
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('new_passcode'))
            self.driver.find_element_by_name('change_password_button').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_new_passcode').text)
            message_new_passcode = self.driver.find_element_by_id('message_new_passcode').text
            self.assertEqual(message_new_passcode, '請輸入新密碼')
            print('不輸入密碼送出跳出wording : ' + message_new_passcode)
            message_confirm_password = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(message_confirm_password, '請再次輸入新密碼')
            print('不輸入確認密碼送出跳出wording : ' + message_confirm_password)

            print('\n=======輸入不合規則密碼、確認密碼送出=======')
            self.driver.find_element_by_id('new_passcode').send_keys('tvbs')
            self.driver.find_element_by_id('confirmPassword').send_keys('tvbs')
            self.driver.find_element_by_name('change_password_button').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_new_passcode').text)
            message_new_passcode = self.driver.find_element_by_id('message_new_passcode').text
            self.assertEqual(message_new_passcode, '密碼建議為6~12位數，必須是英文數字混合！')
            print('輸入不合規則密碼送出跳出wording : ' + message_new_passcode)
            message_confirm_password = self.driver.find_element_by_id('message_confirmPassword').text
            self.assertEqual(message_confirm_password, '密碼建議為6~12位數，必須是英文數字混合！')
            print('輸入不合規則確認密碼送出跳出wording : ' + message_confirm_password)

            print('\n=======輸入和密碼不同的確認密碼送出=======')
            self.driver.find_element_by_id('new_passcode').clear()
            self.driver.find_element_by_id('confirmPassword').clear()
            self.driver.find_element_by_id('new_passcode').send_keys('tvbs2020')
            self.driver.find_element_by_id('confirmPassword').send_keys('tvbs202')
            self.driver.find_element_by_name('change_password_button').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_new_passcode').text)
            message_new_passcode = self.driver.find_element_by_id('message_new_passcode').text
            self.assertEqual(message_new_passcode, '密碼與確認密碼不符，請重新確認!')
            print('輸入和密碼不同的確認密碼送出跳出wording : ' + message_new_passcode)

            print('\n=======輸入和舊密碼相同的新密碼送出=======')
            self.driver.find_element_by_id('new_passcode').clear()
            self.driver.find_element_by_id('confirmPassword').clear()
            self.driver.find_element_by_id('new_passcode').send_keys('tvbs2020')
            self.driver.find_element_by_id('confirmPassword').send_keys('tvbs2020')
            self.driver.find_element_by_name('change_password_button').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('message_new_passcode').text)
            message_new_passcode = self.driver.find_element_by_id('message_new_passcode').text
            self.assertEqual(message_new_passcode, '新舊密碼相同，請改用其他密碼!')
            print('輸入和舊密碼相同的新密碼送出跳出wording : ' + message_new_passcode)

            print('\n=======輸入正確格式的密碼、確認密碼送出=======')
            self.driver.find_element_by_id('new_passcode').clear()
            self.driver.find_element_by_id('confirmPassword').clear()
            self.driver.find_element_by_id('new_passcode').send_keys('tvbstvbs2020')
            self.driver.find_element_by_id('confirmPassword').send_keys('tvbstvbs2020')
            self.driver.find_element_by_name('change_password_button').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('t1'))
            print(self.driver.find_element_by_class_name('t1').text)

            # 比對個人資料
            print('\n=======個人資料=======')
            self.driver.get('https://member-st.tvbs.com.tw/index?back_url=https://'
                            'supertaste-shop-ec-test.tvbs.com.tw/?menucat=0&site=SupertasteEC&t=1594025730')
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('account')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('password')
            # 定位驗證碼欄位
            captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
            # 定位登入按鈕
            login_btn = self.driver.find_element_by_id('signin')

            # 登入TVBS會員
            account_blank.send_keys(register_account)
            password_blank.send_keys('tvbstvbs2020')
            # 圖形辨識
            pic = self.driver.find_element_by_xpath(
                '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
            urlretrieve(pic, '../../../screenshot/Captcha/get.png')
            pytesseract.pytesseract.tesseract_cmd = \
                '../../Tesseract-OCR/tesseract.exe'
            img = Image.open('../../../screenshot/Captcha/get.png')
            img = img.convert('L')
            captcha = pytesseract.image_to_string(img)
            print('此次驗證碼為 : ' + captcha)
            captcha_blank.send_keys(captcha)
            login_btn.click()
            sleep(2)
            url = self.driver.current_url
            while url.find('member') != -1:
                print('驗證碼辨識失敗，重整頁面')
                self.driver.refresh()
                sleep(2)
                # 定位帳號欄位
                account_blank = self.driver.find_element_by_id('account')
                # 定位密碼欄位
                password_blank = self.driver.find_element_by_id('password')
                # 定位驗證碼欄位
                captcha_blank = self.driver.find_element_by_id('InputCaptcha1')
                # 定位登入按鈕
                login_btn = self.driver.find_element_by_id('signin')
                account_blank.send_keys(register_account)
                password_blank.send_keys('tvbstvbs2020')
                # 圖形辨識
                pic = self.driver.find_element_by_xpath(
                    '//*[@id="login_div"]/div[2]/div[5]/div[3]/div[1]/div[1]/img').get_attribute('src')
                urlretrieve(pic, '../../../screenshot/Captcha/get.png')
                pytesseract.pytesseract.tesseract_cmd = \
                    '../../Tesseract-OCR/tesseract.exe'
                img = Image.open('../../../screenshot/Captcha/get.png')
                img = img.convert('L')
                captcha = pytesseract.image_to_string(img)
                print('此次驗證碼為 : ' + captcha)
                captcha_blank.send_keys(captcha)
                login_btn.click()
                sleep(3)
                url = self.driver.current_url
                if url == 'https://supertaste-shop-ec-test.tvbs.com.tw/?menucat=0':
                    break

            # 跳轉到個人頁面
            self.driver.get('https://supertaste-shop-ec-test.tvbs.com.tw/Checkout/MemberUpdate')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('data').text)
            account = self.driver.find_element_by_class_name('data').text
            self.assertEqual(register_account, account)
            # 大頭貼下方顯示帳號
            nickname = account[:-12]
            nickname_web = self.driver.find_element_by_id('nickname')
            self.assertEqual(nickname, nickname_web.get_attribute('value'))
            # 性別
            gender_web = self.driver.find_element_by_xpath('//*[@id="genderId"]/div[2]').get_attribute('class')
            self.assertEqual(gender_web, 'gender02 ative')
            # 生日
            birth_web = self.driver.find_element_by_xpath('//*[@id="memberupdateform"]/div[4]/div[2]').text
            self.assertEqual(birth_web, '1994年09月08日')
            print('帳號、暱稱、性別、生日顯示正確')

            name = self.driver.find_element_by_id('name')
            mobile = self.driver.find_element_by_id('mobile')
            telzone = self.driver.find_element_by_id('telzone')
            telnumber = self.driver.find_element_by_id('telnumber')
            update_btn = self.driver.find_element_by_id('update')
            gender_editable = self.is_element_exist('img_box')
            birthday_editable = self.is_element_exist('message_birth')
            address = self.driver.find_element_by_id('addr_overseas')

            # 地址填寫特殊字元
            address.send_keys('，')
            update_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('dialogMessage').text)
            errmsg = self.driver.find_element_by_id('dialogMessage').text
            self.assertEqual(errmsg, '個人資料變更失敗!')
            print('地址填寫特殊字元無法變更個人資料')
            self.driver.find_element_by_id('btnConfirm').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('update'))

            # 暱稱、姓名、手機、市話欄位防呆
            address.clear()
            nickname_web.clear()
            name.send_keys('$')
            mobile.send_keys('123')
            telzone.send_keys('k')
            update_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('nicknameformError').text)

            nickname_error = self.driver.find_element_by_class_name('nicknameformError').text
            name_error = self.driver.find_element_by_class_name('nameformError').text
            mobile_error = self.driver.find_element_by_class_name('mobileformError').text
            telzone_error = self.driver.find_element_by_class_name('telzoneformError').text
            telnumber_error = self.driver.find_element_by_class_name('telnumberformError').text

            self.assertEqual(nickname_error, '*此欄位必填！')
            print('\n暱稱空值錯誤訊息 : ' + nickname_error)
            self.assertEqual(name_error, '僅能輸入中/英文姓名\n中英文姓名至少要兩個字')
            print('\n姓名輸入非中英文字元錯誤訊息 : \n' + name_error)
            self.assertEqual(mobile_error, '* 手機號碼格式不正確！')
            print('\n輸入錯誤格式手機錯誤訊息 : ' + mobile_error)
            self.assertEqual(telzone_error, '* 只能輸入數字！\n* 最少輸入 2 個字元')
            print('\n輸入英文區碼錯誤訊息 : \n' + telzone_error)
            self.assertEqual(telnumber_error, '*此欄位必填！')
            print('\n號碼空值錯誤訊息 : ' + telnumber_error)
            self.assertFalse(gender_editable, '性別可更改！')
            print('\n性別狀態不可更改')
            self.assertFalse(birthday_editable, '生日可更改！')
            print('生日狀態不可更改')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/memberCenterRegisterTVBS_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 註冊FB會員
    def test_memberCenterRegisterFB(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://member-st.tvbs.com.tw/index?back_url=https://'
                            'supertaste-shop-ec-test.tvbs.com.tw/?menucat=0&site=SupertasteEC&t=1594025730')
            self.driver.maximize_window()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]'))

            # 註冊FB會員
            print('\n=======註冊FB會員=======')
            # 使用已註冊FB會員註冊
            self.driver.find_element_by_id('singinWithFacebook').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('email'))
            self.driver.find_element_by_id('email').send_keys('s23321286@gmail.com')
            self.driver.find_element_by_id('pass').send_keys('Tvbs2020')
            self.driver.find_element_by_id('loginbutton').click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('bt-member'))
            self.driver.find_element_by_id('bt-member').click()
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_link_text('登出'))
            print('使用已註冊FB會員註冊可正常登入')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/memberCenterRegisterFB_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 註冊Apple ID會員
    def test_memberCenterRegisterAppleID(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://member-st.tvbs.com.tw/index?back_url=https://'
                            'supertaste-shop-ec-test.tvbs.com.tw/?menucat=0&site=SupertasteEC&t=1594025730')
            self.driver.maximize_window()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]'))

            # 註冊Apple ID會員
            print('\n=======註冊Apple ID會員=======')
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('account_name_text_field'))
            self.driver.find_element_by_id('account_name_text_field').clear()
            self.driver.find_element_by_id('account_name_text_field').send_keys('s0932748681@gmail.com')
            self.driver.find_element_by_class_name('icon_sign_in').click()
            sleep(1)
            self.driver.find_element_by_id('password_text_field').clear()
            self.driver.find_element_by_id('password_text_field').send_keys('Qa23321286')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('icon_sign_in'))
            self.driver.find_element_by_class_name('icon_sign_in').click()
            print('註冊Apple ID功能正常')
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('overflow-text'))
            # self.driver.find_element_by_class_name('overflow-text').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('bt-member'))
            # self.driver.find_element_by_id('bt-member').click()
            # WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_link_text('登出'))
            # print('登入Apple ID會員成功')
            # self.driver.find_element_by_partial_link_text('登出').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('bt-member'))
            # self.driver.find_element_by_id('bt-member').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_link_text('登入 / 註冊'))
            # print('登出Apple ID會員成功')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/memberCenterRegisterAppleID_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_index(self):
        flag = True
        # noinspection PyBroadException
        try:
            print('\n=======首頁=======')
            self.driver.get('https://supertaste-pre.tvbs.com.tw/')
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

            # ERROR判斷
            web_error_inspect.error_inspect(self)

            # 官方帳號
            print('\n=======官方帳號=======')
            web_index.index_fb_direct(self)  # FB官方帳號
            web_index.index_youtube_direct(self)  # YouTube官方帳號
            web_index.index_line_direct(self)  # LINE官方帳號

            # 主視覺
            print('\n=======主視覺=======')
            if self.is_element_exist('owl-nav') is False:
                print('主視覺尚未設定')
            else:
                banner = self.driver.find_element_by_class_name('owl-stage-outer').find_element_by_class_name('img')
                banner.is_enabled()
                self.driver.find_element_by_class_name('owl-prev').is_enabled()
                self.driver.find_element_by_class_name('owl-next').is_enabled()
                print('主視覺功能正常')

            # 首頁文章跳轉
            web_index.index_article_direct(self)
            self.driver.back()

            # More按鈕
            print('\n=======More按鈕=======')
            category_title = self.driver.find_element_by_class_name('talk_content_R').find_element_by_class_name(
                'R2').find_element_by_tag_name('p').text
            more_icon = self.driver.find_element_by_class_name('more_icon')
            more_icon.click()
            direct_category_title = self.driver.find_element_by_class_name('R2').find_element_by_tag_name('p').text
            self.assertEqual(category_title, direct_category_title)
            print('More按鈕功能正常，當前分類頁標題 : ' + direct_category_title)
            self.driver.back()

            # 人氣點閱榜
            web_common_component.hot_click(self)

            # 小編強推薦
            js = "var action=document.documentElement.scrollTop=500"
            self.driver.execute_script(js)
            web_common_component.editor_recommend(self)

            # 小編強推薦後台比對
            editor_recommend_title_list = []
            for j in range(6):
                editor_recommend_title_list.append(self.driver.find_elements_by_class_name(
                    'sidebar_div')[1].find_elements_by_class_name('txt')[j + 1].text)

            # 後台
            web_backend.backend_direct(self)
            web_backend.backend_login(self)

            # 新開一個視窗，通過執行js來新開一個視窗 (小編推薦與首頁分類置頂)
            js = 'window.open("http://2017back-pre.tvbs.com.tw/index.php/program_supertaste/supertaste_articles_sort");'
            self.driver.execute_script(js)

            # 獲取當前視窗控制代碼集合（列表型別）
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])

            backend_editor_recommend_title_list = []
            for j in range(6):
                backend_editor_recommend_title_list.append(self.driver.find_elements_by_class_name('td_title')[j].text)
            self.assertEqual(editor_recommend_title_list, backend_editor_recommend_title_list)
            print('後台文章設定有正確顯示於前台')

            self.driver.get('https://supertaste-pre.tvbs.com.tw/')

            # 好康搶先報
            web_common_component.good_news(self)

            # FB區塊
            web_common_component.is_fb_exist(self)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('combolistUl'))

            # 最新文章
            web_index.index_latest_article_backend_compare(self)

            # 熱搜關鍵字
            print('\n=======熱搜關鍵字=======')
            search_text = self.driver.find_elements_by_class_name('tag_block')[0].text
            self.driver.find_elements_by_class_name('tag_block')[0].click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('search'))
            search_blank = self.driver.find_elements_by_class_name('txt_box')[-1]
            search_blank_text = search_blank.get_attribute('value')
            self.assertEqual(search_text, search_blank_text)  # 判斷搜尋框帶入輸入的關鍵字
            web_search.search_related_result(self)
            print('熱搜關鍵字功能正常')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/index_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_articlePage(self):
        flag = True
        menu_url = ['food', 'drink', 'travel', 'hot', 'review']
        title = ['美食搶獨家', '品飲新風潮', '旅行新焦點', '今日熱話題', '節目主打星']
        for i in range(1):
            url = 'https://supertaste-pre.tvbs.com.tw/' + menu_url[i]
            print('\n*********' + title[i] + '*********')
            # noinspection PyBroadException
            try:
                self.driver.get(url)
                self.driver.maximize_window()
                self.driver.implicitly_wait(10)

                # ERROR判斷
                web_error_inspect.error_inspect(self)

                # 分類頁跳轉判斷
                category_title = self.driver.find_element_by_class_name('talk_content_title').\
                    find_element_by_class_name('R2').text
                self.assertEqual(category_title, title[i])
                print('確認當前分類頁為 : ' + category_title)

                # 分類頁文章跳轉判斷
                web_classified_page.classified_page_article_direct(self)

                # 人氣點閱榜
                web_common_component.hot_click(self)

                # 小編強推薦
                js = "var action=document.documentElement.scrollTop=500"
                self.driver.execute_script(js)
                web_common_component.editor_recommend(self)

                # 好康搶先報
                web_common_component.good_news(self)

                # FB區塊
                web_common_component.is_fb_exist(self)

                # 跳轉上一篇、下一篇文章
                web_article_page.article_pre_next(self)

                # 文章內頁 LINE 官方帳號
                print('\n*********文章內頁下方官方帳號*********')
                web_article_page.article_line_direct(self)

                # 文章內頁 YouTube 官方帳號
                web_article_page.article_youtube_direct(self)

                # 文章內頁 FB 官方帳號
                web_article_page.article_fb_direct(self)

            except:
                flag = False
                if flag is False or Exception:
                    self.driver.save_screenshot(
                        '../../../screenshot/supertasteWebFail/articlePage_Fail_{}.png'.format(current_time))
                    self.assertTrue(flag, 'Execute Fail.')

    # 文章內容比對
    def test_articleCompare(self):
        flag = True
        # noinspection PyBroadException
        try:
            # 後台 (WEB4.1)
            web_backend.backend_direct(self)
            web_backend.backend_login(self)

            # 新開一個視窗，通過執行js來新開一個視窗 (文章總覽-網站編輯)
            js = 'window.open("http://2017back-pre.tvbs.com.tw/index.php/program_supertaste/supertaste_articles/' \
                 'index/web_editor");'
            self.driver.execute_script(js)

            # 獲取當前視窗控制代碼集合（列表型別）
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])

            # 檢查上架狀態 & 發佈時間
            i = 0
            while True:
                self.driver.find_element_by_xpath(
                    '//*[@id="content-list_table"]/table/tbody/tr[%d]/td[9]/a/img' % (i+3)).click()
                articles_status = Select(self.driver.find_element_by_id('articles_status')).first_selected_option.text
                time_status = self.driver.find_element_by_name('publish').get_attribute('value')  # 獲取發佈時間
                time_local = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 獲取現在時間
                if time_status > time_local or articles_status.strip() == '下架':  # 如果發佈時間比現在時間晚 or 狀態是下架
                    self.driver.back()
                    i += 1
                else:
                    backend_title = self.driver.find_element_by_name('title').get_attribute('value')  # 獲取後台文章標題
                    self.driver.find_element_by_id('cke_17').click()  # 原始碼按鈕
                    # 藉由get_attribute('value')獲取編輯器內文字
                    content_source = self.driver.find_element_by_name('article_content').get_attribute('value')
                    chinese_content = ''.join(re.findall('[\u4e00-\u9fa5]', content_source))  # 去除中文以外字元
                    print('\n此次比對文章標題 : ' + backend_title)
                    print('後台文章內容 : ' + chinese_content)
                    break

            # 新開一個視窗，通過執行js來新開一個視窗
            js = 'window.open("https://supertaste-pre.tvbs.com.tw/");'
            self.driver.execute_script(js)

            # 獲取當前視窗控制代碼集合（列表型別）
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])

            # 前台尋找欲比對的文章
            txt_count = self.driver.page_source.count('class="txt"')  # 獲取頁面所有含有txt的標籤
            text_list = []
            for i in range(txt_count - 1):
                # 藉由後臺獲取的文章標題來找尋文章
                if self.driver.find_elements_by_class_name('txt')[i].text == backend_title:
                    self.driver.find_elements_by_class_name('txt')[i].click()
                    sleep(3)
                    self.driver.find_element_by_link_text('我同意').click()
                    all_p = self.driver.find_elements_by_xpath('//p')
                    text_list = []
                    for p in all_p:
                        text = ''.join(re.findall('[\u4e00-\u9fa5]', p.text))  # 去除中文以外字元
                        text_list += text  # 將處理過的字串加入列表
                    break
            text_string = "".join(text_list)  # 將列表轉為字串
            print('前台文章內容 : ' + text_string)

            # 前台尋找欲比對的文章
            article_content = set(text_string)
            backend_article_content = set(chinese_content)
            if len(article_content.symmetric_difference(backend_article_content)) < 10:  # 文章內容文字長度大於0且文章內容有跟後台編輯器內容相似
                print('文章內容正確～')
            elif len(text_string) == 0:  # 文章內容文字長度為0 (後台為上架狀態，但前台尚未更新)
                flag = False
                self.assertTrue(flag, '文章尚未於前台顯示！')
            else:
                flag = False
                self.assertTrue(flag, '文章內容錯誤！')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/memberCenterRegisterFB_Fail_{}.png'.format(
                        current_time))
                self.assertTrue(flag, 'Execute Fail.')  # 文章內容比對

    def test_infoCard(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.get('https://supertaste-pre.tvbs.com.tw/infocard')
            self.driver.maximize_window()
            # web_error_inspect.error_inspect(self)  # ERROR判斷
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_search_box'))
            self.driver.find_element_by_link_text('我同意').click()

            # 探索台灣 (輪播圖)
            print('\n=======探索台灣 (輪播圖)=======')
            self.driver.find_element_by_class_name('owl-next').click()
            self.driver.find_element_by_class_name('owl-prev').click()
            print('輪播圖可手動輪播')

            # 輪播圖跳轉
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_css_selector(
                "div[class = 'owl-item active']"))
            self.driver.find_element_by_css_selector("div[class = 'owl-item active']").click()
            web_error_inspect.error_inspect(self)  # ERROR判斷
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('act'))
            focus_text = self.driver.find_element_by_class_name('act').text
            self.assertEqual(focus_text, '店家')  # 判斷"店家" Tag 為 Focus 狀態
            print('跳轉後"店家" Tag 為 Focus 狀態')
            search_blank = self.driver.find_elements_by_class_name('txt_box')[-1]
            search_blank_text = search_blank.get_attribute('value')
            if len(search_blank_text) == 0:  # 判斷搜尋框帶入輸入的關鍵字
                flag = False
                self.assertTrue(flag, "搜尋框未帶入縣市")
            print('搜尋框帶入縣市 : ' + search_blank_text)
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name('supertaste_store')[0])

            # 節目店家
            # 縮圖、店名、縣市比對
            print('\n=======節目店家=======')
            store_name = self.driver.find_elements_by_class_name(
                'supertaste_store')[0].find_element_by_class_name('txt').find_element_by_tag_name('p').text
            self.driver.find_elements_by_class_name('supertaste_store')[0].find_element_by_class_name('img').click()
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_store'))
            print('節目店家點選縮圖可跳轉')
            self.driver.find_elements_by_class_name('supertaste_store')[0].find_element_by_class_name('txt').click()
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_store'))
            print('節目店家點選店名可跳轉')
            self.driver.find_elements_by_class_name('supertaste_store')[0].find_element_by_class_name('city').click()
            print('節目店家點選縣市可跳轉')

            # 店名比對
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('title1'))
            directed_store_name = self.driver.find_element_by_class_name('title1').text
            self.assertEqual(store_name, directed_store_name)
            print('節目店家店名比對正確 :' + store_name)

            # 熱門度人數判斷
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('point'))
            print(self.driver.find_element_by_class_name('point').text)

            # 店家圖片、地圖判斷
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('lazyimage'))
            print('節目店家店家圖片正常顯示')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('map_box'))
            print('節目店家地圖正常顯示')

            # 店家內頁
            # 立即導航看路線
            self.driver.find_element_by_class_name('color1').click()
            sleep(1)
            # 獲取當前視窗控制代碼集合（列表型別）
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            if 'www.google.com/maps' in self.driver.current_url:
                print('立即導航看路線可跳轉google map')
            else:
                flag = False
                self.assertTrue(flag, '立即導航看路線無法跳轉google map')
            self.driver.switch_to.window(handles[0])
                
            # 下載APP藏口袋
            self.driver.find_element_by_class_name('color2').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('pc_download_app_content'))
            print('點選下載APP藏口袋可跳出 QR Code')
            self.driver.back()
            WebDriverWait(self.driver, 40).until(lambda x: x.find_element_by_class_name('txt_box'))

            # 最新店家店名比對
            web_search.latest_store_direct(self)

            # 熱門度人數判斷
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('point'))
            print(self.driver.find_element_by_class_name('point').text)

            # 店家圖片、地圖判斷
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('lazyimage'))
            print('節目店家店家圖片正常顯示')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('map_box'))
            print('節目店家地圖正常顯示')

            # 點選店家關鍵字
            print('\n=======點選店家關鍵字=======')
            self.assertEqual(self.driver.find_element_by_class_name('radius').text[0], '#')
            print('店家關鍵字字首有 #')
            key_word = self.driver.find_element_by_class_name('radius').text[1:]
            self.driver.find_element_by_link_text('我同意').click()
            self.driver.find_element_by_class_name('radius').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('search'))
            search_blank = self.driver.find_elements_by_class_name('txt_box')[-1]
            search_blank_text = search_blank.get_attribute('value')
            self.assertEqual(search_blank_text, key_word)  # 判斷搜尋框帶入輸入的關鍵字
            print('點選店家關鍵字搜尋框帶入文字 : ' + key_word)
            focus_text = self.driver.find_element_by_class_name('act').text
            self.assertEqual(focus_text, '店家')  # 判斷"店家" Tag 為 Focus 狀態
            print('點選店家關鍵字跳轉後"店家" Tag 為 Focus 狀態')

            # 檢測搜尋框 Placeholder
            self.driver.get('https://supertaste-pre.tvbs.com.tw/infocard')
            search_blank = self.driver.find_elements_by_class_name('txt_box')[-1]
            search_blank_text = search_blank.get_attribute('placeholder')
            print('\n=======店家搜尋=======')
            self.assertEqual(search_blank_text, '輸入關鍵字，來場探索之旅')  # 判斷搜尋框 Placeholder
            print('搜尋框Placeholder : ' + search_blank_text)

            # 輸入空值搜尋
            self.driver.find_element_by_id('btn_search').click()
            WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())  # 等待 alert 出現
            alert_message = self.driver.switch_to.alert.text
            self.assertEqual(alert_message, '請輸入關鍵字')  # 判斷跳出訊息
            print('輸入空值搜尋跳出訊息 : ' + alert_message)
            self.driver.switch_to.alert.accept()

            # # 輸入特殊字元搜尋
            # search_blank.send_keys('!@#')
            # self.driver.find_element_by_id('btn_search').click()
            # sleep(1)
            # web_error_inspect.error_inspect(self)  # ERROR判斷
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('act'))
            # focus_text = self.driver.find_element_by_class_name('act').text
            # self.assertEqual(focus_text, '店家')  # 判斷"店家" Tag 為 Focus 狀態
            # print('輸入特殊字元搜尋可正常搜尋')
            # self.driver.back()

            # 輸入兩個關鍵詞中間以空白間隔搜尋
            search_blank = self.driver.find_elements_by_class_name('txt_box')[-1]
            search_blank.send_keys('台北 甜點')
            self.driver.find_element_by_id('btn_search').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('act'))
            print('輸入兩個關鍵詞中間以空白間隔可正常搜尋')
            self.driver.back()
            sleep(1)

            # 輸入關鍵字搜尋
            search_blank = self.driver.find_elements_by_class_name('txt_box')[-1]
            search_blank.clear()
            search_blank.send_keys('台北')
            self.driver.find_element_by_id('btn_search').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('act'))
            focus_text = self.driver.find_element_by_class_name('act').text
            self.assertEqual(focus_text, '店家')  # 判斷"店家" Tag 為 Focus 狀態
            print('輸入關鍵字可正常搜尋')
            print('"店家" Tag 為 Focus 狀態')

            # 搜尋框帶入輸入的關鍵字
            search_blank = self.driver.find_elements_by_class_name('txt_box')[-1]
            search_blank_text = search_blank.get_attribute('value')
            self.assertEqual(search_blank_text, '台北')  # 判斷搜尋框帶入輸入的關鍵字
            print('搜尋框帶入文字 : ' + search_blank_text)

            # 相關店家顯示輸入關鍵字 & 筆數
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('search_num'))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('num'))
            print('相關店家有顯示輸入關鍵字 & 筆數')

            if int(self.driver.find_element_by_css_selector("span[class = 'num']").text) < 24:
                print('搜尋結果未超過24則，無換頁按鈕')
            else:
                # 下一頁
                js = "var action=document.documentElement.scrollTop=10000"
                self.driver.execute_script(js)
                sleep(1)
                self.driver.find_element_by_class_name('jump_aft').find_elements_by_tag_name('a')[0].click()
                page_index = self.driver.current_url[-1]
                self.assertEqual(page_index, '2')
                print('點選 ( > ) 可正常跳轉下一頁')

                # 上一頁
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('jump_box'))
                js = "var action=document.documentElement.scrollTop=10000"
                self.driver.execute_script(js)
                sleep(1)
                self.driver.find_element_by_class_name('jump_bef').find_elements_by_tag_name('a')[1].click()
                page_index = self.driver.current_url[-1]
                self.assertEqual(page_index, '1')
                print('點選 ( < ) 可正常跳轉上一頁')

                # 最後一頁
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('jump_box'))
                js = "var action=document.documentElement.scrollTop=10000"
                for i in range(2):
                    self.driver.execute_script(js)
                    sleep(1)
                self.driver.find_element_by_class_name('jump_aft').find_elements_by_tag_name('a')[1].click()
                page_index = self.driver.current_url[-1]
                self.assertEqual(page_index, '5')
                print('點選 ( >| ) 可正常跳轉最後一頁')

                # 第一頁
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('jump_box'))
                self.driver.find_element_by_class_name('jump_bef').find_elements_by_tag_name('a')[0].click()
                page_index = self.driver.current_url[-1]
                self.assertEqual(page_index, '1')
                print('點選 ( <| ) 可正常跳轉第一頁')

                # # 點選 "全部" Tag，相關文章顯示輸入關鍵字 & 筆數
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('search_num'))
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('num'))
                # print('點選 "全部" Tag，相關文章有顯示輸入關鍵字 & 筆數')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/infocard_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_storeKeyWord(self):
        flag = True
        # noinspection PyBroadException
        try:
            # 跳轉搜尋頁面
            web_search.search_go_page(self)
            # 搜尋框熱門關鍵字
            web_search.search_blank_keyword(self)

            # 全部
            print('\n=======全部 Tag=======')
            self.driver.get('https://supertaste-pre.tvbs.com.tw/infocard')
            web_search.search_all_tag(self, '點心')

            # 顯示相關文章、相關店家、相關商品
            web_search.search_related_result(self)

            # 相關文章
            print('\n＊＊＊文章＊＊＊')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name('overlay-color')[0])

            # 文章跳轉
            web_search.search_article_direct(self)
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_store'))

            # 店家跳轉
            print('\n＊＊＊店家＊＊＊')
            store_name = self.driver.find_element_by_class_name('supertaste_store').find_elements_by_class_name(
                'txt')[0].find_element_by_tag_name('p').text
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('city'))  # 判斷有無縣市
            self.driver.find_element_by_class_name('supertaste_store').find_elements_by_class_name(
                'overlay-color')[0].click()
            # 店名比對
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('title1'))
            directed_store_name = self.driver.find_element_by_class_name('title1').text
            self.assertEqual(store_name, directed_store_name)
            print('店家店名比對正確 : ' + store_name)
            # 熱門度人數判斷
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('point'))
            print(self.driver.find_element_by_class_name('point').text)
            # 店家圖片、地圖判斷
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('lazyimage'))
            print('店家圖片正常顯示')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('map_box'))
            print('店家地圖正常顯示')
            print('跳轉店家功能正常')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_store'))

            # 商品跳轉
            print('\n＊＊＊商品＊＊＊')
            commodity_name = self.driver.find_element_by_class_name('supertaste_commodity').find_elements_by_class_name(
                'txt')[0].find_element_by_tag_name('p').text
            commodity_price = self.driver.find_element_by_class_name('price').text
            self.driver.find_element_by_class_name('supertaste_commodity').find_elements_by_class_name(
                'lazyimage')[0].click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('store_title').text)
            directed_commodity_name = self.driver.find_element_by_id('store_title').text
            self.assertEqual(commodity_name, directed_commodity_name)
            print('商品名稱比對正確 : ' + commodity_name)
            directed_commodity_price = self.driver.find_element_by_tag_name('strong').text
            self.assertEqual(commodity_price, directed_commodity_price)
            print('商品價格比對正確 : ' + commodity_price)
            print('跳轉商品功能正常')
            self.driver.back()

            # More按鈕
            print('\n=======More按鈕=======')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_article'))
            # 相關文章
            print('＊＊＊文章＊＊＊')
            if int(self.driver.find_elements_by_class_name('num')[0].text) > 6:
                self.driver.find_element_by_class_name('supertaste_article').find_element_by_class_name('more2').click()
                print('相關文章More按鈕正常')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('act'))
                focus_text = self.driver.find_element_by_class_name('act').text
                self.assertEqual(focus_text, '文章')  # 判斷"文章" Tag 為 Focus 狀態
                print('點選搜尋框關鍵字跳轉後"文章" Tag 為 Focus 狀態')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name(
                    'supertaste_article').find_element_by_class_name('list').find_elements_by_class_name('overlay-color')[6])
                print('點選More按鈕後文章則數有延展')
                self.driver.back()
            else:
                print('相關文章未超過6則，無More按鈕')
            # 相關店家
            print('\n＊＊＊店家＊＊＊')
            if int(self.driver.find_elements_by_class_name('num')[1].text) > 6:
                self.driver.find_element_by_class_name('supertaste_store').find_element_by_class_name('more2').click()
                print('相關店家More按鈕正常')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('act'))
                focus_text = self.driver.find_element_by_class_name('act').text
                self.assertEqual(focus_text, '店家')  # 判斷"店家" Tag 為 Focus 狀態
                print('點選搜尋框關鍵字跳轉後"店家" Tag 為 Focus 狀態')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name(
                    'supertaste_store').find_element_by_class_name('list').find_elements_by_class_name('overlay-color')[6])
                print('點選More按鈕後店家間數有延展')
                self.driver.back()
            else:
                print('相關店家未超過6則，無More按鈕')
            # 相關商品
            print('\n＊＊＊商品＊＊＊')
            if int(self.driver.find_elements_by_class_name('num')[2].text) > 6:
                self.driver.find_element_by_class_name('supertaste_commodity').find_element_by_class_name('more2').click()
                print('相關商品More按鈕正常')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('act'))
                focus_text = self.driver.find_element_by_class_name('act').text
                self.assertEqual(focus_text, '商品')  # 判斷"商品" Tag 為 Focus 狀態
                print('點選搜尋框關鍵字跳轉後"商品" Tag 為 Focus 狀態')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name(
                    'supertaste_commodity').find_element_by_class_name('list').find_elements_by_class_name(
                    'lazyimage')[6])
                print('點選More按鈕後商品數量有延展')
                self.driver.back()
            else:
                print('相關商品未超過6則，無More按鈕')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/storeKeyWord_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_commonFlow1(self):
        flag = True
        # noinspection PyBroadException
        try:
            web_common_flow.index_article(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/commonFlow1_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_commonFlow2(self):
        flag = True
        # noinspection PyBroadException
        try:
            web_common_flow.index_article_fb_share(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/commonFlow2_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_commonFlow3(self):
        flag = True
        # noinspection PyBroadException
        try:
            web_common_flow.classified_page_article(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/commonFlow3_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_commonFlow4(self):
        flag = True
        # noinspection PyBroadException
        try:
            web_common_flow.classified_page_article_fb_share(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/commonFlow4_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_commonFlow5(self):
        flag = True
        # noinspection PyBroadException
        try:
            web_common_flow.search_article(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/commonFlow5_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_commonFlow6(self):
        flag = True
        # noinspection PyBroadException
        try:
            web_common_flow.search_article_fb_share(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/commonFlow6_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_commonFlow7(self):
        flag = True
        # noinspection PyBroadException
        try:
            web_common_flow.index_classified_article_check(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/commonFlow7_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_commonFlow8(self):
        flag = True
        # noinspection PyBroadException
        try:
            web_common_flow.classified_page_article_check(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/commonFlow8_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_commonFlow9(self):
        flag = True
        # noinspection PyBroadException
        try:
            web_common_flow.store_check(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteWebFail/commonFlow9_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = ('../../../report/supertasteWebReport/supertaste_Web_Report_{}.html'.format(current_time))
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    # suite.addTest(SuperTaste('test_memberCenterLoginPageCheck'))  # 登入頁面欄位、邏輯
    # suite.addTest(SuperTaste('test_memberCenterLoginTVBS'))  # 登入TVBS會員
    # suite.addTest(SuperTaste('test_memberCenterLoginFB'))  # 登入FB會員
    # suite.addTest(SuperTaste('test_memberCenterLoginAppleID'))  # 登入Apple ID會員
    # suite.addTest(SuperTaste('test_memberCenterRegisterPageCheck'))  # 註冊頁面欄位、邏輯
    # suite.addTest(SuperTaste('test_memberCenterForgotPasswordPageCheck'))  # 忘記密碼欄位、邏輯
    # suite.addTest(SuperTaste('test_memberCenterRegisterTVBS'))  # 註冊TVBS會員、忘記密碼、重設密碼、個人資料
    # suite.addTest(SuperTaste('test_memberCenterRegisterFB'))  # 註冊FB會員
    # suite.addTest(SuperTaste('test_memberCenterRegisterAppleID'))  # 註冊Apple ID會員(X)
    # suite.addTest(SuperTaste('test_index'))  # 首頁
    # suite.addTest(SuperTaste('test_articlePage'))  # 文章內頁
    # suite.addTest(SuperTaste('test_articleCompare'))  # 文章內容比對
    # suite.addTest(SuperTaste('test_infoCard'))  # 店家
    # suite.addTest(SuperTaste('test_storeKeyWord'))  # 店家搜尋框關鍵字
    # suite.addTest(SuperTaste('test_commonFlow1'))  # 在首頁點擊文章，進入文章內頁
    # suite.addTest(SuperTaste('test_commonFlow2'))  # 在首頁點擊文章，進入文章內頁，分享至 FB
    # suite.addTest(SuperTaste('test_commonFlow3'))  # 在分類頁點擊文章，進入文章內頁
    # suite.addTest(SuperTaste('test_commonFlow4'))  # 在分類頁點擊文章，進入文章內頁，分享至 FB
    # suite.addTest(SuperTaste('test_commonFlow5'))  # 搜尋關鍵字後，點擊搜尋文章，進入文章內頁
    # suite.addTest(SuperTaste('test_commonFlow6'))  # 搜尋關鍵字後，點擊搜尋文章，進入文章內頁，分享至 FB
    # suite.addTest(SuperTaste('test_commonFlow7'))  # 使用者瀏覽首頁分類區塊
    # suite.addTest(SuperTaste('test_commonFlow8'))  # 使用者瀏覽首頁最新文章區塊
    suite.addTest(SuperTaste('test_commonFlow9'))  # 使用者瀏覽店家頁面

    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='SuperTaste Web Test Report')
    runner.run(suite)
