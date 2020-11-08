import datetime
from time import sleep

from selenium.webdriver.support.select import Select

import web_backend
import web_error_inspect
from selenium.webdriver.support.wait import WebDriverWait


def classified_page_article_direct(self):
    # 分類頁文章跳轉判斷
    article_title = self.driver.find_element_by_id('combolistUl').find_element_by_class_name('txt').text
    print('文章標題 : ' + article_title)
    self.driver.find_element_by_class_name('overlay-color').click()
    sleep(3)
    web_error_inspect.error_inspect(self)  # ERROR判斷
    direct_article_title = self.driver.find_elements_by_class_name('margin_b10')[2].text
    self.assertEqual(article_title, direct_article_title)
    print('跳轉文章功能正常')
    sleep(0.5)


def classified_page_article_backend_compare(self):
    # 分類頁文章跳轉
    print('\n=======分類頁文章跳轉=======')
    web_error_inspect.error_inspect(self)  # ERROR判斷
    # 判斷分類頁文章有無重複
    article_list = []
    article_url_list = []

    for i in range(6):
        article_list.append(self.driver.find_element_by_id(
            'combolistUl').find_elements_by_class_name('txt')[i].text)

    for i in range(9):
        self.driver.find_element_by_id('combolistUl').find_elements_by_class_name('txt')[i].click()
        self.driver.implicitly_wait(5)
        article_url_list.append(self.driver.current_url)
        print(self.driver.current_url)
        self.driver.back()
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('talk_article'))
    self.assertEqual(len(set(article_url_list)), 9)
    print('『分類頁無重複文章』')

    # 判斷時間格式
    date_time = self.driver.find_element_by_id('combolistUl').find_element_by_class_name('time').text
    datetime.datetime.strptime(date_time, '%Y/%m/%d %H:%M')
    print('時間格式正確 : ' + date_time)

    # 跳轉驗證
    article_title = self.driver.find_element_by_id('combolistUl').find_element_by_class_name('txt').text
    self.driver.find_element_by_id('combolistUl').find_element_by_class_name('txt').click()
    sleep(2)
    direct_article_title = self.driver.find_elements_by_class_name('margin_b10')[2].text
    self.assertEqual(article_title, direct_article_title)
    print('跳轉文章功能正常')

    # 後台
    web_backend.backend_direct(self)
    web_backend.backend_login(self)

    # 前後台文章標題比對
    print('\n=======前後台文章標題比對=======')
    self.driver.get("http://2017back-pre.tvbs.com.tw/index.php/program_supertaste/supertaste_articles/index/web_editor")
    Select(self.driver.find_element_by_name('search_categories_id')).select_by_value('22')  # 美食
    Select(self.driver.find_element_by_name('search_articles_status')).select_by_value('1')  # 上架
    self.driver.find_element_by_css_selector("input[value = '查詢']").click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('content'))
    backend_article_title = self.driver.find_element_by_class_name('td_title').text
    self.assertEqual(article_title, backend_article_title)
    print('前後台文章標題比對正確')
