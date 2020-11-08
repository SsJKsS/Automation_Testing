from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def backend_direct(self):
    # 後台 (WEB4.1)
    self.driver.get('http://2017back-pre.tvbs.com.tw/index.php/admission_list')
    self.driver.maximize_window()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('login_adm_name'))


def backend_login(self):
    # 後台登入
    login_adm_name = self.driver.find_element_by_id('login_adm_name')
    login_adm_pw = self.driver.find_element_by_id('login_adm_pw')
    login_adm_name.send_keys('jacktsao')
    login_adm_pw.send_keys('TVBS2020')
    self.driver.find_element_by_xpath("//input[@value='登入']").click()
    self.driver.implicitly_wait(6)

