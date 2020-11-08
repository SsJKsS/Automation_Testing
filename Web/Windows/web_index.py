from time import sleep

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import web_error_inspect
import web_backend


def index_fb_direct(self):
    # 首頁FB官方帳號跳轉
    self.driver.find_elements_by_class_name('header_community1')[1].find_elements_by_tag_name('a')[0].click()
    self.driver.implicitly_wait(5)

    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[1])
    fb_check = False
    if '食尚玩家' in self.driver.page_source:
        fb_check = True
    self.assertTrue(fb_check, '未跳轉到FB官方帳號')
    print('FB官方帳號跳轉正常 : ' + self.driver.title)
    self.driver.close()
    self.driver.switch_to.window(handles[0])
    self.driver.implicitly_wait(3)


def index_youtube_direct(self):
    # 首頁YouTube官方帳號跳轉
    self.driver.find_elements_by_class_name('header_community1')[1].find_elements_by_tag_name('a')[1].click()
    self.driver.implicitly_wait(5)

    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[1])
    yt_check = False
    if '食尚玩家' in self.driver.page_source:
        yt_check = True
    self.assertTrue(yt_check, '未跳轉到YouTube官方帳號')
    print('YouTube官方帳號跳轉正常 : ' + self.driver.title)
    self.driver.close()
    self.driver.switch_to.window(handles[0])
    self.driver.implicitly_wait(3)


def index_line_direct(self):
    # 首頁LINE官方帳號跳轉
    self.driver.find_elements_by_class_name('header_community1')[1].find_elements_by_tag_name('a')[2].click()
    self.driver.implicitly_wait(5)

    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[1])
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('mdQrCode'))
    print('LINE官方帳號跳轉正常 : ' + self.driver.title)
    self.driver.close()
    self.driver.switch_to.window(handles[0])
    self.driver.implicitly_wait(3)


def index_article_direct(self):
    # 首頁文章跳轉
    print('\n=======首頁文章跳轉=======')
    article_title = self.driver.find_element_by_class_name(
                    'talk_content_big').find_element_by_class_name('txt').text
    print('文章標題 : ' + article_title)
    date_time = self.driver.find_element_by_class_name('time').text
    datetime.datetime.strptime(date_time, '%Y/%m/%d %H:%M')
    print('時間格式正確 : ' + date_time)
    js = "var action=document.documentElement.scrollTop=500"
    self.driver.execute_script(js)
    sleep(1)
    self.driver.find_element_by_class_name('overlay-color').click()
    sleep(2)
    web_error_inspect.error_inspect(self)
    direct_article_title = self.driver.find_element_by_tag_name('h1').text
    self.assertEqual(article_title, direct_article_title)
    print('跳轉文章功能正常')


def index_article_backend_compare(self):
    # 首頁文章跳轉
    print('\n=======首頁文章跳轉=======')
    article_title = self.driver.find_element_by_class_name(
        'talk_content_big').find_element_by_class_name('txt').text
    print('文章標題 : ' + article_title)
    date_time = self.driver.find_element_by_class_name('time').text
    datetime.datetime.strptime(date_time, '%Y/%m/%d %H:%M')
    print('時間格式正確 : ' + date_time)
    js = "var action=document.documentElement.scrollTop=500"
    self.driver.execute_script(js)
    sleep(1)
    self.driver.find_element_by_class_name('overlay-color').click()
    sleep(2)
    web_error_inspect.error_inspect(self)
    direct_article_title = self.driver.find_element_by_tag_name('h1').text
    self.assertEqual(article_title, direct_article_title)
    print('跳轉文章功能正常')

    # 後台
    web_backend.backend_direct(self)
    web_backend.backend_login(self)

    # 前後台文章標題比對
    print('\n=======前後台文章標題比對=======')
    self.driver.get("http://2017back-pre.tvbs.com.tw/index.php/program_supertaste/supertaste_articles/index/web_editor")
    Select(self.driver.find_element_by_name('search_categories_id')).select_by_value('46')  # 雜貨
    Select(self.driver.find_element_by_name('search_articles_status')).select_by_value('1')  # 上架
    self.driver.find_element_by_css_selector("input[value = '查詢']").click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('content'))
    backend_article_title = self.driver.find_element_by_class_name('td_title').text
    self.assertEqual(article_title, backend_article_title)
    print('前後台文章標題比對正確')


def index_latest_article_backend_compare(self):
    # 最新文章
    print('\n=======最新文章=======')
    # 判斷最新文章有無重複
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
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('talk_kv'))
    self.assertEqual(len(set(article_url_list)), 9)
    print('『最新文章內無重複文章』')

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

    # 後台 - 小編推薦與首頁分類置頂
    self.driver.get('http://2017back-pre.tvbs.com.tw/index.php/program_supertaste/supertaste_articles/index/web_editor')

    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[-1])

    backend_article_list = []
    Select(self.driver.find_element_by_name('search_articles_status')).select_by_value('1')  # 上架
    self.driver.find_element_by_css_selector("input[value = '查詢']").click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('content'))
    for j in range(6):
        backend_article_list.append(self.driver.find_elements_by_class_name('td_title')[j].text)
    self.assertEqual(article_list, backend_article_list)
    print(article_list)
    print(backend_article_list)
    print('後台文章設定有正確顯示於前台')

