from time import sleep

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import web_backend
import web_common_component
import web_error_inspect
import web_index
import web_classified_page
import web_search
import web_article_page


def index_article(self):
    print('\n=======在首頁點擊文章，進入文章內頁=======')
    self.driver.get('https://supertaste-pre.tvbs.com.tw/')
    self.driver.maximize_window()
    web_error_inspect.error_inspect(self)
    sleep(1)
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('header_logo'))
    web_index.index_article_direct(self)
    web_common_component.hot_click(self)
    js = "var action=document.documentElement.scrollTop=500"
    self.driver.execute_script(js)
    web_common_component.editor_recommend(self)
    web_common_component.good_news(self)
    web_common_component.is_fb_exist(self)
    web_article_page.article_line_direct(self)
    web_article_page.article_youtube_direct(self)
    web_article_page.article_fb_direct(self)


def index_article_fb_share(self):
    print('\n=======在首頁點擊文章，進入文章內頁，分享至 FB =======')
    index_article(self)
    article_title = self.driver.find_element_by_tag_name('h1').text
    print(article_title)
    web_article_page.article_fb_share(self)
    if article_title in self.driver.page_source:
        print('文章分享至 FB 可正常顯示')
    else:
        flag = False
        self.assertTrue(flag, "文章分享至 FB 未正常顯示")


def classified_page_article(self):
    print('\n=======在分類頁點擊文章，進入文章內頁=======')
    self.driver.get('https://supertaste-pre.tvbs.com.tw/food')
    self.driver.maximize_window()
    web_error_inspect.error_inspect(self)
    sleep(1)
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('header_logo'))
    web_classified_page.classified_page_article_direct(self)
    web_common_component.hot_click(self)
    js = "var action=document.documentElement.scrollTop=500"
    self.driver.execute_script(js)
    web_common_component.editor_recommend(self)
    web_common_component.good_news(self)
    web_common_component.is_fb_exist(self)
    web_article_page.article_line_direct(self)
    web_article_page.article_youtube_direct(self)
    web_article_page.article_fb_direct(self)


def classified_page_article_fb_share(self):
    print('\n=======在分類頁點擊文章，進入文章內頁，分享至 FB =======')
    classified_page_article(self)
    article_title = self.driver.find_element_by_tag_name('h1').text
    print(article_title)
    web_article_page.article_fb_share(self)
    if article_title in self.driver.page_source:
        print('文章分享至 FB 可正常顯示')
    else:
        flag = False
        self.assertTrue(flag, "文章分享至 FB 未正常顯示")


def search_article(self):
    print('\n=======搜尋關鍵字後，點擊搜尋文章，進入文章內頁=======')
    web_search.search_go_page(self)
    web_search.search_all_tag(self, '點心')
    web_search.search_article_direct(self)
    web_common_component.hot_click(self)
    js = "var action=document.documentElement.scrollTop=500"
    self.driver.execute_script(js)
    web_common_component.editor_recommend(self)
    web_common_component.good_news(self)
    web_common_component.is_fb_exist(self)
    web_article_page.article_line_direct(self)
    web_article_page.article_youtube_direct(self)
    web_article_page.article_fb_direct(self)


def search_article_fb_share(self):
    print('\n=======搜尋關鍵字後，點擊搜尋文章，進入文章內頁，分享至 FB =======')
    search_article(self)
    article_title = self.driver.find_element_by_tag_name('h1').text
    print(article_title)
    web_article_page.article_fb_share(self)
    if article_title in self.driver.page_source:
        print('文章分享至 FB 可正常顯示')
    else:
        flag = False
        self.assertTrue(flag, "文章分享至 FB 未正常顯示")


def index_classified_article_check(self):
    print('\n=======使用者瀏覽首頁分類區塊=======')
    self.driver.get('https://supertaste-pre.tvbs.com.tw')
    self.driver.maximize_window()
    web_error_inspect.error_inspect(self)
    sleep(1)
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('overlay-color'))
    print('文章主圖正常顯示')
    web_index.index_article_backend_compare(self)


def index_latest_article_check(self):
    print('\n=======使用者瀏覽首頁分類區塊=======')
    self.driver.get('https://supertaste-pre.tvbs.com.tw')
    self.driver.maximize_window()
    web_error_inspect.error_inspect(self)
    sleep(1)
    WebDriverWait(self.driver, 20).until(
        lambda x: x.find_element_by_class_name('talk_article').find_element_by_class_name('overlay-color'))
    print('文章主圖正常顯示')
    web_index.index_latest_article_backend_compare(self)


def classified_page_article_check(self):
    print('\n=======使用者瀏覽分類頁=======')
    self.driver.get('https://supertaste-pre.tvbs.com.tw/food')  # 美食
    self.driver.maximize_window()
    web_error_inspect.error_inspect(self)
    sleep(1)
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('overlay-color'))
    print('文章主圖正常顯示')
    web_classified_page.classified_page_article_backend_compare(self)


def store_check(self):
    print('\n=======使用者瀏覽店家頁面=======')
    self.driver.get('https://supertaste-pre.tvbs.com.tw/infocard')  # 店家頁面
    self.driver.maximize_window()
    web_error_inspect.error_inspect(self)
    sleep(1)
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('overlay-color'))
    print('店家主圖正常顯示')
    store_url_list = []
    store_list = []

    for i in range(6):
        store_list.append(self.driver.find_element_by_id('newstore').find_elements_by_class_name('txt')[i]
                          .find_element_by_tag_name('p').text)

    for i in range(6):
        self.driver.find_element_by_id('newstore').find_elements_by_class_name('overlay-color')[i].click()
        self.driver.implicitly_wait(5)
        store_url_list.append(self.driver.current_url)
        print(self.driver.current_url)
        self.driver.back()
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('newstore'))
    self.assertEqual(len(set(store_url_list)), 6)
    print('最新店家內無重複店家')

    # 最新店家店名比對
    web_search.latest_store_direct(self)

    # 後台
    web_backend.backend_direct(self)
    web_backend.backend_login(self)

    # 後台 - 小編推薦與首頁分類置頂
    self.driver.get('http://2017back-pre.tvbs.com.tw/index.php/program/program_store/program_store_list')

    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[-1])

    backend_store_list = []
    self.driver.find_element_by_xpath('//input[@value="1"]').click()
    Select(self.driver.find_element_by_name('store_status')).select_by_value('1')  # 上架
    self.driver.find_element_by_css_selector("input[value = '查詢']").click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('content-list_table'))
    for j in range(6):
        backend_store_list.append(self.driver.find_elements_by_tag_name('tr')[j + 2].find_elements_by_tag_name('td')[2]
                                  .text)
    self.assertEqual(store_list, backend_store_list)
    print('後台店家設定有正確顯示於前台')



