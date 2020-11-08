from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import web_error_inspect


def search_go_page(self):
    # 跳轉搜尋頁面
    self.driver.get('https://supertaste-pre.tvbs.com.tw/infocard')
    self.driver.maximize_window()
    # web_error_inspect.error_inspect(self)  # ERROR判斷
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_search_box'))


def search_blank_keyword(self):
    # 搜尋框熱門關鍵字
    print('\n=======搜尋框熱門關鍵字=======')
    self.assertEqual(self.driver.find_element_by_class_name('radius').text[0], '#')
    print('搜尋框關鍵字字首有 #')
    key_word = self.driver.find_element_by_class_name('radius').text[1:]
    self.driver.find_element_by_class_name('radius').click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('search'))
    search_blank = self.driver.find_elements_by_class_name('txt_box')[-1]
    search_blank_text = search_blank.get_attribute('value')
    self.assertEqual(search_blank_text, key_word)  # 判斷搜尋框帶入輸入的關鍵字
    print('點選搜尋框關鍵字搜尋框帶入文字 : ' + key_word)
    focus_text = self.driver.find_element_by_class_name('act').text
    self.assertEqual(focus_text, '店家')  # 判斷"店家" Tag 為 Focus 狀態
    print('點選搜尋框關鍵字跳轉後"店家" Tag 為 Focus 狀態')
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('search_num'))
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('num'))
    print('相關店家有顯示輸入關鍵字 & 筆數')


def search_all_tag(self, keyword):
    # 全部
    print('\n=======全部 Tag=======')
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('txt_box'))
    search_blank = self.driver.find_elements_by_class_name('txt_box')[-1]
    search_blank.send_keys(keyword)
    self.driver.find_element_by_id('btn_search').click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('act'))
    self.driver.find_element_by_link_text('全部').click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_content_title'))


def search_related_result(self):
    # 顯示相關文章、相關店家、相關商品
    self.assertEqual(self.driver.find_elements_by_class_name('supertaste_content_title')[0].text, '相關文章')
    self.assertEqual(self.driver.find_elements_by_class_name('supertaste_content_title')[1].text, '相關店家')
    self.assertEqual(self.driver.find_elements_by_class_name('supertaste_content_title')[2].text, '相關商品')
    print('有顯示相關文章、相關店家、相關商品')
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('search_num'))
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('num'))
    print('相關文章有顯示輸入關鍵字 & 筆數')


def search_article_direct(self):
    # 時間格式判斷
    date_time = self.driver.find_element_by_class_name('date').text
    datetime.datetime.strptime(date_time, '%Y/%m/%d %H:%M')
    print('時間格式正確 : ' + date_time)
    # 文章跳轉
    article_title = self.driver.find_element_by_class_name('list').find_elements_by_class_name('txt')[0]\
        .find_element_by_tag_name('p').text
    self.driver.find_element_by_class_name('supertaste_article').find_elements_by_class_name(
        'overlay-color')[0].click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('title'))
    direct_article_title = self.driver.find_element_by_class_name('title').find_element_by_class_name(
        'margin_b10').text
    self.assertEqual(article_title, direct_article_title)
    print('文章標題比對正確 : ' + article_title)
    direct_time = self.driver.find_element_by_class_name('icon_time').text
    self.assertEqual(date_time, direct_time)
    print('跳轉文章時間格式正確 : ' + date_time)


def latest_store_direct(self):
    # 最新店家
    store_name = self.driver.find_elements_by_class_name(
        'supertaste_store')[1].find_element_by_class_name('txt').find_element_by_tag_name('p').text
    self.driver.find_elements_by_class_name('supertaste_store')[1].find_element_by_class_name('img').click()
    self.driver.back()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_store'))
    print('最新店家點選縮圖可跳轉')
    self.driver.find_elements_by_class_name('supertaste_store')[1].find_element_by_class_name('txt').click()
    self.driver.back()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('supertaste_store'))
    print('最新店家點選店名可跳轉')
    self.driver.find_elements_by_class_name('supertaste_store')[1].find_element_by_class_name('city').click()
    print('最新店家點選縣市可跳轉')

    # 店名比對
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('title1'))
    directed_store_name = self.driver.find_element_by_class_name('title1').text
    self.assertEqual(store_name, directed_store_name)
    print('節目店家店名比對正確 : ' + store_name)

