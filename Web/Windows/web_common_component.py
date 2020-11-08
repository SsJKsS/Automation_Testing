from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


def hot_click(self):
    # 人氣點閱榜
    print('\n=======人氣點閱榜=======')
    # 判斷文章是否重複且滿六則
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('list_text'))
    hot_click_title_list = []
    for hot_click_counter in range(6):
        hot_click_title_list.append(self.driver.find_elements_by_class_name(
            'sidebar_div')[0].find_elements_by_class_name('txt')[hot_click_counter + 1].text)
    print(hot_click_title_list)
    self.assertEqual(len(set(hot_click_title_list)), 6)
    print('『人氣點閱榜內無重複文章』')
    hot_click_article_title = hot_click_title_list[0]
    self.driver.find_elements_by_class_name('sidebar_div')[0].find_element_by_class_name(
        'list_text').find_element_by_class_name('txt').click()
    sleep(2)
    hot_click_direct_article_title = self.driver.find_element_by_tag_name('h1').text
    self.assertEqual(hot_click_article_title, hot_click_direct_article_title)
    print('跳轉文章功能正常')
    sleep(0.5)


def editor_recommend(self):
    # 小編強推薦
    print('\n=======小編強推薦=======')
    # 判斷文章是否重複且滿六則
    editor_recommend_title_list = []
    for j in range(6):
        editor_recommend_title_list.append(self.driver.find_elements_by_class_name(
            'sidebar_div')[1].find_elements_by_class_name('txt')[j + 1].text)
    print(editor_recommend_title_list)
    self.assertEqual(len(set(editor_recommend_title_list)), 6)
    print('『小編強推薦內無重複文章』')
    article_title = editor_recommend_title_list[0]
    self.driver.find_elements_by_class_name('sidebar_div')[1].find_element_by_class_name(
        'list_text').find_element_by_class_name('txt').click()
    sleep(2)
    direct_article_title = self.driver.find_element_by_tag_name('h1').text
    self.assertEqual(article_title, direct_article_title)
    print('跳轉文章功能正常')
    sleep(2)


def good_news(self):
    # 好康搶先報
    print('\n=======好康搶先報=======')
    WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name('list_photo')[0])
    self.driver.find_elements_by_class_name('list_photo')[0].click()
    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[len(handles) - 1])
    self.driver.close()
    self.driver.switch_to.window(handles[len(handles) - 2])
    print('好康搶先報功能正常')


def is_fb_exist(self):
    # FB區塊
    print('\n=======FB區塊=======')
    flag = self.is_element_exist('fb-page')
    self.assertTrue(flag, 'FB區塊不存在')
    print('FB區塊存在')


def hot_search(self):
    # FB區塊
    print('\n=======FB區塊=======')
    flag = self.is_element_exist('fb-page')
    self.assertTrue(flag, 'FB區塊不存在')
    print('FB區塊存在')
